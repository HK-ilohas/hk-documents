import gmpy2
from Crypto.Util.number import *


n = 17686671842400393574730512034200128521336919569735972791676605056286778473230718426958508878942631584704817342304959293060507614074800553670579033399679041334863156902030934895197677543142202110781629494451453351396962137377411477899492555830982701449692561594175162623580987453151328408850116454058162370273736356068319648567105512452893736866939200297071602994288258295231751117991408160569998347640357251625243671483903597718500241970108698224998200840245865354411520826506950733058870602392209113565367230443261205476636664049066621093558272244061778795051583920491406620090704660526753969180791952189324046618283
e = 3
c = 213791751530017111508691084168363024686878057337971319880256924185393737150704342725042841488547315925971960389230453332319371876092968032513149023976287158698990251640298360876589330810813199260879441426084508864252450551111064068694725939412142626401778628362399359107132506177231354040057205570428678822068599327926328920350319336256613

m = gmpy2.iroot(c, e)[0]
print(long_to_bytes(m).decode())
