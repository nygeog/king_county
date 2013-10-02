// UW FINAL XY
// created Sept 26 2013
// updated Oct 01 2013

use "C:\Users\tkk2109\AppData\Local\Temp\Temp1_kco_regeocode_bygooglemap.zip\kco_regeocode_bygooglemap.dta", clear 
save "P:\tkk2109\NETS\UW CABS\KingCountyNETS\TK\kco_regeocode_bygooglemap_TK.dta", replace

use "P:\tkk2109\NETS\UW CABS\KingCountyNETS\TK\kco_regeocode_bygooglemap_TK.dta", clear

gen final_x=.
replace final_x=GPrimLongitude if GPrimLongitude !=.
replace final_x=GSecLongitude if GSecLongitude !=. & GPrimLongitude ==.
replace final_x=PrimLongitude if PrimLongitude !=. & GPrimLongitude ==. & GSecLongitude ==.

gen final_y=.
replace final_y=GPrimLatitude if GPrimLatitude !=.
replace final_y=GSecLatitude if GSecLatitude !=. & GPrimLatitude ==.
replace final_y=PrimLatitude if PrimLatitude !=. & GPrimLatitude ==. & GSecLatitude ==.


gen final_xy=""
replace final_xy="GPrim" if GPrimLatitude !=.
replace final_xy="GSec" if GSecLatitude !=. & GPrimLatitude ==.
replace final_xy="Prim" if PrimLatitude !=. & GPrimLatitude ==. & GSecLatitude ==.

tab final_xy
/* 
   final_xy |      Freq.     Percent        Cum.
------------+-----------------------------------
      GPrim |    368,087       97.35       97.35
       GSec |         14        0.00       97.36
       Prim |      9,990        2.64      100.00
------------+-----------------------------------
      Total |    378,091      100.00
*/
 
save "P:\tkk2109\NETS\UW CABS\KingCountyNETS\TK\KingCounty_finalxy.dta", replace
