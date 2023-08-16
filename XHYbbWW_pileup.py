import ROOT, glob
from TIMBER.Analyzer import TIMBERPATH, analyzer, Correction
from TIMBER.Tools.AutoPU import MakePU

'''
to be run *before* creating snapshots
'''

if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-s', type=str, dest='setname',
                        action='store', required=True,
                        help='Setname to process.')
    parser.add_argument('-y', type=str, dest='era',
                        action='store', required=True,
                        help='Year of set (16, 17, 18).')
    args = parser.parse_args()
    setname=args.setname
    era=args.era

    # setname: 
    #	DataX		MX_XMASS_MY_YMASS
    fullname = '%s_%s'%(setname,era)

    filename = 'raw_nano/{}_{}.txt'.format(setname,era)
    out = ROOT.TFile.Open('XHYbbWW_pileup_{}.root'.format(fullname), 'RECREATE')

    a = analyzer(filename)

    # get pointer to histogram
    #hptr = MakePU(a, '20%sUL'%args.era, fullname+'.root')
    hptr = MakePU(a, era, ULflag=True, filename=fullname+'.root')	# update to latest TIMBER version
    hout = hptr.Clone()
    out.WriteTObject(hout, fullname)
    out.Close()
