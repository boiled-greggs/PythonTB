#!/usr/bin/env python

# Copyright under GNU General Public License 2010, 2012, 2016
# by Sinisa Coh and David Vanderbilt (see gpl-pythtb.txt)

from __future__ import print_function
from pythtb import * # import TB model class
import numpy as np
import pylab as plt

# define lattice vectors
lat=[[20.466999054, 0.0, 0.0], [-10.233499527, 17.72494112, 0.0], [0.0, 0.0, 6.797990]]
# define coordinates of orbitals
orb=[[0.044059607, 0.085567664, 0.38950849], \
    [0.086075183, 0.043547802, 0.926547134], \
    [0.00290946, 0.002518158, 0.38845676], \
    [0.003027153, 0.002399342, 0.927614239], \
    [0.168303936, 0.084557122, 0.386358827], \
    [0.210963907, 0.043203574, 0.921756162], \
    [0.127392444, 0.001954699, 0.38548012], \
    [0.127984625, 0.001953727, 0.924155116], \
    [0.29361911, 0.084060673, 0.384948708], \
    [0.335879172, 0.043186398, 0.921505267], \
    [0.252338124, 0.001474884, 0.38407292], \
    [0.25252796, 0.00157546, 0.921273333], \
    [0.419293737, 0.084209531, 0.386193667], \
    [0.460852358, 0.043263676, 0.926464937], \
    [0.37774241, 0.001720834, 0.385402889], \
    [0.377466908, 0.001755698, 0.923982022], \
    [0.544716429, 0.085192569, 0.389593368], \
    [0.585956227, 0.04372976, 0.929657839], \
    [0.502908274, 0.002151694, 0.388454607], \
    [0.502659658, 0.002032058, 0.927614174], \
    [0.669900565, 0.085686876, 0.39256445], \
    [0.711198898, 0.044300335, 0.931703591], \
    [0.628313178, 0.002596197, 0.391839626], \
    [0.627705313, 0.002595647, 0.930596775], \
    [0.794591559, 0.085794211, 0.394134891], \
    [0.836388535, 0.044361523, 0.931737461], \
    [0.753235355, 0.002975767, 0.39466802], \
    [0.753132336, 0.003074009, 0.931987857], \
    [0.919377624, 0.085974202, 0.392562459], \
    [0.96132979, 0.043997549, 0.929654836], \
    [0.877993348, 0.002795282, 0.392011762], \
    [0.878290429, 0.002830089, 0.930674194], \
    [0.043716199, 0.210455047, 0.394218813], \
    [0.085067099, 0.167792295, 0.929732475], \
    [0.002466151, 0.127477267, 0.391841166], \
    [0.002464608, 0.126881668, 0.93059475], \
    [0.167650224, 0.209683761, 0.393794443], \
    [0.21019037, 0.167136778, 0.922282302], \
    [0.126711478, 0.126569857, 0.388262909], \
    [0.127077214, 0.126199635, 0.927816982], \
    [0.292211129, 0.207371643, 0.396715342], \
    [0.33608204, 0.16837317, 0.906733471], \
    [0.251303809, 0.125449018, 0.38679086], \
    [0.252442987, 0.126400809, 0.917690072], \
    [0.418006304, 0.206909137, 0.396093064], \
    [0.460724836, 0.16689075, 0.92235814], \
    [0.377076511, 0.125019281, 0.386396667], \
    [0.377715973, 0.126203451, 0.917536048], \
    [0.5448435, 0.208944373, 0.393736799], \
    [0.586277776, 0.167705522, 0.929909977], \
    [0.502970341, 0.126158324, 0.388467152], \
    [0.502599908, 0.125977205, 0.927622525], \
    [0.669690971, 0.210086559, 0.394477603], \
    [0.71126341, 0.168672173, 0.931739498], \
    [0.628104916, 0.127071347, 0.392017075], \
    [0.627829407, 0.126770455, 0.930678701], \
    [0.79450279, 0.210468839, 0.394137365], \
    [0.836116767, 0.168944677, 0.932183152], \
    [0.752913315, 0.127247978, 0.393791115], \
    [0.752839747, 0.127293361, 0.931986326], \
    [0.919269903, 0.210560031, 0.394133706], \
    [0.960760235, 0.168670592, 0.931703204], \
    [0.877815715, 0.127427388, 0.393790024], \
    [0.87776795, 0.127319009, 0.931987686], \
    [0.043698951, 0.33537203, 0.394463693], \
    [0.084571154, 0.293109409, 0.931138893], \
    [0.002086915, 0.252019766, 0.394666151], \
    [0.001985185, 0.251828564, 0.931985027], \
    [0.168891019, 0.335576349, 0.409341848], \
    [0.207883159, 0.29170013, 0.919416339], \
    [0.126916265, 0.251935614, 0.398336056], \
    [0.125960759, 0.250793982, 0.929312083], \
    [0.289962915, 0.331079343, 0.452643143], \
    [0.331593836, 0.289451935, 0.863585536], \
    [0.250405184, 0.250459181, 0.406298294], \
    [0.250965227, 0.249891615, 0.909857434], \
    [0.412472583, 0.321202837, 0.493861097], \
    [0.46313561, 0.289842064, 0.861746891], \
    [0.374678225, 0.246088351, 0.409103264], \
    [0.377373008, 0.250690834, 0.872695313], \
    [0.542436918, 0.329479701, 0.454501523], \
    [0.587563157, 0.291692785, 0.920065021], \
    [0.502447491, 0.249560097, 0.405484475], \
    [0.503123247, 0.249902281, 0.910695935], \
    [0.669490461, 0.335071507, 0.409364562], \
    [0.71195317, 0.293231117, 0.931154557], \
    [0.627853993, 0.251265034, 0.398506346], \
    [0.628495691, 0.250732264, 0.929725219], \
    [0.794606815, 0.335020463, 0.394229922], \
    [0.836390275, 0.293859677, 0.931709938], \
    [0.753040817, 0.251825906, 0.394676112], \
    [0.75323064, 0.251926328, 0.931994212], \
    [0.919091617, 0.335163573, 0.392562981], \
    [0.960697436, 0.29379698, 0.931733171], \
    [0.877638109, 0.252148662, 0.393790362], \
    [0.877742442, 0.252219492, 0.931987313], \
    [0.043776599, 0.460343551, 0.389582203], \
    [0.084718596, 0.418784345, 0.929892103], \
    [0.002268901, 0.376957825, 0.392006698], \
    [0.002230256, 0.377232206, 0.930668357], \
    [0.16740554, 0.460217007, 0.393710225], \
    [0.207419712, 0.417497731, 0.9200345], \
    [0.126719166, 0.377210278, 0.398483734], \
    [0.125530067, 0.376566929, 0.929702163], \
    [0.290354479, 0.462632335, 0.454471828], \
    [0.321732823, 0.411972241, 0.822403536], \
    [0.251203787, 0.376864522, 0.443500226], \
    [0.246607074, 0.374172721, 0.907078757], \
    [0.364705983, 0.353205719, 0.555275784], \
    [0.353745545, 0.364210484, 0.76101847], \
    [0.593096019, 0.411535106, 0.822426208], \
    [0.49123482, 0.353297722, 0.551547734], \
    [0.514331322, 0.364868402, 0.764752477], \
    [0.673983407, 0.460641286, 0.452659797], \
    [0.7133657, 0.417958009, 0.919441113], \
    [0.628202952, 0.376099313, 0.443521581], \
    [0.630891001, 0.374205573, 0.907108262], \
    [0.795377649, 0.459722932, 0.393806985], \
    [0.837271027, 0.419046985, 0.929744079], \
    [0.753127782, 0.376737496, 0.398351487], \
    [0.754271286, 0.376938972, 0.929329487], \
    [0.91949603, 0.46025347, 0.389511119], \
    [0.96106392, 0.419103964, 0.929654889], \
    [0.877587606, 0.37675101, 0.391846909], \
    [0.878180559, 0.377355158, 0.930602873], \
    [0.044240976, 0.585448209, 0.386421982], \
    [0.085699529, 0.544206632, 0.926454857], \
    [0.002543429, 0.50215136, 0.388453774], \
    [0.002660164, 0.502398622, 0.927611693], \
    [0.168218348, 0.585770483, 0.386178721], \
    [0.209450229, 0.544333621, 0.922331878], \
    [0.126490996, 0.502091258, 0.388448231], \
    [0.126665579, 0.502460009, 0.927603949], \
    [0.292206198, 0.587057455, 0.396067455], \
    [0.329993483, 0.541930464, 0.861719139], \
    [0.250417873, 0.502614796, 0.405453179], \
    [0.250065698, 0.501936794, 0.910663409], \
    [0.412038546, 0.592599669, 0.493843902], \
    [0.365367567, 0.513838463, 0.551537075], \
    [0.353834615, 0.490738947, 0.764738329], \
    [0.683864169, 0.593028488, 0.493863345], \
    [0.715610269, 0.543915124, 0.86359497], \
    [0.651856084, 0.513260208, 0.555278846], \
    [0.640857165, 0.491306583, 0.761026978], \
    [0.797692872, 0.586596807, 0.396721455], \
    [0.837923712, 0.544826966, 0.922292974], \
    [0.754603602, 0.501703034, 0.406310665], \
    [0.755171363, 0.502848876, 0.90987489], \
    [0.920507117, 0.585505606, 0.386365401], \
    [0.961512125, 0.544298351, 0.926549663], \
    [0.878494203, 0.501899953, 0.388270347], \
    [0.878862199, 0.502649186, 0.927825295], \
    [0.044811756, 0.710690075, 0.38434858], \
    [0.086194917, 0.669389383, 0.923398798], \
    [0.003107673, 0.627196755, 0.385482593], \
    [0.003106756, 0.627802846, 0.924156178], \
    [0.169182667, 0.710755023, 0.384310567], \
    [0.210594466, 0.669181195, 0.921494918], \
    [0.127281963, 0.627321369, 0.385396438], \
    [0.127578019, 0.62759455, 0.923974547], \
    [0.293741479, 0.711444182, 0.384936741], \
    [0.335577734, 0.668981017, 0.906714187], \
    [0.251243346, 0.627987997, 0.386379245], \
    [0.251772046, 0.627345005, 0.917515876], \
    [0.418466749, 0.712856791, 0.396697407], \
    [0.461146213, 0.673466156, 0.863573817], \
    [0.374713012, 0.630388094, 0.409080601], \
    [0.376608737, 0.627692124, 0.872676556], \
    [0.544420199, 0.715102845, 0.452642504], \
    [0.593529522, 0.683331459, 0.822409844], \
    [0.491804973, 0.640364933, 0.555270734], \
    [0.513758098, 0.651316163, 0.761019389], \
    [0.675584871, 0.714715233, 0.454486662], \
    [0.715224475, 0.675068069, 0.861739861], \
    [0.65176984, 0.639698029, 0.551543984], \
    [0.640197739, 0.6512322, 0.764744253], \
    [0.798158388, 0.712859002, 0.39609198], \
    [0.836690611, 0.66948438, 0.906737321], \
    [0.758975844, 0.630348754, 0.409104338], \
    [0.754374044, 0.628454733, 0.872696589], \
    [0.921003649, 0.71132126, 0.384952473], \
    [0.961858899, 0.669534256, 0.921759292], \
    [0.879614372, 0.627615137, 0.386796919], \
    [0.878661741, 0.627817489, 0.917695774], \
    [0.044872702, 0.835880158, 0.384316222], \
    [0.086303269, 0.794081778, 0.921779982], \
    [0.003586083, 0.752624279, 0.3840755], \
    [0.003485324, 0.752725632, 0.921276486], \
    [0.16945549, 0.835607882, 0.383838303], \
    [0.210977619, 0.79399243, 0.921777825], \
    [0.12780446, 0.752330344, 0.384046807], \
    [0.127756986, 0.752402874, 0.922126016], \
    [0.294369674, 0.835882029, 0.384342373], \
    [0.335527484, 0.794095742, 0.921745257], \
    [0.252436201, 0.752722356, 0.384066001], \
    [0.252334011, 0.752530334, 0.921265549], \
    [0.419556855, 0.836761886, 0.386350304], \
    [0.46023062, 0.794867781, 0.922274536], \
    [0.377448676, 0.753762895, 0.386777898], \
    [0.377243853, 0.752617173, 0.917676681], \
    [0.545336488, 0.837413232, 0.393786094], \
    [0.587101736, 0.797177176, 0.91942351], \
    [0.503358819, 0.75466008, 0.406285364], \
    [0.502210661, 0.754093271, 0.909853001], \
    [0.669992799, 0.836176532, 0.409347126], \
    [0.713368361, 0.797645189, 0.920048709], \
    [0.628965267, 0.753863558, 0.443506544], \
    [0.630852928, 0.758455087, 0.907090974], \
    [0.796117133, 0.837659643, 0.39372785], \
    [0.838170585, 0.795608462, 0.922353996], \
    [0.75550559, 0.75464996, 0.405476158], \
    [0.755161821, 0.754997407, 0.910684389], \
    [0.920855382, 0.836844353, 0.386194111], \
    [0.961875362, 0.794466065, 0.92151113], \
    [0.880046392, 0.753818358, 0.386398212], \
    [0.878859712, 0.753287393, 0.917538431], \
    [0.044508225, 0.960820084, 0.386424252], \
    [0.086482541, 0.918866622, 0.923402819], \
    [0.00334116, 0.877781428, 0.38540438], \
    [0.003305872, 0.877484162, 0.923986361], \
    [0.169180774, 0.960250609, 0.384346982], \
    [0.211068193, 0.918758434, 0.921780227], \
    [0.127829229, 0.877259289, 0.384047512], \
    [0.127935858, 0.877305054, 0.922127115], \
    [0.294306911, 0.96018768, 0.384314805], \
    [0.335672361, 0.918579813, 0.923398834], \
    [0.252730609, 0.877233466, 0.384046142], \
    [0.252657377, 0.877126464, 0.922126932], \
    [0.419613974, 0.960555199, 0.386421829], \
    [0.460761422, 0.918985649, 0.926543232], \
    [0.377865003, 0.877672115, 0.385474989], \
    [0.377259267, 0.877077514, 0.924148006], \
    [0.544808214, 0.961001886, 0.389503175], \
    [0.586012703, 0.919994822, 0.929734701], \
    [0.503159926, 0.878352585, 0.388254811], \
    [0.502408557, 0.877984071, 0.927813686], \
    [0.670043014, 0.961348632, 0.394217983], \
    [0.711829825, 0.92049134, 0.93114493], \
    [0.628324984, 0.878149769, 0.398332611], \
    [0.628122483, 0.879101172, 0.929318142], \
    [0.794976259, 0.961364718, 0.394468542], \
    [0.837353789, 0.920344008, 0.929903356], \
    [0.753797196, 0.878347295, 0.39849417], \
    [0.754327711, 0.879534608, 0.929713081], \
    [0.919871484, 0.961287375, 0.38959114], \
    [0.961797627, 0.919362122, 0.926465939], \
    [0.878904502, 0.878572792, 0.388464669], \
    [0.879082623, 0.878395842, 0.927619727]]

# make two dimensional tight-binding graphene model
my_model = tb_model(3,3,lat,orb)

# set model parameters
delta=0.0
t=-1.0

# set on-site energies
my_model.set_onsite([delta, delta, delta, delta, delta, delta, delta, delta, \
        delta, delta, delta, delta, delta, delta, delta, delta, delta, delta, \
        delta, delta, delta, delta, delta, delta, delta, delta, delta, \
        delta, delta, delta, delta, delta, delta, delta, delta, delta, delta, \
        delta, delta, delta, delta, delta, delta, delta, delta, delta, \
        delta, delta, delta, delta, delta, delta, delta, delta, delta, delta, \
        delta, delta, delta, delta, delta, delta, delta, delta, delta, \
        delta, delta, delta, delta, delta, delta, delta, delta, delta, delta, \
        delta, delta, delta, delta, delta, delta, delta, delta, delta, \
        delta, delta, delta, delta, delta, delta, delta, delta, delta, delta, \
        delta, delta, delta, delta, delta, delta, delta, delta, delta, \
        delta, delta, delta, delta, delta, delta, delta, delta, delta, delta, \
        delta, delta, delta, delta, delta, delta, delta, delta, delta, \
        delta, delta, delta, delta, delta, delta, delta, delta, delta, delta, \
        delta, delta, delta, delta, delta, delta, delta, delta, delta, \
        delta, delta, delta, delta, delta, delta, delta, delta, delta, delta, \
        delta, delta, delta, delta, delta, delta, delta, delta, delta, \
        delta, delta, delta, delta, delta, delta, delta, delta, delta, delta, \
        delta, delta, delta, delta, delta, delta, delta, delta, delta, \
        delta, delta, delta, delta, delta, delta, delta, delta, delta, delta, \
        delta, delta, delta, delta, delta, delta, delta, delta, delta, \
        delta, delta, delta, delta, delta, delta, delta, delta, delta, delta, \
        delta, delta, delta, delta, delta, delta, delta, delta, delta, \
        delta, delta, delta, delta, delta, delta, delta, delta, delta, delta, \
        delta, delta, delta, delta, delta, delta, delta, delta, delta, \
        delta, delta, delta, delta, delta, delta, delta, delta, delta, delta,\
        delta, delta])
# set hoppings (one for each connected pair of orbitals)
# (amplitude, i, j, [lattice vector to cell containing j])
for x in range(0,248):
    if orb[x][0] > .960000 and orb[x][2] < 0.5000:
        placeholder
    if orb[x][0] > .960000 and orb[x][2] > 0.5000:
        placeholder
    else if orb[x][0] < 0.004000 and orb[x][2] < 0.5000:
        placeholder
    else if orb[x][0] < 0.004000 and orb[x][2] > 0.5000:
        placeholder
    else if orb[x][1] < 0.003000 and orb[x][2] < 0.5000: 
        placeholder
    else if orb[x][1] < 0.003000 and orb[x][2] > 0.5000:
        placeholder
    else if orb[x][1] > 0.960000 and orb[x][2] < 0.5000:
        placeholder
    else if orb[x][1] > 0.960000 and orb[x][2] > 0.5000:
        placeholder
    
    for y in range(x+1, 248): 
        dist = np.sqrt( (orb[x][0] - orb[y][0])**2 + (orb[x][1] - orb[y][1])**2 )
        if  dist < 0.10000000:
            my_model.set_hop(t, x, y, [0, 0, 0])
"""
my_model.set_hop(t, 1, 0, [ 1, 0, 0])
my_model.set_hop(t, 1, 0, [ 0, 1, 0])
my_model.set_hop(t, 0, 1, [ 1, 0, 0])
my_model.set_hop(t, 0, 1, [ 0, 1, 0])
"""
# print tight-binding model
my_model.display()
    
# generate list of k-points following a segmented path in the BZ
# list of nodes (high-symmetry points) that will be connected
# DON'T KNOW HOW TO DO THIS 
path=[[0., 0., 0.5], [2./3., 1./3., 0.5], [0.5, 0.5, 0.5], [0., 0., 0.5]]
label=(r'$\Gamma $',r'$K$', r'$M$', r'$\Gamma $')
# total number of interpolated k-points along the path
nk=800

# call function k_path to construct the actual path
(k_vec,k_dist,k_node)=my_model.k_path(path,nk)
# inputs:
#   path, nk: see above
#   my_model: the pythtb model
# outputs:
#   k_vec: list of interpolated k-points
#   k_dist: horizontal axis position of each k-point in the list
#   k_node: horizontal axis position of each original node

print('---------------------------------------')
print('starting calculation')
print('---------------------------------------')
print('Calculating bands...')

# obtain eigenvalues to be plotted
evals=my_model.solve_all(k_vec)

# figure for bandstructure

fig, ax = plt.subplots()
# specify horizontal axis details
# set range of horizontal axis
ax.set_xlim([0,k_node[-1]])
# put tickmarks and labels at node positions
ax.set_xticks(k_node)
ax.set_xticklabels(label)
# add vertical lines at node positions
for n in range(len(k_node)):
  ax.axvline(x=k_node[n],linewidth=0.5, color='k')
# put title
ax.set_title("holey bilayer band structure")
ax.set_xlabel("Path in k-space")
ax.set_ylabel("Band energy")

# plot first and second band
ax.plot(k_dist,evals[0])
ax.plot(k_dist,evals[1])

# make an PDF figure of a plot
fig.tight_layout()
fig.savefig("holeybilayer3.pdf")

print('Done.\n')