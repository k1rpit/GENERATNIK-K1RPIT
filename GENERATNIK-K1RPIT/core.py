from tools_generator.gen_nik import *
from tools_generator.mutat_nik import *
import sys


def main() -> str:
    while True:
        try:
            print('--'*32)
            print('[1]--Basic nickname generation')
            print('[2]--Gamer nickname generation')
            print('[3]--Real nickname generation')
            print('[4]--Anonymous nickname generation')
            print('[5]--Nickname mutation')
            print('[0]--exit')
            print('--'*32)

            user_input = input('>>>')

            if user_input == '1':
                print('__'*16)
                print(gen_basic())
                print('__'*16)
            elif user_input == '2':
                print('__'*16)
                print(gen_game())
                print('__'*16)
            elif user_input == '3':
                print('__'*16)
                print(gen_real())
                print('__'*16)
            elif user_input == '4':
                print('__'*16)
                print(gen_anon())
                print('__'*16)
            elif user_input == '5':
                print('__'*16)
                print('[0]--basic mutat;',end=' ')
                print('[1]--hard mutat')
                print('__'*16)

                user_input_nik = input('input you user name>>>')
                user_input_mutat = input('[0/1]>>')
                if user_input_mutat == '0':
                    print('__'*16)
                    print(mutat_basic(user=user_input_nik))
                    print('__'*16)
                elif user_input_mutat == '1':
                    print('__'*16)
                    print(mutat_hard(user=user_input_nik))
                    print('__'*16)
                else:
                    print('!invalid input!')
            elif user_input == '0':
                sys.exit(1)
            else:
                print('--'*32)
                print('[1]--Basic nickname generation')
                print('[2]--Gamer nickname generation')
                print('[3]--Real nickname generation')
                print('[4]--Anonymous nickname generation')
                print('[5]--Nickname mutation')
                print('[0]--exit')
                print('--'*32)
        except KeyboardInterrupt:
            sys.exit(1)

        


if __name__ == '__main__':
    main()