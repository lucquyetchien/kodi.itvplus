#!/usr/bin/python
# coding=utf-8
import os , xbmc , xbmcaddon , xbmcplugin , xbmcgui , sys , urllib , urllib2 , re , random , base64 , json , time , datetime
if 64 - 64: i11iIiiIii
OO0o = 'plugin.video.kodi4vn.megafun'
Oo0Ooo = xbmcaddon . Addon ( OO0o )
O0O0OO0O0O0 = int ( sys . argv [ 1 ] )
if 5 - 5: iiI / ii1I
def ooO0OO000o ( ) :
 iI1 = i1I11i ( )
 for OoOoOO00 in iI1 [ 'object' ] :
  if ( OoOoOO00 [ 'owner' ] [ 'name' ] . encode ( 'utf-8' ) . strip ( ) not in [ 'True Sport' , 'QTV1' , 'QTV3' ] ) :
   I11i = 'http://c2.cdn.truelife.vn/offica/community/avatar?c=%s&m=1' % OoOoOO00 [ 'ownerId' ]
   O0O = '[B][COLOR green]%s[/COLOR][/B] - ' % OoOoOO00 [ 'owner' ] [ 'name' ] . encode ( 'utf-8' ) . strip ( )
   Oo = ''
   I1ii11iIi11i = '[B]Đang chiếu[/B]'
   if OoOoOO00 [ 'categoryName' ] . encode ( 'utf-8' ) != 'Khác' : Oo = '[B]%s[/B]: ' % OoOoOO00 [ 'categoryName' ] . encode ( 'utf-8' ) . strip ( )
   if OoOoOO00 [ 'title' ] . encode ( 'utf-8' ) != 'Không rõ' : I1ii11iIi11i = '[COLOR yellow]%s[/COLOR]' % OoOoOO00 [ 'title' ] . encode ( 'utf-8' ) . strip ( )
   I1IiI ( O0O + Oo + I1ii11iIi11i , OoOoOO00 [ 'ownerId' ] , I11i , 'channelprogram' )
def Ooo0OO0oOO ( channelid ) :
 oooO0oo0oOOOO = O0oO ( channelid )
 o0oO0 = oo00 ( )
 o00 = datetime . datetime . fromtimestamp ( o0oO0 ) . strftime ( '%Y-%m-%d %H:%M:%S' )
 Oo0oO0ooo ( '[B]%s: Đang chiếu...[/B]' % ( o00 ) , channelid , 'playvideo' , '' , '' )
 if 56 - 56: ooO00oOoo - O0OOo
 for II1Iiii1111i in reversed ( oooO0oo0oOOOO [ 'object' ] ) :
  i1IIi11111i = II1Iiii1111i [ 'dateTimeBegin' ] . split ( '.' ) [ 0 ]
  o000o0o00o0Oo = time . mktime ( time . strptime ( i1IIi11111i , '%Y-%m-%d %H:%M:%S' ) )
  if o000o0o00o0Oo < o0oO0 :
   oo = '[B]%s[/B]: ' % II1Iiii1111i [ 'dateTimeBegin' ] . encode ( 'utf-8' ) . strip ( ) . split ( '.' ) [ 0 ]
   Oo = ''
   IiII1I1i1i1ii = '[B]Đang chiếu[/B]'
   if II1Iiii1111i [ 'categoryName' ] . encode ( 'utf-8' ) != 'Khác' : Oo = '[COLOR yellow]%s[/COLOR]: ' % II1Iiii1111i [ 'categoryName' ] . encode ( 'utf-8' ) . strip ( )
   if II1Iiii1111i [ 'title' ] . encode ( 'utf-8' ) != 'Không rõ' : IiII1I1i1i1ii = '[B]%s[/B]' % II1Iiii1111i [ 'title' ] . encode ( 'utf-8' ) . strip ( )
   Oo0oO0ooo ( oo + Oo + IiII1I1i1i1ii , channelid , 'playvideo' , II1Iiii1111i [ 'dateTimeBegin' ] , str ( II1Iiii1111i [ 'duration' ] ) )
   if 44 - 44: OOo0o0 / OOoOoo00oo - iI1OoOooOOOO + i1iiIII111ii + i1iIIi1
def ii11iIi1I ( channelid , starttime , duration ) :
 iI111I11I1I1 = OOooO0OOoo ( channelid )
 iIii1 = iI111I11I1I1 [ 'object' ] [ 0 ] [ 'streamingUrl' ] . split ( '&' ) [ 0 ] . replace ( 'c=' , '' )
 iIii1 = iIii1 . replace ( 'vstv018' , 'vstv093' )
 if starttime != '' or duration != '' :
  o000o0o00o0Oo = time . mktime ( time . strptime ( starttime . split ( '.' ) [ 0 ] , '%Y-%m-%d %H:%M:%S' ) )
  if 71 - 71: IiI1I1
  oo = datetime . datetime . fromtimestamp ( o000o0o00o0Oo ) . strftime ( '%H%M' )
  OoO000 = datetime . datetime . fromtimestamp ( o000o0o00o0Oo ) . strftime ( '%y%m%d' )
  IIiiIiI1 = iiIiIIi ( iIii1 , OoO000 , oo )
 else :
  IIiiIiI1 = ooOoo0O ( iIii1 )
 OooO0 = xbmc . Player ( )
 OooO0 . play ( IIiiIiI1 )
 if 35 - 35: Ooooo0Oo00oO0 % Ooo . oo0Oo00Oo0 % oOOO00o
def oo00 ( ) :
 O0O00o0OOO0 = urllib2 . Request ( "http://truelife.vn/offica/community/action?_f=7&jsoncallback=Ext.data.JsonP.callback2" )
 Ii1iIIIi1ii = urllib2 . urlopen ( O0O00o0OOO0 )
 o0oo0o0O00OO = Ii1iIIIi1ii . read ( )
 Ii1iIIIi1ii . close ( )
 o0oo0o0O00OO = '' . join ( o0oo0o0O00OO . splitlines ( ) )
 o0oo0o0O00OO = o0oo0o0O00OO . replace ( "Ext.data.JsonP.callback2(" , "" )
 o0oo0o0O00OO = o0oo0o0O00OO . replace ( ")" , "" )
 o0oO = json . loads ( o0oo0o0O00OO )
 I1i1iii = o0oO [ 'header' ] [ 'sysdate' ] . replace ( ' ICT' , '' ) . encode ( 'utf-8' )
 i1iiI11I = time . mktime ( time . strptime ( I1i1iii , '%a %b %d %H:%M:%S %Y' ) )
 return i1iiI11I
 if 29 - 29: iiIi
def OOooO0OOoo ( channelid ) :
 O0O00o0OOO0 = urllib2 . Request ( "http://truelife.vn/offica/truelifetv/lib/action?_f=119&tvChannelId=%s&ownerId=1532&jsoncallback=Ext.data.JsonP.tvprofile" % channelid )
 O0O00o0OOO0 . add_header ( 'Host' , 'truelife.vn' )
 O0O00o0OOO0 . add_header ( 'Accept-Encoding' , 'gzip, deflate' )
 O0O00o0OOO0 . add_header ( 'Referer' , 'http://megafun.vn/tv/' )
 O0O00o0OOO0 . add_header ( 'Cookie' , 'ojid="UryGHmUCni0KfiuwTUS2zetq|QZcIptDEA4Rd4pyY3GUauEPigwgClr3zopggcFFuzcqH90Y3MdEz9BOdNMAeYFL3kHVnrovgSQcEM7wp05s6Ovedh74CQjH6krC9J4Yqiq|DuqGSPeU2gaX9VKCJvDE1HIHREnmHbaJbKVVNyAsEMqwvy162y0dPlCA5mNkifc6O4j0GJgCCLiKGAzj69vma5O2h7XkqLpvQI2vNeA="' )
 O0O00o0OOO0 . add_header ( 'Connection' , 'keep-alive' )
 Ii1iIIIi1ii = urllib2 . urlopen ( O0O00o0OOO0 )
 o0oo0o0O00OO = Ii1iIIIi1ii . read ( )
 Ii1iIIIi1ii . close ( )
 o0oo0o0O00OO = '' . join ( o0oo0o0O00OO . splitlines ( ) )
 o0oo0o0O00OO = o0oo0o0O00OO . replace ( "Ext.data.JsonP.tvprofile(" , "" )
 o0oo0o0O00OO = o0oo0o0O00OO . replace ( ")" , "" )
 o0oO = json . loads ( o0oo0o0O00OO )
 return o0oO
 if 98 - 98: I1IIIii % OOoOoo00oo * OOo0o0 % iiI
def O0oO ( channelid ) :
 O0O00o0OOO0 = urllib2 . Request ( "http://truelife.vn/offica/tvchannel/tvshow/action?_f=14&communityId=%s&jsoncallback=Ext.data.JsonP.tvshow1205151412" % channelid )
 O0O00o0OOO0 . add_header ( 'Host' , 'truelife.vn' )
 O0O00o0OOO0 . add_header ( 'Accept-Encoding' , 'gzip, deflate' )
 O0O00o0OOO0 . add_header ( 'Referer' , 'http://megafun.vn/tv/' )
 O0O00o0OOO0 . add_header ( 'Cookie' , 'ojid="UryGHmUCni0KfiuwTUS2zetq|QZcIptDEA4Rd4pyY3GUauEPigwgClr3zopggcFFuzcqH90Y3MdEz9BOdNMAeYFL3kHVnrovgSQcEM7wp05s6Ovedh74CQjH6krC9J4Yqiq|DuqGSPeU2gaX9VKCJisQ26UQYnnCkwbck2oeVngMSDmkUKxjgYQoWsu|6GGsifc6O4j0GJgCCLiKGAzj69vma5O2h7XkqLpvQI2vNeA="' )
 O0O00o0OOO0 . add_header ( 'Connection' , 'keep-alive' )
 Ii1iIIIi1ii = urllib2 . urlopen ( O0O00o0OOO0 )
 o0oo0o0O00OO = Ii1iIIIi1ii . read ( )
 Ii1iIIIi1ii . close ( )
 o0oo0o0O00OO = '' . join ( o0oo0o0O00OO . splitlines ( ) )
 o0oo0o0O00OO = o0oo0o0O00OO . replace ( "Ext.data.JsonP.tvshow1205151412(" , "" )
 o0oo0o0O00OO = o0oo0o0O00OO . replace ( ")" , "" )
 o0oO = json . loads ( o0oo0o0O00OO )
 return o0oO
 if 63 - 63: ii1I
def i1I11i ( ) :
 O0O00o0OOO0 = urllib2 . Request ( "http://truelife.vn/offica/tvchannel/tvshow/action?_f=17&ownerId=1532&jsoncallback=Ext.data.JsonP.tvshow1205151412" )
 O0O00o0OOO0 . add_header ( 'Host' , 'truelife.vn' )
 O0O00o0OOO0 . add_header ( 'Accept-Encoding' , 'gzip, deflate' )
 O0O00o0OOO0 . add_header ( 'Referer' , 'http://megafun.vn/tv/' )
 O0O00o0OOO0 . add_header ( 'DNT' , '1' )
 O0O00o0OOO0 . add_header ( 'Connection' , 'keep-alive' )
 Ii1iIIIi1ii = urllib2 . urlopen ( O0O00o0OOO0 )
 o0oo0o0O00OO = Ii1iIIIi1ii . read ( )
 Ii1iIIIi1ii . close ( )
 o0oo0o0O00OO = '' . join ( o0oo0o0O00OO . splitlines ( ) )
 o0oo0o0O00OO = o0oo0o0O00OO . replace ( "Ext.data.JsonP.tvshow1205151412(" , "" )
 o0oo0o0O00OO = o0oo0o0O00OO . replace ( ")" , "" )
 o0oO = json . loads ( o0oo0o0O00OO )
 return o0oO
 if 57 - 57: ii1I * Ooo
def OOOO ( ) :
 O0O00o0OOO0 = urllib2 . Request ( urllib . unquote_plus ( "http://s22.ctl.vsolutions.vn/ctl/tvlive/s/?script&json" ) )
 O0O00o0OOO0 . add_header ( 'Host' , 's22.ctl.vsolutions.vn' )
 O0O00o0OOO0 . add_header ( 'Accept-Encoding' , 'gzip, deflate' )
 Ii1iIIIi1ii = urllib2 . urlopen ( O0O00o0OOO0 )
 o0oo0o0O00OO = Ii1iIIIi1ii . read ( )
 Ii1iIIIi1ii . close ( )
 o0oo0o0O00OO = '' . join ( o0oo0o0O00OO . splitlines ( ) )
 o0oo0o0O00OO = o0oo0o0O00OO . replace ( "null(" , "" )
 o0oo0o0O00OO = o0oo0o0O00OO . replace ( ")" , "" )
 o0oO = json . loads ( o0oo0o0O00OO )
 return o0oO
 if 87 - 87: i1iIIi1 / Ooooo0Oo00oO0 - Ooo0O * IiI1I1 / ooOo . iiI
def iiIiIIi ( vstv , date , st ) :
 iii11I111 = str ( int ( time . time ( ) ) )
 OOOO00ooo0Ooo = base64 . b64encode ( iii11I111 )
 OOOooOooo00O0 = ""
 for Oo0OO in range ( 1 , 7 ) :
  oOOoOo00o = random . randrange ( 0 , len ( "ABCDEFGHIJKLMNOPQRSTUVXYZ1234567890" ) )
  OOOooOooo00O0 = OOOooOooo00O0 + "ABCDEFGHIJKLMNOPQRSTUVXYZ1234567890" [ oOOoOo00o : oOOoOo00o + 1 ]
 o0OOoo0OO0OOO = "" ;
 for iI1iI1I1i1I in range ( 0 , len ( OOOO00ooo0Ooo ) ) :
  o0OOoo0OO0OOO = o0OOoo0OO0OOO + OOOO00ooo0Ooo [ iI1iI1I1i1I : iI1iI1I1i1I + 1 ]
  if ( iI1iI1I1i1I < len ( OOOooOooo00O0 ) ) :
   o0OOoo0OO0OOO = o0OOoo0OO0OOO + OOOooOooo00O0 [ iI1iI1I1i1I : iI1iI1I1i1I + 1 ]
 iIi11Ii1 = base64 . b64encode ( o0OOoo0OO0OOO )
 Ii11iII1 = ""
 for Oo0O0O0ooO0O in range ( 0 , len ( iIi11Ii1 ) - 1 ) :
  Ii11iII1 = Ii11iII1 + iIi11Ii1 [ Oo0O0O0ooO0O : Oo0O0O0ooO0O + 1 ]
  if ( Oo0O0O0ooO0O < len ( OOOooOooo00O0 ) ) :
   Ii11iII1 = Ii11iII1 + OOOooOooo00O0 [ Oo0O0O0ooO0O : Oo0O0O0ooO0O + 1 ]
 Ii11iII1 = Ii11iII1 . replace ( "=" , "" )
 IIIIii = { 'location' : '' , 'device_type' : '2' , 'mf_code' : vstv , 'device_id' : '487142' , 'date' : date , 'channel_id' : '1' , 'member_id' : '107805' , 'end_time' : '2359' , 'app_v' : '63' , 'manufacturer_id' : 'E94F6043C85AF86080CA27A439A1D766' , 'start_time' : st , 'tid' : Ii11iII1 , 'profile' : '2' }
 O0o0 = urllib . urlencode ( IIIIii )
 if 71 - 71: IiI1I1 + I1IIIii % i11iIiiIii + i1iiIII111ii - oOOO00o
 O0O00o0OOO0 = urllib2 . Request ( urllib . unquote_plus ( OoO000 ( "u" , "3enp5a-kpOTp6aPi7unr49rpo-vjpOuqpNjd1uPj2uGk4uTX3uHapOnr5Nmi6ufh" ) ) )
 O0O00o0OOO0 . add_header ( 'Content-Type' , 'application/x-www-form-urlencoded; charset=utf-8' )
 O0O00o0OOO0 . add_header ( 'User-Agent' , 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; Nexus 5 Build/KOT49H)' )
 O0O00o0OOO0 . add_header ( 'Host' , 'ott.mytvnet.vn' )
 O0O00o0OOO0 . add_header ( 'Connection' , 'Keep-Alive' )
 O0O00o0OOO0 . add_header ( 'Accept-Encoding' , 'gzip' )
 Ii1iIIIi1ii = urllib2 . urlopen ( O0O00o0OOO0 , O0o0 )
 o0oo0o0O00OO = Ii1iIIIi1ii . read ( )
 Ii1iIIIi1ii . close ( )
 o0oo0o0O00OO = '' . join ( o0oo0o0O00OO . splitlines ( ) )
 o0oo0o0O00OO = o0oo0o0O00OO . replace ( "null(" , "" )
 o0oo0o0O00OO = o0oo0o0O00OO . replace ( ")" , "" )
 o0oO = json . loads ( o0oo0o0O00OO )
 o0oo0o0O00OO = re . sub ( "http://.+?/" , "http://m3.mytvnet.vn/" , o0oO [ 'data' ] [ 'url' ] )
 return o0oo0o0O00OO
 if 88 - 88: OOoOoo00oo - OOo0o0 % IiI1I1
def ooOoo0O ( vstv ) :
 O0O00o0OOO0 = urllib2 . Request ( urllib . unquote_plus ( "http://truelife.vn/offica/resourcesubcription/action?_f=6666&c=%s&q=high&type=tv" ) % ( vstv ) )
 O0O00o0OOO0 . add_header ( 'Host' , 'truelife.vn' )
 O0O00o0OOO0 . add_header ( 'Accept-Encoding' , 'gzip, deflate' )
 O0O00o0OOO0 . add_header ( 'Cookie' , 'ojid="dspsns19Lgzd0JHP2kJt|qI9iwnktcCR7lIlfhJM8vYlsqnyhQ7Xlmh2Mfm0jf4cm0ly8DMtoNkb4LIJysPDFP0/cuXcCXjTYxsofpWHjNJFo6hcah5xggY/g4xS7Avl24d4WcPzYgzRd79ETkW2RrzizZBjeNk7hihYpWYbyc/z2Q1jL/Q6kpw0u92OERt0BaxPHC8j|vYqOE2Pnd/h2DdkurOJPoJEi4Ia9KiV3Qs="' )
 O0O00o0OOO0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (iPad; CPU OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B554a Safari/9537.53' )
 Ii1iIIIi1ii = urllib2 . urlopen ( O0O00o0OOO0 )
 o0oo0o0O00OO = Ii1iIIIi1ii . read ( )
 Ii1iIIIi1ii . close ( )
 o0oo0o0O00OO = '' . join ( o0oo0o0O00OO . splitlines ( ) )
 o0oo0o0O00OO = o0oo0o0O00OO . replace ( "null(" , "" )
 o0oo0o0O00OO = o0oo0o0O00OO . replace ( ")" , "" )
 o0oO = json . loads ( o0oo0o0O00OO )
 iI1I111Ii111i = o0oO [ "object" ] [ 0 ] [ "token" ]
 I11IiI1I11i1i = o0oO [ "object" ] [ 0 ] [ "time" ]
 if 38 - 38: iI1OoOooOOOO
 o0oo0o0O00OO = 'http://m3.mytvnet.vn/live.m3u8?c=' + vstv + '&q=high&token=' + iI1I111Ii111i + '&time=' + I11IiI1I11i1i
 return o0oo0o0O00OO
 if 57 - 57: iiI / i1iIIi1 * iiIi / OOoOoo00oo . I1II1
def i11iIIIIIi1 ( url ) :
 o0oo0o0O00OO = ""
 if os . path . exists ( url ) == True :
  o0oo0o0O00OO = open ( url ) . read ( )
 else :
  O0O00o0OOO0 = urllib2 . Request ( url )
  O0O00o0OOO0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)' )
  Ii1iIIIi1ii = urllib2 . urlopen ( O0O00o0OOO0 )
  o0oo0o0O00OO = Ii1iIIIi1ii . read ( )
  Ii1iIIIi1ii . close ( )
 o0oo0o0O00OO = '' . join ( o0oo0o0O00OO . splitlines ( ) ) . replace ( '\'' , '"' )
 o0oo0o0O00OO = o0oo0o0O00OO . replace ( '\n' , '' )
 o0oo0o0O00OO = o0oo0o0O00OO . replace ( '\t' , '' )
 o0oo0o0O00OO = re . sub ( '  +' , ' ' , o0oo0o0O00OO )
 o0oo0o0O00OO = o0oo0o0O00OO . replace ( '> <' , '><' )
 return o0oo0o0O00OO
 if 20 - 20: Ooo0O + i1iiIII111ii - I1IIIii
def OoO000 ( k , e ) :
 IiI11iII1 = [ ]
 e = base64 . urlsafe_b64decode ( e )
 for IIII11I1I in range ( len ( e ) ) :
  OOO0o = k [ IIII11I1I % len ( k ) ]
  IiI1 = chr ( ( 256 + ord ( e [ IIII11I1I ] ) - ord ( OOO0o ) ) % 256 )
  IiI11iII1 . append ( IiI1 )
 return "" . join ( IiI11iII1 )
 if 54 - 54: I1II1 % OOoOoo00oo % Ooooo0Oo00oO0 % ii1I + ii1I * I1IIIii
def Oo0oO0ooo ( name , channelid , mode , starttime , duration ) :
 O00O0oOO00O00 = sys . argv [ 0 ] + "?name=" + urllib . quote_plus ( name ) + "&channelid=" + urllib . quote_plus ( str ( channelid ) ) + "&mode=" + str ( mode ) + "&starttime=" + urllib . quote_plus ( starttime ) + "&duration=" + str ( duration )
 i1 = True
 Oo00 = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = '' )
 Oo00 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 i1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O00O0oOO00O00 , listitem = Oo00 )
 return i1
 if 31 - 31: iiIi . OOoOoo00oo / iiI
def I1IiI ( name , channelid , channelimg , mode ) :
 O00O0oOO00O00 = sys . argv [ 0 ] + "?name=" + urllib . quote_plus ( name ) + "&channelid=" + urllib . quote_plus ( str ( channelid ) ) + "&mode=" + str ( mode )
 i1 = True
 Oo00 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = channelimg )
 Oo00 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 i1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O00O0oOO00O00 , listitem = Oo00 , isFolder = True )
 return i1
 if 89 - 89: OOoOoo00oo
def OO0oOoOO0oOO0 ( parameters ) :
 oO0OOoo0OO = { }
 if 65 - 65: Ooo . ii1I / iiI - Ooo
 if parameters :
  iii1i1iiiiIi = parameters [ 1 : ] . split ( "&" )
  for Iiii in iii1i1iiiiIi :
   OO0OoO0o00 = Iiii . split ( '=' )
   if ( len ( OO0OoO0o00 ) ) == 2 :
    oO0OOoo0OO [ OO0OoO0o00 [ 0 ] ] = OO0OoO0o00 [ 1 ]
 return oO0OOoo0OO
 if 53 - 53: iiI * OOo0o0 + IiI1I1
Ii = OO0oOoOO0oOO0 ( sys . argv [ 2 ] )
oOOo0 = Ii . get ( 'mode' )
oo00O00oO = Ii . get ( 'channelid' )
iIiIIIi = Ii . get ( 'name' )
ooo00OOOooO = Ii . get ( 'starttime' )
O00OOOoOoo0O = Ii . get ( 'duration' )
if 77 - 77: oo0Oo00Oo0 % oo0Oo00Oo0 * i1iIIi1 - i11iIiiIii
if type ( ooo00OOOooO ) == type ( str ( ) ) :
 ooo00OOOooO = urllib . unquote_plus ( ooo00OOOooO )
if type ( oo00O00oO ) == type ( str ( ) ) :
 oo00O00oO = urllib . unquote_plus ( oo00O00oO )
if type ( iIiIIIi ) == type ( str ( ) ) :
 iIiIIIi = urllib . unquote_plus ( iIiIIIi )
 if 93 - 93: ooOo / ooO00oOoo % i11iIiiIii + i1iiIII111ii * OOo0o0
I1 = str ( sys . argv [ 1 ] )
if oOOo0 == 'channelprogram' :
 Ooo0OO0oOO ( oo00O00oO )
elif oOOo0 == 'playvideo' :
 iI11Ii = xbmcgui . DialogProgress ( )
 iI11Ii . create ( 'megafun.vn' , 'Loading video. Please wait...' )
 ii11iIi1I ( oo00O00oO , ooo00OOOooO , O00OOOoOoo0O )
 iI11Ii . close ( )
 del iI11Ii
else :
 ooO0OO000o ( )
xbmcplugin . endOfDirectory ( int ( I1 ) ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
