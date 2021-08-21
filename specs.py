"""PDB record specifications from https://www.wwpdb.org/documentation/file-format-content/format23/sect9.html

Columns should be tab separated
"""

ALL_SPECS = dict(
    Header="""
        1 - 6	 Record name 	"HEADER"
        11 - 50	 String(40)	classification	Classifies the molecule(s)
        51 - 59	 Date	depDate	Deposition date.
        63 - 66	 IDcode	idCode	This identifier is unique within the PDB
        """,
    Obslte="""
        1 - 6	 Record name	"OBSLTE"
        9 - 10	 Continuation 	continuation	 Allows concatenation of multiple records
        12 - 20	 Date	repDate	 Date that this entry was replaced.
        22 - 25	 IDcode	idCode	 ID code of this entry.
        32 - 35	 IDcode	rIdCode	 ID code of entry that replaced this one.
        37 - 40	 IDcode	rIdCode1	 ID code of entry that replaced this one.
        42 - 45	 IDcode	rIdCode2	 ID code of entry that replaced this one.
        47 - 50	 IDcode	rIdCode3	 ID code of entry that replaced this one.
        52 - 55	 IDcode	rIdCode4	 ID code of entry that replaced this one.
        57 - 60	 IDcode	rIdCode5	 ID code of entry that replaced this one.
        62 - 65	 IDcode	rIdCode6	 ID code of entry that replaced this one.
        67 - 70	 IDcode	rIdCode7	 ID code of entry that replaced this one.""",
    Title="""
        1 - 6 	Record name	"TITLE "
        9 - 10 	Continuation 	continuation	Allows concatenation of multiple records.
        11 - 70 	String	title	Title of the experiment.""",
    Caveat="""
        1 - 6	Record name	"CAVEAT"
        9 - 10	Continuation	continuation	Allows concatenation of multiple records.
        12 - 15	IDcode	idCode	PDB ID code of this entry.
        20 - 70	String	comment	Free text giving the reason for the CAVEAT.""",
    Compnd="""
        1 - 6 	Record name	"COMPND"
        9 - 10 	Continuation	continuation 	Allows concatenation of multiple records.
        11 - 70 	Specification 	compound	Description of the molecular""",
    Source="""
        1 - 6	Record name	"SOURCE"
        9 - 10	Continuation	continuation 	Allows concatenation of multiple records.
        11 - 70	Specification 	srcName	Identifies the source of the macromolecule in """,
    Atom="""
        1 - 6	Record name	"ATOM"
        7 - 11	Integer	serial	Atomserial number.
        13 - 16	Atom	name	Atom name.
        17	Character	altLoc	Alternate location indicator.
        18 - 20	Residue name 	resName	Residue name.
        22	Character	chainID	Chain identifier.
        23 - 26	Integer	resSeq	Residue sequence number.
        27	AChar	iCode	Code for insertion of residues.
        31 - 38	Real(8.3)	x	Orthogonal coordinates for X in Angstroms.
        39 - 46	Real(8.3)	y	Orthogonal coordinates for Y in Angstroms.
        47 - 54	Real(8.3)	z	Orthogonal coordinates for Z in Angstroms.
        55 - 60	Real(6.2)	occupancy 	Occupancy.
        61 - 66	Real(6.2)	tempFactor	Temperaturefactor.
        77 - 78	LString(2)	element	Element symbol, right-justified.
        79 - 80	LString(2)	charge	Chargeon the atom. """,
    Hetatm="""
        1 - 6	Record name	 "HETATM"
        7 - 11	Integer	 serial	Atom serial number.
        13 - 16	Atom	 name	Atom name.
        17	Character	 altLoc	Alternate location indicator.
        18 - 20	Residue name	resName	Residue name.
        22	Character	 chainID	Chain identifier.
        23 - 26	Integer	 resSeq	Residue sequence number.
        27	AChar	 iCode	Code for insertion of residues.
        31 - 38	Real(8.3)	 x	Orthogonal coordinates for X.
        39 - 46	Real(8.3)	 y	Orthogonal coordinates for Y.
        47 - 54	Real(8.3)	 z	Orthogonal coordinates for Z.
        55 - 60	Real(6.2)	 occupancy	Occupancy.
        61 - 66	Real(6.2)	 tempFactor 	Temperature factor.
        77 - 78	LString(2)	 element	Element symbol; right-justified.
        79 - 80	LString(2)	 charge	Charge on the atom.""",
    Anisou="""
        1 - 6	Record name	"ANISOU"
        7 - 11 	Integer	serial	Atom serial number.
        13 - 16 	Atom	name	Atom name.
        17	Character	altLoc	Alternate location indicator
        18 - 20 	Residue name 	resName	Residue name.
        22	Character	chainID	Chain identifier.
        23 - 26 	Integer	resSeq	Residue sequence number.
        27	AChar	iCode	Insertion code.
        29 - 35 	Integer	u[0][0]	U(1,1)
        36 - 42 	Integer	u[1][1]	U(2,2)
        43 - 49 	Integer	u[2][2]	U(3,3)
        50 - 56 	Integer	u[0][1]	U(1,2)
        57 - 63 	Integer	u[0][2]	U(1,3)
        64 - 70 	Integer	u[1][2]	U(2,3)
        77 - 78 	LString(2)	element	Element symbol, right-justified.
        79 - 80 	LString(2)	charge	Charge on the atom.""",
    Ter="""
        1 - 6	Record name	"TER"
        7 - 11	Integer	serial	Serial number.
        18 - 20	Residue name 	resName	Residue name.
        22	Character	chainID	Chain identifier.
        23 - 26	Integer	resSeq	Residue sequence number.
        27	AChar	iCode	Insertion code.
        """,
    Model="""
        1 - 6	Record name	"MODEL "
        11 - 14	Integer	serial	Model serial number.
        """,
    Endmdl="""
        2 - 6 	Record name 	"ENDMDL" 	end model
        """,
    Siguij="""
        1 - 6	 Record name	"SIGUIJ"	siguij
        7 - 11	 Integer	serial	Atom serial number.
        13 - 16	 Atom	name	Atom name.
        17	 Character	altLoc	Alternate location indicator.
        18 - 20	 Residue name	resName	Residue name.
        22	 Character	chainID	Chain identifier.
        23 - 26	 Integer	resSeq	Residue sequence number.
        27	 AChar	iCode	Insertion code.
        29 - 35	 Integer	sig[1][1] 	Sigma U(1,1)
        36 - 42	 Integer	sig[2][2] 	Sigma U(2,2)
        43 - 49	 Integer	sig[3][3] 	Sigma U(3,3)
        50 - 56	 Integer	sig[1][2] 	Sigma U(1,2)
        57 - 63	 Integer	sig[1][3] 	Sigma U(1,3)
        64 - 70	 Integer	sig[2][3] 	Sigma U(2,3)
        77 - 78	 LString(2)	element	Element symbol, right-justified.
        79 - 80	 LString(2)	charge	Charge on the atom.
        """,
    Sigatm="""
        1 - 6 	Record name	"SIGATM" 	sigatm
        7 - 11 	Integer	serial	Atom serial number.
        13 - 16 	Atom	name	Atom name.
        17	Character	altLoc	Alternate location indicator.
        18 - 20 	Residue name 	resName	Residue name.
        22	Character	chainID	Chain identifier.
        23 - 26 	Integer	resSeq	Residue sequence number.
        27	AChar	iCode	Insertion code.
        31 - 38 	Real(8.3)	sigX	Standard deviations of the stored
        39 - 46 	Real(8.3)	sigY	Standard deviations of the stored
        47 - 54 	Real(8.3)	sigZ	Standard deviations of the stored
        55 - 60 	Real(6.2)	sigOcc	Standard deviation of occupancy.
        61 - 66 	Real(6.2)	sigTemp	Standard deviation of temperature
        77 - 78 	LString(2)	element	Element symbol, right-justified.
        79 - 80 	LString(2)	charge	Charge on the atom.
        """,
    Modres="""
        1 - 6	 Record name	 "MODRES"
        8 - 11	 IDcode	 idCode	 ID code of this entry.
        13 - 15	 Residue name	 resName	 Residue name used in this entry.
        17	 Character	 chainID	 Chain identifier.
        19 - 22	 Integer	 seqNum	 Sequence number.
        23	 AChar	 iCode	 Insertion code.
        25 - 27	 Residue name	 stdRes	 Standard residue name.
        30 - 70	 String	 comment	 Description of the residue
        """,
    Seqres="""
        1 - 6	Record name	"SEQRES"
        9 - 10	Integer	serNum	Serial number of the SEQRES record for the current chain. Starts at 1 and increments by one each line.Reset to 1 for each chain.
        12	Character	chainID	Chain identifier. This may be any single legal character, including a blank which is used if there is only one chain.
        14 - 17	Integer	numRes	Number of residues in the chain.This value is repeated on every record.
        20 - 22	Residue name 	resName	Residue name.
        24 - 26	Residue name 	resName1 	Residue name.
        28 - 30	Residue name 	resName2 	Residue name.
        32 - 34	Residue name 	resName3 	Residue name.
        36 - 38	Residue name 	resName4 	Residue name.
        40 - 42	Residue name 	resName5 	Residue name.
        44 - 46	Residue name 	resName6 	Residue name.
        48 - 50	Residue name 	resName7 	Residue name.
        52 - 54	Residue name 	resName8 	Residue name.
        56 - 58	Residue name 	resName9 	Residue name.
        60 - 62	Residue name 	resName10 	Residue name.
        64 - 66	Residue name 	resName11 	Residue name.
        68 - 70	Residue name 	resName12 	Residue name.
        """,
    Seqadv="""
        1 - 6	Record name 	"SEQADV"
        8 - 11	IDcode	idCode	ID code of this entry.
        13 - 15	Residue name	resName 	Name of the PDB residue in conflict.
        17	Character	chainID 	PDB chain identifier.
        19 - 22	Integer	seqNum	PDB sequence number.
        23	AChar	iCode	PDB insertion code.
        25 - 28	LString	database
        30 - 38	LString	dbIdCode	Sequence database accession number.
        40 - 42	Residue name	dbRes	Sequence database residue name.
        44 - 48	Integer	dbSeq	Sequence database sequence number.
        50 - 70	LString	conflict 	Conflict comment.
        """,
    Dbref="""
        1 - 6	Record name 	"DBREF "
        8 - 11	IDcode	idCode	ID code of this entry.
        13	Character	chainID	Chain identifier.
        15 - 18	Integer	seqBegin	Initial sequence number of the PDB sequence segment.
        19	AChar	insertBegin 	Initial insertion code of the PDB sequence segment.
        21 - 24	Integer	seqEnd	Ending sequence number of the PDB sequence segment.
        25	AChar	insertEnd	Ending insertion code of the PDB sequence segment.
        27 - 32	LString	database	Sequence database name.
        34 - 41	LString	dbAccession 	Sequence database accession code.
        43 - 54	LString	dbIdCode	Sequence database identification code.
        56 - 60	Integer	dbseqBegin	Initial sequence number of the database seqment.
        61	AChar	idbnsBeg	Insertion code of initial residue of the segment, if PDB is the reference.
        63 - 67	Integer	dbseqEnd	Ending sequence number of the database segment.
        68	AChar	dbinsEnd	Insertion code of the ending residue of the segment, if PDB is the reference.
        """,
    Conect="""
        1 - 6	Record name	 "CONECT"
        7 - 11	Integer	 serial	Atom serial number
        12 - 16	Integer	 serial1	Serial number of bonded atom
        17 - 21	Integer	 serial2	Serial number of bonded atom
        22 - 26	Integer	 serial3	Serial number of bonded atom
        27 - 31	Integer	 serial4	Serial number of bonded atom
        """,
    Cryst1="""
        1 - 6	Record name	"CRYST1"
        7 - 15	Real(9.3)	a	a (Angstroms).
        16 - 24	Real(9.3)	b	b (Angstroms).
        25 - 33	Real(9.3)	c	c (Angstroms).
        34 - 40	Real(7.2)	alpha	alpha (degrees).
        41 - 47	Real(7.2)	beta	beta (degrees).
        48 - 54	Real(7.2)	gamma	gamma (degrees).
        56 - 66	LString	sGroup	Space group.
        67 - 70	Integer	z	Z value.
        """,
    Tvect="""
        1 - 6 	Record name	"TVECT "
        8 - 10 	Integer	serial 	Serial number.
        11 - 20 	Real(10.5)	t[1]	Components of translation vector.
        21 - 30 	Real(10.5)	t[2]	Components of translation vector.
        31 - 40 	Real(10.5)	t[3]	Components of translation vector.
        41 - 70 	String	text	Comment.
        """,
    Helix="""
        1 -  6  	    Record name  	   "HELIX "
        8 - 10  	    Integer      	   serNum      	Serial number of the helix.  This starts at 1 and increases incrementally.
        12 - 14 	     LString(3)  	    helixID    	 Helix identifier. In addition to a serial number, each helix is given an alphanumeric character helix identifier.
        16 - 18 	     Residue name	    initResName	 Name of the initial residue.
        20      	     Character   	    initChainID	 Chain identifier for the chain containing this helix.
        22 - 25 	     Integer     	    initSeqNum 	 Sequence number of the initial residue.
        26      	     AChar       	    initICode  	 Insertion code of the initial residue.
        28 - 30 	     Residue name	    endResName 	 Name of the terminal residue of the helix.
        32      	     Character   	    endChainID 	 Chain identifier for the chain containing this helix.
        34 - 37 	     Integer     	    endSeqNum  	 Sequence number of the terminal residue.
        38      	     AChar       	    endICode   	 Insertion code of the terminal residue.
        39 - 40 	     Integer     	    helixClass 	 Helix class (see below).
        41 - 70 	     String      	    comment    	 Comment about this helix.
        72 - 76 	     Integer     	    length     	 Length of this helix.
        """,
    Sheet="""
        1 -  6 	   Record name   	  "SHEET "
        8 - 10 	   Integer       	  strand     	 Strand number which starts at 1 for each strand within a sheet and increases by one.
        12 - 14 	   LString(3)    	  sheetID    	 Sheet identifier.
        15 - 16 	   Integer       	  numStrands 	 Number of strands in sheet.
        18 - 20 	   Residue name  	  initResName	 Residue name of initial residue.
        22      	   Character     	  initChainID	 Chain identifier of initial residue in strand.
        23 - 26 	   Integer       	  initSeqNum 	 Sequence number of initial residue in strand.
        27      	   AChar         	  initICode  	 Insertion code of initial residue in strand.
        29 - 31 	   Residue name  	  endResName 	 Residue name of terminal residue.
        33      	   Character     	  endChainID 	 Chain identifier of terminal residue.
        34 - 37 	   Integer       	  endSeqNum  	 Sequence number of terminal residue.
        38      	   AChar         	  endICode   	 Insertion code of terminal residue.
        39 - 40 	   Integer       	  sense      	 Sense of strand with respect to previous strand in the sheet. 0 if first strand, 1 if parallel, -1 if anti-parallel.
        42 - 45 	   Atom          	  curAtom    	 Registration. Atom name in current strand.
        46 - 48 	   Residue name  	  curResName 	 Registration. Residue name in current strand.
        50      	   Character     	  curChainId 	 Registration. Chain identifier in current strand.
        51 - 54 	   Integer       	  curResSeq  	 Registration. Residue sequence number in current strand.
        55      	   AChar         	  curICode   	 Registration. Insertion code in current strand.
        57 - 60 	   Atom          	  prevAtom   	 Registration. Atom name in previous strand.
        61 - 63 	   Residue name  	  prevResName	 Registration. Residue name in previous strand.
        65      	   Character     	  prevChainId	 Registration. Chain identifier in previous strand.
        66 - 69 	   Integer       	  prevResSeq 	 Registration. Residue sequence number in previous strand.
        70      	   AChar         	  prevICode  	 Registration. Insertion code in previous strand.
        """,
)
