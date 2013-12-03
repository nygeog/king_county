//Y:\Dropbox\GIS\Projects\king_county\data\processing\tables\utm_xy_round.dta

use Y:\Dropbox\GIS\Projects\king_county\data\processing\tables\utm_xy_round.dta
gen utm_x = POINT_X
gen utm_y = POINT_Y
gen utm_x_round = x_round
gen utm_y_round = y_round
gen unique_xy_round = string( utm_x_round)+ "^" + string(utm_y_round)
drop  POINT_X POINT_Y x_round y_round
save "Y:\Dropbox\GIS\Projects\king_county\data\processing\tables\utm_xy_round.dta", replace