import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('github_setup', Path(__file__).parents[1] / 'scripts/github_setup.py')
setup = importlib.util.module_from_spec(spec)
spec.loader.exec_module(setup)


class SetupTests(unittest.TestCase):
    def test_fixed_exclusion_survives_registry_edit(self):
        with tempfile.TemporaryDirectory() as tmp:
            registry = Path(tmp) / 'registry'
            registry.mkdir()
            (registry / 'repos.json').write_text(json.dumps({'owner':'zinnoberHaus','excluded':[], 'repositories':[{'name':'microyee-ai','url':'https://github.com/zinnoberHaus/microyee-ai'}]}))
            (registry / 'ticketing.json').write_text('{"owner":"zinnoberHaus"}')
            with patch.object(setup, 'ROOT', Path(tmp)):
                with self.assertRaisesRegex(ValueError, 'excluded'):
                    setup.load_targets()

    def test_private_existing_project_never_becomes_public(self):
        board = {'number':1, 'url':'https://github.com/users/zinnoberHaus/projects/1','title':'Portfolio','public':False}
        with patch.object(setup, 'gh', return_value={'projects':[board]}) as api:
            with self.assertRaisesRegex(RuntimeError, 'private'):
                setup.project('zinnoberHaus', [], {'project':{'title':'Portfolio','number':None}})
            self.assertEqual(api.call_count, 1)

    def test_missing_recorded_project_never_recreated(self):
        with patch.object(setup, 'gh', return_value={'projects':[]}) as api:
            with self.assertRaisesRegex(RuntimeError, 'missing or closed'):
                setup.project('zinnoberHaus', [], {'project':{'title':'Portfolio','number':4}})
            self.assertEqual(api.call_count, 1)

    def test_field_drift_does_not_report_active(self):
        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp,'registry').mkdir()
            state = {'project':{'title':'Portfolio','number':1,'fields':[{'name':'Priority','type':'SINGLE_SELECT','options':['P1']}]}}
            board = {'number':1,'title':'Portfolio','url':'https://github.com/users/zinnoberHaus/projects/1','public':True}
            replies = [{'projects':[board]}, None, {'data':{'user':{'projectV2':{'fields':{'nodes':[{'name':'Priority','dataType':'TEXT'}], 'pageInfo':{'hasNextPage':False}}}}}}]
            with patch.object(setup,'ROOT',Path(tmp)), patch.object(setup,'gh',side_effect=replies):
                with self.assertRaisesRegex(RuntimeError,'field drift'):
                    setup.project('zinnoberHaus',[],state)
            self.assertEqual(state['project']['state'],'configuring')

    def test_unchanged_labels_do_not_mutate(self):
        labels = [{'name':'type:bug','description':'A defect','color':'ff0000'}]
        with patch.object(setup,'gh',return_value=[labels]) as api:
            setup.labels('zinnoberHaus',['zettel'],{'labels':labels})
            self.assertEqual(api.call_count,1)

if __name__ == '__main__':
    unittest.main()
