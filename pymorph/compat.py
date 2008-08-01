from mmorph import *
from text import *

# old abbreviations:

clohole=close_holes
ero=erode
cero=cerode
dil=dilate
cdil=cdilate
sedil=sedilate
add4dil=add4dilate
uint8=to_uint8
uint16=to_uint16
int32=to_int32

# mmnames:

mmadd4dil=add4dil
mmaddm=addm
mmareaclose=areaclose
mmareaopen=areaopen
mmasf=asf
mmasfrec=asfrec
mmbench=bench
mmbinary=binary
mmblob=blob
mmbshow=bshow
mmcbisector=cbisector
mmcdil=cdil
mmcenter=center
mmcero=cero
mmclohole=clohole
mmclose=close
mmcloserec=closerec
mmcloserecth=closerecth
mmcloseth=closeth
mmconcat=concat
mmcthick=cthick
mmcthin=cthin
mmcwatershed=cwatershed
mmdatatype=datatype
mmdil=dil
mmdist=dist
mmdrawv=drawv
mmdtshow=dtshow
mmedgeoff=edgeoff
mmendpoints=endpoints
mmero=ero
mmflood=flood
mmframe=frame
mmfreedom=freedom
mmgdist=gdist
mmgdtshow=gdtshow
mmglblshow=glblshow
mmgradm=gradm
mmgrain=grain
mmgray=gray
mmgshow=gshow
mmhistogram=histogram
mmhmax=hmax
mmhmin=hmin
mmhomothick=homothick
mmhomothin=homothin
mmimg2se=img2se
mminfcanon=infcanon
mminfgen=infgen
mminfrec=infrec
mminpos=inpos
mminterot=interot
mmintersec=intersec
mmintershow=intershow
mmisbinary=isbinary
mmisequal=isequal
mmlabel=label
mmlabelflat=labelflat
mmlastero=lastero
mmlblshow=lblshow
mmlimits=limits
mmmat2set=mat2set
mmmaxleveltype=maxleveltype
mmneg=neg
mmopen=open
mmopenrec=openrec
mmopenrecth=openrecth
mmopenth=openth
mmopentransf=opentransf
mmpad4n=pad4n
mmpatspec=patspec
mmplot=plot
mmreadgray=readgray
mmregmax=regmax
mmregmin=regmin
mmse2hmt=se2hmt
mmse2interval=se2interval
mmsebox=sebox
mmsecross=secross
mmsedil=sedil
mmsedisk=sedisk
mmseline=seline
mmsereflect=sereflect
mmserot=serot
mmseshow=seshow
mmsesum=sesum
mmset2mat=set2mat
mmsetrans=setrans
mmseunion=seunion
mmshow=show
mmskelm=skelm
mmskelmrec=skelmrec
mmskiz=skiz
mmsubm=subm
mmsupcanon=supcanon
mmsupgen=supgen
mmsuprec=suprec
mmswatershed=swatershed
mmsymdif=symdif
mmtext=text
mmthick=thick
mmthin=thin
mmthreshad=threshad
mmtoggle=toggle
mmunion=union
mmvmax=vmax
mmwatershed=watershed

# Functions which were removed:

def mminstall(*args):
    pass
def mmversion(*args):
    pass
def mmregister(*args):
    pass


def mmcmp(f1, oper, f2, oper1=None, f3=None):
    """
        - Alternative:
            Consider using array operations directly, i.e., instead of 
                mmcmp(f1, '>', f2)
            simply use
                f1 > f2
        - Purpose
            Compare two images pixelwisely.
        - Synopsis
            y = mmcmp(f1, oper, f2, oper1=None, f3=None)
        - Input
            f1:    Gray-scale (uint8 or uint16) or binary image.
            oper:  String Default: "". relationship from: '==', '~=',
                   '<','<=', '>', '>='.
            f2:    Gray-scale (uint8 or uint16) or binary image.
            oper1: String Default: None. relationship from: '==', '~=',
                   '<','<=', '>', '>='.
            f3:    Gray-scale (uint8 or uint16) or binary image. Default:
                   None.
        - Output
            y: Binary image.
        - Description
            Apply the relation oper to each pixel of images f1 and f2 , the
            result is a binary image with the same size. Optionally, it is
            possible to make the comparison among three image. It is
            possible to use a constant value in place of any image, in this
            case the constant is treated as an image of the same size as the
            others with all pixels with the value of the constant.
        - Examples
            #
            #   example 1
            #
            print cmp(to_uint8([1, 2, 3]),'<', to_uint8(2))
            print cmp(to_uint8([1, 2, 3]),'<', to_uint8([0, 2, 4]))
            print cmp(to_uint8([1, 2, 3]),'==', to_uint8([1, 1, 3]))
            #
            #   example 2
            #
            f=readgray('keyb.tif')
            fbin=cmp(to_uint8(10), '<', f, '<', to_uint8(50))
            show(f)
            show(fbin)
    """

    if   oper == '==':    y = (f1==f2)
    elif oper == '~=':    y = (f1!=f2)
    elif oper == '<=':    y = (f1<=f2)
    elif oper == '>=':    y = (f1>=f2)
    elif oper == '>':     y = (f1> f2)
    elif oper == '<':     y = (f1< f2)
    else:
        assert 0, 'oper must be one of: ==, ~=, >, >=, <, <=, it was:'+oper
    if oper1 != None:
        if   oper1 == '==':     y = intersec(y, f2==f3)
        elif oper1 == '~=':     y = intersec(y, f2!=f3)
        elif oper1 == '<=':     y = intersec(y, f2<=f3)
        elif oper1 == '>=':     y = intersec(y, f2>=f3)
        elif oper1 == '>':      y = intersec(y, f2> f3)
        elif oper1 == '<':      y = intersec(y, f2< f3)
        else:
            assert 0, 'oper1 must be one of: ==, ~=, >, >=, <, <=, it was:'+oper1

    y = binary(y)
    return y


def mmvdome(f, v=1, Bc=None):
    """
        - Purpose
            Obsolete, use vmax.
        - Synopsis
            y = mmvdome(f, v=1, Bc=None)
        - Input
            f:  Gray-scale (uint8 or uint16) image.
            v:  Default: 1. Volume parameter.
            Bc: Structuring Element Default: None (3x3 elementary cross).
                Structuring element (connectivity).
        - Output
            y: Gray-scale (uint8 or uint16) or binary image.
        - Description
            The correct name for this operator mmvdome is vmax.

    """

    if Bc is None: Bc = secross()
    y = hmax(f,v,Bc);
    return y

def mmis(f1, oper, f2=None, oper1=None, f3=None):
    """
        - Alternative
            Consider using array operations or isbinary()
        - Purpose
            Verify if a relationship among images is true or false.
        - Synopsis
            y = mmis(f1, oper, f2=None, oper1=None, f3=None)
        - Input
            f1:    Gray-scale (uint8 or uint16) or binary image.
            oper:  String relationship from: '==', '~=', '<','<=', '>',
                   '>=', 'binary', 'gray'.
            f2:    Gray-scale (uint8 or uint16) or binary image. Default:
                   None.
            oper1: String Default: None. relationship from: '==', '~=',
                   '<','<=', '>', '>='.
            f3:    Gray-scale (uint8 or uint16) or binary image. Default:
                   None.
        - Output
            y: Bool value: 0 or 1
        - Description
            Verify if the property or relatioship between images is true or
            false. The result is true if the relationship is true for all
            the pixels in the image, and false otherwise. (Obs: This
            function replaces is equal, is lesseq, is binary ).
        - Examples
            #
            fbin=binary([0, 1])
            f1=to_uint8([1, 2, 3])
            f2=to_uint8([2, 2, 3])
            f3=to_uint8([2, 3, 4])
            mmis(fbin,'binary')
            mmis(f1,'gray')
            mmis(f1,'==',f2)
            mmis(f1,'<',f3)
            mmis(f1,'<=',f2)
            mmis(f1,'<=',f2,'<=',f3)
    """
    from string import upper

    if f2 == None:
        oper=upper(oper);
        if   oper == 'BINARY': return isbinary(f1)
        elif oper == 'GRAY'  : return not isbinary(f1)
        else:
            assert 0,'oper should be BINARY or GRAY, was'+oper
    elif oper == '==':    y = isequal(f1, f2)
    elif oper == '~=':    y = not isequal(f1,f2)
    elif oper == '<=':    y = mmislesseq(f1,f2)
    elif oper == '>=':    y = mmislesseq(f2,f1)
    elif oper == '>':     y = isequal(neg(threshad(f2,f1)),binary(1))
    elif oper == '<':     y = isequal(neg(threshad(f1,f2)),binary(1))
    else:
        assert 0,'oper must be one of: ==, ~=, >, >=, <, <=, it was:'+oper
    if oper1 != None:
        if   oper1 == '==': y = y and isequal(f2,f3)
        elif oper1 == '~=': y = y and (not isequal(f2,f3))
        elif oper1 == '<=': y = y and mmislesseq(f2,f3)
        elif oper1 == '>=': y = y and mmislesseq(f3,f2)
        elif oper1 == '>':  y = y and isequal(neg(threshad(f3,f2)),binary(1))
        elif oper1 == '<':  y = y and isequal(neg(threshad(f2,f3)),binary(1))
        else:
            assert 0,'oper1 must be one of: ==, ~=, >, >=, <, <=, it was:'+oper1
    return y


def mmislesseq(f1, f2, MSG=None):
    """
        - Alternative
            Consider using f1 <= f2
        - Purpose
            Verify if one image is less or equal another (is beneath)
        - Synopsis
            bool = mmislesseq(f1, f2)
        - Input
            f1:  Gray-scale (uint8 or uint16) or binary image.
            f2:  Gray-scale (uint8 or uint16) or binary image.
        - Output
            bool: Boolean
        - Description
            mmislesseq compares the images f1 and f2 and returns true (1),
            if f1(x) <= f2(x) , for every pixel x, and false (0), otherwise.
        - Examples
            #
            f1 = to_uint8([0, 1, 2, 3])
            f2 = to_uint8([9, 5, 3, 3])
            print mmislesseq(f1,f2)
            print mmislesseq(f2,f1)
            print mmislesseq(f1,f1)
    """
    from numpy import ravel

    bool = min(ravel(f1<=f2))
    return bool

def mmstats(f, measurement):
    """
        - Purpose
            Find global image statistics.
        - Synopsis
            y = mmstats(f, measurement)
        - Input
            f:           
            measurement: String Default: "". Choose the measure to compute:
                         'max', 'min', 'median', 'mean', 'sum', 'std',
                         'std1'.
        - Output
            y:
        - Description
            Compute global image statistics: 'max' - maximum gray-scale
            value in image; 'min' - minimum gray-scale value in image; 'sum'
            - sum of all pixel values; 'median' - median value of all pixels
            in image; 'mean' - mean value of all pixels in image; 'std' -
            standard deviation of all pixels (normalized by N-1); 'std1' -
            idem, normalized by N.

    """
    from string import upper
    from numpy import ravel
    from numpy.oldnumeric.mlab import mean, median, std

    measurement = upper(measurement)
    if measurement == 'MAX': return f.max()
    elif measurement == 'MIN': return f.min()
    elif measurement == 'MEAN': return f.mean()
    elif measurement == 'MEDIAN': return f.median()
    elif measurement == 'STD': return f.std()
    else:
        assert 0,'pymorph.compat.mmstats: Not a valid measurement'

def mmsurf(f,options = None):
    return f
