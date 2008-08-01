"""
    Module morph -- SDC Morphology Toolbox
    -------------------------------------------------------------------
    The pymorph Morphology Toolbox for Python is a powerful collection of latest
    state-of-the-art gray-scale morphological tools that can be applied to image
    segmentation, non-linear filtering, pattern recognition and image analysis.
    -------------------------------------------------------------------
    add4dilate()   -- Addition for dilation
    addm()         -- Addition of two images, with saturation.
    areaclose()    -- Area closing
    areaopen()     -- Area opening
    asf()          -- Alternating Sequential Filtering
    asfrec()       -- Reconstructive Alternating Sequential Filtering
    bench()        -- benchmarking main functions of the toolbox.
    binary()       -- Convert a gray-scale image into a binary image
    blob()         -- Blob measurements from a labeled image.
    bshow()        -- Generate a graphical representation of overlaid binary
                      images.
    cbisector()    -- N-Conditional bisector.
    cdilate()      -- Dilate an image conditionally.
    center()       -- Center filter.
    cerode()       -- Erode an image conditionally.
    close_holes()  -- Close holes of binary and gray-scale images.
    close()        -- Morphological closing.
    closerec()     -- Closing by reconstruction.
    closerecth()   -- Close-by-Reconstruction Top-Hat.
    closeth()      -- Closing Top Hat.
    concat()       -- Concatenate two or more images along width, height or
                      depth.
    cthick()       -- Image transformation by conditional thickening.
    cthin()        -- Image transformation by conditional thinning.
    cwatershed()   -- Detection of watershed from markers.
    datatype()     -- Return the image datatype string
    dilate()       -- Dilate an image by a structuring element.
    dist()         -- Distance transform.
    drawv()        -- Superpose points, rectangles and lines on an image.
    dtshow()       -- Display a distance transform image with an iso-line
                      color table.
    edgeoff()      -- Eliminate the objects that hit the image frame.
    endpoints()    -- Interval to detect end-points.
    erode()        -- Erode an image by a structuring element.
    flood()        -- Flooding filter- h,v,a-basin and dynamics (depth, area,
                      volume)
    frame()        -- Create a frame image.
    freedom()      -- Control automatic data type conversion.
    gdist()        -- Geodesic Distance Transform.
    gdtshow()      -- Apply an iso-line color table to a gray-scale image.
    glblshow()     -- Apply a random color table to a gray-scale image.
    gradm()        -- Morphological gradient.
    grain()        -- Gray-scale statistics for each labeled region.
    gray()         -- Convert a binary image into a gray-scale image.
    gshow()        -- Apply binary overlays as color layers on a binary or
                      gray-scale image
    histogram()    -- Find the histogram of the image f.
    hmax()         -- Remove peaks with contrast less than h.
    hmin()         -- Remove basins with contrast less than h.
    homothick()    -- Interval for homotopic thickening.
    homothin()     -- Interval for homotopic thinning.
    img2se()       -- Create a structuring element from a pair of images.
    infcanon()     -- Intersection of inf-generating operators.
    infgen()       -- Inf-generating.
    infrec()       -- Inf-reconstruction.
    inpos()        -- Minima imposition.
    interot()      -- Rotate an interval
    intersec()     -- Intersection of images.
    intershow()    -- Visualize an interval.
    isbinary()     -- Check for binary image
    label()        -- Label a binary image.
    labelflat()    -- Label the flat zones of gray-scale images.
    lastero()      -- Last erosion.
    lblshow()      -- Display a labeled image assigning a random color for
                      each label.
    limits()       -- Get the possible minimum and maximum of an image.
    mat2set()      -- Converts image representation from matrix to set
    maxleveltype() -- Returns the maximum value associated to an image
                      datatype
    neg()          -- Negate an image.
    open()         -- Morphological opening.
    openrec()      -- Opening by reconstruction.
    openrecth()    -- Open-by-Reconstruction Top-Hat.
    openth()       -- Opening Top Hat.
    opentransf()   -- Open transform.
    pad4n()        -- pad4n
    patspec()      -- Pattern spectrum (also known as granulometric size
                      density).
    plot()         -- Plot a function.
    readgray()     -- Read an image from a commercial file format and stores
                      it as a gray-scale image.
    regmax()       -- Regional Maximum.
    regmin()       -- Regional Minimum (with generalized dynamics).
    se2hmt()       -- Create a Hit-or-Miss Template (or interval) from a pair
                      of structuring elements.
    se2interval()  -- Create an interval from a pair of structuring elements.
    sebox()        -- Create a box structuring element.
    secross()      -- Diamond structuring element and elementary 3x3 cross.
    sedilate()     -- Dilate one structuring element by another
    sedisk()       -- Create a disk or a semi-sphere structuring element.
    seline()       -- Create a line structuring element.
    sereflect()    -- Reflect a structuring element
    serot()        -- Rotate a structuring element.
    seshow()       -- Display a structuring element as an image.
    sesum()        -- N-1 iterative Minkowski additions
    set2mat()      -- Converts image representation from set to matrix
    setrans()      -- Translate a structuring element
    seunion()      -- Union of structuring elements
    show()         -- Display binary or gray-scale images and optionally
                      overlay it with binary images.
    skelm()        -- Morphological skeleton (Medial Axis Transform).
    skelmrec()     -- Morphological skeleton reconstruction (Inverse Medial
                      Axis Transform).
    skiz()         -- Skeleton of Influence Zone - also know as Generalized
                      Voronoi Diagram
    subm()         -- Subtraction of two images, with saturation.
    supcanon()     -- Union of sup-generating or hit-miss operators.
    supgen()       -- Sup-generating (hit-miss).
    suprec()       -- Sup-reconstruction.
    swatershed()   -- Detection of similarity-based watershed from markers.
    symdif()       -- Symmetric difference between two images
    text()         -- Create a binary image of a text.
    thick()        -- Image transformation by thickening.
    thin()         -- Image transformation by thinning.
    threshad()     -- Threshold (adaptive)
    toggle()       -- Image contrast enhancement or classification by the
                      toggle operator.
    union()        -- Union of images.
    vdome()        -- Obsolete, use mmvmax.
    vmax()         -- Remove domes with volume less than v.
    watershed()    -- Watershed detection.
    to_int32()     -- Convert an image to an int32 image.
    to_uint16()    -- Convert an image to a uint16 image.
    to_uint8()     -- Convert an image to an uint8 image.

"""
from __future__ import division
__version__ = '0.88'

__build_date__ = '16 June 2008'


import sys, os
mydir = os.path.dirname(__file__)
try:
    sys.imagepath += [os.path.join(mydir, 'data')]
except:
    sys.imagepath = [os.path.join(mydir, 'data')]


def concat(DIM, X1, X2, X3=None, X4=None):
    """
        - Purpose
            Concatenate two or more images along width, height or depth.
        - Synopsis
            Y = concat(DIM, X1, X2, X3=None, X4=None)
        - Input
            DIM: String Dimension to concatenate. 'WIDTH' or 'W', 'HEIGHT'
                 or 'H', or ' DEPTH' or 'D'.
            X1:  Gray-scale (uint8 or uint16) or binary image.
            X2:  Gray-scale (uint8 or uint16) or binary image.
            X3:  Gray-scale (uint8 or uint16) or binary image. Default:
                 None.
            X4:  Gray-scale (uint8 or uint16) or binary image. Default:
                 None.
        - Output
            Y: Gray-scale (uint8 or uint16) or binary image.
        - Description
            Concatenate two or more images in any of the dimensions: width,
            height or depth. If the images do not match the dimension, a
            larger image is create with zero pixels to accommodate them. The
            images must have the same datatype.
        - Examples
            #
            f1=readgray('cameraman.tif')
            f2=readgray('blob.tif')
            g=concat('W',f1,gray(neg(f2)))
            show(g);
    """
    from numpy import newaxis, sum, zeros

    aux = 'newaxis,'
    d = len(X1.shape)
    if d < 3: X1 = eval('X1[' + (3-d)*aux + ':]')
    d1,h1,w1 = X1.shape
    d = len(X2.shape)
    if d < 3: X2 = eval('X2[' + (3-d)*aux + ':]')
    d2,h2,w2 = X2.shape
    h3 = w3 = d3 = h4 = w4 = d4 = 0
    if X3 is not None:
       d = len(X3.shape)
       if d < 3: X3 = eval('X3[' + (3-d)*aux + ':]')
       d3,h3,w3 = X3.shape
    if X4 is not None:
       d = len(X4.shape)
       if d < 3: X4 = eval('X4[' + (3-d)*aux + ':]')
       d4,h4,w4 = X4.shape
    h = [h1, h2, h3, h4]
    w = [w1, w2, w3, w4]
    d = [d1, d2, d3, d4]
    if DIM in ['WIDTH', 'W', 'w', 'width']:
       hy, wy, dy = max(h), sum(w), max(d)
       Y = zeros((dy,hy,wy))
       Y[0:d1, 0:h1, 0 :w1   ] = X1
       Y[0:d2, 0:h2, w1:w1+w2] = X2
       if X3 is not None:
          Y[0:d3, 0:h3, w1+w2:w1+w2+w3] = X3
          if X4 is not None:
              Y[0:d4, 0:h4, w1+w2+w3::] = X4
    elif DIM in ['HEIGHT', 'H', 'h', 'height']:
       hy, wy, dy = sum(h), max(w), max(d)
       Y = zeros((dy,hy,wy))
       Y[0:d1, 0 :h1   , 0:w1] = X1
       Y[0:d2, h1:h1+h2, 0:w2] = X2
       if X3 is not None:
           Y[0:d3, h1+h2:h1+h2+h3, 0:w3] = X3
           if X4 is not None:
               Y[0:d4, h1+h2+h3::, 0:w4] = X4
    elif DIM in ['DEPTH', 'D', 'd', 'depth']:
       hy, wy, dy = max(h), max(w), sum(d)
       Y = zeros((dy,hy,wy))
       Y[0:d1    , 0:h1, 0:w1   ] = X1
       Y[d1:d1+d2, 0:h2, 0:w2] = X2
       if X3 is not None:
           Y[d1+d2:d1+d2+d3, 0:h3, 0:w3] = X3
           if X4 is not None:
               Y[d1+d2+d3::, 0:h4, 0:w4] = X4
    if Y.shape[0] == 1: # adjustment
       Y = Y[0,:,:]
    return Y

def limits(f):
    """
        - Purpose
            Get the possible minimum and maximum of an image.
        - Synopsis
            y = limits(f)
        - Input
            f: Unsigned gray-scale (uint8 or uint16), signed (int32) or
               binary image.
        - Output
            y: Vector, the first element is the infimum, the second, the
               supremum.
        - Description
            The possible minimum and the possible maximum of an image depend
            on its data type. These values are important to compute many
            morphological operators (for instance, negate of an image). The
            output is a vector, where the first element is the possible
            minimum and the second, the possible maximum.
        - Examples
            #
            print limits(binary([0, 1, 0]))
            print limits(to_uint8([0, 1, 2]))
    """
    from numpy import array, bool, uint8, uint16, int32
    code = f.dtype
    if   code == bool: y=array([0,1])
    elif code == uint8: y=array([0,255])
    elif code == uint16: y=array([0,65535])
    elif code == int32: y=array([-2147483647,2147483647])
    else:
        assert 0,'Does not accept this typecode: %s' % code
    return y


def center(f, b=None):
    """
        - Purpose
            Center filter.
        - Synopsis
            y = center(f, b=None)
        - Input
            f: Gray-scale (uint8 or uint16) or binary image.
            b: Structuring Element Default: None (3x3 elementary cross).
        - Output
            y: Image
        - Description
            center creates the image y by computing recursively the
            morphological center, relative to the structuring element b , of
            the image f .
        - Examples
            #
            f=readgray('gear.tif')
            g=center(f,sedisk(2))
            show(f)
            show(g)
    """

    if b is None: b = secross()
    y = f
    diff = 0
    while not diff:
        aux = y
        beta1 = asf(y,'COC',b,1)
        beta2 = asf(y,'OCO',b,1)
        y = union(intersec(y,beta1),beta2)
        diff = isequal(aux,y)
    return y


def close_holes(f, Bc=None):
    """
        - Purpose
            Close holes of binary and gray-scale images.
        - Synopsis
            y = close_holes(f, Bc=None)
        - Input
            f:  Gray-scale (uint8 or uint16) or binary image.
            Bc: Structuring Element Default: None (3x3 elementary cross). (
                connectivity).
        - Output
            y: (same datatype of f ).
        - Description
            close_holes creates the image y by closing the holes of the image
            f , according with the connectivity defined by the structuring
            element Bc .The images can be either binary or gray-scale.
        - Examples
            #
            #   example 1
            #
            a = readgray('pcb1bin.tif')
            b = close_holes(a)
            show(a)
            show(b)
            #
            #   example 2
            #
            a = readgray('boxdrill-B.tif')
            b = close_holes(a)
            show(a)
            show(b)
    """

    if Bc is None: Bc = secross()
    delta_f = frame(f)
    y = neg( infrec( delta_f, neg(f), Bc))
    return y


def dist(f, Bc=None, METRIC=None):
    """
        - Purpose
            Distance transform.
        - Synopsis
            y = dist(f, Bc=None, METRIC=None)
        - Input
            f:      Binary image.
            Bc:     Structuring Element Default: None (3x3 elementary
                    cross). (connectivity)
            METRIC: String Default: None. 'EUCLIDEAN', or 'EUC2' for squared
                    Euclidean.
        - Output
            y: distance image in uint16, or in int32 datatype with EUC2
               option.
        - Description
            dist creates the distance image y of the binary image f . The
            value of y at the pixel x is the distance of x to the complement
            of f , that is, the distance of x to nearest point in the
            complement of f . The distances available are based on the
            Euclidean metrics and on metrics generated by a a regular graph,
            that is characterized by a connectivity rule defined by the
            structuring element Bc . The implementation of the Euclidean
            algorithm is based on LotuZamp:01 .
        - Examples
            #
            #   example 1
            #
            a = frame(binary(ones((5,9))),2,4)
            f4=dist(a)
            f8=dist(a,sebox())
            fe=dist(a,sebox(),'EUCLIDEAN')
            #
            #   example 2
            #
            f = readgray('gear.tif')
            f = neg(gradm(f))
            d4=dist(f)
            d8=dist(f,sebox())
            de=dist(f,sebox(),'EUCLIDEAN')
            show(f)
            show(d4%8)
            show(d8%8)
            show(de%8)
    """
    from string import upper
    import numpy
    from numpy import zeros, sqrt
    if Bc is None: Bc = secross()
    if METRIC is not None:
       METRIC = upper(METRIC)
    f = gray(f,'uint16')
    y = intersec(f,0)
    if (METRIC == 'EUCLIDEAN') or (METRIC == 'EUC2'):
        b = zeros((3,3),numpy.int32)
        i=1
        while not isequal(f,y):
            a4,a2 = -4*i+2, -2*i+1
            b = to_int32([[a4,a2,a4],
                       [a2, 0,a2],
                       [a4,a2,a4]])
            y=f
            i+=1
            f = erode(f,b)
        if METRIC == 'EUCLIDEAN':
            f = to_uint16(sqrt(f)+0.5)
    else:
        if isequal(Bc, secross()):
            b = to_int32([[-2147483647,  -1, -2147483647],
                       [         -1,   0,          -1],
                       [-2147483647,  -1, -2147483647]])
        elif isequal(Bc, sebox()):
            b = to_int32([[-1,-1,-1],
                       [-1, 0,-1],
                       [-1,-1,-1]])
        else: b = Bc
        while not isequal(f,y):
            y=f
            f = erode(f,b)
    return y


def edgeoff(f, Bc=None):
    """
        - Purpose
            Eliminate the objects that hit the image frame.
        - Synopsis
            y = edgeoff(f, Bc=None)
        - Input
            f:  Binary image.
            Bc: Structuring Element Default: None (3x3 elementary cross). (
                connectivity)
        - Output
            y: Binary image.
        - Description
            edgeoff creates the binary image y by eliminating the objects
            (connected components) of the binary image f that hit the image
            frame, according to the connectivity defined by the structuring
            element Bc .
        - Examples
            #
            a=readgray('form-1.tif')
            b=edgeoff(a)
            show(a)
            show(b)
    """

    if Bc is None: Bc = secross()
    edge = frame(f)
    y = subm( f, infrec(edge, f, Bc))
    return y


def frame(f, WT=1, HT=1, DT=0, k1=None, k2=None):
    """
        - Purpose
            Create a frame image.
        - Synopsis
            y = frame(f, WT=1, HT=1, DT=0, k1=None, k2=None)
        - Input
            f:  Unsigned gray-scale (uint8 or uint16), signed (int32) or
                binary image.
            WT: Double Default: 1. Positive integer ( width thickness).
            HT: Double Default: 1. Positive integer ( height thickness).
            DT: Double Default: 0. Positive integer ( depth thickness).
            k1: Non-negative integer. Default: None (Maximum pixel value
                allowed in f). Frame gray-level.
            k2: Non-negative integer. Default: None (Minimum pixel value
                allowed in f). Background gray level.
        - Output
            y: image of same type as f .
        - Description
            frame creates an image y , with the same dimensions (W,H,D)
            and same pixel type of the image f , such that the value of the
            pixels in the image frame is k1 and the value of the other
            pixels is k2 . The thickness of the image frame is DT.

    """

    if k1 is None: k1 = limits(f)[1]
    if k2 is None: k2 = limits(f)[0]
    assert len(f.shape)<3,'Supports 2D only'
    y = union(intersec(f,limits(f)[0]),k2)
    y[:,0:WT] = k1
    y[:,-WT:] = k1
    y[0:HT,:] = k1
    y[-HT:,:] = k1
    return y


def glblshow(X, border=0.0):
    """
        - Purpose
            Apply a random color table to a gray-scale image.
        - Synopsis
            Y = glblshow(X, border=0.0)
        - Input
            X:      Gray-scale (uint8 or uint16) image. Labeled image.
            border: Boolean Default: 0.0. Labeled image.
        - Output
            Y: Gray-scale (uint8 or uint16) or binary image.

    """
    from numpy import take, resize, shape
    from numpy.random import rand

    mmin = X.min()
    mmax = X.max()
    ncolors = mmax - mmin + 1
    R = to_int32(rand(ncolors)*255)
    G = to_int32(rand(ncolors)*255)
    B = to_int32(rand(ncolors)*255)
    if mmin == 0:
       R[0],G[0],B[0] = 0,0,0
    r=resize(take(R, X.ravel() - mmin),X.shape)
    g=resize(take(G, X.ravel() - mmin),X.shape)
    b=resize(take(B, X.ravel() - mmin),X.shape)
    Y=concat('d',r,g,b)
    return Y


def gdtshow(X, N=10):
    """
        - Purpose
            Apply an iso-line color table to a gray-scale image.
        - Synopsis
            Y = gdtshow(X, N=10)
        - Input
            X: Gray-scale (uint8 or uint16) image. Distance transform image.
            N: Default: 10. Number of iso-contours.
        - Output
            Y: Gray-scale (uint8 or uint16) or binary image.

    """
    from numpy import newaxis, ravel, ceil, zeros, ones, transpose, repeat, concatenate, arange, reshape, floor

    def apply_lut(img, lut):
        def lut_map(intens, lut=lut): return lut[intens]
        g = reshape(transpose(map(lut_map, ravel(img))), (3,img.shape[0],img.shape[1]))
        return g
    np = 1  # number of pixels by isoline
    if len(X.shape) == 1: X = X[newaxis,:]
    maxi, mini = X.max(), X.min()
    d = int(ceil(256./N))
    m = zeros(256)
    m[0:256:d] = 1
    m = transpose([m,m,m])
    # lut gray
    gray = floor(arange(N)*255. // (N-1) + 0.5).astype('B')
    gray = repeat(gray, d)[0:256]
    gray = transpose([gray,gray,gray])
    # lut jet
    r = concatenate((range(126,0,-4),zeros(64),range(0,255,4),255*ones(64),range(255,128,-4)))
    g = concatenate((zeros(32),range(0,255,4),255*ones(64),range(255,0,-4),zeros(32)))
    b = 255 - r
    jet = transpose([r,g,b])
    # apply lut
    XX  = floor((X-mini)*255. // maxi + 0.5).astype('B')
    lut = (1-m)*gray + m*jet
    Y = apply_lut(XX, lut)
    return Y


def gshow(X, X1=None, X2=None, X3=None, X4=None, X5=None, X6=None):
    """
        - Purpose
            Apply binary overlays as color layers on a binary or gray-scale
            image
        - Synopsis
            Y = gshow(X, X1=None, X2=None, X3=None, X4=None, X5=None,
            X6=None)
        - Input
            X:  Gray-scale (uint8 or uint16) or binary image.
            X1: Binary image. Default: None. Red overlay.
            X2: Binary image. Default: None. Green overlay.
            X3: Binary image. Default: None. Blue overlay.
            X4: Binary image. Default: None. Magenta overlay.
            X5: Binary image. Default: None. Yellow overlay.
            X6: Binary image. Default: None. Cyan overlay.
        - Output
            Y: Gray-scale (uint8 or uint16) or binary image.

    """

    if isbinary(X): X = gray(X,'uint8')
    r = X
    g = X
    b = X
    if X1 is not None: # red 1 0 0
      assert isbinary(X1),'X1 must be binary overlay'
      x1 = gray(X1,'uint8')
      r = union(r,x1)
      g = intersec(g,neg(x1))
      b = intersec(b,neg(x1))
    if X2 is not None: # green 0 1 0
      assert isbinary(X2),'X2 must be binary overlay'
      x2 = gray(X2,'uint8')
      r = intersec(r,neg(x2))
      g = union(g,x2)
      b = intersec(b,neg(x2))
    if X3 is not None: # blue 0 0 1
      assert isbinary(X3),'X3 must be binary overlay'
      x3 = gray(X3,'uint8')
      r = intersec(r,neg(x3))
      g = intersec(g,neg(x3))
      b = union(b,x3)
    if X4 is not None: # magenta 1 0 1
      assert isbinary(X4),'X4 must be binary overlay'
      x4 = gray(X4,'uint8')
      r = union(r,x4)
      g = intersec(g,neg(x4))
      b = union(b,x4)
    if X5 is not None: # yellow 1 1 0
      assert isbinary(X5),'X5 must be binary overlay'
      x5 = gray(X5,'uint8')
      r = union(r,x5)
      g = union(g,x5)
      b = intersec(b,neg(x5))
    if X6 is not None: # cyan 0 1 1
      assert isbinary(X6),'X6 must be binary overlay'
      x6 = gray(X6,'uint8')
      r = intersec(r,neg(x6))
      g = union(g,x6)
      b = union(b,x6)
    return concat('d',r,g,b)


def histogram(f, option="uint16"):
    """
        - Purpose
            Find the histogram of the image f.
        - Synopsis
            h = histogram(f, option="uint16")
        - Input
            f:      Gray-scale (uint8 or uint16) or binary image.
            option: String Default: "uint16". Values: "uint16" or "int32".
        - Output
            h: Gray-scale (uint8 or uint16) image. Histogram in a uint16 or
               an int32 vector.
        - Description
            Finds the histogram of the image f and returns the result in the
            vector h . For binary image the vector size is 2, for gray-scale
            uint8 and uint16 images, the vector size is the maximum pixel
            value plus one. h[0] gives the number of pixels with value 0.
        - Examples
            #
            #   example 1
            #
            f=to_uint8([0, 1, 1, 2, 2, 2, 5, 3, 5])
            h=histogram(f)
            print h
            #
            #   example 2
            #
            f=readgray('lenina.tif')
            show(f)
            h=histogram(f)
            plot([[h]],[['style', 'impulses']])
    """
    from numpy import searchsorted, sort, ravel, concatenate, product

    n = searchsorted(sort(ravel(f)), range(f.max()+1))
    n = concatenate([n, [product(f.shape)]])
    h = n[1:]-n[:-1]
    return h


def label(f, Bc=None):
    """
        - Purpose
            Label a binary image.
        - Synopsis
            y = label(f, Bc=None)
        - Input
            f:  Binary image.
            Bc: Structuring Element Default: None (3x3 elementary cross). (
                connectivity).
        - Output
            y: Image If number of labels is less than 65535, the data type
               is uint16, otherwise it is int32.
        - Description
            label creates the image y by labeling the connect components
            of a binary image f , according to the connectivity defined by
            the structuring element Bc . The background pixels (with value
            0) are not labeled. The maximum label value in the output image
            gives the number of its connected components.
        - Examples
            #
            #   example 1
            #
            f=binary([
               [0,1,0,1,1],
               [1,0,0,1,0]])
            g=label(f)
            print g
            #
            #   example 2
            #
            f = readgray('blob3.tif')
            g=label(f)
            nblobs=g.max()
            print nblobs
            show(f)
            lblshow(g)
    """
    from numpy import allclose, ravel, nonzero, array
    if Bc is None: Bc = secross()
    assert isbinary(f),'Can only label binary image'
    zero = subm(f,f)               # zero image
    faux=f
    r = array(zero)
    label = 1
    y = gray( f,'uint16',0)        # zero image (output)
    while not allclose(faux,0):
        x=nonzero(ravel(faux))[0]      # get first unlabeled pixel
        fmark = array(zero)
        fmark.flat[x] = 1              # get the first unlabeled pixel
        r = infrec( fmark, faux, Bc) # detects all pixels connected to it
        faux = subm( faux, r)        # remove them from faux
        r = gray( r,'uint16',label)  # label them with the value label
        y = union( y, r)             # merge them with the labeled image
        label = label + 1
    return y


def neg(f):
    """
        - Purpose
            Negate an image.
        - Synopsis
            y = neg(f)
        - Input
            f: Unsigned gray-scale (uint8 or uint16), signed (int32) or
               binary image.
        - Output
            y: Unsigned gray-scale (uint8 or uint16), signed (int32) or
               binary image.
        - Description
            neg returns an image y that is the negation (i.e., inverse or
            involution) of the image f . In the binary case, y is the
            complement of f .
        - Examples
            #
            #   example 1
            #
            f=to_uint8([255, 255, 0, 10, 20, 10, 0, 255, 255])
            print neg(f)
            print neg(to_uint8([0, 1]))
            print neg(to_int32([0, 1]))
            #
            #   example 2
            #
            a = readgray('gear.tif')
            b = neg(a)
            show(a)
            show(b)
            #
            #   example 3
            #
            c = readgray('astablet.tif')
            d = neg(c)
            show(c)
            show(d)
    """

    y = limits(f)[0] + limits(f)[1] - f
    y = y.astype(f.dtype)
    return y


def threshad(f, f1, f2=None):
    """
        - Purpose
            Threshold (adaptive)
        - Synopsis
            y = threshad(f, f1, f2=None)
        - Input
            f:  Gray-scale (uint8 or uint16) image.
            f1: Gray-scale (uint8 or uint16) image. lower value
            f2: Gray-scale (uint8 or uint16) image. Default: None. upper
                value
        - Output
            y: Binary image.
        - Description
            threshad creates the image y as the threshold of the image f
            by the images f1 and f2 . A pixel in y has the value 1 when the
            value of the corresponding pixel in f is between the values of
            the corresponding pixels in f1 and f2 .
        - Examples
            #
            a = readgray('keyb.tif')
            show(a)
            b = threshad(a,to_uint8(10), to_uint8(50))
            show(b)
            c = threshad(a,238)
            show(c)
    """

    if f2 is None: 
      y = binary(f1 <= f)
    else:
      y = binary((f1 <= f) & (f <= f2))
    return y


def toggle(f, f1, f2, OPTION="GRAY"):
    """
        - Purpose
            Image contrast enhancement or classification by the toggle
            operator.
        - Synopsis
            y = toggle(f, f1, f2, OPTION="GRAY")
        - Input
            f:      Gray-scale (uint8 or uint16) image.
            f1:     Gray-scale (uint8 or uint16) image.
            f2:     Gray-scale (uint8 or uint16) image.
            OPTION: String Default: "GRAY". Values: 'BINARY' or 'GRAY'.
        - Output
            y: Image binary image if option is 'BINARY' or same type as f
        - Description
            toggle creates the image y that is an enhancement or
            classification of the image f by the toggle operator, with
            parameters f1 and f2 . If the OPTION is 'GRAY', it performs an
            enhancement and, if the OPTION is 'BINARY', it performs a binary
            classification. In the enhancement, a pixel takes the value of
            the corresponding pixel in f1 or f2 , according to a minimum
            distance criterion from f to f1 or f to f2 . In the
            classification, the pixels in f nearest to f1 receive the value
            0 , while the ones nearest to f2 receive the value 1.
        - Examples
            #
            #   example 1
            #
            f = to_uint8([0,1,2,3,4,5,6])
            print f
            f1 = to_uint8([0,0,0,0,0,0,0])
            print f1
            f2 = to_uint8([6,6,6,6,6,6,6])
            print f2
            print toggle(f,f1,f2)
            #
            #   example 2
            #
            a = readgray('angiogr.tif')
            b = erode(a,sedisk(2))
            c = dilate(a,sedisk(2))
            d = toggle(a,b,c)
            show(a)
            show(d)
            #
            #   example 3
            #
            e = readgray('lenina.tif')
            f = erode(e,sedisk(2))
            g = dilate(e,sedisk(2))
            h = toggle(e,f,g,'BINARY')
            show(e)
            show(h)
    """
    from string import upper

    y=binary(subm(f,f1),subm(f2,f))
    if upper(OPTION) == 'GRAY':
        t=gray(y)
        y=union(intersec(neg(t),f1),intersec(t,f2))
    return y


def addm(f1, f2):
    """
        - Purpose
            Addition of two images, with saturation.
        - Synopsis
            y = addm(f1, f2)
        - Input
            f1: Unsigned gray-scale (uint8 or uint16), signed (int32) or
                binary image.
            f2: Unsigned gray-scale (uint8 or uint16), signed (int32) or
                binary image. Or constant.
        - Output
            y: Unsigned gray-scale (uint8 or uint16), signed (int32) or
               binary image.
        - Description
            addm creates the image y by pixelwise addition of images f1
            and f2 . When the addition of the values of two pixels saturates
            the image data type considered, the greatest value of this type
            is taken as the result of the addition.
        - Examples
            #
            #   example 1
            #
            f = to_uint8([255,   255,    0,   10,    0,   255,   250])
            g = to_uint8([ 0,    40,   80,   140,  250,    10,    30])
            y1 = addm(f,g)
            print y1
            y2 = addm(g, 100)
            print y2
            #
            #   example 2
            #
            a = readgray('keyb.tif')
            b = addm(a,128)
            show(a)
            show(b)
    """
    from numpy import array, minimum, maximum

    if type(f2) is array:
        assert f1.dtype == f2.dtype, 'Cannot have different datatypes:'
    y = maximum(minimum(f1.astype('d')+f2, limits(f1)[1]),limits(f1)[0])
    y = y.astype(f1.dtype)
    return y


def areaclose(f, a, Bc=None):
    """
        - Purpose
            Area closing
        - Synopsis
            y = areaclose(f, a, Bc=None)
        - Input
            f:  Gray-scale (uint8 or uint16) or binary image.
            a:  Double non negative integer.
            Bc: Structuring Element Default: None (3x3 elementary cross). (
                connectivity).
        - Output
            y: Same type of f
        - Description
            areaclose removes any pore (i.e., background connected
            component) with area less than a of a binary image f . The
            connectivity is given by the structuring element Bc . This
            operator is generalized to gray-scale images by applying the
            binary operator successively on slices of f taken from higher
            threshold levels to lower threshold levels.
        - Examples
            #
            #   example 1
            #
            a=readgray('form-1.tif')
            b=areaclose(a,400)
            show(a)
            show(b)
            #
            #   example 2
            #
            a=readgray('n2538.tif')
            b=areaclose(a,400)
            show(a)
            show(b)
    """

    if Bc is None: Bc = secross()
    y = neg(areaopen(neg(f),a,Bc))
    return y


def areaopen(f, a, Bc=None):
    """
        - Purpose
            Area opening
        - Synopsis
            y = areaopen(f, a, Bc=None)
        - Input
            f:  Gray-scale (uint8 or uint16) or binary image.
            a:  Double non negative integer.
            Bc: Structuring Element Default: None (3x3 elementary cross). (
                connectivity).
        - Output
            y: Same type of f
        - Description
            areaopen removes any grain (i.e., connected component) with
            area less than a of a binary image f . The connectivity is given
            by the structuring element Bc . This operator is generalized to
            gray-scale images by applying the binary operator successively
            on slices of f taken from higher threshold levels to lower
            threshold levels.
        - Examples
            #
            #   example 1
            #
            f=binary(to_uint8([
             [1, 1, 0, 0, 0, 0, 1],
             [1, 0, 1, 1, 1, 0, 1],
             [0, 0, 0, 0, 1, 0, 0]]))
            y=areaopen(f,4,secross())
            print y
            #
            #   example 2
            #
            f=to_uint8([
               [10,   11,   0,    0,   0,   0,  20],
               [10,    0,   5,    8,   9,   0,  15],
               [10,    0,   0,    0,  10,   0,   0]])
            y=areaopen(f,4,secross())
            print y
            #
            #   example 3
            #
            a=readgray('form-1.tif');
            b=areaopen(a,500);
            show(a);
            show(b);
            #
            #   example 4
            #
            a=readgray('bloodcells.tif');
            b=areaopen(a,500);
            show(a);
            show(b);
    """

    if Bc is None: Bc = secross()
    if isbinary(f):
      fr = label(f,Bc)      # binary area open, use area measurement
      g = blob(fr,'area')
      y = threshad(g,a)
    else:
      y = intersec(f,0)
      zero = binary(y)
      k1 = f.min()
      k2 = f.max()
      for k in xrange(k1,k2+1):   # gray-scale, use thresholding decomposition
        fk = threshad(f,k)
        fo = areaopen(fk,a,Bc)
        if isequal(fo,zero):
          break
        y = union(y, gray(fo,datatype(f),k))
    return y


def flood(fin, T, option, Bc=None):
    """
        - Purpose
            Flooding filter- h,v,a-basin and dynamics (depth, area, volume)
        - Synopsis
            y = flood(fin, T, option, Bc=None)
        - Input
            fin:    Gray-scale (uint8 or uint16) image.
            T:      Criterion value. If T==-1, then the dynamics is
                    determined, not the flooding at this criterion. This was
                    selected just to use the same algoritm to compute two
                    completely distinct functions.
            option: String Default: "". criterion: 'AREA', 'VOLUME', 'H'.
            Bc:     Structuring Element Default: None (3x3 elementary
                    cross). Connectivity.
        - Output
            y: Gray-scale (uint8 or uint16) image.
        - Description
            This is a flooding algorithm. It is the basis to implement many
            topological functions. It is a connected filter that floods an
            image following some topological criteria: area, volume, depth.
            These filters are equivalent to area-close, volume-basin or
            h-basin, respectively. This code may be difficult to understand
            because of its many options. Basically, when t is negative, the
            generalized dynamics: area, volume, h is computed. When the
            flooding is computed, every time a new level in the flooding
            happens, a test is made to verify if the criterion has reached.
            This is used to set the value to that height. This value image
            will be used later for sup-reconstruction (flooding) at that
            particular level. This test happens in the raising of the water
            and in the merging of basins.

    """

    if Bc is None: Bc = secross()
    print 'Not implemented yet'
    return None
    return y


def asf(f, SEQ="OC", b=None, n=1):
    """
        - Purpose
            Alternating Sequential Filtering
        - Synopsis
            y = asf(f, SEQ="OC", b=None, n=1)
        - Input
            f:   Gray-scale (uint8 or uint16) or binary image.
            SEQ: String Default: "OC". 'OC', 'CO', 'OCO', 'COC'.
            b:   Structuring Element Default: None (3x3 elementary cross).
            n:   Non-negative integer. Default: 1. (number of iterations).
        - Output
            y: Image
        - Description
            asf creates the image y by filtering the image f by n
            iterations of the close and open alternating sequential filter
            characterized by the structuring element b . The sequence of
            opening and closing is controlled by the parameter SEQ . 'OC'
            performs opening after closing, 'CO' performs closing after
            opening, 'OCO' performs opening after closing after opening, and
            'COC' performs closing after opening after closing.
        - Examples
            #
            #   example 1
            #
            f=readgray('gear.tif')
            g=asf(f,'oc',secross(),2)
            show(f)
            show(g)
            #
            #   example 2
            #
            f=readgray('fabric.tif')
            g=asf(f,'oc',secross(),3)
            show(f)
            show(g)
    """
    from string import upper
    if b is None: b = secross()
    SEQ=upper(SEQ)
    y = f
    if SEQ == 'OC':
        for i in xrange(1,n+1):
            nb = sesum(b,i)
            y = open(close(y,nb),nb)
    elif SEQ == 'CO':
        for i in xrange(1,n+1):
            nb = sesum(b,i)
            y = close(open(y,nb),nb)
    elif SEQ == 'OCO':
        for i in xrange(1,n+1):
            nb = sesum(b,i)
            y = open(close(open(y,nb),nb),nb)
    elif SEQ == 'COC':
        for i in xrange(1,n+1):
            nb = sesum(b,i)
            y = close(open(close(y,nb),nb),nb)
    return y


def asfrec(f, SEQ="OC", b=None, bc=None, n=1):
    """
        - Purpose
            Reconstructive Alternating Sequential Filtering
        - Synopsis
            y = asfrec(f, SEQ="OC", b=None, bc=None, n=1)
        - Input
            f:   Gray-scale (uint8 or uint16) or binary image.
            SEQ: String Default: "OC". Values: "OC" or "CO".
            b:   Structuring Element Default: None (3x3 elementary cross).
            bc:  Structuring Element Default: None (3x3 elementary cross).
            n:   Non-negative integer. Default: 1. (number of iterations).
        - Output
            y: Same type of f
        - Description
            asf creates the image y by filtering the image f by n
            iterations of the close by reconstruction and open by
            reconstruction alternating sequential filter characterized by
            the structuring element b . The structure element bc is used in
            the reconstruction. The sequence of opening and closing is
            controlled by the parameter SEQ . 'OC' performs opening after
            closing, and 'CO' performs closing after opening.
        - Examples
            #
            f=readgray('fabric.tif')
            g=asfrec(f,'oc',secross(),secross(),3)
            show(f)
            show(g)
    """
    from string import upper
    if b is None: b = secross()
    if bc is None: bc = secross()
    SEQ = upper(SEQ)
    y = f
    if SEQ == 'OC':
        for i in xrange(1,n+1):
            nb = sesum(b,i)
            y = closerec(y,nb,bc)
            y = openrec(y,nb,bc)
    elif SEQ == 'CO':
        for i in xrange(1,n+1):
            nb = sesum(b,i)
            y = openrec(y,nb,bc)
            y = closerec(y,nb,bc)
    else:
        assert 0,'Only accepts OC or CO for SEQ parameter'
    return y


def binary(f, k=1):
    """
        - Purpose
            Convert a gray-scale image into a binary image
        - Synopsis
            y = binary(f, k1=1)
        - Input
            f:  Unsigned gray-scale (uint8 or uint16), signed (int32) or
                binary image.
            k1: Double Default: 1. Threshold value.
        - Output
            y: Binary image.
        - Description
            binary converts a gray-scale image f into a binary image y by
            a threshold rule. A pixel in y has the value 1 if and only if
            the corresponding pixel in f has a value greater or equal k1 .
        - Examples
            #
            #   example 1
            #
            a = array([0, 1, 2, 3, 4])
            b=binary(a)
            print b
            #
            #   example 2
            #
            a=readgray('3.tif')
            b=binary(a,82)
            show(a)
            show(b)
    """
    from numpy import asarray
    f=asarray(f)
    return (f >= k)


def blob(fr, measurement, option="image"):
    """
        - Purpose
            Blob measurements from a labeled image.
        - Synopsis
            y = blob(fr, measurement, option="image")
        - Input
            fr:          Gray-scale (uint8 or uint16) image. Labeled image.
            measurement: String Default: "". Choice from 'AREA', 'CENTROID',
                         or 'BOUNDINGBOX'.
            option:      String Default: "image". Output format: 'image':
                         results as a binary image; 'data': results a column
                         vector of measurements (double).
        - Output
            y: Gray-scale (uint8 or uint16) or binary image.
        - Description
            Take measurements from the labeled image fr.
            The measurements are:
                area,
                centroid,
                bounding rectangle.
                
            The parameter option controls the output format:
                'IMAGE': the result is an image;
                'DATA': the result is a double column vector with the
                measurement for each blob.
                
            The region with label zero is not measured as it is normally
            the background. The measurement of region with label 1 appears
            at the first row of the output.
        - Examples
            #
            #   example 1
            #
            fr=to_uint8([
               [1,1,1,0,0,0],
               [1,1,1,0,0,2],
               [1,1,1,0,2,2]])
            f_area=blob(fr,'area')
            print f_area
            f_cent=blob(fr,'centroid')
            print f_cent
            f_bb=blob(fr,'boundingbox')
            print f_bb
            d_area=blob(fr,'area','data')
            print d_area
            d_cent=blob(fr,'centroid','data')
            print d_cent
            d_bb=blob(fr,'boundingbox','data')
            print d_bb
            #
            #   example 2
            #
            f=readgray('blob3.tif')
            fr=label(f)
            g=blob(fr,'area')
            show(f)
            show(g)
            #
            #   example 3
            #
            f=readgray('blob3.tif')
            fr=label(f)
            centr=blob(fr,'centroid')
            show(f,dilate(centr))
            #
            #   example 4
            #
            f=readgray('blob3.tif')
            fr=label(f)
            box=blob(fr,'boundingbox')
            show(f,box)
    """
    import numpy
    from numpy import newaxis, ravel, zeros, sum, nonzero, array
    from string import upper

    measurement = upper(measurement)
    option      = upper(option)
    if len(fr.shape) == 1: fr = fr[newaxis,:]
    n = fr.max()
    if option == 'DATA':
        y = []
    elif measurement == 'CENTROID':
        y = zeros(fr.shape,numpy.bool)
    else:
        y = zeros(fr.shape,numpy.int32)
    if measurement == 'AREA':
        for i in xrange(1,n+1):
            aux  = (fr==i)
            area = aux.sum()
            if option == 'DATA': y.append(area)
            else               : y += area*aux
    elif measurement == 'CENTROID':
        for i in xrange(1,n+1):
            aux  = (fr==i)
            ind,  = nonzero(ravel(aux))
            indx = ind // fr.shape[1]
            indy = ind % fr.shape[1]
            centroid = [sum(indx)//len(ind), sum(indy)//len(ind)]
            if option == 'DATA': y.append([centroid[1],centroid[0]])
            else               : y[centroid] = 1
    elif measurement == 'BOUNDINGBOX':
        for i in xrange(1,n+1):
            aux = fr==i
            aux1, aux2 = aux.any(0), aux.any(1)
            col , row  = nonzero(aux1)  , nonzero(aux2)
            if option == 'DATA': y.append([col[0],row[0],col[-1],row[-1]])
            else:
                y[row[0]:row[-1],col[0] ] = 1
                y[row[0]:row[-1],col[-1]] = 1
                y[row[0], col[0]:col[-1]] = 1
                y[row[-1],col[0]:col[-1]] = 1
    else:
        print "Measurement option should be 'AREA','CENTROID', or 'BOUNDINGBOX'."
    if option == 'DATA':
        y = array(y)
        if len(y.shape) == 1: y = y[:,newaxis]
    return y


def cbisector(f, B, n):
    """
        - Purpose
            N-Conditional bisector.
        - Synopsis
            y = cbisector(f, B, n)
        - Input
            f: Binary image.
            B: Structuring Element
            n: positive integer ( filtering rate)
        - Output
            y: Binary image.
        - Description
            cbisector creates the binary image y by performing a filtering
            of the morphological skeleton of the binary image f , relative
            to the structuring element B . The strength of this filtering is
            controlled by the parameter n. Particularly, if n=0 , y is the
            morphological skeleton of f itself.
        - Examples
            #
            a=readgray('blob2.tif')
            b=cbisector(a,sebox(),1)
            c=cbisector(a,sebox(),3)
            d=cbisector(a,sebox(),10)
            show(a,b)
            show(a,c)
            show(a,d)
    """

    y = intersec(f,0)
    for i in xrange(n):
        nb = sesum(B,i)
        nbp = sesum(B,i+1)
        f1 = erode(f,nbp)
        f2 = cdilate(f1,f,B,n)
        f3 = subm(erode(f,nb),f2)
        y  = union(y,f3)
    return y


def cdilate(f, g, b=None, n=1):
    """
        - Purpose
            Dilate an image conditionally.
        - Synopsis
            y = cdilate(f, g, b=None, n=1)
        - Input
            f: Gray-scale (uint8 or uint16) or binary image.
            g: Gray-scale (uint8 or uint16) or binary image. Conditioning
               image.
            b: Structuring Element Default: None (3x3 elementary cross).
            n: Non-negative integer. Default: 1. (number of iterations).
        - Output
            y: Image
        - Description
            cdil creates the image y by dilating the image f by the
            structuring element b conditionally to the image g . This
            operator may be applied recursively n times.
        - Examples
            #
            #   example 1
            #
            f = binary(to_uint8([[1, 0, 0, 0, 0, 0, 0],\
                [0, 0, 0, 0, 0, 0, 0],\
                [0, 0, 0, 0, 1, 0, 0,]]))
            g = binary(to_uint8([[1, 1, 1, 0, 0, 1, 1],\
                [1, 0, 1, 1, 1, 0, 0],\
                [0, 0, 0, 0, 1, 0, 0]]));
            y1=cdilate(f,g,secross())
            y2=cdilate(f,g,secross(),3)
            #
            #   example 2
            #
            f = to_uint8([\
                [   0,    0,   0,   80,   0,   0],\
                [   0,    0,   0,    0,   0,   0],\
                [  10,   10,   0,  255,   0,   0]])
            g = to_uint8([\
                [   0,    1,   2,   50,   4,   5],\
                [   2,    3,   4,    0,   0,   0],\
                [  12,  255,  14,   15,  16,  17]])
            y1=cdilate(f,g,secross())
            y2=cdilate(f,g,secross(),3)
            #
            #   example 3
            #
            g=readgray('pcb1bin.tif')
            f=frame(g,5,5)
            y5=cdilate(f,g,secross(),5)
            y25=cdilate(f,g,secross(),25)
            show(g)
            show(g,f)
            show(g,y5)
            show(g,y25)
            #
            #   example 4
            #
            g=neg(readgray('n2538.tif'))
            f=intersec(g,0)
            f=draw(f,'LINE:40,30,60,30:END')
            y1=cdilate(f,g,sebox())
            y30=cdilate(f,g,sebox(),30)
            show(g)
            show(f)
            show(y1)
            show(y30)
    """

    if b is None: b = secross()
    y = intersec(f,g)
    for i in xrange(n):
        aux = y
        y = intersec(dilate(y,b),g)
        if isequal(y,aux): break
    return y


def cerode(f, g, b=None, n=1):
    """
        - Purpose
            Erode an image conditionally.
        - Synopsis
            y = cerode(f, g, b=None, n=1)
        - Input
            f: Gray-scale (uint8 or uint16) or binary image.
            g: Gray-scale (uint8 or uint16) or binary image. Conditioning
               image.
            b: Structuring Element Default: None (3x3 elementary cross).
            n: Non-negative integer. Default: 1. (number of iterations).
        - Output
            y: Image
        - Description
            cero creates the image y by eroding the image f by the
            structuring element b conditionally to g . This operator may be
            applied recursively n times.
        - Examples
            #
            f = neg(text('hello'))
            show(f)
            g = dilate(f,seline(7,90))
            show(g)
            a1=cerode(g,f,sebox())
            show(a1)
            a13=cerode(a1,f,sebox(),13)
            show(a13)
    """

    if b is None: b = secross()
    y = union(f,g)
    for i in xrange(n):
        aux = y
        y = union(erode(y,b),g)
        if isequal(y,aux): break
    return y


def close(f, b=None):
    """
        - Purpose
            Morphological closing.
        - Synopsis
            y = close(f, b=None)
        - Input
            f: Gray-scale (uint8 or uint16) or binary image.
            b: Structuring Element Default: None (3x3 elementary cross).
        - Output
            y: Image
        - Description
            close creates the image y by the morphological closing of the
            image f by the structuring element b . In the binary case, the
            closing by a structuring element B may be interpreted as the
            intersection of all the binary images that contain the image f
            and have a hole equal to a translation of B . In the gray-scale
            case, there is a similar interpretation taking the functions
            umbra.
        - Examples
            #
            #   example 1
            #
            f=readgray('blob.tif')
            bimg=readgray('blob1.tif')
            b=img2se(bimg)
            show(f)
            show(close(f,b))
            show(close(f,b),gradm(f))
            #
            #   example 2
            #
            f = readgray('form-1.tif')
            show(f)
            y = close(f,sedisk(4))
            show(y)
            #
            #   example 3
            #
            f = readgray('n2538.tif')
            show(f)
            y = close(f,sedisk(3))
            show(y)
    """

    if b is None: b = secross()
    y = erode(dilate(f,b),b)
    return y


def closerec(f, bdil=None, bc=None):
    """
        - Purpose
            Closing by reconstruction.
        - Synopsis
            y = closerec(f, bdil=None, bc=None)
        - Input
            f:    Gray-scale (uint8 or uint16) or binary image.
            bdil: Structuring Element Default: None (3x3 elementary cross).
                  (dilation).
            bc:   Structuring Element Default: None (3x3 elementary cross).
                  ( connectivity).
        - Output
            y: Same type of f .
        - Description
            closerec creates the image y by a sup-reconstruction ( with
            the connectivity defined by the structuring element bc ) of the
            image f from its dilation by bdil .
        - Examples
            #
            a = readgray('danaus.tif')
            show(a)
            b = closerec(a,sebox(4))
            show(b)
    """

    if bdil is None: bdil = secross()
    if bc is None: bc = secross()
    y = suprec(dilate(f,bdil),f,bc)
    return y


def closerecth(f, bdil=None, bc=None):
    """
        - Purpose
            Close-by-Reconstruction Top-Hat.
        - Synopsis
            y = closerecth(f, bdil=None, bc=None)
        - Input
            f:    Gray-scale (uint8 or uint16) or binary image.
            bdil: Structuring Element Default: None (3x3 elementary cross).
                  (dilation)
            bc:   Structuring Element Default: None (3x3 elementary cross).
                  ( connectivity)
        - Output
            y: Gray-scale (uint8 or uint16) or binary image.
        - Description
            closerecth creates the image y by subtracting the image f of
            its closing by reconstruction, defined by the structuring
            elements bc and bdil .
        - Examples
            #
            a = readgray('danaus.tif')
            show(a)
            b = closerecth(a,sebox(4))
            show(b)
    """

    if bdil is None: bdil = secross()
    if bc is None: bc = secross()
    y = subm(closerec(f,bdil,bc), f)
    return y


def closeth(f, b=None):
    """
        - Purpose
            Closing Top Hat.
        - Synopsis
            y = closeth(f, b=None)
        - Input
            f: Gray-scale (uint8 or uint16) or binary image.
            b: Structuring Element Default: None (3x3 elementary cross).
        - Output
            y: Gray-scale (uint8 or uint16) or binary image. (Same type of f
               ).
        - Description
            closeth creates the image y by subtracting the image f of its
            morphological closing by the structuring element b .
        - Examples
            #
            a = readgray('danaus.tif')
            show(a)
            b = closeth(a,sebox(5))
            show(b)
    """

    if b is None: b = secross()
    return subm( close(f,b), f)


def cthick(f, g, Iab=None, n=-1, theta=45, DIRECTION="CLOCKWISE"):
    """
        - Purpose
            Image transformation by conditional thickening.
        - Synopsis
            y = cthick(f, g, Iab=None, n=-1, theta=45,
            DIRECTION="CLOCKWISE")
        - Input
            f:         Binary image.
            g:         Binary image.
            Iab:       Interval Default: None (homothick).
            n:         Non-negative integer. Default: -1. Number of
                       iterations.
            theta:     Double Default: 45. Degrees of rotation: 45, 90, or
                       180.
            DIRECTION: String Default: "CLOCKWISE". 'CLOCKWISE' or
                       'ANTI-CLOCKWISE'.
        - Output
            y: Binary image.
        - Description
            cthick creates the binary image y by performing a thickening
            of the binary image f conditioned to the binary image g . The
            number of iterations of the conditional thickening is n and in
            each iteration the thickening is characterized by rotations of
            theta of the interval Iab .
        - Examples
            #
            #   example 1
            #
            f=readgray('blob2.tif')
            show(f)
            t=se2hmt(binary([[0,0,0],[0,0,1],[1,1,1]]),
                                      binary([[0,0,0],[0,1,0],[0,0,0]]))
            print intershow(t)
            f1=thick(f,t,40); # The thickening makes the image border grow
            show(f1)
            #
            #   example 2
            #
            f2=cthick(f,neg(frame(f)),t,40) # conditioning to inner pixels
            fn=cthick(f,neg(frame(f)),t) #pseudo convex hull
            show(f2)
            show(fn,f)
    """
    from numpy import product
    from string import upper
    if Iab is None: Iab = homothick()
    DIRECTION = upper(DIRECTION)            
    assert isbinary(f),'f must be binary image'
    if n == -1: n = product(f.shape)
    y = f
    old = y
    for i in xrange(n):
        for t in xrange(0,360,theta):
            sup = supgen( y, interot(Iab, t, DIRECTION))
            y = intersec(union( y, sup),g)
        if isequal(old,y): break
        old = y
    return y


def cthin(f, g, Iab=None, n=-1, theta=45, DIRECTION="CLOCKWISE"):
    """
        - Purpose
            Image transformation by conditional thinning.
        - Synopsis
            y = cthin(f, g, Iab=None, n=-1, theta=45,
            DIRECTION="CLOCKWISE")
        - Input
            f:         Binary image.
            g:         Binary image.
            Iab:       Interval Default: None (homothin).
            n:         Non-negative integer. Default: -1. Number of
                       iterations.
            theta:     Double Default: 45. Degrees of rotations: 45, 90, or
                       180.
            DIRECTION: String Default: "CLOCKWISE". 'CLOCKWISE' or '
                       ANTI-CLOCKWISE'.
        - Output
            y: Binary image.
        - Description
            cthin creates the binary image y by performing a thinning of
            the binary image f conditioned to the binary image g . The
            number of iterations of the conditional thinning is n and in
            each iteration the thinning is characterized by rotations of
            theta of the interval Iab .

    """
    from numpy import product
    from string import upper
    if Iab is None: Iab = homothin()
    DIRECTION = upper(DIRECTION)            
    assert isbinary(f),'f must be binary image'
    if n == -1: n = product(f.shape)
    y = f
    old = y
    for i in xrange(n):
        for t in xrange(0,360,theta):
            sup = supgen( y, interot(Iab, t, DIRECTION))
            y = union(subm( y, sup),g)
        if isequal(old,y): break
        old = y
    return y


def cwatershed(f, g, Bc=None, LINEREG="LINES"):
    """
        - Purpose
            Detection of watershed from markers.
        - Synopsis
            Y = cwatershed(f, g, Bc=None, LINEREG="LINES")
        - Input
            f:       Gray-scale (uint8 or uint16) image.
            g:       Gray-scale (uint8 or uint16) or binary image. marker
                     image: binary or labeled.
            Bc:      Structuring Element Default: None (3x3 elementary
                     cross). (watershed connectivity)
            LINEREG: String Default: "LINES". 'LINES' or ' REGIONS'.
        - Output
            Y: Gray-scale (uint8 or uint16) or binary image.
        - Description
            cwatershed creates the image y by detecting the domain of the
            catchment basins of f indicated by the marker image g ,
            according to the connectivity defined by Bc . According to the
            flag LINEREG y will be a labeled image of the catchment basins
            domain or just a binary image that presents the watershed lines.
            To know more about watershed and watershed from markers, see
            BeucMeye:93 . The implementation of this function is based on
            LotuFalc:00 . WARNING: There is a coon mistake related to the
            marker image g . If this image contains only zeros and ones, but
            it is not a binary image, the result will be an image with all
            ones. If the marker image is binary, you have to set this
            explicitly using the logical function.
        - Examples
            #
            #   example 1
            #
            a = to_uint8([\
                [10,   10,   10,   10,   10,   10,   10],\
                [10,    9,    6,   18,    6,    5,   10],\
                [10,    9,    6,   18,    6,    8,   10],\
                [10,    9,    9,   15,    9,    9,   10],\
                [10,    9,    9,   15,   12,   10,   10],\
                [10,   10,   10,   10,   10,   10,   10]])
            b = (a == 6)
            print cwatershed(a,b)
            print cwatershed(a,b,secross(),'REGIONS')
            #
            #   example 2
            #
            f=readgray('astablet.tif')
            grad=gradm(f)
            mark=regmin(hmin(grad,17))
            w=cwatershed(grad,mark)
            show(grad)
            show(mark)
            show(w)
    """
    from numpy import ones, zeros, nonzero, array, put, take, argmin, transpose, compress, concatenate
    if Bc is None: Bc = secross()
    return g
    print 'starting'
    withline = (LINEREG == 'LINES')
    if isbinary(g):
        g = label(g,Bc)
    print 'before 1. pad4n'
    status = pad4n(to_uint8(zeros(f.shape)),Bc, 3)
    f = pad4n( f,Bc,0)                 #pad input image
    print 'before 2. pad4n'
    y = pad4n( g,Bc,0)                  # pad marker image with 0
    if withline:
        y1 = intersec(binary(y), 0)
    costM = limits(f)[1] * ones(f.shape)  # cuulative cost function image
    mi = nonzero(gradm(y,sebox(0),Bc).ravel())  # 1D index of internal contour of marker
    print 'before put costM'
    put(costM.ravel(),mi, 0)
    HQueue=transpose([mi, take(costM.ravel(), mi)])       # init hierarquical queue: index,value
    print 'before se2list0'
    Bi=se2list0(f,Bc)                # get 1D displacement neighborhood pixels
    x,v = mat2set(Bc)
    while HQueue:
        print 'Hq=',HQueue
        i = argmin(HQueue[:,1])           # i is the index of minimum value
        print 'imin=',i
        pi = HQueue[i,0]
        print 'pi=',pi
        ii = ones(HQueue.shape[0])
        ii[i] = 0
        print 'ii=',ii
        HQueue = transpose(array([compress(ii,HQueue[:,0]),
                                  compress(ii,HQueue[:,1])])) # remove this pixel from queue
        print 'H=',HQueue
        put(status.ravel(), pi, 1)          # make it a permanent label
        for qi in pi+Bi :                # for each neighbor of pi
            if (status.flat[qi] != 3):          # not image border
                if (status.flat[qi] != 1):        # if not permanent
                    cost_M = max(costM.flat[pi], f.flat[qi])
                    if cost_M < costM.flat[qi]:
                        print 'qi=',qi
                        costM.flat[qi] = cost_M
                        y.flat[qi] = y.flat[pi]                  # propagate the label
                        aux = zeros(array(HQueue.shape) + [1,0])
                        aux[:-1,:] = HQueue
                        aux[-1,:]=[qi, cost_M]
                        HQueue = aux # insert pixel in the queue
                        print 'insert H=',HQueue
                elif (withline        and
                     (y.flat[qi] != y.flat[pi]) and
                     (y1.flat[pi] == 0)    and
                     (y1.flat[qi] == 0)     ):
                    y1.flat[pi] = 1
    if withline:
        Y = y1
    else:
        Y = y
    return Y


def dilate(f, b=None):
    """
        - Purpose
            Dilate an image by a structuring element.
        - Synopsis
            y = dilate(f, b=None)
        - Input
            f: Gray-scale (uint8 or uint16) or binary image.
            b: Structuring Element Default: None (3x3 elementary cross).
        - Output
            y: Image
        - Description
            dil performs the dilation of image f by the structuring
            element b . Dilation is a neighbourhood operator that compares
            locally b with f , according to an intersection rule. Since
            Dilation is a fundamental operator to the construction of all
            other morphological operators, it is also called an elementary
            operator of Mathematical Morphology. When f is a gray-scale
            image, b may be a flat or non-flat structuring element.
        - Examples
            #
            #   example 1
            #
            f=binary([
               [0, 0, 0, 0, 0, 0, 1],
               [0, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 0, 0]])
            b=binary([1, 1, 0])
            dilate(f,b)
            f=to_uint8([
               [ 0,   1,  2, 50,  4,  5],
               [ 2,   3,  4,  0,  0,  0],
               [12, 255, 14, 15, 16, 17]])
            dilate(f,b)
            #
            #   example 2
            #
            f=binary(readgray('blob.tif'))
            bimg=binary(readgray('blob1.tif'))
            b=img2se(bimg)
            show(f)
            show(dilate(f,b))
            show(dilate(f,b),gradm(f))
            #
            #   example 3
            #
            f=readgray('pcb_gray.tif')
            b=sedisk(5)
            show(f)
            show(dilate(f,b))
    """
    from numpy import maximum, newaxis, ones, int32
    if b is None: b = secross()
    if len(f.shape) == 1: f = f[newaxis,:]
    h,w = f.shape
    x,v = mat2set(b)
    if len(x)==0:
        y = (ones((h,w),int32) * limits(f)[0]).astype(f.dtype)
    else:
        if isbinary(v):
            v = intersec(gray(v,'int32'),0)
        mh,mw = max(abs(x)[:,0]),max(abs(x)[:,1])
        y = (ones((h+2*mh,w+2*mw),int32) * limits(f)[0]).astype(f.dtype)
        for i in xrange(x.shape[0]):
            if v[i] > -2147483647:
                y[mh+x[i,0]:mh+x[i,0]+h, mw+x[i,1]:mw+x[i,1]+w] = maximum(
                    y[mh+x[i,0]:mh+x[i,0]+h, mw+x[i,1]:mw+x[i,1]+w], add4dilate(f,v[i]))
        y = y[mh:mh+h, mw:mw+w]
    return y


def drawv(f, data, value, GEOM):
    """
        - Purpose
            Superpose points, rectangles and lines on an image.
        - Synopsis
            y = drawv(f, data, value, GEOM)
        - Input
            f:     Gray-scale (uint8 or uint16) or binary image.
            data:  Gray-scale (uint8 or uint16) or binary image. vector of
                   points. Each row gives information regarding a
                   geometrical primitive. The interpretation of this data is
                   dependent on the parameter GEOM. The line drawing
                   algorithm is not invariant to image transposition.
            value: Gray-scale (uint8 or uint16) or binary image. pixel
                   gray-scale value associated to each point in parameter
                   data. It can be a column vector of values or a single
                   value.
            GEOM:  String Default: "". geometrical figure. One of
                   'point','line', 'rect', or 'frect' for drawing points,
                   lines, rectangles or filled rectangles respectively.
        - Output
            y: Gray-scale (uint8 or uint16) or binary image. y has the same
               type of f .
        - Description
            drawv creates the image y by a superposition of points,
            rectangles and lines of gray-level k1 on the image f . The
            parameters for each geometrical primitive are defined by each
            line in the 'data' parameter. For points , they are represented
            by a matrix where each row gives the point's row and column, in
            this order. For lines , they are drawn with the same convention
            used by points, with a straight line connecting them in the
            order given by the data matrix. For rectangles and filled
            rectangles , each row in the data matrix gives the two points of
            the diagonal of the rectangle, where the points use the same
            row, column convention.
        - Examples
            #
            #   example 1
            #
            f=to_uint8(zeros((3,5)))
            pcoords=to_uint16([[0,2,4],
                            [0,0,2]])
            pvalue=to_uint16([1,2,3])
            print drawv(f,pcoords,pvalue,'point')
            print drawv(f,pcoords,pvalue,'line')
            rectcoords=to_uint16([[0],
                               [0],
                               [3],
                               [2]])
            print drawv(f,rectcoords, to_uint16(5), 'rect')
            #
            #   example 2
            #
            f=readgray('blob3.tif')
            pc=blob(label(f),'centroid','data')
            lines=drawv(intersec(f,0),transpose(pc),to_uint8(1),'line')
            show(f,lines)
    """
    from numpy import array, newaxis, zeros, Int, put, ravel, arange, floor
    from string import upper

    GEOM  = upper(GEOM)
    data  = array(data)
    value = array(value)
    y     = array(f)
    lin, col = data[1,:], data[0,:]
    i = lin*f.shape[1] + col; i = i.astype(Int)
    if len(f.shape) == 1: f = f[newaxis,:]
    if value.shape == (): value = value + zeros(lin.shape)
    if len(lin) != len(value):
        print 'Number of points must match n. of colors.'
        return None
    if GEOM == 'POINT':
        put(ravel(y), i, value)
    elif GEOM == 'LINE':
        for k in xrange(len(value)-1):
            delta = 1.*(lin[k+1]-lin[k])/(1e-10 + col[k+1]-col[k])
            if abs(delta) <= 1:
                if col[k] < col[k+1]: x_ = arange(col[k],col[k+1]+1)
                else                : x_ = arange(col[k+1],col[k]+1)
                y_ = floor(delta*(x_-col[k]) + lin[k] + 0.5)
            else:
                if lin[k] < lin[k+1]: y_ = arange(lin[k],lin[k+1]+1)
                else                : y_ = arange(lin[k+1],lin[k]+1)
                x_ = floor((y_-lin[k])/delta + col[k] + 0.5)
            i_ = y_*f.shape[1] + x_; i_ = i_.astype(Int)
            put(ravel(y), i_, value[k])
    elif GEOM == 'RECT':
        for k in xrange(data.shape[1]):
            d = data[:,k]
            x0,y0,x1,y1 = d[1],d[0],d[3],d[2]
            y[x0:x1,y0]   = value[k]
            y[x0:x1,y1]   = value[k]
            y[x0,y0:y1]   = value[k]
            y[x1,y0:y1+1] = value[k]
    elif GEOM == 'FRECT':
        for k in xrange(data.shape[1]):
            d = data[:,k]
            x0,y0,x1,y1 = d[1],d[0],d[3],d[2]
            y[x0:x1+1,y0:y1+1] = value[k]
    else:
        print "GEOM should be 'POINT', 'LINE', 'RECT', or 'FRECT'."
    return y


def dtshow(f, n=10):
    """
        - Purpose
            Display a distance transform image with an iso-line color table.
        - Synopsis
            y = dtshow(f, n=10)
        - Input
            f: Gray-scale (uint8 or uint16) image. Distance transform.
            n: Boolean Default: 10. Number of iso-contours.
        - Output
            y: Gray-scale (uint8 or uint16) or binary image. Optionally
               return RGB uint8 image
        - Description
            Displays the distance transform image f (uint8 or uint16) with a
            special gray-scale color table with n pseudo-color equaly
            spaced. The final appearance of this display is similar to an
            iso-contour image display. The infinity value, which is the
            maximum level allowed in the image, is displayed as black. The
            image is displayed in the MATLAB figure only if no output
            parameter is given.
        - Examples
            #
            f=readgray('blob.tif')
            fd=dist(f)
            show(fd)
            dtshow(fd)
    """
    import adpil

    if (isbinary(f)) or (len(f.shape) != 2):
      print 'Error, dtshow: works only for grayscale labeled image'
      return
    y=gdtshow(f, n)
    adpil.adshow(y)
    return
    return y


def endpoints(OPTION="LOOP"):
    """
        - Purpose
            Interval to detect end-points.
        - Synopsis
            Iab = endpoints(OPTION="LOOP")
        - Input
            OPTION: String Default: "LOOP". 'LOOP' or 'HOMOTOPIC'
        - Output
            Iab: Interval
        - Description
            endpoints creates an interval that is useful to detect
            end-points of curves (i.e., one pixel thick connected
            components) in binary images. It can be used to prune skeletons
            and to mark objects transforming them in a single pixel or
            closed loops if they have holes. There are two options
            available: LOOP, deletes all points but preserves loops if used
            in thin ; HOMOTOPIC, deletes all points but preserves the last
            single point or loops.
        - Examples
            #
            #   example 1
            #
            print intershow(endpoints())
            #
            #   example 2
            #
            print intershow(endpoints('HOMOTOPIC'))
            #
            #   example 3
            #
            f = readgray('pcbholes.tif')
            show(f)
            f1 = thin(f)
            show(f1)
            f2 = thin(f1,endpoints(),20)
            show(f2)
            #
            #   example 4
            #
            fn = thin(f1,endpoints('HOMOTOPIC'))
            show(dilate(fn))
    """
    from string import upper

    Iab = None
    OPTION = upper(OPTION)
    if OPTION == 'LOOP':
        Iab = se2hmt(binary([[0,0,0],
                             [0,1,0],
                             [0,0,0]]),
                        binary([[0,0,0],
                                [1,0,1],
                                [1,1,1]]))
    elif OPTION == 'HOMOTOPIC':
        Iab = se2hmt(binary([[0,1,0],
                             [0,1,0],
                             [0,0,0]]),
                        binary([[0,0,0],
                                [1,0,1],
                                [1,1,1]]))
    return Iab


def erode(f, b=None):
    """
        - Purpose
            Erode an image by a structuring element.
        - Synopsis
            y = erode(f, b=None)
        - Input
            f: Gray-scale (uint8 or uint16) or binary image.
            b: Structuring Element Default: None (3x3 elementary cross).
        - Output
            y: Image
        - Description
            ero performs the erosion of the image f by the structuring
            element b . Erosion is a neighbourhood operator that compairs
            locally b with f , according to an inclusion rule. Since erosion
            is a fundamental operator to the construction of all other
            morphological operators, it is also called an elementary
            operator of Mathematical Morphology. When f is a gray-scale
            image , b may be a flat or non-flat structuring element.
        - Examples
            #
            #   example 1
            #
            f=binary([
               [1, 1, 1, 0, 0, 1, 1],
               [1, 0, 1, 1, 1, 0, 0],
               [0, 0, 0, 0, 1, 0, 0]])
            b=binary([1, 1, 0])
            erode(f,b)
            f=to_uint8([
               [ 0,   1,  2, 50,  4,  5],
               [ 2,   3,  4,  0,  0,  0],
               [12, 255, 14, 15, 16, 17]])
            erode(f,b)
            #
            #   example 2
            #
            f=binary(readgray('blob.tif'))
            bimg=binary(readgray('blob1.tif'))
            b=img2se(bimg)
            g=erode(f,b)
            show(f)
            show(g)
            show(g,gradm(f))
            #
            #   example 3
            #
            f=readgray('pcb_gray.tif')
            b=sedisk(3)
            show(f)
            show(erode(f,b))
    """

    if b is None: b = secross()
    y = neg(dilate(neg(f),sereflect(b)))
    return y


def freedom(L=5):
    """
        - Purpose
            Control automatic data type conversion.
        - Synopsis
            Y = freedom(L=5)
        - Input
            L: Double Default: 5. level of FREEDOM: 0, 1 or 2. If the input
               parameter is omitted, the current level is returned.
        - Output
            Y: Double current FREEDOM level
        - Description
            freedom controls the automatic data type conversion. There are
            3 possible levels, called FREEDOM levels, for automatic
            conversion: 0 - image type conversion is not allowed; 1- image
            type conversion is allowed, but a warning is sent for each
            conversion; 2- image type conversion is allowed without warning.
            The FREEDOM levels are set or inquired by freedom . If an
            image is not in the required datatype, than it should be
            converted to the maximum and nearest pymorph Morphology Toolbox
            datatype. For example, if an image is in int32 and a
            morphological gray-scale processing that accepts only binary,
            uint8 or uint16 images, is required, it will be converted to
            uint16. Another example, if a binary image should be added to a
            uint8 image, the binary image will be converted to uint8. In
            cases of operators that have as parameters an image and a
            constant, the type of the image should be kept as reference,
            while the type of the constant should be converted, if
            necessary.
        - Examples
            #
            #   example 1
            #
            a=subm([4., 2., 1.],to_uint8([3, 2, 0]))
            print a
            print datatype(a)
            #
            #   example 2
            #
            a=subm([4., 2., 1], binary([3, 2, 0]))
            print a
            print datatype(a)
            #
            #   example 3
            #
            a=subm(to_uint8([4, 3, 2, 1]), 1)
            print a
            print datatype(a)
    """

    Y = -1
    return Y


def gdist(f, g, Bc=None, METRIC=None):
    """
        - Purpose
            Geodesic Distance Transform.
        - Synopsis
            y = gdist(f, g, Bc=None, METRIC=None)
        - Input
            f:      Binary image.
            g:      Binary image. Marker image
            Bc:     Structuring Element Default: None (3x3 elementary
                    cross). (metric for distance).
            METRIC: String Default: None. 'EUCLIDEAN' if specified.
        - Output
            y: uint16 (distance image).
        - Description
            gdist creates the geodesic distance image y of the binary
            image f relative to the binary image g . The value of y at the
            pixel x is the length of the smallest path between x and f . The
            distances available are based on the Euclidean metrics and on
            metrics generated by a neighbourhood graph, that is
            characterized by a connectivity rule defined by the structuring
            element Bc . The connectivity for defining the paths is
            consistent with the metrics adopted to measure their length. In
            the case of the Euclidean distance, the space is considered
            continuos and, in the other cases, the connectivity is the one
            defined by Bc .
        - Examples
            #
            #   example 1
            #
            f=binary([
             [1,1,1,1,1,1],
             [1,1,1,0,0,1],
             [1,0,1,0,0,1],
             [1,0,1,1,0,0],
             [0,0,1,1,1,1],
             [0,0,0,1,1,1]])
            g=binary([
             [0,0,0,0,0,0],
             [1,1,0,0,0,0],
             [0,0,0,0,0,0],
             [0,0,0,0,0,0],
             [0,0,0,0,0,0],
             [0,0,0,0,0,1]])
            y=gdist(f,g,secross())
            print y
            #
            #   example 2
            #
            f=readgray('maze_bw.tif')
            g=intersec(f,0)
            g=drawv(g,to_uint16([[2],[2],[6],[6]]),to_uint16(1),'frect')
            y=gdist(f,g,sebox(),'EUCLIDEAN')
            show(f,g)
            dtshow(y,200)
    """

    if Bc is None: Bc = secross()
    assert METRIC is None,'Does not support EUCLIDEAN'
    fneg,gneg = neg(f),neg(g)
    y = gray(gneg,'uint16',1)
    ero = intersec(y,0)
    aux = y
    i = 1
    while not isequal(ero,aux):
        aux = ero
        ero = cerode(gneg,fneg,Bc,i)
        y = addm(y,gray(ero,'uint16',1))
        i = i + 1
    y = union(y,gray(ero,'uint16'))
    return y


def gradm(f, Bdil=None, Bero=None):
    """
        - Purpose
            Morphological gradient.
        - Synopsis
            y = gradm(f, Bdil=None, Bero=None)
        - Input
            f:    Gray-scale (uint8 or uint16) or binary image.
            Bdil: Structuring Element Default: None (3x3 elementary cross).
                  for the dilation.
            Bero: Structuring Element Default: None (3x3 elementary cross).
                  for the erosion.
        - Output
            y: Gray-scale (uint8 or uint16) or binary image. (same type of f
               ).
        - Description
            gradm creates the image y by the subtraction of the erosion of
            the image f by Bero of the dilation of f by Bdil .
        - Examples
            #
            #   example 1
            #
            a = readgray('small_bw.tif')
            b = gradm(a)
            show(a)
            show(b)
            #
            #   example 2
            #
            c=gradm(a,secross(0),secross())
            d=gradm(a,secross(),secross(0))
            show(a,c)
            show(a,d)
            #
            #   example 3
            #
            a = readgray('bloodcells.tif')
            b = gradm(a)
            show(a)
            show(b)
    """

    if Bdil is None: Bdil = secross()
    if Bero is None: Bero = secross()
    y = subm(dilate(f,Bdil),erode(f,Bero))
    return y


def grain(fr, f, measurement, option="image"):
    """
        - Purpose
            Gray-scale statistics for each labeled region.
        - Synopsis
            y = grain(fr, f, measurement, option="image")
        - Input
            fr:          Gray-scale (uint8 or uint16) image. Labeled image,
                         to define the regions. Label 0 is the background
                         region.
            f:           Gray-scale (uint8 or uint16) image. To extract the
                         measuremens.
            measurement: String Default: "". Choose the measure to compute:
                         'max', 'min', 'median', 'mean', 'sum', 'std',
                         'std1'.
            option:      String Default: "image". Output format: 'image':
                         results as a gray-scale mosaic image (uint16);
                         'data': results a column vector of measurements
                         (double).
        - Output
            y: Gray-scale (uint8 or uint16) image. Or a column vector
               (double) with gray-scale statistics per region.
        - Description
            Computes gray-scale statistics of each grain in the image. The
            grains regions are specified by the labeled image fr and the
            gray-scale information is specified by the image f . The
            statistics to compute is specified by the parameter measurement,
            which has the same options as in function stats . The
            parameter option defines: ('image') if the output is an uint16
            image where each label value is changed to the measurement
            value, or ('data') a double column vector. In this case, the
            first element (index 1) is the measurement of region 1. The
            region with label zero is not measure as it is normally the
            background.
        - Examples
            #
            #   example 1
            #
            f=to_uint8([range(6),range(6),range(6)])
            fr=labelflat(f)
            grain(fr,f,'sum','data')
            grain(fr,f,'sum')
            #
            #   example 2
            #
            f=readgray('astablet.tif')
            g=gradm(f)
            marker=regmin(close(g))
            ws=cwatershed(g,marker,sebox(),'regions')
            g=grain(ws,f,'mean')
            show(f)
            show(g)
    """
    from numpy import newaxis, ravel, zeros, sum, nonzero, put, take, array, mean, std
    from string import upper

    measurement = upper(measurement)
    option      = upper(option)
    if len(fr.shape) == 1:
        fr = fr[newaxis,:]
    n = fr.max()
    if option == 'DATA': y = []
    else               : y = zeros(fr.shape)
    if measurement == 'MAX':
        for i in xrange(1,n+1):
            aux = (fr==i)
            val = (aux*f).max()
            if option == 'DATA': y.append(val)
            else               : put(ravel(y), nonzero(ravel(aux)), val)
    elif measurement == 'MIN':
        for i in xrange(1,n+1):
            aux = fr==i
            lin = ravel(aux*f)
            ind = nonzero(ravel(aux))
            val = take(lin,ind).min()
            if option == 'DATA': y.append(val)
            else               : put(ravel(y), ind, val)
    elif measurement == 'SUM':
        for i in xrange(1,n+1):
            aux = fr==i
            val = (aux*f).sum()
            if option == 'DATA': y.append(val)
            else               : put(ravel(y), nonzero(ravel(aux)), val)
    elif measurement == 'MEAN':
        for i in xrange(1,n+1):
            aux = fr==i
            ind = nonzero(ravel(aux))
            val = take(ravel(aux*f), ind).mean()
            if option == 'DATA': y.append(val)
            else               : put(ravel(y), ind, val)
    elif measurement == 'STD':
        for i in xrange(1,n+1):
            aux = fr==i
            ind = nonzero(ravel(aux))
            v   = take(ravel(aux*f), ind)
            if len(v) < 2: val = 0
            else         : val = std(v)
            if option == 'DATA': y.append(val)
            else               : put(ravel(y), ind, val)
    elif measurement == 'STD1':
        print "'STD1' is not implemented"
    else:
        print "Measurement should be 'MAX', 'MIN', 'MEAN', 'SUM', 'STD', 'STD1'."
    if option == 'DATA':
        y = array(y)
        if len(y.shape) == 1: y = y[:,newaxis]
    return y


def gray(f, TYPE="uint8", k1=None):
    """
        - Purpose
            Convert a binary image into a gray-scale image.
        - Synopsis
            y = gray(f, TYPE="uint8", k1=None)
        - Input
            f:    Binary image.
            TYPE: String Default: "uint8". 'uint8', 'uint16', or 'int32'.
            k1:   Non-negative integer. Default: None (Maximum pixel level
                  in pixel type).
        - Output
            y: Unsigned gray-scale (uint8 or uint16), signed (int32) or
               binary image.
        - Description
            gray converts a binary image into a gray-scale image of a
            specified data type. The value k1 is assigned to the 1 pixels of
            f , while the 0 pixels are assigned to the minimum value
            associated to the specified data type.
        - Examples
            #
            b=binary([0, 1, 0, 1])
            print b
            c=gray(b)
            print c
            d=gray(b,'uint8',100)
            print d
            e=gray(b,'uint16')
            print e
            f=gray(b,'int32',0)
            print f
    """
    from numpy import array
    if k1 is None: k1 = maxleveltype(TYPE)
    if type(f) is list: f = binary(f)
    assert isbinary(f), 'f must be binary'
    if   TYPE == 'uint8' : y = to_uint8(f*k1)
    elif TYPE == 'uint16': y = to_uint16(f*k1)
    elif TYPE == 'int32' : y = to_int32(f*k1) - to_int32(neg(f)*maxleveltype(TYPE))
    else:
        assert 0, 'pymorph.gray: type not supported: %s' % TYPE
    return y


def hmin(f, h=1, Bc=None):
    """
        - Purpose
            Remove basins with contrast less than h.
        - Synopsis
            y = hmin(f, h=1, Bc=None)
        - Input
            f:  Gray-scale (uint8 or uint16) image.
            h:  Default: 1. Contrast parameter.
            Bc: Structuring Element Default: None (3x3 elementary cross).
                Structuring element (connectivity).
        - Output
            y: Gray-scale (uint8 or uint16) or binary image.
        - Description
            hmin sup-reconstructs the gray-scale image f from the marker
            created by the addition of the positive integer value h to f ,
            using the connectivity Bc . This operator removes connected
            basins with contrast less than h . This function is very userful
            for simplifying the basins of the image.
        - Examples
            #
            #   example 1
            #
            a = to_uint8([
                [10,   3,   6,  18,  16,  15,  10],
                [10,   9,   6,  18,   6,   5,  10],
                [10,   9,   9,  15,   4,   9,  10],
                [10,  10,  10,  10,  10,  10,  10]])
            print hmin(a,1,sebox())
            #
            #   example 2
            #
            f = readgray('r4x2_256.tif')
            show(f)
            fb = hmin(f,70)
            show(fb)
            show(regmin(fb))
    """

    if Bc is None: Bc = secross()
    g = addm(f,h)
    y = suprec(g,f,Bc);
    return y


def vmax(f, v=1, Bc=None):
    """
        - Purpose
            Remove domes with volume less than v.
        - Synopsis
            y = vmax(f, v=1, Bc=None)
        - Input
            f:  Gray-scale (uint8 or uint16) image.
            v:  Default: 1. Volume parameter.
            Bc: Structuring Element Default: None (3x3 elementary cross).
                Structuring element (connectivity).
        - Output
            y: Gray-scale (uint8 or uint16) or binary image.
        - Description
            vmax This operator removes connected domes with volume less
            than v . This function is very similar to hmax , but instead
            of using a gray scale criterion (contrast) for the dome, it uses
            a volume criterion.
        - Examples
            #
            #   example 1
            #
            a = to_uint8([
                [4,  3,  6,  1,  3,  5,  2],
                [2,  9,  6,  1,  6,  7,  3],
                [8,  9,  3,  2,  4,  9,  4],
                [3,  1,  2,  1,  2,  4,  2]])
            print vmax(a,10,sebox())
            #
            #   example 2
            #
            f = readgray('astablet.tif')
            show(f)
            fb = vmax(f,80000)
            show(fb)
            show(regmax(fb))
    """

    if Bc is None: Bc = secross()
    raise 'Not implemented yet'
    return None
    return y


def hmax(f, h=1, Bc=None):
    """
        - Purpose
            Remove peaks with contrast less than h.
        - Synopsis
            y = hmax(f, h=1, Bc=None)
        - Input
            f:  Gray-scale (uint8 or uint16) image.
            h:  Default: 1. Contrast parameter.
            Bc: Structuring Element Default: None (3x3 elementary cross).
                Structuring element ( connectivity).
        - Output
            y: Gray-scale (uint8 or uint16) or binary image.
        - Description
            hmax inf-reconstructs the gray-scale image f from the marker
            created by the subtraction of the positive integer value h from
            f , using connectivity Bc . This operator removes connected
            peaks with contrast less than h .
        - Examples
            #
            #   example 1
            #
            a = to_uint8([
                [4,   3,   6,  1,  3,  5,  2],
                [2,   9,   6,  1,  6,  7,  3],
                [8,   9,   3,  2,  4,  9,  4],
                [3,   1,   2,  1,  2,  4,  2]])
            print hmax(a,2,sebox())
            #
            #   example 2
            #
            f = readgray('r4x2_256.tif')
            show(f)
            fb = hmax(f,50)
            show(fb)
            show(regmax(fb))
    """

    if Bc is None: Bc = secross()
    g = subm(f,h)
    y = infrec(g,f,Bc);
    return y


def homothick():
    """
        - Purpose
            Interval for homotopic thickening.
        - Synopsis
            Iab = homothick()

        - Output
            Iab: Interval
        - Description
            homothick creates an interval that is useful for the homotopic
            (i.e., that conserves the relation between objects and holes)
            thickening of binary images.
        - Examples
            #
            print intershow(homothick())
    """
    return se2hmt(binary([[1,1,1],
                         [0,0,0],
                         [0,0,0]]),
                  binary([[0,0,0],
                          [0,1,0],
                          [1,1,1]]))


def homothin():
    """
        - Purpose
            Interval for homotopic thinning.
        - Synopsis
            Iab = homothin()

        - Output
            Iab: Interval
        - Description
            homothin creates an interval that is useful for the homotopic
            (i.e., that conserves the relation between objects and holes)
            thinning of binary images.

    """

    Iab = se2hmt(binary([[0,0,0],
                             [0,1,0],
                             [1,1,1]]),
                   binary([[1,1,1],
                             [0,0,0],
                             [0,0,0]]))
    return Iab


def img2se(fd, FLAT="FLAT", f=None):
    """
        - Purpose
            Create a structuring element from a pair of images.
        - Synopsis
            B = img2se(fd, FLAT="FLAT", f=None)
        - Input
            fd:   Binary image. The image is in the matrix format where the
                  origin (0,0) is at the matrix center.
            FLAT: String Default: "FLAT". 'FLAT' or 'NON-FLAT'.
            f:    Unsigned gray-scale (uint8 or uint16), signed (int32) or
                  binary image. Default: None.
        - Output
            B: Structuring Element
        - Description
            img2se creates a flat structuring element B from the binary
            image fd or creates a non-flat structuring element b from the
            binary image fd and the gray-scale image f . fd represents the
            domain of b and f represents the image of the points in fd .
        - Examples
            #
            #   example 1
            #
            a = img2se(binary([
              [0,1,0],
              [1,1,1],
              [0,1,0]]))
            print seshow(a)
            #
            #   example 2
            #
            b = binary([
              [0,1,1,1],
              [1,1,1,0]])
            b1 = img2se(b)
            print seshow(b1)
            #
            #   example 3
            #
            c = binary([
              [0,1,0],
              [1,1,1],
              [0,1,0]])
            d = to_int32([
              [0,0,0],
              [0,1,0],
              [0,0,0]])
            e = img2se(c,'NON-FLAT',d)
            print seshow(e)
    """
    from string import upper
    from numpy import choose, ones

    assert isbinary(fd),'First parameter must be binary'
    FLAT = upper(FLAT)
    if FLAT == 'FLAT':
        return seshow(fd)
    else:
        B = choose(fd, (limits(to_int32([0]))[0]*ones(fd.shape),f) )
    B = seshow(to_int32(B),'NON-FLAT')
    return B


def infcanon(f, Iab, theta=45, DIRECTION="CLOCKWISE"):
    """
        - Purpose
            Intersection of inf-generating operators.
        - Synopsis
            y = infcanon(f, Iab, theta=45, DIRECTION="CLOCKWISE")
        - Input
            f:         Binary image.
            Iab:       Interval
            theta:     Double Default: 45. Degrees of rotation: 45, 90, or
                       180.
            DIRECTION: String Default: "CLOCKWISE". 'CLOCKWISE' or '
                       ANTI-CLOCKWISE'
        - Output
            y: Binary image.
        - Description
            infcanon creates the image y by computing intersections of
            transformations of the image f by inf-generating (i.e., dual of
            the hit-or-miss) operators. These inf-generating operators are
            characterized by rotations (in the clockwise or anti-clockwise
            direction) of theta degrees of the interval Iab .

    """
    from string import upper

    DIRECTION = upper(DIRECTION)            
    y = union(f,1)
    for t in xrange(0,360,theta):
        Irot = interot( Iab, t, DIRECTION )
        y = intersec( y, infgen(f, Irot))
    return y


def infgen(f, Iab):
    """
        - Purpose
            Inf-generating.
        - Synopsis
            y = infgen(f, Iab)
        - Input
            f:   Binary image.
            Iab: Interval
        - Output
            y: Binary image.
        - Description
            infgen creates the image y by computing the transformation of
            the image f by the inf-generating operator (or dual of the
            hit-or-miss) characterized by the interval Iab .

    """

    A,Bc = Iab
    y = union(dilate(f, A),dilate(neg(f), Bc))
    return y


def infrec(f, g, bc=None):
    """
        - Purpose
            Inf-reconstruction.
        - Synopsis
            y = infrec(f, g, bc=None)
        - Input
            f:  Gray-scale (uint8 or uint16) or binary image. Marker image.
            g:  Gray-scale (uint8 or uint16) or binary image. Conditioning
                image.
            bc: Structuring Element Default: None (3x3 elementary cross).
                Structuring element ( connectivity).
        - Output
            y: Image
        - Description
            infrec creates the image y by an infinite number of recursive
            iterations (iterations until stability) of the dilation of f by
            bc conditioned to g . We say the y is the inf-reconstruction of
            g from the marker f . For algorithms and applications, see
            Vinc:93b .
        - Examples
            #
            #   example 1
            #
            g=readgray('text_128.tif')
            f=erode(g,seline(9,90))
            y=infrec(f,g,sebox())
            show(g)
            show(f)
            show(y)
            #
            #   example 2
            #
            g=neg(readgray('n2538.tif'))
            f=intersec(g,0)
            f=draw(f,'LINE:40,30,60,30:END')
            y30=cdilate(f,g,sebox(),30)
            y=infrec(f,g,sebox())
            show(g)
            show(f)
            show(y30)
            show(y)
    """
    from numpy import product
    if bc is None: bc = secross()
    n = product(f.shape)
    y = cdilate(f,g,bc,n);
    return y


def inpos(f, g, bc=None):
    """
        - Purpose
            Minima imposition.
        - Synopsis
            y = inpos(f, g, bc=None)
        - Input
            f:  Binary image. Marker image.
            g:  Gray-scale (uint8 or uint16) image. input image.
            bc: Structuring Element Default: None (3x3 elementary cross).
                (connectivity).
        - Output
            y: Gray-scale (uint8 or uint16) image.
        - Description
            Minima imposition on g based on the marker f . inpos creates
            an image y by filing the valleys of g that does not cover the
            connect components of f . A remarkable property of y is that its
            regional minima are exactly the connect components of g .

    """

    if bc is None: bc = secross()
    assert isbinary(f),'First parameter must be binary image'
    fg = gray(neg(f),datatype(g))
    k1 = limits(g)[1] - 1
    y = suprec(fg, intersec(union(g, 1), k1, fg), bc)
    return y


def interot(Iab, theta=45, DIRECTION="CLOCKWISE"):
    """
        - Purpose
            Rotate an interval
        - Synopsis
            Irot = interot(Iab, theta=45, DIRECTION="CLOCKWISE")
        - Input
            Iab:       Interval
            theta:     Double Default: 45. Degrees of rotation. Available
                       values are multiple of 45 degrees.
            DIRECTION: String Default: "CLOCKWISE". 'CLOCKWISE' or '
                       ANTI-CLOCKWISE'.
        - Output
            Irot: Interval
        - Description
            interot rotates the interval Iab by an angle theta .
        - Examples
            #
            b1 = endpoints()
            b2 = interot(b1)
            print intershow(b1)
            print intershow(b2)
    """
    from string import upper

    DIRECTION = upper(DIRECTION)
    A,Bc = Iab
    if DIRECTION != 'CLOCKWISE':
        theta = 360 - theta
    Irot = se2hmt(serot(A, theta),
                    serot(Bc,theta))
    return Irot


def intersec(f1, f2, f3=None, f4=None, f5=None):
    """
        - Purpose
            Intersection of images.
        - Synopsis
            y = intersec(f1, f2, f3=None, f4=None, f5=None)
        - Input
            f1: Gray-scale (uint8 or uint16) or binary image.
            f2: Gray-scale (uint8 or uint16) or binary image. Or constant.
            f3: Gray-scale (uint8 or uint16) or binary image. Default: None.
                Or constant.
            f4: Gray-scale (uint8 or uint16) or binary image. Default: None.
                Or constant.
            f5: Gray-scale (uint8 or uint16) or binary image. Default: None.
                Or constant.
        - Output
            y: Image
        - Description
            intersec creates the image y by taking the pixelwise minimum
            between the images f1, f2, f3, f4, and f5 . When f1, f2, f3, f4,
            and f5 are binary images, y is the intersection of them.
        - Examples
            #
            #   example 1
            #
            f=to_uint8([255,  255,    0,   10,    0,   255,   250])
            g=to_uint8([ 0,    40,   80,   140,  250,    10,    30])
            print intersec(f, g)
            print intersec(f, 0)
            #
            #   example 2
            #
            a = readgray('form-ok.tif')
            b = readgray('form-1.tif')
            c = intersec(a,b)
            show(a)
            show(b)
            show(c)
            #
            #   example 3
            #
            d = readgray('tplayer1.tif')
            e = readgray('tplayer2.tif')
            f = readgray('tplayer3.tif')
            g = intersec(d,e,f)
            show(d)
            show(e)
            show(f)
            show(g)
    """
    from numpy import minimum

    y = minimum(f1,f2)
    if f3 != None: y = minimum(y,f3)
    if f4 != None: y = minimum(y,f4)
    if f5 != None: y = minimum(y,f5)
    y = y.astype(f1.dtype)
    return y


def intershow(Iab):
    """
        - Purpose
            Visualize an interval.
        - Synopsis
            s = intershow(Iab)
        - Input
            Iab: Interval
        - Output
            s: String ( representation of the interval).
        - Description
            intershow creates a representation for an interval using 0, 1
            and . ( don't care).
        - Examples
            #
            print intershow(homothin())
    """
    from numpy import array, product, reshape, choose
    from string import join

    assert (type(Iab) is tuple) and (len(Iab) == 2),'not proper fortmat of hit-or-miss template'
    A,Bc = Iab
    S = seunion(A,Bc)
    Z = intersec(S,0)
    n = product(S.shape)
    one  = reshape(array(n*'1','c'),S.shape)
    zero = reshape(array(n*'0','c'),S.shape)
    x    = reshape(array(n*'.','c'),S.shape)
    saux = choose( S + seunion(Z,A), ( x, zero, one))
    s = ''
    for i in xrange(saux.shape[0]):
        s=s+(join(list(saux[i]))+' \n')
    return s


def isbinary(f):
    """
        - Purpose
            Check for binary image
        - Synopsis
            bool = isbinary(f)
        - Input
            f:
        - Output
            bool: Boolean
        - Description
            isbinary returns True if the datatype of the input image is
            binary. A binary image has just the values 0 and 1.
        - Examples
            #
            a=to_uint8([0, 1, 0, 1])
            print isbinary(a)
            b=(a)
            print isbinary(b)
    """
    return f.dtype == bool

def isequal(f1, f2):
    """
        - Purpose
            Verify if two images are equal
        - Synopsis
            bool = isequal(f1, f2)
        - Input
            f1:  Unsigned gray-scale (uint8 or uint16), signed (int32) or
                 binary image.
            f2:  Unsigned gray-scale (uint8 or uint16), signed (int32) or
                 binary image.
        - Output
            bool: Boolean
        - Description
            isequal compares the images f1 and f2 and returns True, if
            f1 and f2 have the same size and f1(x)=f2(x), for all pixel x;
            otherwise, returns False
        - Examples
            #
            f1 = to_uint8(arrayrange(4))
            print f1
            f2 = to_uint8([9, 5, 3, 3])
            print f2
            f3 = f1
            isequal(f1,f2)
            isequal(f1,f3)
    """
    import numpy
    if f1.shape != f2.shape:
        return False
    return numpy.all(f1 == f2)


def labelflat(f, Bc=None, _lambda=0):
    """
        - Purpose
            Label the flat zones of gray-scale images.
        - Synopsis
            y = labelflat(f, Bc=None, _lambda=0)
        - Input
            f:       Gray-scale (uint8 or uint16) or binary image.
            Bc:      Structuring Element Default: None (3x3 elementary
                     cross). ( connectivity).
            _lambda: Default: 0. Connectivity given by |f(q)-f(p)|<=_lambda.
        - Output
            y: Image If number of labels is less than 65535, the data type
               is uint16, otherwise it is int32.
        - Description
            labelflat creates the image y by labeling the flat zones of f
            , according to the connectivity defined by the structuring
            element Bc . A flat zone is a connected region of the image
            domain in which all the pixels have the same gray-level
            (lambda=0 ). When lambda is different than zero, a quasi-flat
            zone is detected where two neighboring pixels belong to the same
            region if their difference gray-levels is smaller or equal
            lambda . The minimum label of the output image is 1 and the
            maximum is the number of flat-zones in the image.
        - Examples
            #
            #   example 1
            #
            f=to_uint8([
               [5,5,8,3,0],
               [5,8,8,0,2]])
            g=labelflat(f)
            print g
            g1=labelflat(f,secross(),2)
            print g1
            #
            #   example 2
            #
            f=readgray('blob.tif')
            d=dist(f,sebox(),'euclidean')
            g= d /8
            show(g)
            fz=labelflat(g,sebox());
            lblshow(fz)
            print fz.max()
            #
            #   example 3
            #
            f=readgray('pcb_gray.tif')
            g=labelflat(f,sebox(),3)
            show(f)
            lblshow(g)
    """
    from numpy import allclose, ravel, nonzero, array
    if Bc is None: Bc = secross()
    zero = binary(subm(f,f))       # zero image
    faux = neg(zero)
    r = array(zero)
    label = 1
    y = gray( zero,'uint16',0)          # zero image (output)
    while not allclose(faux,0):
        x=nonzero(ravel(faux))[0]        # get first unlabeled pixel
        fmark = array(zero)
        fmark.flat[x] = 1                # get the first unlabeled pixel
        f2aux = (f == ravel(f)[x])
        r = infrec( fmark, f2aux, Bc)  # detects all pixels connected to it
        faux = subm( faux, r)          # remove them from faux
        r = gray( r,'uint16',label)    # label them with the value label
        y = union( y, r)               # merge them with the labeled image
        label = label + 1
    return y


def lastero(f, B=None):
    """
        - Purpose
            Last erosion.
        - Synopsis
            y = lastero(f, B=None)
        - Input
            f: Binary image.
            B: Structuring Element Default: None (3x3 elementary cross).
        - Output
            y: Binary image.
        - Description
            lastero creates the image y by computing the last erosion by
            the structuring element B of the image f . The objects found in
            y are the objects of the erosion by nB that can not be
            reconstructed from the erosion by (n+1)B , where n is a generic
            non negative integer. The image y is a proper subset of the
            morphological skeleton by B of f .

    """

    if B is None: B = secross()
    assert isbinary(f),'Can only process binary images'
    dt = dist(f,B)
    y = regmax(dt,B)
    return y


def lblshow(f, option='noborder'):
    """
        - Purpose
            Display a labeled image assigning a random color for each label.
        - Synopsis
            y = lblshow(f, option='noborder')
        - Input
            f:      Gray-scale (uint8 or uint16) image. Labeled image.
            option: String Default: 'noborder'. BORDER or NOBORDER: includes
                    or not a white border around each labeled region
        - Output
            y: Gray-scale (uint8 or uint16) or binary image. Optionally
               return RGB uint8 image
        - Description
            Displays the labeled image f (uint8 or uint16) with a pseudo
            color where each label appears with a random color. The image is
            displayed in the MATLAB figure only if no output parameter is
            given.
        - Examples
            #
            f=readgray('blob3.tif')
            f1=label(f,sebox())
            show(f1)
            lblshow(f1)
            lblshow(f1,'border')
    """
    import string
    import adpil

    if (isbinary(f)) or (len(f.shape) != 2):
      print 'Error, lblshow: works only for grayscale labeled image'
      return
    option = string.upper(option);
    if option == 'NOBORDER':
      border = 0.0;
    elif option == 'BORDER':
      border = 1.0;
    else:
      print 'Error: option must be BORDER or NOBORDER'
    y=glblshow(f, border);
    adpil.adshow(y)
    return
    return y


def open(f, b=None):
    """
        - Purpose
            Morphological opening.
        - Synopsis
            y = open(f, b=None)
        - Input
            f: Gray-scale (uint8 or uint16) or binary image.
            b: Structuring Element Default: None (3x3 elementary cross).
        - Output
            y: Image
        - Description
            open creates the image y by the morphological opening of the
            image f by the structuring element b . In the binary case, the
            opening by the structuring element B may be interpreted as the
            union of translations of B included in f . In the gray-scale
            case, there is a similar interpretation taking the functions
            umbra.
        - Examples
            #
            #   example 1
            #
            f=binary(readgray('blob.tif'))
            bimg=binary(readgray('blob1.tif'))
            b=img2se(bimg)
            show(f)
            show(open(f,b))
            show(open(f,b),gradm(f))
            #
            #   example 2
            #
            a=binary(readgray('pcb1bin.tif'))
            b=open(a,sebox(2))
            c=open(a,sebox(4))
            show(a)
            show(b)
            show(c)
            #
            #   example 3
            #
            a=readgray('astablet.tif')
            b=open(a,sedisk(18))
            show(a)
            show(b)
    """

    if b is None: b = secross()
    y = dilate(erode(f,b),b)
    return y


def openrec(f, bero=None, bc=None):
    """
        - Purpose
            Opening by reconstruction.
        - Synopsis
            y = openrec(f, bero=None, bc=None)
        - Input
            f:    Gray-scale (uint8 or uint16) or binary image.
            bero: Structuring Element Default: None (3x3 elementary cross).
                  (erosion).
            bc:   Structuring Element Default: None (3x3 elementary cross).
                  (connectivity).
        - Output
            y: Image (same type of f ).
        - Description
            openrec creates the image y by an inf-reconstruction of the
            image f from its erosion by bero , using the connectivity
            defined by Bc .

    """

    if bero is None: bero = secross()
    if bc is None: bc = secross()
    y = infrec(erode(f,bero),f,bc)
    return y


def openrecth(f, bero=None, bc=None):
    """
        - Purpose
            Open-by-Reconstruction Top-Hat.
        - Synopsis
            y = openrecth(f, bero=None, bc=None)
        - Input
            f:    Gray-scale (uint8 or uint16) or binary image.
            bero: Structuring Element Default: None (3x3 elementary cross).
                  (erosion)
            bc:   Structuring Element Default: None (3x3 elementary cross).
                  ( connectivity)
        - Output
            y: Gray-scale (uint8 or uint16) or binary image. (same type of f
               ).
        - Description
            openrecth creates the image y by subtracting the open by
            reconstruction of f , defined by the structuring elements bero e
            bc , of f itself.

    """

    if bero is None: bero = secross()
    if bc is None: bc = secross()
    y = subm(f, openrec( f, bero, bc))
    return y


def openth(f, b=None):
    """
        - Purpose
            Opening Top Hat.
        - Synopsis
            y = openth(f, b=None)
        - Input
            f: Gray-scale (uint8 or uint16) or binary image.
            b: Structuring Element Default: None (3x3 elementary cross).
               structuring element
        - Output
            y: Gray-scale (uint8 or uint16) or binary image. (same type of f
               ).
        - Description
            openth creates the image y by subtracting the morphological
            opening of f by the structuring element b of f itself.
        - Examples
            #
            a = readgray('keyb.tif')
            show(a)
            b = openth(a,sebox(3))
            show(b)
    """

    if b is None: b = secross()
    y = subm(f, open(f,b))
    return y


def opentransf(f, type='OCTAGON', n=65535, Bc=None, Buser=None):
    """
        - Purpose
            Open transform.
        - Synopsis
            y = opentransf(f, type='OCTAGON', n=65535, Bc=None,
            Buser=None)
        - Input
            f:     Binary image.
            type:  String Default: 'OCTAGON'. Disk family: 'OCTAGON',
                   'CHESSBOARD', 'CITY-BLOCK', 'LINEAR-V', 'LINEAR-H',
                   'LINEAR-45R', 'LINEAR-45L', 'USER'.
            n:     Default: 65535. Maximum disk radii.
            Bc:    Structuring Element Default: None (3x3 elementary cross).
                   Connectivity for the reconstructive opening. Used if
                   '-REC' suffix is appended in the 'type' string.
            Buser: Structuring Element Default: None (3x3 elementary cross).
                   User disk, used if 'type' is 'USER'.
        - Output
            y: Gray-scale (uint8 or uint16) image.
        - Description
            Compute the open transform of a binary image. The value of the
            pixels in the open transform gives the largest radii of the disk
            plus 1, where the open by it is not empty at that pixel. The
            disk sequence must satisfy the following: if r > s, rB is
            sB-open, i.e. rB open by sB is equal rB. Note that the Euclidean
            disk does not satisfy this property in the discrete grid. This
            function also computes the reconstructive open transform by
            adding the suffix '-REC' in the 'type' parameter.
        - Examples
            #
            #   example 1
            #
            f = binary([
                          [0,0,0,0,0,0,0,0],
                          [0,0,1,1,1,1,0,0],
                          [0,0,1,1,1,1,1,0],
                          [0,1,0,1,1,1,0,0],
                          [1,1,0,0,0,0,0,0]])
            print opentransf( f, 'city-block')
            print opentransf( f, 'linear-h')
            print opentransf( f, 'linear-45r')
            print opentransf( f, 'user',10,secross(),binary([0,1,1]))
            print opentransf( f, 'city-block-rec')
            #
            #   example 2
            #
            f=readgray('numbers.tif')
            show(f)
            g=opentransf(f,'OCTAGON')
            show(g)
            #
            #   example 3
            #
            b=sedisk(3,'2D','OCTAGON')
            g1=open(f,b)
            show(g1)
            g2=(g > 3)
            print g1 == g2
    """
    import numpy
    from string import find, upper
    if Bc is None: Bc = secross()
    if Buser is None: Buser = secross()
    assert isbinary(f),'Error: input image is not binary'
    type = upper(type)
    rec_flag = find(type,'-REC')
    if rec_flag != -1:
        type = type[:rec_flag] # remove the -rec suffix
    flag = not ((type == 'OCTAGON')  or
                (type == 'CHESSBOARD') or
                (type == 'CITY-BLOCK'))
    if not flag:
        n  = min(n,min(f.shape))
    elif  type == 'LINEAR-H':
        se = binary([1, 1, 1])
        n  = min(n,f.shape[1])
    elif  type =='LINEAR-V':
        se = binary([[1],[1],[1]])
        n  = min(n,f.shape[0])
    elif  type == 'LINEAR-45R':
        se = binary([[0, 0, 1],[0, 1, 0],[1, 0, 0]])
        n  = min(n,min(f.shape))
    elif  type == 'LINEAR-45L':
        se = binary([[1, 0, 0],[0, 1, 0],[0, 0, 1]])
        n  = min(n,min(f.shape))
    elif  type == 'USER':
        se = Buser
        n  = min(n,min(f.shape))
    else:
        print 'Error: only accepts OCTAGON, CHESSBOARD, CITY-BLOCK, LINEAR-H, LINEAR-V, LINEAR-45R, LINEAR-45L, or USER as type, or with suffix -REC.'
        return []
    k = 0
    y = numpy.zeros(f.shape,numpy.uint16)
    a = binary([1])
    z = binary([0])
    while not (isequal(a,z) or (k>=n)):
        print 'processing r=',k
        if flag:
            a = open(f,sesum(se,k))
        else:
            a = open(f,sedisk(k,'2D',type))
        y = addm(y, gray(a,'uint16',1))
        k = k+1
    if rec_flag != -1:
        y = grain(label(f,Bc),y,'max')
    return y


def patspec(f, type='OCTAGON', n=65535, Bc=None, Buser=None):
    """
        - Purpose
            Pattern spectrum (also known as granulometric size density).
        - Synopsis
            h = patspec(f, type='OCTAGON', n=65535, Bc=None, Buser=None)
        - Input
            f:     Binary image.
            type:  String Default: 'OCTAGON'. Disk family: 'OCTAGON',
                   'CHESSBOARD', 'CITY-BLOCK', 'LINEAR-V', 'LINEAR-H',
                   'LINEAR-45R', 'LINEAR-45L', 'USER'.
            n:     Default: 65535. Maximum disk radii.
            Bc:    Structuring Element Default: None (3x3 elementary cross).
                   Connectivity for the reconstructive granulometry. Used if
                   '-REC' suffix is appended in the 'type' string.
            Buser: Structuring Element Default: None (3x3 elementary cross).
                   User disk, used if 'type' is 'USER'.
        - Output
            h: Gray-scale (uint8 or uint16) or binary image. a uint16
               vector.
        - Description
            Compute the Pattern Spectrum of a binary image. See Mara:89b .
            The pattern spectrum is the histogram of the open transform, not
            taking the zero values.

    """

    if Bc is None: Bc = secross()
    if Buser is None: Buser = secross()
    assert isbinary(f),'Error: input image is not binary'
    g=opentransf(f,type,n,Bc,Buser)
    h=histogram(g)
    h=h[1:]
    return h


def readgray(filename):
    """
        - Purpose
            Read an image from a coercial file format and stores it as a
            gray-scale image.
        - Synopsis
            y = readgray(filename)
        - Input
            filename: String Name of file to read.
        - Output
            y: Gray-scale (uint8 or uint16) or binary image.
        - Description
            readgray reads the image in filename and stores it in y , an
            uint8 gray-scale image (without colormap). If the input file is
            a color RGB image, it is converted to gray-scale using the
            equation: y = 0.2989 R + 0.587 G + 0.114 B. This functions uses
            de PIL module.
        - Examples
            #
            a=readgray('cookies.tif')
            show(a)
    """
    import adpil
    import numpy

    y = adpil.adread(filename)
    if (len(y.shape) == 3) and (y.shape[0] == 3):
       if numpy.alltrue(numpy.alltrue(y[0,:,:] == y[1,:,:] and
                                          y[0,:,:] == y[2,:,:])):
          y = y[0,:,:]
       else:
          print 'Warning: converting true-color RGB image to gray'
          y = ubyte(0.2989 * y[0,:,:] + 
                      0.5870 * y[1,:,:] + 
                      0.1140 * y[2,:,:])
    elif (len(y.shape) == 2):
       pass
    else:
       raise ValueError, 'Error, it is not 2D image'
    return y

def regmax(f, Bc=None):
    """
        - Purpose
            Regional Maximum.
        - Synopsis
            y = regmax(f, Bc=None)
        - Input
            f:  Gray-scale (uint8 or uint16) image.
            Bc: Structuring Element Default: None (3x3 elementary cross).
                (connectivity).
        - Output
            y: Binary image.
        - Description
            regmax creates a binary image y by computing the regional
            maxima of f , according to the connectivity defined by the
            structuring element Bc . A regional maximum is a flat zone not
            surrounded by flat zones of higher gray values.

    """

    if Bc is None: Bc = secross()
    y = regmin(neg(f),Bc)
    return y


def regmin(f, Bc=None, option="binary"):
    """
        - Purpose
            Regional Minimum (with generalized dynamics).
        - Synopsis
            y = regmin(f, Bc=None, option="binary")
        - Input
            f:      Gray-scale (uint8 or uint16) image.
            Bc:     Structuring Element Default: None (3x3 elementary
                    cross). (connectivity).
            option: String Default: "binary". Choose one of: BINARY: output
                One of:
                    'binary': output a binary image
                    'value': output a grayscale image with
                        points at the regional minimum with the pixel values of
                        the input image
                    'dynamics':  output a grayscale image with
                        points at the regional minimum with its dynamics;
                    'area-dyn': int32 image with the area-dynamics;
                    'volume-dyn': int32 image with the volume-dynamics.
        - Output
            y: Gray-scale (uint8 or uint16) or binary image.
        - Description
            regmin creates a binary image f by computing the regional
            minima of f , according to the connectivity defined by the
            structuring element Bc . A regional minimum is a flat zone not
            surrounded by flat zones of lower gray values. A flat zone is a
            maximal connected component of a gray-scale image with same
            pixel values. There are three output options: binary image;
            valued image; and generalized dynamics. The dynamics of a
            regional minima is the minimum height a pixel has to climb in a
            walk to reach another regional minima with a higher dynamics.
            The area-dyn is the minimum area a catchment basin has to raise
            to reach another regional minima with higher area-dynamics. The
            volume-dyn is the minimum volume a catchment basin has to raise
            to reach another regional minima with a higher volume dynamics.
            The dynamics concept was first introduced in Grimaud:92 and it
            is the basic notion for the hierarchical or multiscale watershed
            transform.
        - Examples
            #
            #   example 1
            #
            a = to_uint8([
                [10,  10,  10,  10,  10,  10,  10],
                [10,   9,   6,  18,   6,   5,  10],
                [10,   9,   6,  18,   6,   5,  10],
                [10,   9,   9,  15,   4,   9,  10],
                [10,   9,   9,  15,  12,  10,  10],
                [10,  10,  10,  10,  10,  10,  10]])
            print regmin(a)
            print regmin(a,secross(),'value')
            print regmin(a,secross(),'dynamics')
            #
            #   example 2
            #
            f1=readgray('bloodcells.tif')
            m1=regmin(f1,sebox())
            show(f1,m1)
            f2=hmin(f1,70)
            show(f2)
            m2=regmin(f2,sebox())
            show(f2,m2)
            #
            #   example 3
            #
            f=readgray('cameraman.tif')
            g=gradm(f)
            mh=regmin(g,secross(),'dynamics')
            ws1=cwatershed(g, binary(mh, 20))
            ws2=cwatershed(g, binary(mh, 40))
            show(ws1)
            show(ws2)
    """

    if option != 'binary':
        raise ValueError, "mmorph.regmin only implements option 'binary'"
    if Bc is None: Bc = secross()
    fplus = addm(f,1)
    g = subm(suprec(fplus,f,Bc),f)
    y = union(threshad(g,1),threshad(f,0,0))
    return y


def se2interval(a, b):
    """
        - Purpose
            Create an interval from a pair of structuring elements.
        - Synopsis
            Iab = se2interval(a, b)
        - Input
            a: Structuring Element Left extremity.
            b: Structuring Element Right extremity.
        - Output
            Iab: Interval
        - Description
            se2interval creates the interval [a,b] from the structuring
            elements a and b such that a is less or equal b .

    """

    Iab = (a,neg(b))
    return Iab


def se2hmt(A, Bc):
    """
        - Purpose
            Create a Hit-or-Miss Template (or interval) from a pair of
            structuring elements.
        - Synopsis
            Iab = se2hmt(A, Bc)
        - Input
            A:  Structuring Element Left extremity.
            Bc: Structuring Element Complement of the right extremity.
        - Output
            Iab: Interval
        - Description
            se2hmt creates the Hit-or-Miss Template (HMT), also called
            interval [A,Bc] from the structuring elements A and Bc such that
            A is included in the complement of Bc . The only difference
            between this function and se2interval is that here the second
            structuring element is the complement of the one used in the
            other function. The advantage of this function over
            se2interval is that this one is more flexible in the use of
            the structuring elements as they are not required to have the
            same size.

    """

    Iab = (A,Bc)
    return Iab


def sebox(r=1):
    """
        - Purpose
            Create a box structuring element.
        - Synopsis
            B = sebox(r=1)
        - Input
            r: Non-negative integer. Default: 1. Radius.
        - Output
            B: Structuring Element
        - Description
            sebox creates the structuring element B formed by r successive
            Minkowski additions of the elementary square (i.e., the 3x3
            square centered at the origin) with itself. If R=0, B is the
            unitary set that contains the origin. If R=1, B is the
            elementary square itself.
        - Examples
            #
            b1 = sebox()
            seshow(b1)
            b2 = sebox(2)
            seshow(b2)
    """

    B = sesum(binary([[1,1,1],
                      [1,1,1],
                      [1,1,1]]),r)
    return B


def secross(r=1):
    """
        - Purpose
            Diamond structuring element and elementary 3x3 cross.
        - Synopsis
            B = secross(r=1)
        - Input
            r: Double Default: 1. (radius).
        - Output
            B: Structuring Element
        - Description
            secross creates the structuring element B formed by r
            successive Minkowski additions of the elementary cross (i.e.,
            the 3x3 cross centered at the origin) with itself. If r=0, B is
            the unitary set that contains the origin. If r=1 , B is the
            elementary cross itself.
        - Examples
            #
            b1 = secross()
            print seshow(b1)
            b2 = secross(2)
            print seshow(b2)
    """

    B = sesum(binary([[0,1,0],
                          [1,1,1],
                          [0,1,0]]),r)
    return B


def sedisk(r=3, DIM="2D", METRIC="EUCLIDEAN", FLAT="FLAT", h=0):
    """
        - Purpose
            Create a disk or a semi-sphere structuring element.
        - Synopsis
            B = sedisk(r=3, DIM="2D", METRIC="EUCLIDEAN", FLAT="FLAT",
            h=0)
        - Input
            r:      Non-negative integer. Default: 3. Disk radius.
            DIM:    String Default: "2D". '1D', '2D, or '3D'.
            METRIC: String Default: "EUCLIDEAN". 'EUCLIDEAN', ' CITY-BLOCK',
                    'OCTAGON', or ' CHESSBOARD'.
            FLAT:   String Default: "FLAT". 'FLAT' or 'NON-FLAT'.
            h:      Double Default: 0. Elevation of the center of the
                    semi-sphere.
        - Output
            B: Structuring Element
        - Description
            sedisk creates a flat structuring element B that is disk under
            the metric METRIC , centered at the origin and with radius r or
            a non-flat structuring element that is a semi-sphere under the
            metric METRIC, centered at (0, h) and with radius r . This
            structuring element can be created on the 1D, 2D or 3D space.
        - Examples
            #
            #   example 1
            #
            a=seshow(sedisk(10,'2D','CITY-BLOCK'))
            b=seshow(sedisk(10,'2D','EUCLIDEAN'))
            c=seshow(sedisk(10,'2D','OCTAGON'))
            show(a)
            show(b)
            show(c)
            #
            #   example 2
            #
            d=seshow(sedisk(10,'2D','CITY-BLOCK','NON-FLAT'))
            e=seshow(sedisk(10,'2D','EUCLIDEAN','NON-FLAT'))
            f=seshow(sedisk(10,'2D','OCTAGON','NON-FLAT'))
            show(d)
            show(e)
            show(f)
            #
            #   example 3
            #
            g=sedisk(3,'2D','EUCLIDEAN','NON-FLAT')
            seshow(g)
            h=sedisk(3,'2D','EUCLIDEAN','NON-FLAT',5)
            seshow(h)
    """
    from string import upper
    from numpy import resize, transpose, arange
    from numpy import sqrt, arange, transpose, maximum

    METRIC = upper(METRIC)
    FLAT   = upper(FLAT)            
    assert DIM=='2D','Supports only 2D structuring elements'
    if FLAT=='FLAT': y = binary([1])
    else:            y = to_int32([h])
    if r==0: return y
    if METRIC == 'CITY-BLOCK':
        if FLAT == 'FLAT':
            b = secross(1)
        else:
            b = to_int32([[-2147483647, 0,-2147483647],
                          [          0, 1,          0],
                          [-2147483647, 0,-2147483647]])
        return sedilate(y,sesum(b,r))
    elif METRIC == 'CHESSBOARD':
        if FLAT == 'FLAT':
            b = sebox(1)
        else:
            b = to_int32([[1,1,1],
                          [1,1,1],
                          [1,1,1]])
        return sedilate(y,sesum(b,r))
    elif METRIC == 'OCTAGON':
        if FLAT == 'FLAT':
            b1,b2 = sebox(1),secross(1)
        else:
            b1 = to_int32([[1,1,1],[1,1,1],[1,1,1]])
            b2 = to_int32([[-2147483647, 0,-2147483647],
                           [          0, 1,          0],
                           [-2147483647, 0,-2147483647]])
        if r==1: return b1
        else:    return sedilate( sedilate(y,sesum(b1,r//2)) ,sesum(b2,(r+1)//2))
    elif METRIC == 'EUCLIDEAN':
        v = arange(-r,r+1)
        x = resize(v, (len(v), len(v)))
        y = transpose(x)
        Be = binary(sqrt(x*x + y*y) <= (r+0.5))
        if FLAT=='FLAT':
            return Be
        be = h + to_int32( sqrt( maximum((r+0.5)*(r+0.5) - (x*x) - (y*y),0)))
        be = intersec(gray(Be,'int32'),be)
        return be
    else:
        assert 0,'Non valid metric'
    return B


def seline(l=3, theta=0):
    """
        - Purpose
            Create a line structuring element.
        - Synopsis
            B = seline(l=3, theta=0)
        - Input
            l:     Non-negative integer. Default: 3.
            theta: Double Default: 0. (degrees, clockwise)
        - Output
            B: Structuring Element
        - Description
            seline creates a structuring element B that is a line segment
            that has an extremity at the origin, length l and angle theta (0
            degrees is east direction, clockwise). If l=0 , it generates the
            origin.
        - Examples
            #
            seshow(seline())
            b1 = seline(4,45)
            seshow(b1)
            b2 = seline(4,-180)
            seshow(b2)
            a=text('Line')
            b=dilate(a,b1)
            show(a)
            show(b)
    """
    import numpy
    from numpy import pi, tan, cos, sin, sign, floor, arange, transpose, array, ones

    theta = pi*theta//180
    if abs(tan(theta)) <= 1:
        s  = sign(cos(theta))
        x0 = arange(0, l * cos(theta)-(s*0.5),s)
        x1 = floor(x0 * tan(theta) + 0.5)
    else:
        s  = sign(sin(theta))
        x1 = arange(0, l * sin(theta) - (s*0.5),s)
        x0 = floor(x1 / tan(theta) + 0.5)
    x = to_int32(transpose(array([x1,x0])))
    B = set2mat((x,binary(ones((x.shape[1],1),numpy.uint8))))
    return B


def serot(B, theta=45, DIRECTION="CLOCKWISE"):
    """
        - Purpose
            Rotate a structuring element.
        - Synopsis
            BROT = serot(B, theta=45, DIRECTION="CLOCKWISE")
        - Input
            B:         Structuring Element
            theta:     Double Default: 45. Degrees of rotation. Available
                       values are multiple of 45 degrees.
            DIRECTION: String Default: "CLOCKWISE". 'CLOCKWISE' or '
                       ANTI-CLOCKWISE'.
        - Output
            BROT: Structuring Element
        - Description
            serot rotates a structuring element B of an angle theta .
        - Examples
            #
            b = img2se(binary([[0, 0, 0], [0, 1, 1], [0, 0, 0]]));
            seshow(b)
            seshow(serot(b))
            seshow(serot(b,45,'ANTI-CLOCKWISE'))
    """
    from string import upper
    from numpy import array, sin, cos, transpose
    from numpy import cos, sin, pi, concatenate, transpose, array

    DIRECTION = upper(DIRECTION)            
    if DIRECTION == "ANTI-CLOCKWISE":
       theta = -theta
    SA = mat2set(B)
    theta = pi * theta//180
    (y,v)=SA
    if len(y)==0: return binary([0])
    x0 = y[:,1] * cos(theta) - y[:,0] * sin(theta)
    x1 = y[:,1] * sin(theta) + y[:,0] * cos(theta)
    x0 = to_int32((x0 +0.5)*(x0>=0) + (x0-0.5)*(x0<0))
    x1 = to_int32((x1 +0.5)*(x1>=0) + (x1-0.5)*(x1<0))
    x = transpose(array([transpose(x1),transpose(x0)]))
    BROT = set2mat((x,v))
    return BROT


def seshow(B, option="NORMAL"):
    """
        - Purpose
            Display a structuring element as an image.
        - Synopsis
            y = seshow(B, option="NORMAL")
        - Input
            B:      Structuring Element
            option: String Default: "NORMAL". 'NORMAL', ' EXPAND' or '
                    NON-FLAT'
        - Output
            y: Gray-scale (uint8 or uint16) or binary image.
        - Description
            seshow used with the option EXPAND generates an image y that
            is a suitable graphical representation of the structuring
            element B . This function is useful to convert a structuring
            element to an image. The origin of the structuring element is at
            the center of the image. If B is flat, y is binary, otherwise, y
            is signed int32 image. When using the option NON-FLAT, the
            output y is always a signed int32 image.
        - Examples
            #
            #   example 1
            #
            b=secross(3);
            print seshow(b)
            a = seshow(b,'EXPAND')
            show(a)
            print seshow(b,'NON-FLAT')
            #
            #   example 2
            #
            b=sedisk(2,'2D','EUCLIDEAN','NON-FLAT')
            print seshow(b)
    """
    from string import upper

    option = upper(option)            
    if option=='NON-FLAT': 
        y=to_int32([0])
        if isbinary(B):
            B = intersec(gray(B,'int32'),0)
    elif option=='NORMAL':
        if isbinary(B):    y=binary([1])
        else:
           y=to_int32([0])
    elif option=='EXPAND':
        assert isbinary(B), 'This option is only available with flat SE'
        y = sedilate(binary([1]),B)
        b1= binary(y>=0)
        b0= erode(y,B)
        y = bshow(b1,y,b0)
        return y
    else:
        print 'seshow: not a valid flag: NORMAL, EXPAND or NON-FLAT'
    y = sedilate(y,B)
    return y


def sesum(B=None, N=1):
    """
        - Purpose
            N-1 iterative Minkowski additions
        - Synopsis
            NB = sesum(B=None, N=1)
        - Input
            B: Structuring Element Default: None (3x3 elementary cross).
            N: Non-negative integer. Default: 1.
        - Output
            NB: Structuring Element
        - Description
            sesum creates the structuring element NB from N - 1 iterative
            Minkowski additions with the structuring element B .
        - Examples
            #
            #   example 1
            #
            b = img2se(binary([[1, 1, 1], [1, 1, 1], [0, 1, 0]]))
            seshow(b)
            b3 = sesum(b,3)
            seshow(b3)
            #
            #   example 2
            #
            b = sedisk(1,'2D','CITY-BLOCK','NON-FLAT');
            seshow(b)
            seshow(sesum(b,2))
    """

    if B is None: B = secross()
    if N==0:
        if isbinary(B): return binary([1])
        else:           return to_int32([0]) # identity
    NB = B
    for i in xrange(N-1):
        NB = sedilate(NB,B)
    return NB


def setrans(Bi, t):
    """
        - Purpose
            Translate a structuring element
        - Synopsis
            Bo = setrans(Bi, t)
        - Input
            Bi: Structuring Element
            t:
        - Output
            Bo: Structuring Element
        - Description
            setrans translates a structuring element by a specific value.
        - Examples
            #
            b1 = seline(5)
            seshow(b1)
            b2 = setrans(b1,[2,-2])
            seshow(b2)
    """

    x,v=mat2set(Bi)
    Bo = set2mat((x+t,v))
    Bo = Bo.astype(Bi.dtype)
    return Bo


def sereflect(Bi):
    """
        - Purpose
            Reflect a structuring element
        - Synopsis
            Bo = sereflect(Bi)
        - Input
            Bi: Structuring Element
        - Output
            Bo: Structuring Element
        - Description
            sereflect reflects a structuring element by rotating it 180
            degrees.
        - Examples
            #
            b1 = seline(5,30)
            print seshow(b1)
            b2 = sereflect(b1)
            print seshow(b2)
    """
    Bo = serot(Bi, 180)
    return Bo


def sedilate(B1, B2):
    """
        - Purpose
            Dilate one structuring element by another
        - Synopsis
            Bo = sedilate(B1, B2)
        - Input
            B1: Structuring Element
            B2: Structuring Element
        - Output
            Bo: Structuring Element
        - Description
            sedil dilates an structuring element by another. The main
            difference between this dilation and dil is that the dilation
            between structuring elements are not bounded, returning another
            structuring element usually larger than anyone of them. This
            gives the composition of the two structuring elements by
            Minkowski addition.
        - Examples
            #
            b1 = seline(5)
            seshow(b1)
            b2 = sedisk(2)
            seshow(b2)
            b3 = sedilate(b1,b2)
            seshow(b3)
    """
    from numpy import newaxis, array, int32

    assert (isbinary(B1) or (B1.dtype == int32)) and (isbinary(B2) or B2.dtype == int32), 'pymorph.sedilate: s.e. must be binary or int32'
    if len(B1.shape) == 1: B1 = B1[newaxis,:]
    if len(B2.shape) == 1: B2 = B2[newaxis,:]
    if B1.dtype==int32 or B2.dtype == int32:
       Bo = to_int32([limits(to_int32([0]))[0]])
       if isbinary(B1):
          B1 = gray(B1,'int32',0)
       if isbinary(B2):
          B2 = gray(B2,'int32',0)
    else:
       Bo = binary([0])
    x,v = mat2set(B2)
    if len(x):
        for i in xrange(x.shape[0]):
            s = add4dilate(B1,v[i])
            st= setrans(s,x[i])
            Bo = seunion(Bo,st)
    return Bo


def seunion(B1, B2):
    """
        - Purpose
            Union of structuring elements
        - Synopsis
            B = seunion(B1, B2)
        - Input
            B1: Structuring Element
            B2: Structuring Element
        - Output
            B: Structuring Element
        - Description
            seunion creates a structuring element from the union of two
            structuring elements.
        - Examples
            #
            b1 = seline(5)
            seshow(b1)
            b2 = sedisk(3)
            seshow(b2)
            b3 = seunion(b1,b2)
            seshow(b3)
    """
    from numpy import maximum, ones, asarray, newaxis, int32

    assert B1.dtype == B2.dtype, 'Cannot have different datatypes:'
    type1 = B1.dtype
    if len(B1) == 0: return B2
    if len(B1.shape) == 1: B1 = B1[newaxis,:]
    if len(B2.shape) == 1: B2 = B2[newaxis,:]
    if B1.shape <> B2.shape:
        inf = limits(B1)[0]
        h1,w1 = B1.shape
        h2,w2 = B2.shape
        H,W = max(h1,h2),max(w1,w2)
        Hc,Wc = (H-1)//2,(W-1)//2    # center
        BB1,BB2 = asarray(B1),asarray(B2)
        B1, B2  = inf * ones((H,W),int32), inf *ones((H,W),int32)
        dh1s , dh1e = (h1-1)//2 , (h1-1)//2 + (h1+1)%2 # deal with even and odd dimensions
        dw1s , dw1e = (w1-1)//2 , (w1-1)//2 + (w1+1)%2
        dh2s , dh2e = (h2-1)//2 , (h2-1)//2 + (h2+1)%2
        dw2s , dw2e = (w2-1)//2 , (w2-1)//2 + (w2+1)%2
        B1[ Hc-dh1s : Hc+dh1e+1  ,  Wc-dw1s : Wc+dw1e+1 ] = BB1
        B2[ Hc-dh2s : Hc+dh2e+1  ,  Wc-dw2s : Wc+dw2e+1 ] = BB2
    B = maximum(B1,B2).astype(type1)
    return B


def show(f, f1=None, f2=None, f3=None, f4=None, f5=None, f6=None):
    """
        - Purpose
            Display binary or gray-scale images and optionally overlay it
            with binary images.
        - Synopsis
            show(f, f1=None, f2=None, f3=None, f4=None, f5=None, f6=None)
        - Input
            f:  Gray-scale (uint8 or uint16) or binary image.
            f1: Binary image. Default: None. Red overlay.
            f2: Binary image. Default: None. Green overlay.
            f3: Binary image. Default: None. Blue overlay.
            f4: Binary image. Default: None. Magenta overlay.
            f5: Binary image. Default: None. Yellow overlay.
            f6: Binary image. Default: None. Cyan overlay.

        - Description
            Displays the binary or gray-scale (uint8 or uint16) image f ,
            and optionally overlay it with up to six binary images f1 to f6
            in the following colors: f1 as red, f2 as green, f3 as blue, f4
            as yellow, f5 as magenta, and f6 as cian. The image is displayed
            in the MATLAB figure only if no output parameter is given.
        - Examples
            #
            f=readgray('mribrain.tif');
            f150=threshad(f,150);
            f200=threshad(f,200);
            show(f);
            show(f150);
            show(f,f150,f200);
    """
    import adpil

    if len(f.shape) != 2:
       print "Error, show: can only process gray-scale and binary images."
       return
    if   f1 == None: y = gshow(f)
    elif f2 == None: y = gshow(f,f1)
    elif f3 == None: y = gshow(f,f1,f2)
    elif f4 == None: y = gshow(f,f1,f2,f3)
    elif f5 == None: y = gshow(f,f1,f2,f3,f4)
    elif f6 == None: y = gshow(f,f1,f2,f3,f4,f5)
    elif f6 == None: y = gshow(f,f1,f2,f3,f4,f5)
    else:            y = gshow(f,f1,f2,f3,f4,f5,f6)
    adpil.adshow(y)
    return


def skelm(f, B=None, option="binary"):
    """
        - Purpose
            Morphological skeleton (Medial Axis Transform).
        - Synopsis
            y = skelm(f, B=None, option="binary")
        - Input
            f:      Binary image.
            B:      Structuring Element Default: None (3x3 elementary
                    cross).
            option: String Default: "binary". Choose one of: binary: output
                    a binary image (medial axis); value: output a grayscale
                    image with values of the radius of the disk to
                    reconstruct the original image (medial axis transform).
        - Output
            y: Gray-scale (uint8 or uint16) or binary image.
        - Description
            skelm creates the image y by computing the morphological
            skeleton by B of the image f , when option is BINARY. In this
            case, the pixels of value 1 in y are center of maximal balls
            (generated from B ) included in f . This is also called Medial
            Axis. If option is VALUE, the non zeros pixels in y are the
            radius plus 1 of the maximal balls. This is called Medial Axis
            Transform or valued morphological skeleton.
        - Examples
            #
            #   example 1
            #
            from numpy import ones
            a=neg(frame(binary(ones((7,9)))))
            print a
            print skelm(a)
            print skelm(a,sebox())
            #
            #   example 2
            #
            a=readgray('pcbholes.tif')
            b=skelm(a)
            show(a)
            show(b)
            #
            #   example 3
            #
            c=skelm(a,secross(),'value')
            show(c)
    """
    from string import upper
    from numpy import asarray
    if B is None: B = secross()
    assert isbinary(f),'Input binary image only'
    option = upper(option)
    k1,k2 = limits(f)
    y = gray(intersec(f, k1),'uint16')
    iszero = asarray(y)
    nb = sesum(B,0)
    for r in xrange(1,65535):
        ero = erode(f,nb)
        if isequal(ero, iszero): break
        f1 = openth( ero, B)
        nb = sedilate(nb, B)
        y = union(y, gray(f1,'uint16',r))
    if option == 'BINARY':
        y = binary(y)
    return y


def skelmrec(f, B=None):
    """
        - Purpose
            Morphological skeleton reconstruction (Inverse Medial Axis
            Transform).
        - Synopsis
            y = skelmrec(f, B=None)
        - Input
            f: Gray-scale (uint8 or uint16) or binary image.
            B: Structuring Element Default: None (3x3 elementary cross).
        - Output
            y: Binary image.
        - Description
            skelmrec reconstructs the valued morphological skeleton to
            recover the original image.
        - Examples
            #
            from numpy import ones
            a=neg(frame(binary(ones((7,9)))))
            print a
            b=skelm(a,secross(),'value')
            print b
            c=skelmrec(b,secross())
            print c
    """
    from numpy import ravel
    if B is None: B = secross()
    y = binary(intersec(f, 0))
    for r in xrange(f.max(),1,-1):
        y = dilate(union(y,binary(f,r)), B)
    y = union(y, binary(f,1))
    return y


def skiz(f, Bc=None, LINEREG="LINES", METRIC=None):
    """
        - Purpose
            Skeleton of Influence Zone - also know as Generalized Voronoi
            Diagram
        - Synopsis
            y = skiz(f, Bc=None, LINEREG="LINES", METRIC=None)
        - Input
            f:       Binary image.
            Bc:      Structuring Element Default: None (3x3 elementary
                     cross). Connectivity for the distance measurement.
            LINEREG: String Default: "LINES". 'LINES' or 'REGIONS'.
            METRIC:  String Default: None. 'EUCLIDEAN' if specified.
        - Output
            y: Gray-scale (uint8 or uint16) or binary image.
        - Description
            skiz creates the image y by detecting the lines which are
            equidistant to two or more connected components of f , according
            to the connectivity defined by Bc . Depending on with the flag
            LINEREG, y will be a binary image with the skiz lines or a
            labeled image representing the zone of influence regions. When
            the connected objects of f are single points, the skiz is the
            Voronoi diagram.
        - Examples
            #
            #   example 1
            #
            f=readgray('blob2.tif')
            y=skiz(f,sebox(),'LINES','EUCLIDEAN')
            show(f,y)
            #
            #   example 2
            #
            from numpy import zeros
            f=binary(zeros((100,100)))
            f[30,25],f[20,75],f[50,50],f[70,30],f[80,70] = 1,1,1,1,1
            y = skiz(f,sebox(),'LINES','EUCLIDEAN')
            show(f,y)
    """
    from string import upper
    if Bc is None: Bc = secross()
    LINEREG = upper(LINEREG)
    if METRIC is not None: METRIC = upper(METRIC)
    d = dist( neg(f), Bc, METRIC)
    return cwatershed(d,f,Bc,LINEREG)
    return y

def subm(f1, f2):
    """
        - Purpose
            Subtraction of two images, with saturation.
        - Synopsis
            y = subm(f1, f2)
        - Input
            f1: Unsigned gray-scale (uint8 or uint16), signed (int32) or
                binary image.
            f2: Unsigned gray-scale (uint8 or uint16), signed (int32) or
                binary image. Or constant.
        - Output
            y: Unsigned gray-scale (uint8 or uint16), signed (int32) or
               binary image.
        - Description
            subm creates the image y by pixelwise subtraction of the image
            f2 from the image f1 . When the subtraction of the values of two
            pixels is negative, 0 is taken as the result of the subtraction.
            When f1 and f2 are binary images, y represents the set
            subtraction of f2 from f1 .
        - Examples
            #
            #   example 1
            #
            f = to_uint8([255,   255,    0,   10,   20,   10,    0,   255,  255])
            g = to_uint8([10,     20,   30,   40,   50,   40,   30,    20,    10])
            print subm(f, g)
            print subm(f, 100)
            print subm(100, f)
            #
            #   example 2
            #
            a = readgray('boxdrill-C.tif')
            b = readgray('boxdrill-B.tif')
            c = subm(a,b)
            show(a)
            show(b)
            show(c)
    """
    from numpy import array, clip

    if type(f2) is array:
        assert f1.dtype == f2.dtype, 'Cannot have different datatypes:'
    bottom,top=limits(f1)
    y = clip(f1.astype('d') - f2, bottom, top)
    y = y.astype(f1.dtype)
    return y


def supcanon(f, Iab, theta=45, DIRECTION="CLOCKWISE"):
    """
        - Purpose
            Union of sup-generating or hit-miss operators.
        - Synopsis
            y = supcanon(f, Iab, theta=45, DIRECTION="CLOCKWISE")
        - Input
            f:         Binary image.
            Iab:       Interval
            theta:     Double Default: 45. Degrees of rotation: 45, 90, or
                       180.
            DIRECTION: String Default: "CLOCKWISE". 'CLOCKWISE' or '
                       ANTI-CLOCKWISE'
        - Output
            y: Binary image.
        - Description
            supcanon creates the image y by computing the union of
            transformations of the image f by sup-generating operators.
            These hit-miss operators are characterized by rotations (in the
            clockwise or anti-clockwise direction) of theta degrees of the
            interval Iab .

    """
    from string import upper

    DIRECTION = upper(DIRECTION)            
    y = intersec(f,0)
    for t in xrange(0,360,theta):
        Irot = interot( Iab, t, DIRECTION )
        y = union( y, supgen(f, Irot))
    return y


def supgen(f, INTER):
    """
        - Purpose
            Sup-generating (hit-miss).
        - Synopsis
            y = supgen(f, INTER)
        - Input
            f:     Binary image.
            INTER: Interval
        - Output
            y: Binary image.
        - Description
            supgen creates the binary image y by computing the
            transformation of the image f by the sup-generating operator
            characterized by the interval Iab . The sup-generating operator
            is just a relaxed template matching, where the criterion to keep
            a shape is that it be inside the interval Iab . Note that we
            have the classical template matching when a=b . Note yet that
            the sup-generating operator is equivalent to the classical
            hit-miss operator.
        - Examples
            #
            #   example 1
            #
            f=binary([
               [0,0,1,0,0,1,1],
               [0,1,0,0,1,0,0],
               [0,0,0,1,1,0,0]])
            i=endpoints()
            print intershow(i)
            g=supgen(f,i)
            print g
            #
            #   example 2
            #
            a=readgray('gear.tif')
            b=supgen(a,endpoints())
            show(a)
            show(dilate(b))
    """

    A,Bc = INTER
    y = intersec(erode(f,A),
                   erode(neg(f),Bc))
    return y


def suprec(f, g, Bc=None):
    """
        - Purpose
            Sup-reconstruction.
        - Synopsis
            y = suprec(f, g, Bc=None)
        - Input
            f:  Gray-scale (uint8 or uint16) or binary image. Marker image.
            g:  Gray-scale (uint8 or uint16) or binary image. Conditioning
                image.
            Bc: Structuring Element Default: None (3x3 elementary cross). (
                connectivity).
        - Output
            y: Image
        - Description
            suprec creates the image y by an infinite number of recursive
            iterations (iterations until stability) of the erosion of f by
            Bc conditioned to g . We say that y is the sup-reconstruction of
            g from the marker f .

    """
    from numpy import product
    if Bc is None: Bc = secross()
    n = product(f.shape)
    y = cerode(f,g,Bc,n);
    return y


def bshow(f1, f2=None, f3=None, factor=17):
    """
        - Purpose
            Generate a graphical representation of overlaid binary images.
        - Synopsis
            y = bshow(f1, f2=None, f3=None, factor=17)
        - Input
            f1:     Binary image.
            f2:     Binary image. Default: None.
            f3:     Binary image. Default: None.
            factor: Double Default: 17. Expansion factor for the output
                    image. Use odd values above 9.
        - Output
            y: Binary image. shaded image.
        - Description
            Generate an expanded binary image as a graphical representation
            of up to three binary input images. The 1-pixels of the first
            image are represented by square contours, the pixels of the
            optional second image are represented by circles and for the
            third image they are represented by shaded squares. This
            function is useful to create graphical illustration of small
            images.
        - Examples
            #
            f1=text('b')
            f2=text('w')
            g2=bshow(f1,f2)
            show(g2)
            f3=text('x')
            g3=bshow(f1,f2,f3)
            show(g3);
    """
    import numpy
    from numpy import newaxis, zeros, resize, transpose, floor, arange, array

    if f1.shape == (): f1 = array([f1])
    if len(f1.shape) == 1: f1 = f1[newaxis,:]
    if (`f1.shape` != `f2.shape`) or \
       (`f1.shape` != `f3.shape`) or \
       (`f2.shape` != `f3.shape`):
        print 'Different sizes.'
        return None
    s = factor
    if factor < 9: s = 9
    h,w = f1.shape
    y = zeros((s*h, s*w),numpy.int32)
    xc = resize(range(s), (s,s))
    yc = transpose(xc)
    r  = int(floor((s-8)/2. + 0.5))
    circle = (xc - s//2)**2 + (yc - s//2)**2 <= r**2
    r = arange(s) % 2
    fillrect = resize(array([r, 1-r]), (s,s))
    fillrect[0  ,:] = 0
    fillrect[s-1,:] = 0
    fillrect[:  ,0] = 0
    fillrect[:  ,s-1] = 0
    for i in xrange(h):
        for j in xrange(w):
            m, n = s*i, s*j
            if f1 and f1[i,j]:
                y[m     ,n:n+s] = 1
                y[m+s-1 ,n:n+s] = 1
                y[m:m+s ,n    ] = 1
                y[m:m+s ,n+s-1] = 1
            if f2 and f2[i,j]:
                y[m:m+s, n:n+s] = y[m:m+s, n:n+s] + circle
            if f3 and f3[i,j]:
                y[m:m+s, n:n+s] = y[m:m+s, n:n+s] + fillrect
    y = y > 0
    return y


def swatershed(f, g, B=None, LINEREG="LINES"):
    """
        - Purpose
            Detection of similarity-based watershed from markers.
        - Synopsis
            y = swatershed(f, g, B=None, LINEREG="LINES")
        - Input
            f:       Gray-scale (uint8 or uint16) image.
            g:       Gray-scale (uint8 or uint16) or binary image. Marker
                     image. If binary, each connected component is an object
                     marker. If gray, it is assumed it is a labeled image.
            B:       Structuring Element Default: None (3x3 elementary
                     cross). (watershed connectivity)
            LINEREG: String Default: "LINES". 'LINES' or ' REGIONS'.
        - Output
            y: Gray-scale (uint8 or uint16) or binary image.
        - Description
            swatershed creates the image y by detecting the domain of the
            catchment basins of f indicated by g , according with the
            connectivity defined by B . This watershed is a modified version
            where each basin is defined by a similarity criterion between
            pixels. The original watershed is normally applied to the
            gradient of the image. In this case, the gradient is taken
            internally. According to the flag LINEREG y will be a labeled
            image of the catchment basins domain or just a binary image that
            presents the watershed lines. The implementation of this
            function is based on LotuFalc:00 .
        - Examples
            #
            f = to_uint8([
                [0,  0,  0,  0,  0,  0,  0],
                [0,  1,  0,  0,  0,  1,  0],
                [0,  1,  0,  0,  0,  1,  0],
                [0,  1,  1,  1,  1,  1,  0],
                [0,  1,  0,  0,  0,  0,  0],
                [0,  0,  0,  0,  0,  0,  0]])
            m = to_uint8([
                [0,  0,  0,  0,  0,  0,  0],
                [0,  1,  0,  0,  0,  0,  0],
                [0,  0,  0,  0,  0,  0,  0],
                [0,  0,  0,  0,  0,  0,  0],
                [0,  0,  0,  0,  0,  0,  0],
                [0,  0,  0,  2,  0,  0,  0]])
            print swatershed(f,m,secross(),'REGIONS')
    """

    if B is None: B = secross()
    print 'Not implemented yet'
    return None
    return y


def symdif(f1, f2):
    """
        - Purpose
            Syetric difference between two images
        - Synopsis
            y = symdif(f1, f2)
        - Input
            f1: Gray-scale (uint8 or uint16) or binary image.
            f2: Gray-scale (uint8 or uint16) or binary image.
        - Output
            y: Image i
        - Description
            symdif creates the image y by taken the union of the
            subtractions of f1 from f2 and f2 from f1 . When f1 and f2 are
            binary images, y represents the set of points that are in f1 and
            not in f2 or that are in f2 and not in f1 .
        - Examples
            #
            #   example 1
            #
            a = to_uint8([1, 2, 3, 4, 5])
            b = to_uint8([5, 4, 3, 2, 1])
            print symdif(a,b)
            #
            #   example 2
            #
            c = readgray('tplayer1.tif')
            d = readgray('tplayer2.tif')
            e = symdif(c,d)
            show(c)
            show(d)
            show(e)
    """

    y = union(subm(f1,f2),subm(f2,f1))
    return y


def thick(f, Iab=None, n=-1, theta=45, DIRECTION="CLOCKWISE"):
    """
        - Purpose
            Image transformation by thickening.
        - Synopsis
            y = thick(f, Iab=None, n=-1, theta=45, DIRECTION="CLOCKWISE")
        - Input
            f:         Binary image.
            Iab:       Interval Default: None (homothick).
            n:         Non-negative integer. Default: -1. Number of
                       iterations.
            theta:     Double Default: 45. Degrees of rotation: 45, 90, or
                       180.
            DIRECTION: String Default: "CLOCKWISE". 'CLOCKWISE' or '
                       ANTI-CLOCKWISE'
        - Output
            y: Binary image.
        - Description
            thick creates the binary image y by performing a thickening of
            the binary image f . The number of iterations of the thickening
            is n and each iteration is performed by union of f with the
            points that are detected in f by the hit-miss operators
            characterized by rotations of theta degrees of the interval Iab
            .

    """
    from numpy import product
    from string import upper
    if Iab is None: Iab = homothick()
    DIRECTION = upper(DIRECTION)            
    assert isbinary(f),'f must be binary image'
    if n == -1: n = product(f.shape)
    y = f
    zero = intersec(f,0)
    for i in xrange(n):
        aux = zero
        for t in xrange(0,360,theta):
            sup = supgen( y, interot(Iab, t, DIRECTION))
            aux = union( aux, sup)
            y = union( y, sup)
        if isequal(aux,zero): break
    return y


def thin(f, Iab=None, n=-1, theta=45, DIRECTION="CLOCKWISE"):
    """
        - Purpose
            Image transformation by thinning.
        - Synopsis
            y = thin(f, Iab=None, n=-1, theta=45, DIRECTION="CLOCKWISE")
        - Input
            f:         Binary image.
            Iab:       Interval Default: None (homothin).
            n:         Non-negative integer. Default: -1. Number of
                       iterations.
            theta:     Double Default: 45. Degrees of rotation: 45, 90, or
                       180.
            DIRECTION: String Default: "CLOCKWISE". 'CLOCKWISE' or '
                       ANTI-CLOCKWISE'
        - Output
            y: Binary image.
        - Description
            thin creates the binary image y by performing a thinning of
            the binary image f . The number of iterations of the thinning is
            n and each iteration is performed by subtracting the points that
            are detect in f by hit-miss operators characterized by rotations
            of theta of the interval Iab . When n is infinite and the
            interval is homothin (default conditions), thin gives the
            skeleton by thinning.
        - Examples
            #
            f=readgray('scissors.tif')
            f1=thin(f)
            show(f,f1) # skeleton
            f2=thin(f1,endpoints(),15) # prunning 15 pixels
            show(f,f2) # prunned skeleton
    """
    from numpy import product
    from string import upper
    if Iab is None: Iab = homothin()
    DIRECTION = upper(DIRECTION)            
    assert isbinary(f),'f must be binary image'
    if n == -1: n = product(f.shape)
    y = f
    zero = intersec(f,0)
    for i in xrange(n):
        aux = zero
        for t in xrange(0,360,theta):
            sup = supgen( y, interot(Iab, t, DIRECTION))
            aux = union( aux, sup)
            y = subm( y, sup)
        if isequal(aux,zero): break
    return y


def union(f1, f2, f3=None, f4=None, f5=None):
    """
        - Purpose
            Union of images.
        - Synopsis
            y = union(f1, f2, f3=None, f4=None, f5=None)
        - Input
            f1: Gray-scale (uint8 or uint16) or binary image.
            f2: Gray-scale (uint8 or uint16) or binary image. Or constant
            f3: Gray-scale (uint8 or uint16) or binary image. Default: None.
                Or constant.
            f4: Gray-scale (uint8 or uint16) or binary image. Default: None.
                Or constant.
            f5: Gray-scale (uint8 or uint16) or binary image. Default: None.
                Or constant.
        - Output
            y: Image
        - Description
            union creates the image y by taking the pixelwise maximum
            between the images f1, f2, f3, f4, and f5 . When f1, f2, f3, f4,
            and f5 are binary images, y represents the union of them.
        - Examples
            #
            #   example 1
            #
            f=to_uint8([255, 255,  0,  10,   0, 255, 250])
            print 'f=',f
            g=to_uint8([  0,  40, 80, 140, 250,  10,  30])
            print 'g=',g
            print union(f, g)
            print union(f, 255)
            #
            #   example 2
            #
            a = readgray('form-ok.tif')
            b = readgray('form-1.tif')
            c = union(a,b)
            show(a)
            show(b)
            show(c)
            #
            #   example 3
            #
            d = readgray('danaus.tif')
            e = (d < 80)
            f = union(d,gray(e))
            show(d)
            show(e)
            show(f)
            #
            #   example 4
            #
            g = readgray('tplayer1.tif')
            h = readgray('tplayer2.tif')
            i = readgray('tplayer3.tif')
            j = union(g,h,i)
            show(g)
            show(h)
            show(i)
            show(j)
    """
    from numpy import maximum

    y = maximum(f1,f2)
    if f3: y = maximum(y,f3)
    if f4: y = maximum(y,f4)
    if f5: y = maximum(y,f5)
    y = y.astype(f1.dtype)
    return y


def watershed(f, Bc=None, LINEREG="LINES"):
    """
        - Purpose
            Watershed detection.
        - Synopsis
            y = watershed(f, Bc=None, LINEREG="LINES")
        - Input
            f:       Gray-scale (uint8 or uint16) or binary image.
            Bc:      Structuring Element Default: None (3x3 elementary
                     cross). ( connectivity)
            LINEREG: String Default: "LINES". 'LINES' or ' REGIONS'.
        - Output
            y: Gray-scale (uint8 or uint16) or binary image.
        - Description
            watershed creates the image y by detecting the domain of the
            catchment basins of f , according to the connectivity defined by
            Bc . According to the flag LINEREG y will be a labeled image of
            the catchment basins domain or just a binary image that presents
            the watershed lines. The implementation of this function is
            based on VincSoil:91 .
        - Examples
            #
            f=readgray('astablet.tif')
            grad=gradm(f)
            w1=watershed(grad,sebox())
            w2=watershed(grad,sebox(),'REGIONS')
            show(grad)
            show(w1)
            lblshow(w2)
    """
    from string import upper
    if Bc is None: Bc = secross()
    return cwatershed(f,regmin(f,Bc),upper(LINEREG))
    return y


def bench(count=10):
    """
        - Purpose
            benchmarking main functions of the toolbox.
        - Synopsis
            bench(count=10)
        - Input
            count: Double Default: 10. Number of repetitions of each
                   function.

        - Description
            bench measures the speed of many of SDC Morphology Toolbox
            functions in seconds. An illustrative example of the output of
            bench is, for a MS-Windows 2000 Pentium 4, 2.4GHz, 533MHz
            system bus, machine: SDC Morphology Toolbox V1.2 27Sep02
            Benchmark Made on Wed Jul 16 15:33:17 2003 computer= win32 image
            filename= csample.jpg width= 640 , height= 480 Function time
            (sec.) 1. Union bin 0.00939999818802 2. Union gray-scale
            0.00319999456406 3. Dilation bin, secross 0.0110000014305 4.
            Dilation gray, secross 0.00780000686646 5. Dilation gray,
            non-flat 3x3 SE 0.0125 6. Open bin, secross 0.0125 7. Open
            gray-scale, secross 0.0141000032425 8. Open gray, non-flat 3x3
            SE 0.0235000014305 9. Distance secross 0.021899998188 10.
            Distance Euclidean 0.0264999985695 11. Geodesic distance
            secross 0.028100001812 12. Geodesic distance Euclidean
            0.303100001812 13. Area open bin 0.0639999985695 14. Area open
            gray-scale 0.148500001431 15. Label secross 0.071899998188 16.
            Regional maximum, secross 0.043700003624 17. Open by rec,
            gray, secross 0.0515000104904 18. ASF by rec, oc, secross, 1
            0.090600001812 19. Gradient, gray-scale, secross
            0.0171999931335 20. Thinning 0.0984999895096 21. Watershed
            0.268799996376 Average 0.0632523809161

    """
    from sys import platform
    from time import time, asctime
    from numpy import average, zeros

    filename = 'csample.jpg'
    f = readgray(filename)
    fbin=threshad(f,150)
    se = img2se(binary([[0,1,0],[1,1,1],[0,1,0]]),'NON-FLAT',to_int32([[0,1,0],[1,2,1],[0,1,0]]))
    m=thin(fbin)
    tasks=[
       [' 1. Union  bin                      ','union(fbin,fbin)'],
       [' 2. Union  gray-scale               ','union(f,f)'],
       [' 3. Dilation  bin, secross        ','dilate(fbin)'],
       [' 4. Dilation  gray, secross       ','dilate(f)'],
       [' 5. Dilation  gray, non-flat 3x3 SE ','dilate(f,se)'],
       [' 6. Open      bin, secross        ','open(fbin)'],
       [' 7. Open      gray-scale, secross ','open(f)'],
       [' 8. Open      gray, non-flat 3x3 SE ','open(f,se)'],
       [' 9. Distance  secross             ','dist(fbin)'],
       ['10. Distance  Euclidean             ','dist(fbin,sebox(),"euclidean")'],
       ['11. Geodesic distance secross     ','gdist(fbin,m)'],
       ['12. Geodesic distance Euclidean     ','gdist(fbin,m,sebox(),"euclidean")'],
       ['13. Area open bin                   ','areaopen(fbin,100)'],
       ['14. Area open gray-scale            ','areaopen(f,100)'],
       ['15. Label secross                 ','label(fbin)'],
       ['16. Regional maximum, secross     ','regmax(f)'],
       ['17. Open by rec, gray, secross    ','openrec(f)'],
       ['18. ASF by rec, oc, secross, 1    ','asfrec(f)'],
       ['19. Gradient, gray-scale, secross ','gradm(f)'],
       ['20. Thinning                        ','thin(fbin)'],
       ['21. Watershed                       ','cwatershed(f,fbin)']]
    result = zeros((21),'d')
    for t in xrange(len(tasks)):
       print tasks[t][0],tasks[t][1]
       t1=time()
       for k in xrange(count):
          a=eval(tasks[t][1])
       t2=time()
       result[t]= (t2-t1)/(count+0.0)
    print version() +' Benchmark'
    print 'Made on ',asctime(),' computer=',platform
    print 'image filename=',filename,' width=', f.shape[1],', height=',f.shape[0]
    print '    Function                            time (sec.)'
    for j in xrange(21):
     print tasks[j][0], result[j]
    print '    Average                         ', average(result)
    out=[]


def maxleveltype(TYPE='uint8'):
    """
        - Purpose
            Returns the maximum value associated to an image datatype
        - Synopsis
            max = maxleveltype(TYPE='uint8')
        - Input
            TYPE: String Default: 'uint8'. One of the strings 'uint8',
                  'uint16' or 'int32', specifying the image type
        - Output
            max: the maximum level value of type TYPE

    """

    max = 0
    if   TYPE == 'uint8'  : max=255
    elif TYPE == 'binary' : max=1
    elif TYPE == 'uint16' : max=65535
    elif TYPE == 'int32'  : max=2147483647
    else:
        assert 0, 'does not support this data type:'+TYPE
    return max


def to_int32(f):
    """
        - Purpose
            Convert an image to an int32 image.
        - Synopsis
            img = to_int32(f)
        - Input
            f: Any image
        - Output
            img: The converted image
        - Description
            int32 clips the input image between the values -2147483647 and
            2147483647 and converts it to the signed 32-bit datatype.

    """
    from numpy import array, clip

    img = array(clip(f,-2147483647,2147483647)).astype('i')
    return img


def to_uint8(f):
    """
        - Purpose
            Convert an image to an uint8 image.
        - Synopsis
            img = to_uint8(f)
        - Input
            f: Any image
        - Output
            img: Gray-scale uint8 image. The converted image
        - Description
            uint8 clips the input image between the values 0 and 255 and
            converts it to the unsigned 8-bit datatype.
        - Examples
            #
            a = to_int32([-3,0,8,600])
            print to_uint8(a)
    """
    from numpy import array, clip, uint8

    img = array(clip(f,0,255),uint8)
    return img


def to_uint16(f):
    """
        - Purpose
            Convert an image to a uint16 image.
        - Synopsis
            img = to_uint16(f)
        - Input
            f: Any image
        - Output
            img: The converted image
        - Description
            uint16 clips the input image between the values 0 and 65535 and
            converts it to the unsigned 16-bit datatype.
        - Examples
            #
            a = to_int32([-3,0,8,100000])
            print to_uint16(a)
    """
    from numpy import array, clip

    img = array(clip(f,0,65535)).astype('H')
    return img


def datatype(f):
    """
        - Purpose
            Return the image datatype string
        - Synopsis
            type = datatype(f)
        - Input
            f: Unsigned gray-scale (uint8 or uint16), signed (int32) or
               binary image. Any image
        - Output
            type: String String representation of image type: 'binary',
                  'uint8', 'uint16' or 'int32'
        - Description
            datatype returns a string that identifies the pixel datatype
            of the image f .

    """
    from numpy import bool, uint8, uint16, int32
    code = f.dtype
    if   code == bool: type='binary'
    elif code == uint8: type='uint8'
    elif code == uint16: type='uint16'
    elif code == int32: type='int32'
    else:
        assert 0,'Does not accept this typecode: %s' % code
    return type


def add4dilate(f, c):
    """
        - Purpose
            Addition for dilation
        - Synopsis
            a = add4dilate(f, c)
        - Input
            f: Gray-scale (uint8 or uint16) or binary image. Image
            c: Gray-scale (uint8 or uint16) or binary image. Constant
        - Output
            a: Image f + c

    """
    from numpy import asarray, minimum, maximum

    if c:            
       y = asarray(f,'d') + c
       k1,k2 = limits(f)
       y = ((f==k1) * k1) + ((f!=k1) * y)
       y = maximum(minimum(y,k2),k1)
       a = y.astype(f.dtype)
    else:
       a = f
    return a


def mat2set(A):
    """
        - Purpose
            Converts image representation from matrix to set
        - Synopsis
            CV = mat2set(A)
        - Input
            A: Image in matrix format, where the origin (0,0) is at the
               center of the matrix.
        - Output
            CV: Image Tuple with array of pixel coordinates and array of
                corresponding pixel values
        - Description
            Return tuple with array of pixel coordinates and array of
            corresponding pixel values. The input image is in the matrix
            format, like the structuring element, where the origin (0,0) is
            at the center of the matrix.
        - Examples
            #
            #   example 1
            #
            f=to_uint8([[1,2,3],[4,5,6],[7,8,9]])
            i,v=mat2set(f)
            print i
            print v
            #
            #   example 2
            #
            f=to_uint8([[1,2,3,4],[5,6,7,8]])
            i,v=mat2set(f)
            print i
            print v
    """
    from numpy import take, ravel, nonzero, transpose, newaxis

    if len(A.shape) == 1: A = A[newaxis,:]
    offsets = nonzero(ravel(A) - limits(A)[0])[0]
    if len(offsets) == 0: return ([],[])
    (h,w) = A.shape
    x = [0,1]
    x[0] = offsets//w - (h-1)//2
    x[1] = offsets%w - (w-1)//2
    x = transpose(x)
    CV = x,take(ravel(A),offsets)
    return CV


def set2mat(A):
    """
        - Purpose
            Converts image representation from set to matrix
        - Synopsis
            M = set2mat(A)
        - Input
            A: Tuple with array of pixel coordinates and optional array of
               corresponding pixel values
        - Output
            M: Image in matrix format, origin (0,0) at the matrix center
        - Description
            Return an image in the matrix format built from a tuple of an
            array of pixel coordinates and a corresponding array of pixel
            values
        - Examples
            #
            coord=to_int32([
              [ 0,0],
              [-1,0],
              [ 1,1]])
            A=set2mat((coord,))
            print A
            print datatype(A)
            vu = to_uint8([1,2,3])
            f=set2mat((coord,vu))
            print f
            print datatype(f)
            vi = to_int32([1,2,3])
            g=set2mat((coord,vi))
            print g
            print datatype(g)
    """
    from numpy import put, ones, ravel, shape, newaxis, array, asarray, max, int32

    if len(A) == 2:            
        x, v = A
        v = asarray(v)
    elif len(A) == 1:
        x = A[0]
        v = ones((len(x),), '1')
    else:
        raise TypeError, 'Argument must be a tuple of length 1 or 2'
    if len(x) == 0:  return array([0]).astype(v.dtype)
    if len(x.shape) == 1: x = x[newaxis,:]
    dh,dw = abs(x).max(0)
    h,w = (2*dh)+1, (2*dw)+1 
    M=ones((h,w),int32) * limits(v)[0]
    offset = x[:,0] * w + x[:,1] + (dh*w + dw)
    put(M,offset,v)
    return M.astype(v.dtype)

def pad4n(f, Bc, value, scale=1):
    """
        - Purpose
            pad4n
        - Synopsis
            y = pad4n(f, Bc, value, scale=1)
        - Input
            f:     Image
            Bc:    Structuring Element ( connectivity).
            value: 
            scale: Default: 1.
        - Output
            y: The converted image

    """
    from numpy import ones, array

    if type(Bc) is not array:
      Bc = seshow(Bc)            
    Bh, Bw = Bc.shape
    assert Bh%2 and Bw%2, 'structuring element must be odd sized'
    ch, cw = scale * Bh/2, scale * Bw/2
    g = value * ones( f.shape + scale * (array(Bc.shape) - 1))
    g[ ch: -ch, cw: -cw] = f
    y = g.astype(f.dtype)
    return y


__figs__ = [None]

def plot(plotitems=[], options=[], outfig=-1, filename=None):
    """
        - Purpose
            Plot a function.
        - Synopsis
            fig = plot(plotitems=[], options=[], outfig=-1, filename=None)
        - Input
            plotitems: Default: []. List of plotitems.
            options:   Default: []. List of options.
            outfig:    Default: -1. Integer. Figure number. 0 creates a new
                       figure.
            filename:  Default: None. String. Name of the PNG output file.
        - Output
            fig: Figure number.

        - Examples
            #
            import numpy
            #
            x = numpy.arange(0, 2*numpy.pi, 0.1)
            plot([[x]])
            y1 = numpy.sin(x)
            y2 = numpy.cos(x)
            opts = [['title', 'Example Plot'],\
                    ['grid'],\
                    ['style', 'linespoints'],\
                    ['xlabel', '"X values"'],\
                    ['ylabel', '"Y Values"']]
            y1_plt = [x, y1, None,    'sin(X)']
            y2_plt = [x, y2, 'lines', 'cos(X)']
            #
            # plotting two graphs using one step
            fig1 = plot([y1_plt, y2_plt], opts, 0)
            #
            # plotting the same graphs using two steps
            fig2 = plot([y1_plt], opts, 0)
            fig2 = plot([y2_plt], opts, fig2)
            #
            # first function has been lost, lets recover it
            opts.append(['replot'])
            fig2 = plot([y1_plt], opts, fig2)
    """
    import matplotlib
    import numpy

    newfig = 0
    if (plotitems == 'reset'):
        __figs__[0] = None
        __figs__[1:] = []
        return 0
    if len(plotitems) == 0:
        # no plotitems specified: replot current figure
        if __figs__[0]:
            outfig = __figs__[0]
            g = __figs__[outfig]
            g.replot()
            return outfig
        else:
            #assert 0, "plot error: There is no current figure\n"
            print "plot error: There is no current figure\n"
            return 0
    # figure to be plotted
    if ((outfig < 0) and __figs__[0]):
        # current figure
        outfig = __figs__[0]
    elif ( (outfig == 0) or ( (outfig == -1) and not __figs__[0] )  ):
        # new figure
        newfig = 1
        outfig = len(__figs__)
    elif outfig >= len(__figs__):
        #assert 0, 'plot error: Figure ' + str(outfig) + 'does not exist\n'
        print 'plot error: Figure ' + str(outfig) + 'does not exist\n'
        return 0
    #current figure
    __figs__[0] = outfig
    # Gnuplot pointer
    if newfig:
        if len(__figs__) > 20:
            print '''plot error: could not create figure. Too many PlotItems in memory (20). Use
                     plot('reset') to clear table'''
            return 0

        g = Gnuplot.Gnuplot()
        __figs__.append(g)
    else:
        g = __figs__[outfig]

    # options
    try:
        options.remove(['replot'])
    except:
        g.reset()
    try:
        #default style
        g('set data style lines')
        for option in options:
            if option[0] == 'grid':
                g('set grid')
            elif option[0] == 'title':
                g('set title "' + option[1] + '"')
            elif option[0] == 'xlabel':
                g('set xlabel ' + option[1])
            elif option[0] == 'ylabel':
                g('set ylabel ' + option[1])
            elif option[0] == 'style':
                g('set data style ' + option[1])
            else:
                print "plot warning: Unknown option: " + option[0]
    except:
        print "plot warning: Bad usage in options! Using default values. Please, use help.\n"
    # Plot items: item[0]=x, item[1]=y, item[2]=style
    for item in plotitems:
        try:
            title = None
            style = None
            x = numpy.ravel(item[0])
            if len(item) > 1:
                # y axis specified
                y = numpy.ravel(item[1])
                if len(item) > 2:
                    # style specified
                    style = item[2]
                    if len(item) > 3:
                        title = item[3]
            else:
                # no y axis specified
                y = x
                x = numpy.arange(len(y))
            g.replot(Gnuplot.Data(x, y, title=title, with=style))
        except:
            g.reset()
            if newfig:
                __figs__.pop()
            #assert 0, "plot error: Bad usage in plotitems! Impossible to plot graph. Please, use help.\n"
            print "plot error: Bad usage in plotitems! Impossible to plot graph. Please, use help.\n"
            return 0
    # PNG file
    if filename:
        g.hardcopy(filename, terminal='png', color=1)
    fig = outfig
    return fig

# vim: set ts=4 sts=4 sw=4 expandtab smartindent:
