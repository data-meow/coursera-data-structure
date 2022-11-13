from unittest import TestCase, main
import os
from pathlib import Path
import sys
from check_brackets import main as mainAlgo  # import your algorythm main function here


class Test(TestCase):
    def test_from_file(self):
        for i in range(1, 55):
            p_str = f"{i}".rjust(2, '0')  # test case file name
            p = Path(os.getcwd()) / Path('tests') / p_str  # test case file full path
            with open(p, 'r') as input_file:
                sys.stdin = input_file
                responses = [mainAlgo()]

            p_str += '.a'  # test answer file
            ansF = Path(os.getcwd()) / Path('tests') / p_str
            with open(ansF, 'r') as ans_file:
                ans = [int(i.strip()) if i.strip() != 'Success' else i.strip() for i in ans_file.readlines()]
                print(i, responses, ans)
                self.assertEqual(responses, ans)


if __name__ == '__main__':
    main()
