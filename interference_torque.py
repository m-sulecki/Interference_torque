from abaqus import *
from abaqusConstants import *
def createInterferentionwithTorque(dso, dwo, dwi, l, fr, tq, s1, s11, s2,s22,ts, tw, wybor, toleranceIN, toleranceOUT, check, Younguser, Poissonuser,):

# opis przedzialu
# ----------------------------------------------------------------------
# przydzial wiersza dla wymiaru walka
# dso - dimension shaft outside, srednica zewnetrzna walka
#dsoValues - tablica z granicznymi wartosciami przedzialow
    dsoValues = [3,6,10,14,18,24,30,40,50,65,80,100,120,140,160,180,200,225,250,280,315,355,400,450,500]
    row_s = -1
    if dso <= 1:
        dso=dso
    else:
        # ponumerowanie kazdego elementu w tablicy dsoValues
        for index_s, dsoValue in enumerate(dsoValues):
            if (dso <= dsoValue):
                row_s = index_s
                break
#-------------------------------------------------------------------------
#dwiValues - tablica z granicznymi wartosciami przedzialow
    dwiValues = [3,6,10,14,18,24,30,40,50,65,80,100,120,140,160,180,200,225,250,280,315,355,400,450,500]
    row_w = -1
    if dwi <= 1:
        dwi=dwi
    else:
        # ponumerowanie kazdego elementu w tablicy dwiValues
        for index_w, dwiValue in enumerate(dwiValues):
            if (dwi <= dwiValue):
                row_w = index_w
                break

# przydzial kolumny
# -----------------------------------------------------------------
    toleranceOUTs = ['h6', 'h7', 'h8', 'p6', 'p7', 'p8', 'r6', 'r7', 'r8', 's6', 's7', 's8', 't6', 't7', 't8', 'u6',
                     'u7', 'u8', 'x6', 'x7', 'x8', 'z6', 'z7', 'z8', 'none']

    for index_s, toleranceOUT2 in enumerate(toleranceOUTs):
        if toleranceOUT2 == toleranceOUT:
            col_s = index_s
            break

    # przydzial kolumny
    # -----------------------------------------------------------------
    toleranceINs = ['H6', 'H7', 'H8', 'P6', 'P7', 'P8', 'R6', 'R7', 'R8', 'S6', 'S7', 'S8', 'T6', 'T7', 'T8', 'U6',
                    'U7', 'U8', 'X6', 'X7', 'X8', 'Z6', 'Z7', 'Z8', 'none']

    for index_w, toleranceIN2 in enumerate(toleranceINs):
        if toleranceIN2 == toleranceIN:
            col_w = index_w
            break

    #zapisana tabela jest tolerancja dla wymiarow zewnetrznych, tj. walek. Dla walka nalezy DODAC (!!!) wartosc z tabeli, natomiast dla otworow ODJAC (!!!)
    deviation = [
        ['-0.006', '-0.01', '-0.014', '0.006', '0.006', '0.006', '0.01', '0.01', '0.01', '0.014', '0.014', '0.014', '0',
         '0', '0', '0.018', '0.018', '0.018', '0.02', '0.02', '0.02', '0.026', '0.026', '0.026', '0'],
        ['-0.008', '-0.012', '-0.018', '0.012', '0.012', '0.012', '0.015', '0.015', '0.015', '0.019', '0.019', '0.019',
         '0', '0', '0', '0.023', '0.023', '0.023', '0.028', '0.028', '0.028', '0.035', '0.035', '0.035', '0'],
        ['-0.009', '-0.015', '-0.022', '0.015', '0.015', '0.015', '0.019', '0.019', '0.019', '0.023', '0.023', '0.023',
         '0', '0', '0', '0.028', '0.028', '0.028', '0.034', '0.034', '0.034', '0.042', '0.042', '0.042', '0'],
        ['-0.011', '-0.018', '-0.027', '0.018', '0.018', '0.018', '0.023', '0.023', '0.023', '0.028', '0.028', '0.028',
         '0', '0', '0', '0.033', '0.033', '0.033', '0.04', '0.04', '0.04', '0.05', '0.05', '0.05', '0'],
        ['-0.011', '-0.018', '-0.027', '0.018', '0.018', '0.018', '0.023', '0.023', '0.023', '0.028', '0.028', '0.028',
         '0', '0', '0', '0.033', '0.033', '0.033', '0.045', '0.045', '0.045', '0.06', '0.06', '0.06', '0'],
        ['-0.013', '-0.021', '-0.033', '0.022', '0.022', '0.022', '0.028', '0.028', '0.028', '0.035', '0.035', '0.035',
         '0', '0', '0', '0.041', '0.041', '0.041', '0.054', '0.054', '0.054', '0.073', '0.073', '0.073', '0'],
        ['-0.013', '-0.021', '-0.033', '0.022', '0.022', '0.022', '0.028', '0.028', '0.028', '0.035', '0.035', '0.035',
         '0.041', '0.041', '0.041', '0.048', '0.048', '0.048', '0.064', '0.064', '0.064', '0.088', '0.088', '0.088', '0'],
        ['-0.016', '-0.025', '-0.039', '0.026', '0.026', '0.026', '0.034', '0.034', '0.034', '0.043', '0.043', '0.043',
         '0.048', '0.048', '0.048', '0.06', '0.06', '0.06', '0.08', '0.08', '0.08', '0.112', '0.112', '0.112', '0'],
        ['-0.016', '-0.025', '-0.039', '0.026', '0.026', '0.026', '0.034', '0.034', '0.034', '0.043', '0.043', '0.043',
         '0.054', '0.054', '0.054', '0.07', '0.07', '0.07', '0.097', '0.097', '0.097', '0.136', '0.136', '0.136', '0'],
        ['-0.019', '-0.03', '-0.046', '0.032', '0.032', '0.032', '0.041', '0.041', '0.041', '0.053', '0.053', '0.053',
         '0.066', '0.066', '0.066', '0.087', '0.087', '0.087', '0.122', '0.122', '0.122', '0.172', '0.172', '0.172', '0'],
        ['-0.019', '-0.03', '-0.046', '0.032', '0.032', '0.032', '0.043', '0.043', '0.043', '0.059', '0.059', '0.059',
         '0.075', '0.075', '0.075', '0.102', '0.102', '0.102', '0.146', '0.146', '0.146', '0.21', '0.21', '0.21', '0'],
        ['-0.022', '-0.035', '-0.054', '0.037', '0.037', '0.037', '0.051', '0.051', '0.051', '0.071', '0.071', '0.071',
         '0.091', '0.091', '0.092', '0.124', '0.124', '0.124', '0.178', '0.178', '0.178', '0.258', '0.258', '0.258', '0'],
        ['-0.022', '-0.035', '-0.054', '0.037', '0.037', '0.037', '0.054', '0.054', '0.054', '0.079', '0.079', '0.079',
         '0.104', '0.104', '0.104', '0.144', '0.144', '0.144', '0.21', '0.21', '0.21', '0.31', '0.31', '0.31', '0'],
        ['-0.025', '-0.04', '-0.063', '0.043', '0.043', '0.043', '0.063', '0.063', '0.063', '0.092', '0.092', '0.092',
         '0.122', '0.122', '0.122', '0.17', '0.17', '0.17', '0.248', '0.248', '0.248', '0.365', '0.365', '0.365', '0'],
        ['-0.025', '-0.04', '-0.063', '0.043', '0.043', '0.043', '0.065', '0.065', '0.065', '0.1', '0.1', '0.1',
         '0.134', '0.134', '0.134', '0.19', '0.19', '0.19', '0.28', '0.28', '0.28', '0.415', '0.415', '0.415', '0'],
        ['-0.025', '-0.04', '-0.063', '0.043', '0.043', '0.043', '0.068', '0.068', '0.068', '0.108', '0.108', '0.108',
         '0.146', '0.146', '0.146', '0.21', '0.21', '0.21', '0.31', '0.31', '0.31', '0.465', '0.465', '0.465', '0'],
        ['-0.029', '-0.046', '-0.072', '0.05', '0.05', '0.05', '0.077', '0.077', '0.077', '0.122', '0.122', '0.122',
         '0.166', '0.166', '0.166', '0.236', '0.236', '0.236', '0.35', '0.35', '0.35', '0.52', '0.52', '0.52', '0'],
        ['-0.029', '-0.046', '-0.072', '0.05', '0.05', '0.05', '0.08', '0.08', '0.08', '0.13', '0.13', '0.13', '0.18',
         '0.18', '0.18', '0.258', '0.258', '0.258', '0.385', '0.385', '0.385', '0.575', '0.575', '0.575', '0'],
        ['-0.029', '-0.046', '-0.072', '0.05', '0.05', '0.05', '0.084', '0.084', '0.084', '0.14', '0.14', '0.14',
         '0.196', '0.196', '0.196', '0.284', '0.284', '0.284', '0.425', '0.425', '0.425', '0.64', '0.64', '0.64', '0'],
        ['-0.032', '-0.052', '-0.081', '0.056', '0.056', '0.056', '0.094', '0.094', '0.094', '0.158', '0.158', '0.158',
         '0.218', '0.218', '0.218', '0.315', '0.315', '0.315', '0.475', '0.475', '0.475', '0.71', '0.71', '0.71', '0'],
        ['-0.032', '-0.052', '-0.081', '0.056', '0.056', '0.056', '0.098', '0.098', '0.098', '0.17', '0.17', '0.17',
         '0.24', '0.24', '0.24', '0.35', '0.35', '0.35', '0.525', '0.525', '0.525', '0.79', '0.79', '0.79', '0'],
        ['-0.036', '-0.057', '-0.089', '0.062', '0.062', '0.062', '0.108', '0.108', '0.108', '0.19', '0.19', '0.19',
         '0.268', '0.268', '0.268', '0.39', '0.39', '0.39', '0.59', '0.59', '0.59', '0.9', '0.9', '0.9', '0'],
        ['-0.036', '-0.057', '-0.089', '0.062', '0.062', '0.062', '0.114', '0.114', '0.114', '0.208', '0.208', '0.208',
         '0.294', '0.294', '0.294', '0.435', '0.435', '0.435', '0.66', '0.66', '0.66', '1', '1', '1', '0'],
        ['-0.04', '-0.063', '-0.097', '0.068', '0.068', '0.068', '0.126', '0.126', '0.126', '0.232', '0.232', '0.232',
         '0.33', '0.33', '0.33', '0.49', '0.49', '0.49', '0.74', '0.74', '0.74', '1.1', '1.1', '1.1', '0'],
        ['-0.04', '-0.063', '-0.097', '0.068', '0.068', '0.068', '0.132', '0.132', '0.132', '0.252', '0.252', '0.252',
         '0.36', '0.36', '0.36', '0.54', '0.54', '0.54', '0.82', '0.82', '0.82', '1.25', '1.25', '1.25', '0']]

    # ks- wartosc odczytana z tabeli odchylek dla walka
    # kw- wartosc odczytana z tabeli odchylek dla piasty
#row_s - rzad dla walka (shaft)
#row_w - rzad dla piasty (wheel)
#col_s - kolumna dla walka (shaft)
#col_w - kolumna dla piasty (wheel)
    ks = float(deviation[row_s][col_s])
    kw = float(deviation[row_w][col_w])
#--------------------------------------------------------------------------------------------------------------------------
    #utworzenie czesci walek
    mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=100.0)
    mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(0.0, 0.0), point1=((dso+ks)/2, 0.0))
    mdb.models['Model-1'].Part(dimensionality=THREE_D, name='shaft', type=DEFORMABLE_BODY)
    mdb.models['Model-1'].parts['shaft'].BaseSolidExtrude(depth=l*1.2, sketch=
        mdb.models['Model-1'].sketches['__profile__'])

    #utworzenie czesci piasta
    mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=100.0)
    mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
        0.0, 0.0), point1=((dwi-kw)/2, 0.0))
    mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
        0.0, 0.0), point1=(dwo/2, 0.0))
    mdb.models['Model-1'].Part(dimensionality=THREE_D, name='wheel', type=
        DEFORMABLE_BODY)
    mdb.models['Model-1'].parts['wheel'].BaseSolidExtrude(depth=l, sketch=
        mdb.models['Model-1'].sketches['__profile__'])

    # utworzenie materialu
    if (check == False):

        if wybor=='Steel':
            materialName='Steel'
            Young=210000
            Poisson=0.29
        elif wybor=='Aluminium':
            materialName = 'Aluminium'
            Young = 70000
            Poisson = 0.33

        elif wybor=='Titanum':
            materialName = 'Titanum'
            Young = 110000
            Poisson = 0.36

        elif wybor=='Copper':
            materialName = 'Copper'
            Young = 117000
            Poisson = 0.35

    elif (check == True):
        materialName = 'User Define'
        Young = Younguser
        Poisson = Poissonuser



    mdb.models['Model-1'].Material(description='Material', name=materialName)
    mdb.models['Model-1'].materials[materialName].Elastic(table=((Young, Poisson),))

    # utworzenie sekcji
    mdb.models['Model-1'].HomogeneousSolidSection(material=materialName, name='Section-1_IT', thickness=None)
    mdb.models['Model-1'].HomogeneousSolidSection(material=materialName, name='Section-2_IT', thickness=None)

    # przypisanie czesci do sekcji
    mdb.models['Model-1'].parts['shaft'].Set(cells=
    mdb.models['Model-1'].parts['shaft'].cells.getSequenceFromMask(('[#1 ]',),),name='Set-1')
    mdb.models['Model-1'].parts['shaft'].SectionAssignment(offset=0.0, offsetField='',offsetType=MIDDLE_SURFACE, region=
        mdb.models['Model-1'].parts['shaft'].sets['Set-1'],sectionName='Section-1_IT',thicknessAssignment=FROM_SECTION)
    mdb.models['Model-1'].parts['wheel'].Set(cells=mdb.models['Model-1'].parts['wheel'].cells.getSequenceFromMask(('[#1 ]',),),name='Set-2')
    mdb.models['Model-1'].parts['wheel'].SectionAssignment(offset=0.0, offsetField='',offsetType=MIDDLE_SURFACE, region=
        mdb.models['Model-1'].parts['wheel'].sets['Set-2'],sectionName='Section-2_IT',thicknessAssignment=FROM_SECTION)

    #ZMIENNA ----------------------------------------------------------
    # utworzenie zlozenia
    mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
    mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='shaft-1', part=
        mdb.models['Model-1'].parts['shaft'])
    mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='wheel-1', part=
        mdb.models['Model-1'].parts['wheel'])
    mdb.models['Model-1'].rootAssembly.translate(instanceList=('shaft-1',),vector=(0.0, 0.0, -(l*0.1)))

    # utworzenie kolejnych krokow
    mdb.models['Model-1'].StaticStep(description='Obciazenie od polaczenia na wcisk', initialInc=0.1,
                                     maxNumInc=100000,minInc=1e-12, name='Step-1_IT', previous='Initial')
    mdb.models['Model-1'].StaticStep(description='obciazenei momentem skrecajacym',initialInc=0.1,
                                     maxNumInc=100000, minInc=1e-12, name='Step-2_IT', nlgeom=OFF, previous='Step-1_IT')

    # zdefiniowanie punktu lezacego na osi piasty i skojarzenie go z powierzchnia czolowa,
    # zastosowanie coupling
    mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(0.0, 0.0, 0.0))
    mdb.models['Model-1'].rootAssembly.Set(name='m_Set-1', referencePoints=(
        mdb.models['Model-1'].rootAssembly.referencePoints[6],))
    mdb.models['Model-1'].rootAssembly.Set(name='m_Set-5', referencePoints=(
        mdb.models['Model-1'].rootAssembly.referencePoints[6],))
    mdb.models['Model-1'].rootAssembly.Surface(name='s_Surf-4', side1Faces=
        mdb.models['Model-1'].rootAssembly.instances['wheel-1'].faces.getSequenceFromMask(('[#1 ]',), ))
    mdb.models['Model-1'].Coupling(controlPoint=
        mdb.models['Model-1'].rootAssembly.sets['m_Set-5'], couplingType=DISTRIBUTING,
                                   influenceRadius=WHOLE_SURFACE,localCsys=None, name='Constraint-1', surface=
        mdb.models['Model-1'].rootAssembly.surfaces['s_Surf-4'],
                                   u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON, weightingMethod=UNIFORM)

    #ZMIENNA TARCIE---------------------------------------------
    # zdefiniowanie wlasciwosci kontaktowych
    mdb.models['Model-1'].ContactProperty('IntProp-1_IT')
    # Tangential Behavior
    mdb.models['Model-1'].interactionProperties['IntProp-1_IT'].TangentialBehavior(
        dependencies=0, directionality=ISOTROPIC, elasticSlipStiffness=None,
        formulation=PENALTY, fraction=0.005, maximumElasticSlip=FRACTION,
        pressureDependency=OFF, shearStressLimit=None, slipRateDependency=OFF,
        table=((fr,),), temperatureDependency=OFF)
    # Normal behavior
    mdb.models['Model-1'].interactionProperties['IntProp-1_IT'].NormalBehavior(
        allowSeparation=ON, constraintEnforcementMethod=DEFAULT, pressureOverclosure=HARD)

    # ukrycie jednej z czesci
    mdb.models['Model-1'].rootAssembly.Surface(name='m_Surf-2', side1Faces=
        mdb.models['Model-1'].rootAssembly.instances['wheel-1'].faces.getSequenceFromMask(('[#2 ]',), ))
    mdb.models['Model-1'].rootAssembly.Surface(name='s_Surf-2', side1Faces=
        mdb.models['Model-1'].rootAssembly.instances['shaft-1'].faces.getSequenceFromMask(('[#1 ]',), ))

    # opis zjawiska kontaktowego,
    # zaznaczenie powierzchni kontaktowych slave i master
    mdb.models['Model-1'].SurfaceToSurfaceContactStd(adjustMethod=NONE,clearanceRegion=None, createStepName='Initial',
                                                     datumAxis=None,initialClearance=OMIT, interactionProperty='IntProp-1_IT', master=
                                                     mdb.models['Model-1'].rootAssembly.surfaces['m_Surf-2'],name='Int-1_IT',
                                                     slave=mdb.models['Model-1'].rootAssembly.surfaces['s_Surf-2'],
                                                     bondingSet=None, enforcement=SURFACE_TO_SURFACE,
                                                     sliding=SMALL, supplementaryContact=SELECTIVE, thickness=ON)
    mdb.models['Model-1'].interactions['Int-1_IT'].setValuesInStep(interferenceType=SHRINK_FIT, stepName='Step-1_IT')

    # opis warunkow brzegowych
    # dla walka
    mdb.models['Model-1'].rootAssembly.Set(faces=
        mdb.models['Model-1'].rootAssembly.instances['shaft-1'].faces.getSequenceFromMask(('[#6 ]',), ), name='Set-2')
    mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial',
                                         distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-1',
                                         region=mdb.models['Model-1'].rootAssembly.sets['Set-2'], u1=SET, u2=SET,
                                         u3=SET, ur1=UNSET, ur2=UNSET, ur3=UNSET)
    # dla piasty
    #mdb.models['Model-1'].rootAssembly.Set(faces=
        #mdb.models['Model-1'].rootAssembly.instances['wheel-1'].faces.getSequenceFromMask(('[#c ]',), ), name='Set-3')
    #mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial',
                                         #distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-2_IT',
                                         #region=mdb.models['Model-1'].rootAssembly.sets['Set-3'], u1=SET, u2=SET
                                         #, u3=UNSET, ur1=UNSET, ur2=UNSET, ur3=UNSET)

    #ZMIENNA MOMENT SKRECAJACY ---------------------------------------------
    # przylozenie momentu skrecajacego do piasty
    mdb.models['Model-1'].rootAssembly.Set(name='Set-4', referencePoints=(
        mdb.models['Model-1'].rootAssembly.referencePoints[6],))
    mdb.models['Model-1'].Moment(cm3=tq, createStepName='Step-2_IT',
                                 distributionType=UNIFORM, field='', follower=ON, localCsys=None, name=
                                 'Torque', region=mdb.models['Model-1'].rootAssembly.sets['Set-4'])


#-----------------------------------------------------------------------------------------------------------

    #utworzenie osi Z wzdluz walka
    mdb.models['Model-1'].parts['shaft'].DatumAxisByPrincipalAxis(principalAxis=
        ZAXIS)
    #utworzenie partycji na powierzchni bocznej walka
    mdb.models['Model-1'].parts['shaft'].PartitionFaceByShortestPath(faces=
        mdb.models['Model-1'].parts['shaft'].faces.getSequenceFromMask(('[#1 ]', ),
        ), point1=mdb.models['Model-1'].parts['shaft'].InterestingPoint(
        mdb.models['Model-1'].parts['shaft'].edges[1], MIDDLE), point2=
        mdb.models['Model-1'].parts['shaft'].InterestingPoint(
        mdb.models['Model-1'].parts['shaft'].edges[0], MIDDLE))

    #szkicowanie na czole walka
    mdb.models['Model-1'].ConstrainedSketch(gridSpacing=2, name='__profile__',
        sheetSize=100, transform=
        mdb.models['Model-1'].parts['shaft'].MakeSketchTransform(
        sketchPlane=mdb.models['Model-1'].parts['shaft'].faces[2],
        sketchPlaneSide=SIDE1,
        sketchUpEdge=mdb.models['Model-1'].parts['shaft'].edges[3],
        sketchOrientation=RIGHT, origin=(0.0, 0.0, 0.0)))
    mdb.models['Model-1'].parts['shaft'].projectReferencesOntoSketch(filter=
        COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
    mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
        0.0, 0.0), point1=((dso/2)-ts, 0.0))
    mdb.models['Model-1'].parts['shaft'].PartitionFaceBySketch(faces=
        mdb.models['Model-1'].parts['shaft'].faces.getSequenceFromMask(('[#4 ]', ),
        ), sketch=mdb.models['Model-1'].sketches['__profile__'], sketchUpEdge=
        mdb.models['Model-1'].parts['shaft'].edges[3])
    del mdb.models['Model-1'].sketches['__profile__']

    #partycjonowanie przez wyciagniecie szkicu
    mdb.models['Model-1'].parts['shaft'].PartitionCellByExtrudeEdge(cells=
        mdb.models['Model-1'].parts['shaft'].cells.getSequenceFromMask(('[#1 ]', ),
        ), edges=(mdb.models['Model-1'].parts['shaft'].edges[2], ), line=
        mdb.models['Model-1'].parts['shaft'].datums[3], sense=FORWARD)

    #nalozenie siatki na walek
    mdb.models['Model-1'].parts['shaft'].seedPart(deviationFactor=0.1,
        minSizeFactor=0.1, size=s1)
    mdb.models['Model-1'].parts['shaft'].seedEdgeBySize(constraint=FINER,
        deviationFactor=0.1, edges=
        mdb.models['Model-1'].parts['shaft'].edges.getSequenceFromMask(('[#4c ]',
        ), ), minSizeFactor=0.1, size=s11)
    mdb.models['Model-1'].parts['shaft'].generateMesh()


    #os z wzdluz piasty
    mdb.models['Model-1'].parts['wheel'].DatumAxisByPrincipalAxis(principalAxis=
        ZAXIS)

    #partycjonowanie powierzchni bocznej piasty
    mdb.models['Model-1'].parts['wheel'].PartitionFaceByShortestPath(faces=
        mdb.models['Model-1'].parts['wheel'].faces.getSequenceFromMask(('[#1 ]', ),
        ), point1=mdb.models['Model-1'].parts['wheel'].vertices[1], point2=
        mdb.models['Model-1'].parts['wheel'].vertices[0])

    #szkic na czole piasty
    mdb.models['Model-1'].ConstrainedSketch(gridSpacing=2, name='__profile__',
        sheetSize=100, transform=
        mdb.models['Model-1'].parts['wheel'].MakeSketchTransform(
        sketchPlane=mdb.models['Model-1'].parts['wheel'].faces[3],
        sketchPlaneSide=SIDE1,
        sketchUpEdge=mdb.models['Model-1'].parts['wheel'].edges[4],
        sketchOrientation=RIGHT, origin=(0.0, 0.0, 0.0)))
    mdb.models['Model-1'].parts['wheel'].projectReferencesOntoSketch(filter=
        COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
    mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
        0.0, 0.0), point1=((dwi/2)+tw, 0.0))
    mdb.models['Model-1'].parts['wheel'].PartitionFaceBySketch(faces=
        mdb.models['Model-1'].parts['wheel'].faces.getSequenceFromMask(('[#8 ]', ),
        ), sketch=mdb.models['Model-1'].sketches['__profile__'], sketchUpEdge=
        mdb.models['Model-1'].parts['wheel'].edges[4])
    del mdb.models['Model-1'].sketches['__profile__']

    #partycjonowanie przez wyciagniecie szkicu
    mdb.models['Model-1'].parts['wheel'].PartitionCellByExtrudeEdge(cells=
        mdb.models['Model-1'].parts['wheel'].cells.getSequenceFromMask(('[#1 ]', ),
        ), edges=(mdb.models['Model-1'].parts['wheel'].edges[1], ), line=
        mdb.models['Model-1'].parts['wheel'].datums[3], sense=FORWARD)

    #siatka mes na piascie
    mdb.models['Model-1'].parts['wheel'].seedPart(deviationFactor=0.1,
        minSizeFactor=0.1, size=s2)
    mdb.models['Model-1'].parts['wheel'].seedEdgeBySize(constraint=FINER,
        deviationFactor=0.1, edges=
        mdb.models['Model-1'].parts['wheel'].edges.getSequenceFromMask(('[#50 ]',
        ), ), minSizeFactor=0.1, size=s22)
    mdb.models['Model-1'].parts['wheel'].generateMesh()


    # definicja wartosci wyjsciowych
    mdb.models['Model-1'].HistoryOutputRequest(createStepName='Step-2_IT', name=
    'H-Output-1_IT', variables=PRESELECT)
    mdb.models['Model-1'].FieldOutputRequest(createStepName='Step-2_IT', name=
    'F-Output-1_IT', variables=('S', 'E', 'UT', 'UR', 'RT', 'RM'))

    # stworzenie analizy zagadnienia
    mdb.models['Model-1'].rootAssembly.regenerate()
    mdb.Job(atTime=None, contactPrint=OFF, description='analiza tego czegos',
            echoPrint=OFF, explicitPrecision=SINGLE, getMemoryFromAnalysis=True,
            historyPrint=OFF, memory=90, memoryUnits=PERCENTAGE, model='Model-1',
            modelPrint=OFF, multiprocessingMode=DEFAULT, name='analiza',
            nodalOutputPrecision=SINGLE, numCpus=1, numGPUs=0, queue=None,
            resultsFormat=ODB, scratch='', type=ANALYSIS, userSubroutine='', waitHours=
            0, waitMinutes=0)
     #Run the job
    #mdb.jobs['analiza'].submit(consistencyChecking=OFF)
    #mdb.jobs['analiza'].waitForCompletion()
    #beam_viewport = session.Viewport(name='Results Viewport')
    #beam_Odb_Path = 'analiza.odb'
    #an_odb_object = session.openOdb(name=beam_Odb_Path)
    #beam_viewport.setValues(displayedObject=an_odb_object)
    #beam_viewport.odbDisplay.display.setValues(plotState=(DEFORMED,))

    # Post processing
    #import visualization
    #beam_viewport = session.Viewport(name='Results Viewport')
    #beam_Odb_Path = 'analiza.odb'
    #an_odb_object = session.openOdb(name=beam_Odb_Path)
    #beam_viewport.setValues(displayedObject=an_odb_object)
    #beam_viewport.odbDisplay.display.setValues(plotState=(DEFORMED,))

