import os
import re
import sys
import argparse
import saspy
import getpass

translation = {'proc':'canhaz',
               'summary':'summy',
               'data=':'canuze=',
               'class':'donewifth',
               'output':'gimmeh',
               'out':'gouze',
               'run':'kthxbye',
               'export':'goaway',
               'outfile=':'goherez='}

loltranslate = {v:k for k,v in  translation.items()}

def translate_lol(lolsascode):
    for lol, sas in loltranslate.items():
        lolsascode = re.sub(lol,sas,lolsascode,0,re.IGNORECASE)
    return lolsascode

def open_session():
    try:
        if 'session' not in globals():
            global session 
            user = input('can haz u name 0w0? ')
            pw = getpass.getpass('wot iz tha secretz? ')
            print('\nokay i finking...')
            with open(os.devnull,"w") as devNull:
                original = sys.stdout
                sys.stdout = devNull
                session = saspy.SASsession(
                    omruser=user,
                    omrpw=pw,
                    cfgfile=r'<CFIGIFLE>', 
                    cfgname='winiomwin'
                )
                sys.stdout = original
            print('u haz ses.')
        return 1
    except Exception as e:
        print(f'ohnoez. no sas 4 u. {e}')
        return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("lolsasfile", help="can haz lolsas file plz?")
    args = parser.parse_args()
    if 'lolsasfile' in args:
        print('\nOAKY LETZ DO A LOLZAZ\n\n')
        with open(args.lolsasfile,'r') as f:
            lolsascode = f.read()
            sascode = translate_lol(lolsascode)
            open_session()
            print('gonna do '+args.lolsasfile)
            c = session.submit(sascode)
            print('k done now bye.')
    else:
        print('ohnoes no lolsas. byexx')

if __name__=='__main__':
    main()
        
