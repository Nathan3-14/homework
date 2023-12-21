_IIIIIIIIlIlIIllII ='#######'
_IIlllIlllIlllIllI ='##########'
_IIllllIIllIllIllI ='left'
_IIIlIIIlllIlIIlll ='from'
_IlllllIIIIlIIlIIl ='right'
_IlIlIIllIllIIlIII ='map'
import sys ,time ,keyboard ,os 
def IIIlIlIIIIIllIIll (IIIIIllllIlIlIllI ):
	IIlIIllIIIIIIlIII ='errors.log'
	if not os .path .exists (IIlIIllIIIIIIlIII ):IlllIIIllIIIIIlIl =open (IIlIIllIIIIIIlIII ,'w');IlllIIIllIIIIIlIl .close ()
	with open (IIlIIllIIIIIIlIII ,'a')as IlIlIIlIlllllIlll :IlIlIIlIlllllIlll .write (f"{IIIIIllllIlIlIllI}\n")
def IIllIIIlIlllIlIll ():
	global map ;global IlIllllIIIllIIlII ;IIlIIllIIlllIIllI (len (IlIllllIIIllIIlII [_IlIlIIllIllIIlIII ]))
	try :
		IllIIlIllllllllll =''
		for (IIIllIIlIIIllllII ,IlIIIIlIIIIIllIlI )in enumerate (IlIllllIIIllIIlII [_IlIlIIllIllIIlIII ]):
			IIIlIIlIIlIIIlIll =''
			for (IIllIlllIIlIIIIIl ,IlllllllIIIIIlIll )in enumerate (IlIIIIlIIIIIllIlI ):
				if IIllIlllIIlIIIIIl ==IllllIIlIIlllIlIl [0 ]and IIIllIIlIIIllllII ==IllllIIlIIlllIlIl [1 ]:IIIlIIlIIlIIIlIll +='@'
				else :IIIlIIlIIlIIIlIll +=IlllllllIIIIIlIll 
			IllIIlIllllllllll +=IIIlIIlIIlIIIlIll +'\n'
		IllIIlIllllllllll =IllIIlIllllllllll .strip ()
	except :pass 
	finally :print (IllIIlIllllllllll )
def IIlIIllIIlllIIllI (IIIIlIlIllIIIllIl =1 ):
	for IllIIlIIllIIIlIIl in range (IIIIlIlIllIIIllIl ):sys .stdout .write ('\x1b[F');sys .stdout .write ('\x1b[K')
def IlllIIllIIllIIIIl (IIlIlllIlllIIlIlI ,IlIlllIllIIIlllll ):
	global IllllIIlIIlllIlIl ;global IlIllllIIIllIIlII ;global map ;global IIlIIIIIIllIIlllI ;IllIllllllIlIlIII =[IIlIlllIlllIIlIlI ,IlIlllIllIIIlllll ];IllIlIllIIlllllll =IllllIIlIIlllIlIl .copy ();IllllIIlIIlllIlIl [0 ]+=IllIllllllIlIlIII [0 ];IllllIIlIIlllIlIl [1 ]+=IllIllllllIlIlIII [1 ]
	try :
		IIIIlllIlIlllIIIl =IlIllllIIIllIIlII [_IlIlIIllIllIIlIII ][IllllIIlIIlllIlIl [1 ]][IllllIIlIIlllIlIl [0 ]]
		if IIIIlllIlIlllIIIl =='#':IllllIIlIIlllIlIl =IllIlIllIIlllllll 
		if IIIIlllIlIlllIIIl =='>':
			try :IlIllllIIIllIIlII =IIIlIIIlIlIlIIIII [IlIllllIIIllIIlII [_IlllllIIIIlIIlIIl ]];IllllIIlIIlllIlIl =IlIllllIIIllIIlII [_IIIlIIIlllIlIIlll ][_IIllllIIllIllIllI ].copy ()
			except Exception as IlIlIlIIIlIlIIIll :IIIlIlIIIIIllIIll (IlIlIlIIIlIlIIIll )
		if IIIIlllIlIlllIIIl =='<':
			try :IlIllllIIIllIIlII =IIIlIIIlIlIlIIIII [IlIllllIIIllIIlII [_IIllllIIllIllIllI ]];IllllIIlIIlllIlIl =IlIllllIIIllIIlII [_IIIlIIIlllIlIIlll ][_IlllllIIIIlIIlIIl ].copy ()
			except Exception as IlIlIlIIIlIlIIIll :IIIlIlIIIIIllIIll (IlIlIlIIIlIlIIIll )
		if IIIIlllIlIlllIIIl =='~':IIlIIIIIIllIIlllI ='You won!';IlIlIllllllIIIIlI ()
	except Exception as IlIlIlIIIlIlIIIll :IIIlIlIIIIIllIIll (IlIlIlIIIlIlIIIll );IllllIIlIIlllIlIl =IllIlIllIIlllllll 
def IlIlIllllllIIIIlI ():global IIIlIIlIIllllIIll ;IIIlIIlIIllllIIll =False 
IlllIllIllIIlIlll =[_IIlllIlllIlllIllI ,'#  ##    >','##     ###',_IIlllIlllIlllIllI ]
IlIIIllIIlIIllllI =[_IIIIIIIIlIlIIllII ,'<   #~#','##    #',_IIIIIIIIlIlIIllII ]
IIIlIIIlIlIlIIIII ={'1':{_IlIlIIllIllIIlIII :IlllIllIllIIlIlll ,_IIIlIIIlllIlIIlll :{_IlllllIIIIlIIlIIl :[8 ,1 ]},_IlllllIIIIlIIlIIl :'2'},'2':{_IlIlIIllIllIIlIII :IlIIIllIIlIIllllI ,_IIIlIIIlllIlIIlll :{_IIllllIIllIllIllI :[1 ,1 ]},_IIllllIIllIllIllI :'1'}}
IlIllllIIIllIIlII =IIIlIIIlIlIlIIIII ['1']
IlIlIlllIllIIIlII =[2 ,2 ]
IllllIIlIIlllIlIl =IlIlIlllIllIIIlII 
IIIlIIlIIllllIIll =True 
IIlIIIIIIllIIlllI =''
keyboard .add_hotkey ('w',IlllIIllIIllIIIIl ,(0 ,-1 ))
keyboard .add_hotkey ('s',IlllIIllIIllIIIIl ,(0 ,1 ))
keyboard .add_hotkey ('a',IlllIIllIIllIIIIl ,(-1 ,0 ))
keyboard .add_hotkey ('d',IlllIIllIIllIIIIl ,(1 ,0 ))
keyboard .add_hotkey ('esc',IlIlIllllllIIIIlI )
print ('\n'*len (IlIllllIIIllIIlII [_IlIlIIllIllIIlIII ]))
while IIIlIIlIIllllIIll :IIllIIIlIlllIlIll ()
print (IIlIIIIIIllIIlllI )
input ("Here's all of your moves!\n  (Press enter to continue and exit)\n")