from pytest_test_project.example import reverse

def test_reverse():
        assert reverse('Hexlet') == 'telxeH'

        def test_reverse_for_empty_string():
                assert reverse('') == ''
