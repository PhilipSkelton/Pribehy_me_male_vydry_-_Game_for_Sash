#       ╔════════════════════════╗
#       ║  𝒫říběhy mé malé vydry ║
#       ╚════════════════════════╝


#       settings


# Field style map

level_map1 = [
' X                                                      ',
'                                                        ',
' X                                                      ',
' YY    YYY            YY                                ',
' XX       P                               XXXXXX        ',
' XXYYYYYYYYYYYYYZ        XX              X              ',
' XXXX       XX                          X               ',
' XX    Y  YYXX    YY  XXXXXXXXXXXXXXXXXX        XXXXXXXX',
'       X  XXXX    XX  XXX                               ',
'    YYYX  XXXXYY  XX  XXXX                              ',
'YYYYXXXXSSXXXXXXSSXXSSXXXX                              ']





# Bratislava style map

level_map2 = [
'                                           ',
'                                           ',
'                                           ',
'                                           ',
'                                           ',
'                                           ',
'                                           ',
'          P                                ',
'       X  XXXX    XX  XXX    X   X   X   X ',
'    YYYX  XXXXYY  XX  XXXX                 ',
'YYYYXXXXSSXXXXXXSSXXSSXXXX                 ']





# Welsh Cave map

level_map3 = [
'                                           ',
'                                           ',
'                                           ',
' YY    YYY            YY                   ',
' XX P                                     X',
' XXYYYYYYYYYYYYY         XX              X ',
' XXXX       XX                          X  ',
' XX    Y  YYXX    YY  XXXXXXXXXXXXXXXXXX   ',
'       X  XXXX    XX  XXX                  ',
'    YYYX  XXXXYY  XX  XXXX                 ',
'YYYYXXXXSSXXXXXXSSXXSSXXXX                 ']





# Matrix style map

hidden_level_map = [
'                                           ',
'                                           ',
'                                           ',
'                                           ',
'                                           ',
'                                           ', 
'                                           ',
'                                           ',
'                                           ',
'     P                                     ',
'YYYYXXXXSSXXXXXXSSXXSSXXXXSYXSYXSYXSYXSYXSY']

tile_size = 64
screen_width = 1200
screen_height = len(level_map1) * tile_size