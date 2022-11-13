import io
from contextlib import redirect_stdout
from unittest import TestCase, main
import os
from pathlib import Path
import sys
from process_packages import main as mainAlgo  # import your algorythm main function here


class Test(TestCase):
    def test_from_file(self):
        for i in range(1, 23):
            p_str = f"{i}".rjust(2, '0')  # test case file name
            p = Path(os.getcwd()) / Path('tests') / p_str  # test case file full path
            with open(p, 'r') as input_file:
                sys.stdin = input_file
                with io.StringIO() as buf, redirect_stdout(buf):
                    mainAlgo()
                    responses = list(map(int, buf.getvalue().split()))

            p_str += '.a'  # test answer file
            ansF = Path(os.getcwd()) / Path('tests') / p_str
            with open(ansF, 'r') as ans_file:
                ans = [int(i.strip()) for i in ans_file.readlines()]
                # print(i, responses, ans)
                self.assertEqual(responses, ans)


if __name__ == '__main__':
    main()
