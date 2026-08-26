#!/usr/bin/env python
# coding: utf-8

# In[1]:


def stepnum(ypsl0,ypsl1,ypsl2):
    kpos = 12.8*2
    kneg = kpos/15
    ED=2.5*2
    kNL=200*2
    kD=50*2
    kr=9.2
    p=1
    P0T=(1/kD+1/kr)/(1/kD+1/kr+1/kpos)
    P0L=(1/kD+1/kr)/(1/kD+1/kr+1/kneg)
    if ypsl0-ypsl1>1000:
        ypsl1=ypsl0-1000
    if ypsl0-ypsl1<-1000:
        ypsl1=ypsl0+1000
    if ypsl0-ypsl2>1000:
        ypsl2=ypsl0-1000
    if ypsl0-ypsl2<-1000:
        ypsl2=ypsl0+1000
    PE1=math.exp(ED+((ypsl0-ypsl1)*p)/4.11)/(math.exp(ED+((ypsl0-ypsl1)*p)/4.11)+1)
    PE11=1-PE1
    PE2=math.exp(ED+((ypsl2-ypsl0)*p)/4.11)/(math.exp(ED+((ypsl2-ypsl0)*p)/4.11)+1)
    PE21=1-PE2
    kT=PE1/(1/kpos+P0T/kr)+PE11/(1/kD+1/kpos+1/kr)
    kL=PE2/(1/kD+1/kr+1/kneg)+PE21/(1/kneg+P0L/kr)
    ran3 = random.uniform(0, 1)
    ran4 = random.uniform(0, 1)
    na1 = 0
    if ran3 < kT*PE1 * h:
        na1+= 1
        #print(kT*PE1,kL*PE21,ypsl0,ypsl1,ypsl2)
    if ran4 < kL*PE21 * h:
        na1-= 1
        #print(kT*PE1,kL*PE21,ypsl0,ypsl1,ypsl2)
    return na1


# In[2]:


def rebind():
    u=0.2
    ran4 = random.uniform(0, 1)
    Kin=0
    if ran4 < u * h:
        Kin = 1
    return Kin        


# In[3]:


def dissociation(F,ypsl0,ypsl1,ypsl2):
    F=-F
    kpos = 12.8*2
    kneg = kpos/15
    ED=2.5*2
    kNL=200*2
    kD=50*2
    dpos=8.2
    p=1
    delta=1
    kr=9.2
    kw0=5
    es0=0.1
    deltas=2.3
    ran3 = random.uniform(0, 1)
    if F <= 0 :
        P1=kneg/(kNL+kneg)
    if F >= 4:
        P1=kpos/(kNL+kpos)
    if F > 0 and F < 4:
        k=kneg+(kpos-kneg)*F/4
        P1=k/(kNL+k) 
    if ypsl0-ypsl1>1000:
        ypsl1=ypsl0-1000
    if ypsl0-ypsl1<-1000:
        ypsl1=ypsl0+1000
    if ypsl0-ypsl2>1000:
        ypsl2=ypsl0-1000
    if ypsl0-ypsl2<-1000:
        ypsl2=ypsl0+1000
    Pd1=1
    PE1=math.exp(ED+((ypsl0-ypsl1)*p)/4.11)/(math.exp(ED+((ypsl0-ypsl1)*p)/4.11)+1)
    PE11=1-PE1
    PE2=math.exp(ED+((ypsl2-ypsl0)*p)/4.11)/(math.exp(ED+((ypsl2-ypsl0)*p)/4.11)+1)
    PE21=1-PE2
    P2T=PE1*kpos/(kpos+kD)+PE11*kneg/(kneg+kD)
    P2L=PE2*kpos/(kpos+kD)+PE21*kneg/(kneg+kD)
    kd2=kw0*math.exp(abs(F)*delta/4.130238407)
    Pd2=kd2/(kd2+kD)
    P0T=(1/kD+1/kr)/(1/kD+1/kr+1/kpos)
    P0L=(1/kD+1/kr)/(1/kD+1/kr+1/kneg)
    kT=PE1/(1/kpos+P0T/kr)+(1-PE1)/(1/kD+1/kpos+1/kr)
    kL=PE2/(1/kD+1/kr+1/kneg)+(1-PE2)/(1/kneg+P0L/kr)
    episilon=kT*P1*Pd1+(kT*P2T+kL*P2L)*Pd2+es0*math.exp(abs(F)*deltas/4.130238407)
    Kin=1
    #print(episilon)
    if ran3 < episilon * h:
        Kin= 0
    return Kin


# In[4]:


def jiao(dxc,dxcp,dxcpx,F1,F2,F3,F4,monum,monump,monumpx):
    de=[0,[0 for i in range(pair)],[0 for i in range(pair)],[0 for i in range(pair)],[0 for i in range(pair)],0,0,0]
    num1=[0 for i in range(pair)]
    num2=[0 for i in range(pair)]
    nump1=[0 for i in range(pair)]
    nump2=[0 for i in range(pair)]
    numpx1=[0 for i in range(pair)]
    numpx2=[0 for i in range(pair)]
    fen0=[[] for i in range(pair)]
    fen1=[[] for i in range(pair)]
    fen2=[[] for i in range(pair)]
    fenp0=[[] for i in range(pair)]
    fenp1=[[] for i in range(pair)]
    fenp2=[[] for i in range(pair)]
    fenpx0=[[] for i in range(pair)]
    fenpx1=[[] for i in range(pair)]
    fenpx2=[[] for i in range(pair)]
    jisuan=[[] for i in range(pair)]
    jisuanp=[[] for i in range(pair)]
    jisuanpx=[[] for i in range(pair)]
    ji=[[] for i in range(pair)]
    F0=-FPE
    F7=FPE
    F5=FPE
    F6=-FPE
    Fcc=0
    for x2 in range(pair):
        F0+=Kp1*(l1l[x2]-Xpole)+Kp2*(l2l[x2]-Xpole)
        F7+=Kp1*(l4r[x2]-Xpo)+Kp2*(l3r[x2]-Xpo)
        F5+=Kp3*(l1r[x2]-Xkin)+Kp4*(Xkin1-Xkin-kdis)
        F6+=Kp4*(Xkin-Xkin1+kdis)+Kp3*(l4l[x2]-Xkin1)
        if abs(F1[x2])>0.00001 or abs(F2[x2])>0.00001 or abs(F3[x2])>0.00001 or abs(F4[x2])>0.00001:
            Fcc=1
    if abs(F0)>0.0001 or abs(F5)>0.00001 or abs(F6)>0.00001 or abs(F7)>0.00001:
        Fcc=1
    if Fcc==0:
        return de[0],de[1],de[2],de[3],de[4],de[5],de[6],de[7]
    #print(F1,F2,F3,F4,F0,F5,F6,F7)
    for x2 in range(pair):
        nu[x2]=len(kina[x2])
        nu1[x2]=len(kinap[x2])
        nu1x[x2]=len(kinapx[x2])
        for ton1 in range(nu[x2]):
            if kina[x2][ton1]==1 and kinb[x2][ton1]==1:
                if dxc[x2][ton1]>xdmotor:
                    num1[x2]+=1
                if dxc[x2][ton1]<-xdmotor:
                    num2[x2]+=1
        for ton1 in range(nu1[x2]):
            if kinap[x2][ton1]==1 and kinbp[x2][ton1]==1:
                if dxcp[x2][ton1]>xdmotor:
                    nump1[x2]+=1
                if dxcp[x2][ton1]<-xdmotor:
                    nump2[x2]+=1
        for ton1 in range(nu1x[x2]):
            if kinapx[x2][ton1]==1 and kinbpx[x2][ton1]==1:
                if dxcpx[x2][ton1]>xdmotor:
                    numpx1[x2]+=1
                if dxcpx[x2][ton1]<-xdmotor:
                    numpx2[x2]+=1
        jisuan[x2]=sorted(dxc[x2])
        for ton1 in range(nu[x2]-monum[x2]):
            jisuan[x2].remove(0)
        jisuanp[x2]=sorted(dxcp[x2])
        for ton1 in range(nu1[x2]-monump[x2]):
            jisuanp[x2].remove(0)
        jisuanpx[x2]=sorted(dxcpx[x2])
        for ton1 in range(nu1x[x2]-monumpx[x2]):
            jisuanpx[x2].remove(0)
        cnn0=0
        zq=0

        m1=[monum[x2]-num1[x2]]
        m0=[num2[x2]]
        m2=[0]
        if monum[x2]>0:
            ttt=jisuan[x2][0]
            for tt1 in range(monum[x2]):
                if abs(jisuan[x2][tt1]-ttt)>0.0001:
                    if jisuan[x2][tt1]<-xdmotor:
                        m2.append(tt1)
                    if jisuan[x2][tt1]>=-xdmotor and ttt<xdmotor:
                        m0.append(tt1)
                    if jisuan[x2][tt1]>xdmotor:
                        m1.append(tt1)
                    ttt=jisuan[x2][tt1]
            m2.append(num2[x2])
            m0.append(monum[x2]-num1[x2])
            m1.append(monum[x2])
        fen2[x2]=list(set(m2))
        fen1[x2]=list(set(m1))
        fen0[x2]=list(set(m0))
        fen2[x2].sort(key=m2.index)
        fen1[x2].sort(key=m1.index)
        fen0[x2].sort(key=m0.index)

        m1=[monump[x2]-nump1[x2]]
        m0=[nump2[x2]]
        m2=[0]
        if monump[x2]>0:
            ttt=jisuanp[x2][0]
            for tt1 in range(monump[x2]):
                if abs(jisuanp[x2][tt1]-ttt)>0.0001:
                    if jisuanp[x2][tt1]<-xdmotor:
                        m2.append(tt1)
                    if jisuanp[x2][tt1]>=-xdmotor and ttt<xdmotor:
                        m0.append(tt1)
                    if jisuanp[x2][tt1]>xdmotor:
                        m1.append(tt1)
                    ttt=jisuanp[x2][tt1]
            m2.append(nump2[x2])
            m0.append(monump[x2]-nump1[x2])
            m1.append(monump[x2])
        fenp2[x2]=list(set(m2))
        fenp1[x2]=list(set(m1))
        fenp0[x2]=list(set(m0))
        fenp2[x2].sort(key=m2.index)
        fenp1[x2].sort(key=m1.index)
        fenp0[x2].sort(key=m0.index)

        m1=[monumpx[x2]-numpx1[x2]]
        m0=[numpx2[x2]]
        m2=[0]
        if monumpx[x2]>0:
            ttt=jisuanpx[x2][0]
            for tt1 in range(monumpx[x2]):
                if abs(jisuanpx[x2][tt1]-ttt)>0.0001:
                    if jisuanpx[x2][tt1]<-xdmotor:
                        m2.append(tt1)
                    if jisuanpx[x2][tt1]>=-xdmotor and ttt<xdmotor:
                        m0.append(tt1)
                    if jisuanpx[x2][tt1]>xdmotor:
                        m1.append(tt1)
                    ttt=jisuanpx[x2][tt1]
            m2.append(numpx2[x2])
            m0.append(monumpx[x2]-numpx1[x2])
            m1.append(monumpx[x2])
        fenpx2[x2]=list(set(m2))
        fenpx1[x2]=list(set(m1))
        fenpx0[x2]=list(set(m0))
        fenpx2[x2].sort(key=m2.index)
        fenpx1[x2].sort(key=m1.index)
        fenpx0[x2].sort(key=m0.index)    
    #########################################dzk,dz0
    
    dzk=[[[0 for xxn2 in range(len(fen0[0]))] for xxn1 in range(2)]]
    dz0=[[[0 for xxn2 in range(len(fen2[0]))],[0 for xxn1 in range(len(fen1[0]))]]]
    dzkp=[[[0 for xxn2 in range(len(fenp0[0]))] for xxn1 in range(2)]]
    dz0p=[[[0 for xxn2 in range(len(fenp1[0]))],[0 for xxn1 in range(len(fenp2[0]))]]]
    dzkpx=[[[0 for xxn2 in range(len(fenpx0[0]))] for xxn1 in range(2)]]
    dz0px=[[[0 for xxn2 in range(len(fenpx1[0]))],[0 for xxn1 in range(len(fenpx2[0]))]]]
    for x3 in range(1,pair):
        dzk.append([[0 for xxn2 in range(len(fen0[x3]))] for xxn1 in range(2)])
        dz0.append([[0 for xxn2 in range(len(fen2[x3]))],[0 for xxn1 in range(len(fen1[x3]))]])
        dzkp.append([[0 for xxn2 in range(len(fenp0[x3]))] for xxn1 in range(2)])
        dz0p.append([[0 for xxn2 in range(len(fenp1[x3]))],[0 for xxn1 in range(len(fenp2[x3]))]])
        dzkpx.append([[0 for xxn2 in range(len(fenpx0[x3]))] for xxn1 in range(2)])
        dz0px.append([[0 for xxn2 in range(len(fenpx1[x3]))],[0 for xxn1 in range(len(fenpx2[x3]))]])
    for x2 in range(pair):
        ta1=-1
        for xck in fen0[x2]:
            ta1+=1
            cnnk=monum[x2]-num1[x2]-fen0[x2][-ta1-1]
            chek=monum[x2]-num1[x2]-1#dxc增，ds1>0
            for xxxn in range(cnnk):
                dzk[x2][0][ta1]+=jisuan[x2][chek-xxxn]-xdmotor
        ta1=-1
        for xck in fen0[x2]:
            ta1+=1
            cnnk=xck-num2[x2]
            chek=num2[x2]
            for xxxn in range(cnnk):
                dzk[x2][1][ta1]+=jisuan[x2][chek+xxxn]+xdmotor 
        ta2=-1
        for xckp in fenp0[x2]:
            ta2+=1
            cnnkp=xckp-nump2[x2]
            chekp=nump2[x2]
            for xxxn in range(cnnkp):
                dzkp[x2][0][ta2]+=jisuanp[x2][chekp+xxxn]+xdmotor
        ta2=-1
        for xckp in fenp0[x2]:
            ta2+=1
            cnnkp=monump[x2]-nump1[x2]-fenp0[x2][-ta2-1]
            chekp=monump[x2]-nump1[x2]-1 
            for xxxn in range(cnnkp):
                dzkp[x2][1][ta2]+=jisuanp[x2][chekp-xxxn]-xdmotor 
        ta2=-1
        for xckpx in fenpx0[x2]:
            ta2+=1
            cnnkpx=xckpx-numpx2[x2]
            chekpx=numpx2[x2]
            for xxxn in range(cnnkpx):
                dzkpx[x2][0][ta2]+=jisuanpx[x2][chekpx+xxxn]+xdmotor
        ta2=-1
        for xckpx in fenpx0[x2]:
            ta2+=1
            cnnkpx=monumpx[x2]-numpx1[x2]-fenpx0[x2][-ta2-1]
            chekpx=monumpx[x2]-numpx1[x2]-1 
            for xxxn in range(cnnkpx):
                dzkpx[x2][1][ta2]+=jisuanpx[x2][chekpx-xxxn]-xdmotor 
        ta3=-1
        for xc0 in fen2[x2]:
            ta3+=1
            cnn0=num2[x2]-fen2[x2][-ta3-1]
            che0=num2[x2]-1
            for xxxn in range(cnn0):
                dz0[x2][0][ta3]+=jisuan[x2][che0-xxxn]+xdmotor
        ta3=-1
        for xc0 in fen1[x2]:    
            ta3+=1
            cnn0=xc0-monum[x2]+num1[x2]
            che0=monum[x2]-num1[x2]
            for xxxn in range(cnn0):
                dz0[x2][1][ta3]+=jisuan[x2][che0+xxxn]-xdmotor
        ta4=-1
        for xc0p in fenp1[x2]:
            ta4+=1
            cnn0p=xc0p-monump[x2]+nump1[x2]
            che0p=monump[x2]-nump1[x2]
            for xxxn in range(cnn0p):#dxcp decrease，ds3>0
                dz0p[x2][0][ta4]+=jisuanp[x2][che0p+xxxn]-xdmotor
        ta4=-1
        for xc0p in fenp2[x2]:
            ta4+=1
            cnn0p=nump2[x2]-fenp2[x2][-ta4-1]
            che0p=nump2[x2]-1
            for xxxn in range(cnn0p):
                dz0p[x2][1][ta4]+=jisuanp[x2][che0p-xxxn]+xdmotor
        ta4=-1
        for xc0px in fenpx1[x2]:
            ta4+=1
            cnn0px=xc0px-monumpx[x2]+numpx1[x2]
            che0px=monumpx[x2]-numpx1[x2]
            for xxxn in range(cnn0px):#dxcp减，ds3>0
                dz0px[x2][0][ta4]+=jisuanpx[x2][che0px+xxxn]-xdmotor
        ta4=-1
        for xc0px in fenpx2[x2]:
            ta4+=1
            cnn0px=numpx2[x2]-fenpx2[x2][-ta4-1]
            che0px=numpx2[x2]-1
            for xxxn in range(cnn0px):
                dz0px[x2][1][ta4]+=jisuanpx[x2][che0px-xxxn]+xdmotor

    #print(round(F0),round(F1,2),round(F2,2),round(F3,2),round(F4,2),round(F5,2),round(F6,2),round(F7,2))
    for x2 in range(pair):
        for xx1 in range(2):
            ta1=-1
            for xck in fen0[x2]:
                ta1+=1
                if xx1==0: 
                    if ta1<len(dzk[x2][0]):
                        cnnk=monum[x2]-num1[x2]-fen0[x2][-ta1-1]
                    if ta1>=len(dzk[x2][0]):
                        break
                if xx1==1:
                    if ta1<len(dzk[x2][1]):
                        cnnk=xck-num2[x2]
                    if ta1>=len(dzk[x2][1]):
                        break
                for xx2 in range(2):
                    ta2=-1
                    for xckp in fenp0[x2]:
                        ta2+=1
                        if xx2==0:
                            if ta2<len(dzkp[x2][0]):
                                cnnkp=xckp-nump2[x2]
                            if ta2>=len(dzkp[x2][0]):
                                break
                        if xx2==1:
                            if ta2<len(dzkp[x2][1]):
                                cnnkp=monump[x2]-nump1[x2]-fenp0[x2][-ta2-1]
                            if ta2>=len(dzkp[x2][1]):
                                break
                        for xx3 in range(2):
                            ta5=-1
                            for xckpx in fenpx0[x2]:    
                                ta5+=1
                                if xx3==0:
                                    if ta5<len(dzkpx[x2][0]):
                                        cnnkpx=xckpx-numpx2[x2]
                                    if ta5>=len(dzkpx[x2][0]):
                                        break
                                if xx3==1:
                                    if ta5<len(dzkpx[x2][1]):
                                        cnnkpx=monumpx[x2]-numpx1[x2]-fenpx0[x2][-ta5-1]
                                    if ta5>=len(dzkpx[x2][1]):
                                        break
                                if xx1==0:
                                    xa3=fen2[x2]
                                if xx1==1:
                                    xa3=fen1[x2]
                                ta3=-1
                                for xc0 in xa3:
                                    #print(xqq,xc0,len(dz0[xqq][1]),len(dz0[xqq][0]),'3')
                                    ta3+=1  
                                    if xx1==0:
                                        if ta3<len(dz0[x2][0]):
                                            cnn0=num2[x2]-fen2[x2][-ta3-1]
                                        if ta3>=len(dz0[x2][0]):
                                            break
                                    if xx1==1:
                                        if ta3<len(dz0[x2][1]):
                                            cnn0=xc0-monum[x2]+num1[x2]
                                        if ta3>=len(dz0[x2][1]):
                                            break
                                    if xx2==0:
                                        xa4=fenp1[x2]
                                    if xx2==1:
                                        xa4=fenp2[x2]
                                    ta4=-1
                                    for xc0p in xa4:
                                        ta4+=1
                                        if xx2==0:
                                            if ta4<len(dz0p[x2][0]):
                                                cnn0p=xc0p-monump[x2]+nump1[x2]
                                            if ta4>=len(dz0p[x2][0]):
                                                break
                                        if xx2==1:
                                            if ta4<len(dz0p[x2][1]):
                                                cnn0p=nump2[x2]-fenp2[x2][-ta4-1]    
                                        if xx3==0:
                                            xa5=fenpx1[x2]
                                        if xx3==1:
                                            xa5=fenpx2[x2]
                                        ta6=-1
                                        for xc0px in xa5:
                                            ta6+=1
                                            if xx3==0:
                                                if ta6<len(dz0px[x2][0]):
                                                    cnn0px=xc0px-monumpx[x2]+numpx1[x2]
                                                if ta6>=len(dz0px[x2][0]):
                                                    break
                                            if xx3==1:
                                                if ta6<len(dz0px[x2][1]):
                                                    cnn0px=numpx2[x2]-fenpx2[x2][-ta6-1] 
                                                if ta6>len(dz0px[x2][1]):
                                                    break
                                            if cnn0+cnnk==0 and xx1!=0:
                                                continue
                                            if cnn0p+cnnkp==0 and xx2!=0:
                                                continue
                                            if cnn0px+cnnkpx==0 and xx3!=0:
                                                continue    
                                            
                                            ji[x2].append([cnn0,cnnk,cnn0p,cnnkp,cnn0px,cnnkpx,xx1,xx2,xx3,ta1,ta2,ta3,ta4,ta5,ta6])
    a00=round(2*(-Kp1-Kp2),3);a10=Kp2;a30=Kp1;a80=Kp2;a100=Kp1
    a21=Kp2;a41=Kp1;a71=round((-Kp1-Kp2)*2,3);a91=Kp2;a111a=Kp1
    a32=Kp3;a52=round((-Kp3-Kp4)*2,3);a62=round(Kp4*2,3);a102=Kp3
    a43=Kp3;a53=round(Kp4*2,3);a63=round((-Kp3-Kp4 )*2,3);a113=Kp3
    zq=[0 for i in range(pair)]
    cxx=[0 for i in range(pair)]
    for cx0 in range(len(ji[0])):
        cxx[0]=cx0
        if abs(sum(zq)-pair)<0.01:
            break
        for cx1 in range(len(ji[1])):
            cxx[1]=cx1
            if abs(sum(zq)-pair)<0.01:
                break
             
            cnn0=ji[0][cxx[0]][0]
            cnnk=ji[0][cxx[0]][1]
            cnn0p=ji[0][cxx[0]][2]
            cnnkp=ji[0][cxx[0]][3]
            cnn0px=ji[0][cxx[0]][4]
            cnnkpx=ji[0][cxx[0]][5]
            xx1=ji[0][cxx[0]][6]
            xx2=ji[0][cxx[0]][7]
            xx3=ji[0][cxx[0]][8]
            ta1=ji[0][cxx[0]][9]
            ta2=ji[0][cxx[0]][10]
            ta3=ji[0][cxx[0]][11]
            ta4=ji[0][cxx[0]][12]
            ta5=ji[0][cxx[0]][13]
            ta6=ji[0][cxx[0]][14]
            a04=-Kp1;a24=round(-(nump1[0]+nump2[0]+cnnkp-cnn0p)*Km,3);a34=round((nump1[0]+nump2[0]+cnnkp-cnn0p)*Km+Kp1+Kp3+Kpn5*nunum1[0][0],3);
            a54=-Kp3;a0104=round(-Kpn5*nunum1[0][0],3)
            a05=-Kp2;a15=round(((numpx1[0]+numpx2[0]+cnnkpx-cnn0px)+(num1[0]+num2[0]+cnnk-cnn0))*Km+Kp2+Kpn5*nunum[0]+Kpn5*nunum1[0][0],3);
            a25=round(-Km*(num1[0]+num2[0]+cnnk-cnn0),3);a35=round(-Kpn5*nunum1[0][0],3);a45=round(-(numpx1[0]+numpx2[0]+cnnkpx-cnn0px)*Km,3);a85=round(-Kpn5*nunum[0],3)
            a16=round((num1[0]+num2[0]+cnnk-cnn0)*Km,3);a26=round(-Km*(nump1[0]+nump2[0]+cnnkp-cnn0p+num1[0]+num2[0]+cnnk-cnn0)-Kp2-Kpn5*nunum[1]-Kpn5*nunum1[0][1],3)
            a36=round(Km*(nump1[0]+nump2[0]+cnnkp-cnn0p),3);a46=round(Kpn5*nunum1[0][1],3);a76=Kp2;a96=round(Kpn5*nunum[1],3)
            a17=round(Km*(numpx1[0]+numpx2[0]+cnnkpx-cnn0px),3);a47=round(-Km*(numpx1[0]+numpx2[0]+cnnkpx-cnn0px)-Kp1-Kp3-Kpn5*nunum1[0][1],3)
            a67=Kp3;a77=Kp1;a27=round(Kpn5*nunum1[0][1],3)
            b4=-Km*(dzkp[0][xx2][ta2]-dz0p[0][xx2][ta4])-F1[0]
            b5=-Km*(-dzkpx[0][xx3][ta5]+dz0px[0][xx3][ta6]+dzk[0][xx1][ta1]-dz0[0][xx1][ta3])-F2[0]
            b6=-Km*(dzkp[0][xx2][ta2]-dz0p[0][xx2][ta4]+dzk[0][xx1][ta1]-dz0[0][xx1][ta3])-F3[0]
            b7=Km*(dzkpx[0][xx3][ta5]-dz0px[0][xx3][ta6])-F4[0]
            cnn0=ji[1][cxx[1]][0]
            cnnk=ji[1][cxx[1]][1]
            cnn0p=ji[1][cxx[1]][2]
            cnnkp=ji[1][cxx[1]][3]
            cnn0px=ji[1][cxx[1]][4]
            cnnkpx=ji[1][cxx[1]][5]
            xx1=ji[1][cxx[1]][6]
            xx2=ji[1][cxx[1]][7]
            xx3=ji[1][cxx[1]][8]
            ta1=ji[1][cxx[1]][9]
            ta2=ji[1][cxx[1]][10]
            ta3=ji[1][cxx[1]][11]
            ta4=ji[1][cxx[1]][12]
            ta5=ji[1][cxx[1]][13]
            ta6=ji[1][cxx[1]][14]
            a08=-Kp1;a28=round(-(nump1[1]+nump2[1]+cnnkp-cnn0p)*Km,3);a38=round((nump1[1]+nump2[1]+cnnkp-cnn0p)*Km+Kp1+Kp3+Kpn5*nunum1[1][0],3)
            a58=-Kp3;a88=-round(Kpn5*nunum1[1][0],3)
            a09=-Kp2;a19=round(((numpx1[1]+numpx2[1]+cnnkpx-cnn0px)+(num1[1]+num2[1]+cnnk-cnn0))*Km+Kp2+Kpn5*nunum[0]+Kpn5*nunum1[1][0],3);a019=-round(Kpn5*nunum[0],3)
            a29=round(-Km*(num1[1]+num2[1]+cnnk-cnn0),3);a49=round(-(numpx1[1]+numpx2[1]+cnnkpx-cnn0px)*Km,3);a109=-round(Kpn5*nunum1[1][0],3)
            a110=round((num1[1]+num2[1]+cnnk-cnn0)*Km,3);a210=round(-Km*(nump1[1]+nump2[1]+cnnkp-cnn0p+num1[1]+num2[1]+cnnk-cnn0)-Kp2-Kpn5*nunum[1]-Kpn5*nunum1[1][1],3)
            a310=round(Km*(nump1[1]+nump2[1]+cnnkp-cnn0p),3);a710=Kp2;a0210=round(Kpn5*nunum[1],3);a1110=round(Kpn5*nunum1[1][1],3)
            a111=round(Km*(numpx1[1]+numpx2[1]+cnnkpx-cnn0px),3);a411=round(-Km*(numpx1[1]+numpx2[1]+cnnkpx-cnn0px)-Kp1-Kp3-Kpn5*nunum1[1][1],3)
            a611=Kp3;a711=Kp1;a911=round(Kpn5*nunum1[1][1],3)
            b8=-Km*(dzkp[1][xx2][ta2]-dz0p[1][xx2][ta4])-F1[1]
            b9=-Km*(-dzkpx[1][xx3][ta5]+dz0px[1][xx3][ta6]+dzk[1][xx1][ta1]-dz0[1][xx1][ta3])-F2[1]
            b10=-Km*(dzkp[1][xx2][ta2]-dz0p[1][xx2][ta4]+dzk[1][xx1][ta1]-dz0[1][xx1][ta3])-F3[1]
            b11=Km*(dzkpx[1][xx3][ta5]-dz0px[1][xx3][ta6])-F4[1] 
            b=np.array([round(-F0,14),round(-F7,14),round(-F5,14),round(-F6,14),round(b4,14),round(b5,14),round(b6,14),round(b7,14),round(b8,14),round(b9,14),round(b10,14),round(b11,14)])
            try:
                
                A=np.array([[a00,a10,0,a30,0,0,0,0,a80,0,a100,0],[0,0,a21,0,a41,0,0,a71,0,a91,0,a111a],
                             [0,0,0,a32,0,a52,a62,0,0,0,a102,0],[0,0,0,0,a43,a53,a63,0,0,0,0,a113],
                             [a04,a0104,a24,a34,0,a54,0,0,0,0,0,0],[a05,a15,a25,a35,a45,0,0,0,a85,0,0,0],
                             [0,a16,a26,a36,a46,0,0,a76,0,a96,0,0],[0,a17,a27,0,a47,0,a67,a77,0,0,0,0],
                             [a08,0,0,0,0,a58,0,0,a88,a28,a38,0],[a09,a019,0,0,0,0,0,0,a19,a29,a109,a49],
                             [0,0,a0210,0,0,0,0,a710,a110,a210,a310,a1110],[0,0,0,0,0,0,a611,a711,a111,a911,0,a411]])

                #b=np.array([-F0,-F7,-F5,-F6,b4,b5,b6,b7])
                #print(A,b)
                mtui=np.linalg.solve(A,b)

            except:
                #print(A,b)
                """po,  x1, x2, x3, x4, ink, in1, po1, y1, y2, y3, y4 = symbols('po x1 x2 x3 x4 po1 ink in1 y1 y2 y3 y4')
                eqs = [Eq(a00*po+a10*po1+a30*in1+a80*y1+a100*y3,round(-F0,14)),
                       Eq(a21*x2+a41*x4+a71*in1+a91*y2+a111a*y4, round(-F7,14)),
                       Eq(a32*x3+a52*ink+a62*in1+a102*y3, round(-F5,14)),
                       Eq(a43*x4+a53*ink+a63*in1+a113*y4 ,round(-F6,14) ),
                       Eq(a04*po+a24*x2+a34*x3+a54*ink+a104*y3,round(b4,14) ),
                       Eq(a05*po+a15*x1+a25*x2+a45*x4+a85*y1,round(b5,14) ),
                       Eq(a16*x1+a26*x2+a36*x3+a76*po1+a96*y2,round(b6,14)),
                       Eq(a17*x1+a47*x4+a67*in1+a77*po1+a117*y4,round(b7,14)),
                       Eq(a08*po+a038*x3+a58*ink+a28*y2+a38*y3,round(b8,14)),
                       Eq(a09*po+a019*x1+a19*y1+a29*y2+a49*y4,round(b9,14)),
                       Eq(a0210*x2+a710*po1+a110*y1+a210*y2+a310*y3,round(b10,14)),
                       Eq(a0411*x4+a611*in1+a711*po1+a111*y1+a411*y4,round(b11,14))]
                initialValue = [0, 0, 0, 0, 0,0,0 ,0 , 0,0, 0,0]
                print(solve(eqs, [po,  x1, x2, x3, x4, ink, in1, po1, y1, y2, y3, y4 ]))
                mtui=solve(eqs, [po,  x1, x2, x3, x4, ink, in1, po1, y1, y2, y3, y4 ])
                print(mtui)"""
                #mtui = np.linalg.pinv(A) @ b
                mtui = gaussian_elimination(A,b)
            tuzx=(mtui[0]+mtui[7])/2
            for xn in range(12):
                mtui[xn]-=tuzx

            de=[mtui[0],[mtui[1],mtui[8]],[mtui[2],mtui[9]],[mtui[3],mtui[10]],[mtui[4],mtui[11]],mtui[5],mtui[6],mtui[7]]
            #print(de,'xx')
            #print(b)
            chezq=0
            for x3 in range(pair):
                check0=-1############
                checkk=-1############
                checkp0=-1###########
                checkpk=-1#############
                checkpx0=-1#############
                checkpxk=-1#################
                cnn0=ji[x3][cxx[x3]][0]
                cnnk=ji[x3][cxx[x3]][1]
                cnn0p=ji[x3][cxx[x3]][2]
                cnnkp=ji[x3][cxx[x3]][3]
                cnn0px=ji[x3][cxx[x3]][4]
                cnnkpx=ji[x3][cxx[x3]][5]
                xx1=ji[x3][cxx[x3]][6]
                xx2=ji[x3][cxx[x3]][7]
                xx3=ji[x3][cxx[x3]][8]
                #print(chezq)
                if cnn0+cnnk==0:
                    for ton1 in range(monum[x3]):
                        if abs(jisuan[x3][ton1])<=xdmotor and abs(jisuan[x3][ton1]+de[1][x3]-de[2][x3])>xdmotor:
                            chezq=-1
                            break
                        if abs(jisuan[x3][ton1])>xdmotor and abs(jisuan[x3][ton1]+de[1][x3]-de[2][x3])<=xdmotor:
                            chezq=-1
                            break
                #print(chezq)
                if cnn0+cnnk!=0:    
                    if xx1==0 and de[1][x3]-de[2][x3]>=0:
                        check0=0#############
                        checkk=0##############
                        for ton1 in range(monum[x3]):
                            if jisuan[x3][ton1]<-xdmotor and abs(jisuan[x3][ton1]+de[1][x3]-de[2][x3])<=xdmotor:
                                check0+=1
                            if abs(jisuan[x3][ton1])<=xdmotor and jisuan[x3][ton1]+de[1][x3]-de[2][x3]>xdmotor:
                                checkk+=1
                    if xx1==1 and de[1][x3]-de[2][x3]<=0:
                        check0=0###########
                        checkk=0##############
                        for ton1 in range(monum[x3]):
                            if abs(jisuan[x3][ton1])<=xdmotor and jisuan[x3][ton1]+de[1][x3]-de[2][x3]<-xdmotor:
                                checkk+=1
                            if jisuan[x3][ton1]>xdmotor and abs(jisuan[x3][ton1]+de[1][x3]-de[2][x3])<=xdmotor:
                                check0+=1
                    if check0!=cnn0 or checkk!=cnnk:
                        chezq=-1
                        break
                #print(chezq)
                if chezq==-1:
                    #print(x3)
                    break
                if cnn0p+cnnkp==0:
                    for ton1 in range(monump[x3]):
                        if abs(jisuanp[x3][ton1])<=xdmotor and abs(jisuanp[x3][ton1]+de[3][x3]-de[2][x3])>xdmotor:
                            chezq=-1
                            break
                        if abs(jisuanp[x3][ton1])>xdmotor and abs(jisuanp[x3][ton1]+de[3][x3]-de[2][x3])<=xdmotor:
                            chezq=-1
                            break
                #print(chezq)
                if cnn0p+cnnkp!=0:
                    if xx2==1 and de[3][x3]-de[2][x3]>=0:
                        checkp0=0################
                        checkpk=0##############
                        for ton1 in range(monump[x3]):
                            if jisuanp[x3][ton1]<-xdmotor and abs(jisuanp[x3][ton1]+de[3][x3]-de[2][x3])<=xdmotor:
                                checkp0+=1
                            if abs(jisuanp[x3][ton1])<=xdmotor and jisuanp[x3][ton1]+de[3][x3]-de[2][x3]>xdmotor:
                                checkpk+=1
                    if xx2==0 and de[3][x3]-de[2][x3]<=0:
                        checkp0=0
                        checkpk=0
                        for ton1 in range(monump[x3]):
                            if abs(jisuanp[x3][ton1])<=xdmotor and jisuanp[x3][ton1]+de[3][x3]-de[2][x3]<-xdmotor:
                                checkpk+=1
                            if jisuanp[x3][ton1]>xdmotor and abs(jisuanp[x3][ton1]+de[3][x3]-de[2][x3])<=xdmotor:
                                checkp0+=1
                    if checkp0!=cnn0p or checkpk!=cnnkp:
                        chezq=-1
                        break
                #print(chezq)
                if chezq==-1:
                    #print(x3,'p')
                    break
                if cnn0px+cnnkpx==0:
                    for ton1 in range(monumpx[x3]):
                        if abs(jisuanpx[x3][ton1])<=xdmotor and abs(jisuanpx[x3][ton1]+de[4][x3]-de[1][x3])>xdmotor:
                            chezq=-1
                            break
                        if abs(jisuanpx[x3][ton1])>xdmotor and abs(jisuanpx[x3][ton1]+de[4][x3]-de[1][x3])<=xdmotor:
                            chezq=-1
                            break
                #print(chezq)
                if cnn0px+cnnkpx!=0:
                    if xx3==1 and de[4][x3]-de[1][x3]>=0:
                        checkpx0=0#################
                        checkpxk=0#################
                        for ton1 in range(monumpx[x3]):
                            if jisuanpx[x3][ton1]<-xdmotor and abs(jisuanpx[x3][ton1]+de[4][x3]-de[1][x3])<=xdmotor:
                                checkpx0+=1
                            if abs(jisuanpx[x3][ton1])<=xdmotor and jisuanpx[x3][ton1]+de[4][x3]-de[1][x3]>xdmotor:
                                checkpxk+=1
                    if xx3==0 and de[4][x3]-de[1][x3]<=0:
                        checkpx0=0###############
                        checkpxk=0###############
                        for ton1 in range(monumpx[x3]):
                            if abs(jisuanpx[x3][ton1])<=xdmotor and jisuanpx[x3][ton1]+de[4][x3]-de[1][x3]<-xdmotor:
                                checkpxk+=1
                            if jisuanpx[x3][ton1]>xdmotor and abs(jisuanpx[x3][ton1]+de[4][x3]-de[1][x3])<=xdmotor:
                                checkpx0+=1
                    if checkpx0!=cnn0px or checkpxk!=cnnkpx:
                        chezq=-1
                        break
                #print(chezq)
                if chezq==-1:
                    #print(x3,'px')
                    break
            if chezq==-1:
                continue
            #print(jisuan,jisuanp,jisuanpx)
            #print(ji[0][cxx[0]],ji[1][cxx[1]])
            #print(ji)
            return de[0],de[1],de[2],de[3],de[4],de[5],de[6],de[7]
    #print(jisuan,jisuanp,jisuanpx)
    dpn=0
    if sum(zq)!=pair:
        for xqq in range(pair):
            if abs(F1[xqq])>0.001 or abs(F2[xqq])>0.001 or abs(F3[xqq])>0.001 or abs(F4[xqq])>0.001 :
                dpn=xqq
                break
    #print(dpn,num1[dpn]+numpx2[dpn]+num2[dpn]+numpx1[dpn]+1,nump2[dpn]+nump1[dpn]+1)
    tq=1
    if abs(F2[dpn])>0.0001 and abs(F3[dpn])<0.0001:
        tq=0
    p1=[0 for xxx in range(pair)]
    p2=[0 for xxx in range(pair)]
    p3=[0 for xxx in range(pair)]
    p4=[0 for xxx in range(pair)]
    for xxx in range(pair):
        p1[xxx]=F1[xxx]
        p2[xxx]=F2[xxx]
        p3[xxx]=F3[xxx]
        p4[xxx]=F4[xxx]
    if tq==0:
        lastui1=-1000
        for xn in range(num1[dpn]+numpx2[dpn]+num2[dpn]+numpx1[dpn]+1):#MT2
            if xn < num1[dpn]:
                tui1=-(jisuan[dpn][-num1[dpn]+xn]-xdmotor+0.1)
            if xn >= num1[dpn] and xn <num1[dpn]+numpx2[dpn]:
                tui1=(jisuanpx[dpn][numpx2[dpn]-1-xn+num1[dpn]]+xdmotor-0.1)
            if xn >= num1[dpn]+numpx2[dpn] and xn <num1[dpn]+numpx2[dpn]+num2[dpn]:
                tui1=-(jisuan[dpn][num2[dpn]-1-xn+num1[dpn]+numpx2[dpn]]+xdmotor-0.1)
            if xn >= num1[dpn]+numpx2[dpn]+num2[dpn] and xn <num1[dpn]+numpx2[dpn]+num2[dpn]+numpx1[dpn]:
                tui1=(jisuanpx[dpn][monumpx[dpn]-numpx1[dpn]+xn-num1[dpn]-numpx2[dpn]-num2[dpn]]-xdmotor+0.1)
            if xn==num1[dpn]+numpx2[dpn]+num2[dpn]+numpx1[dpn]:
                tui1=0
            if abs(tui1-lastui1)<0.0001:
                continue
            lastui1=tui1
            lastui2=-1000
            for xn1 in range(nump2[dpn]+nump1[dpn]+1):#MT1
                if xn1 <nump1[dpn]:
                    tui2=(-jisuanp[dpn][-nump1[dpn]+xn1]+xdmotor-0.1)
                if xn1 >= nump1[dpn] and xn1 <nump1[dpn]+nump2[dpn]:
                    tui2=-(jisuanp[dpn][nump2[dpn]-1-xn1+nump1[dpn]]+xdmotor-0.1)
                if xn1==nump1[dpn]+nump2[dpn]:
                    tui2=0
                if abs(tui2-lastui2)<0.0001 or abs(tui1)+abs(tui2)==0:
                    continue
                lastui2=tui2#####MT3往前tui1,MT4往前tui2
                F0=-FPE
                F7=FPE
                F5=FPE
                F6=-FPE
                for x2 in range(pair):
                    if x2!=dpn:
                        F0+=Kp1*(l1l[x2]-Xpole)+Kp2*(l2l[x2]-Xpole)
                        F7+=Kp1*(l4r[x2]-Xpo)+Kp2*(l3r[x2]-Xpo)
                        F5+=Kp3*(l1r[x2]-Xkin)+Kp4*(Xkin1-Xkin-kdis)
                        F6+=Kp4*(Xkin-Xkin1+kdis)+Kp3*(l4l[x2]-Xkin1)
                        F3[x2]=Kp2*(Xpo-l3r[x2])
                        F1[x2]=Kp1*(l1l[x2]-Xpole)+Kp3*(l1r[x2]-Xkin)
                        F2[x2]=Kp2*(l2l[x2]-Xpole)
                        F4[x2]=Kp1*(Xpo-l4r[x2])+Kp3*(Xkin1-l4l[x2])
                        for ton1 in range(monum[x2]):
                            if jisuan[x2][ton1]>xdmotor:
                                F3[x2]+=(jisuan[x2][ton1]-xdmotor)*Km
                                F2[x2]+=(jisuan[x2][ton1]-xdmotor)*Km
                            if jisuan[x2][ton1]<-xdmotor:
                                F3[x2]+=(jisuan[x2][ton1]+xdmotor)*Km
                                F2[x2]+=(jisuan[x2][ton1]+xdmotor)*Km
                        for ton1 in range(monump[x2]):
                            if jisuanp[x2][ton1]>xdmotor:
                                F3[x2]+=(jisuanp[x2][ton1]-xdmotor)*Km
                                F1[x2]+=(jisuanp[x2][ton1]-xdmotor)*Km
                            if jisuanp[x2][ton1]<-xdmotor:
                                F3[x2]+=(jisuanp[x2][ton1]+xdmotor)*Km
                                F1[x2]+=(jisuanp[x2][ton1]+xdmotor)*Km
                        for ton1 in range(monumpx[x2]):
                            if jisuanpx[x2][ton1]>xdmotor:
                                F4[x2]-=(jisuanpx[x2][ton1]-xdmotor)*Km
                                F2[x2]-=(jisuanpx[x2][ton1]-xdmotor)*Km
                            if jisuanpx[x2][ton1]<-xdmotor:
                                F4[x2]-=(jisuanpx[x2][ton1]+xdmotor)*Km
                                F2[x2]-=(jisuanpx[x2][ton1]+xdmotor)*Km
                    if x2==dpn:
                        F0+=Kp1*(l1l[x2]+tui2-Xpole)+Kp2*(l2l[x2]+tui1-Xpole)
                        F7+=Kp1*(l4r[x2]-Xpo)+Kp2*(l3r[x2]-Xpo)
                        F5+=Kp3*(l1r[x2]+tui2-Xkin)+Kp4*(Xkin1-Xkin-kdis)
                        F6+=Kp4*(Xkin-Xkin1+kdis)+Kp3*(l4l[x2]-Xkin1)
                        F3[x2]=Kp2*(Xpo-l3r[x2])
                        F1[x2]=Kp1*(l1l[x2]+tui2-Xpole)+Kp3*(l1r[x2]+tui2-Xkin)
                        F2[x2]=Kp2*(l2l[x2]+tui1-Xpole)
                        F4[x2]=Kp1*(Xpo-l4r[x2])+Kp3*(Xkin1-l4l[x2])
                        for ton1 in range(monum[x2]):
                            if jisuan[x2][ton1]+tui1>xdmotor:
                                F3[x2]+=(jisuan[x2][ton1]+tui1-xdmotor)*Km
                                F2[x2]+=(jisuan[x2][ton1]+tui1-xdmotor)*Km
                            if jisuan[x2][ton1]+tui1<-xdmotor:
                                F3[x2]+=(jisuan[x2][ton1]+tui1+xdmotor)*Km
                                F2[x2]+=(jisuan[x2][ton1]+tui1+xdmotor)*Km
                        for ton1 in range(monump[x2]):
                            if jisuanp[x2][ton1]+tui2>xdmotor:
                                F3[x2]+=(jisuanp[x2][ton1]+tui2-xdmotor)*Km
                                F1[x2]+=(jisuanp[x2][ton1]+tui2-xdmotor)*Km
                            if jisuanp[x2][ton1]+tui2<-xdmotor:
                                F3[x2]+=(jisuanp[x2][ton1]+tui2+xdmotor)*Km
                                F1[x2]+=(jisuanp[x2][ton1]+tui2+xdmotor)*Km
                        for ton1 in range(monumpx[x2]):
                            if jisuanpx[x2][ton1]-tui1>xdmotor:
                                F4[x2]-=(jisuanpx[x2][ton1]-tui1-xdmotor)*Km
                                F2[x2]-=(jisuanpx[x2][ton1]-tui1-xdmotor)*Km
                            if jisuanpx[x2][ton1]-tui1<-xdmotor:
                                F4[x2]-=(jisuanpx[x2][ton1]-tui1+xdmotor)*Km
                                F2[x2]-=(jisuanpx[x2][ton1]-tui1+xdmotor)*Km
                for ssx in range(2):
                    for xn in range(MTnumber):
                        if dpn==0:
                            kua0=tui1;kua1=0
                        if dpn==1:
                            kua0=0;kua1=tui1 
                        for ton1 in range(Nma[ssx][xn][0]):
                            if kinam[ssx][xn][0][ton1]==1 and kinbm[ssx][xn][0][ton1]==1:
                                dxnuma=numa[ssx][xn][0][ton1][0]-numa[ssx][xn][0][ton1][1]+kua0-kua1
                                for to2 in range(xn,MTnumber-1):
                                    dxnuma+=overlap[0][ssx][1][to2]-overlap[1][ssx][1][to2]
                                F2[0]+=Kpn5*dxnuma
                                F2[1]-=Kpn5*dxnuma
                        for ton1 in range(Nma[ssx][xn][1]):
                            if kinam[ssx][xn][1][ton1]==1 and kinbm[ssx][xn][1][ton1]==1:
                                dxnuma=numa[ssx][xn][1][ton1][0]-numa[ssx][xn][1][ton1][1]
                                for to2 in range(xn,MTnumber-1):
                                    dxnuma+=-overlap[0][ssx][2][to2]+overlap[1][ssx][2][to2]
                                F3[0]-=Kpn5*dxnuma
                                F3[1]+=Kpn5*dxnuma
                        for sik in range(2):
                            for ton1 in range(Nma1[sik][ssx][xn][0]):
                                if kinam1[sik][ssx][xn][0][ton1]==1 and kinbm1[sik][ssx][xn][0][ton1]==1:
                                    if dpn!=sik:
                                        dxnuma1=numa1[sik][ssx][xn][0][ton1][0]-numa1[sik][ssx][xn][0][ton1][1]
                                    if dpn==sik:
                                        dxnuma1=numa1[sik][ssx][xn][0][ton1][0]-numa1[sik][ssx][xn][0][ton1][1]+tui2-tui1
                                    for to2 in range(xn,MTnumber-1):
                                        dxnuma1+=overlap[sik][ssx][0][to2]-overlap[sik][ssx][1][to2]
                                    F1[sik]+=Kpn5*dxnuma1
                                    F2[sik]-=Kpn5*dxnuma1
                            for ton1 in range(Nma1[sik][ssx][xn][1]):
                                if kinam1[sik][ssx][xn][1][ton1]==1 and kinbm1[sik][ssx][xn][1][ton1]==1:
                                    dxnuma1=numa1[sik][ssx][xn][1][ton1][0]-numa1[sik][ssx][xn][1][ton1][1]
                                    for to2 in range(xn,MTnumber-1):
                                        dxnuma1+=-overlap[sik][ssx][3][to2]+overlap[sik][ssx][2][to2]
                                    F4[sik]-=Kpn5*dxnuma1
                                    F3[sik]+=Kpn5*dxnuma1
                
                       

                Fcc=0
                for x2 in range(pair):
                    if abs(F1[x2])+abs(F2[x2])+abs(F3[x2])+abs(F4[x2])>0.01:
                        Fcc=1
                        break
                if Fcc==0 and abs(F0)<0.0001 and abs(F5)<0.00001 and abs(F6)<0.00001 and abs(F7)<0.00001:
                    de[1][dpn]+=tui1;de[3][dpn]+=tui2
                    for xxx in range(pair):
                        F1[xxx]=p1[xxx]
                        F2[xxx]=p2[xxx]
                        F3[xxx]=p3[xxx]
                        F4[xxx]=p4[xxx]
                    return de[0],de[1],de[2],de[3],de[4],de[5],de[6],de[7]

                jisuan1=[[] for i in range(pair)]
                jisuanp1=[[] for i in range(pair)]
                jisuanpx1=[[] for i in range(pair)]
                for x2 in range(pair):
                    if x2==dpn:
                        for ton1 in range(monum[x2]):
                            jisuan1[x2].append(jisuan[x2][ton1]+tui1)
                        for ton1 in range(monump[x2]):
                            jisuanp1[x2].append(jisuanp[x2][ton1]+tui2)
                        for ton1 in range(monumpx[x2]):
                            jisuanpx1[x2].append(jisuanpx[x2][ton1]-tui1)
                    if x2!=dpn:
                        for ton1 in range(monum[x2]):
                            jisuan1[x2].append(jisuan[x2][ton1])
                        for ton1 in range(monump[x2]):
                            jisuanp1[x2].append(jisuanp[x2][ton1])
                        for ton1 in range(monumpx[x2]):
                            jisuanpx1[x2].append(jisuanpx[x2][ton1])
                #print(jisuan1,jisuanp1,jisuanpx1,F0,F1,F2,F3,F4,F5,F6,F7,'cc1')
                tuf,de[0],de[1],de[2],de[3],de[4],de[5],de[6],de[7]=jiaocheck(jisuan1,jisuanp1,jisuanpx1,F0,F1,F2,F3,F4,F5,F6,F7)
                if tuf==1:
                    de[1][dpn]+=tui1
                    de[3][dpn]+=tui2
                    for xxx in range(pair):
                        F1[xxx]=p1[xxx]
                        F2[xxx]=p2[xxx]
                        F3[xxx]=p3[xxx]
                        F4[xxx]=p4[xxx]
                    return de[0],de[1],de[2],de[3],de[4],de[5],de[6],de[7]
                    break
    if tq==1:
        lastui1=-1000
        for xn in range(num1[dpn]+nump2[dpn]+num2[dpn]+nump1[dpn]+1):
            if xn < num1[dpn]:
                tui1=(jisuan[dpn][-num1[dpn]+xn]-xdmotor+0.1)
            if xn >= num1[dpn] and xn <num1[dpn]+nump2[dpn]:
                tui1=(jisuanp[dpn][nump2[dpn]-1-xn+num1[dpn]]+xdmotor-0.1)
            if xn >= num1[dpn]+nump2[dpn] and xn <num1[dpn]+nump2[dpn]+num2[dpn]:
                tui1=(jisuan[dpn][num2[dpn]-1-xn+num1[dpn]+nump2[dpn]]+xdmotor-0.1)
            if xn >= num1[dpn]+nump2[dpn]+num2[dpn] and xn <num1[dpn]+nump2[dpn]+num2[dpn]+nump1[dpn]:
                tui1=(jisuanp[dpn][monump[dpn]-nump1[dpn]+xn-num1[dpn]-nump2[dpn]-num2[dpn]]-xdmotor+0.1)
            if xn==num1[dpn]+nump2[dpn]+num2[dpn]+nump1[dpn]:
                tui1=0
            if abs(tui1-lastui1)<0.0001:
                continue
            lastui1=tui1
            lastui2=-1000
            for xn1 in range(numpx2[dpn]+numpx1[dpn]+1):#MT4
                if xn1 <numpx1[dpn]:
                    tui2=(-jisuanpx[dpn][-numpx1[dpn]+xn1]+xdmotor-0.1)
                if xn1 >= numpx1[dpn] and xn1 <numpx1[dpn]+numpx2[dpn]:
                    tui2=-(jisuanpx[dpn][numpx2[dpn]-1-xn1+numpx1[dpn]]+xdmotor-0.1)
                if xn1==numpx1[dpn]+numpx2[dpn]:
                    tui2=0
                if abs(tui2-lastui2)<0.0001 or abs(tui1)+abs(tui2)==0:
                    continue
                lastui2=tui2#####MT3往前tui1,MT4往前tui2
                F0=-FPE
                F7=FPE
                F5=FPE
                F6=-FPE
                for x2 in range(pair):
                    if x2!=dpn:
                        F0+=Kp1*(l1l[x2]-Xpole)+Kp2*(l2l[x2]-Xpole)
                        F7+=Kp1*(l4r[x2]-Xpo)+Kp2*(l3r[x2]-Xpo)
                        F5+=Kp3*(l1r[x2]-Xkin)+Kp4*(Xkin1-Xkin-kdis)
                        F6+=Kp4*(Xkin-Xkin1+kdis)+Kp3*(l4l[x2]-Xkin1)
                        F3[x2]=Kp2*(Xpo-l3r[x2])
                        F1[x2]=Kp1*(l1l[x2]-Xpole)+Kp3*(l1r[x2]-Xkin)
                        F2[x2]=Kp2*(l2l[x2]-Xpole)
                        F4[x2]=Kp1*(Xpo-l4r[x2])+Kp3*(Xkin1-l4l[x2])
                        for ton1 in range(monum[x2]):
                            if jisuan[x2][ton1]>xdmotor:
                                F3[x2]+=(jisuan[x2][ton1]-xdmotor)*Km
                                F2[x2]+=(jisuan[x2][ton1]-xdmotor)*Km
                            if jisuan[x2][ton1]<-xdmotor:
                                F3[x2]+=(jisuan[x2][ton1]+xdmotor)*Km
                                F2[x2]+=(jisuan[x2][ton1]+xdmotor)*Km
                        for ton1 in range(monump[x2]):
                            if jisuanp[x2][ton1]>xdmotor:
                                F3[x2]+=(jisuanp[x2][ton1]-xdmotor)*Km
                                F1[x2]+=(jisuanp[x2][ton1]-xdmotor)*Km
                            if jisuanp[x2][ton1]<-xdmotor:
                                F3[x2]+=(jisuanp[x2][ton1]+xdmotor)*Km
                                F1[x2]+=(jisuanp[x2][ton1]+xdmotor)*Km
                        for ton1 in range(monumpx[x2]):
                            if jisuanpx[x2][ton1]>xdmotor:
                                F4[x2]-=(jisuanpx[x2][ton1]-xdmotor)*Km
                                F2[x2]-=(jisuanpx[x2][ton1]-xdmotor)*Km
                            if jisuanpx[x2][ton1]<-xdmotor:
                                F4[x2]-=(jisuanpx[x2][ton1]+xdmotor)*Km
                                F2[x2]-=(jisuanpx[x2][ton1]+xdmotor)*Km
                    if x2==dpn:
                        F0+=Kp1*(l1l[x2]-Xpole)+Kp2*(l2l[x2]-Xpole)
                        F7+=Kp1*(l4r[x2]+tui2-Xpo)+Kp2*(l3r[x2]+tui1-Xpo)
                        F5+=Kp3*(l1r[x2]-Xkin)+Kp4*(Xkin1-Xkin-kdis)
                        F6+=Kp4*(Xkin-Xkin1+kdis)+Kp3*(l4l[x2]+tui2-Xkin1)
                        F3[x2]=Kp2*(Xpo-l3r[x2]-tui1)
                        F1[x2]=Kp1*(l1l[x2]-Xpole)+Kp3*(l1r[x2]-Xkin)
                        F2[x2]=Kp2*(l2l[x2]-Xpole)
                        F4[x2]=Kp1*(Xpo-l4r[x2]-tui2)+Kp3*(Xkin1-l4l[x2]-tui2)
                        for ton1 in range(monum[x2]):
                            if jisuan[x2][ton1]-tui1>xdmotor:
                                F3[x2]+=(jisuan[x2][ton1]-tui1-xdmotor)*Km
                                F2[x2]+=(jisuan[x2][ton1]-tui1-xdmotor)*Km
                            if jisuan[x2][ton1]-tui1<-xdmotor:
                                F3[x2]+=(jisuan[x2][ton1]-tui1+xdmotor)*Km
                                F2[x2]+=(jisuan[x2][ton1]-tui1+xdmotor)*Km
                        for ton1 in range(monump[x2]):
                            if jisuanp[x2][ton1]-tui1>xdmotor:
                                F3[x2]+=(jisuanp[x2][ton1]-tui1-xdmotor)*Km
                                F1[x2]+=(jisuanp[x2][ton1]-tui1-xdmotor)*Km
                            if jisuanp[x2][ton1]-tui1<-xdmotor:
                                F3[x2]+=(jisuanp[x2][ton1]-tui1+xdmotor)*Km
                                F1[x2]+=(jisuanp[x2][ton1]-tui1+xdmotor)*Km
                        for ton1 in range(monumpx[x2]):
                            if jisuanpx[x2][ton1]+tui2>xdmotor:
                                F4[x2]-=(jisuanpx[x2][ton1]+tui2-xdmotor)*Km
                                F2[x2]-=(jisuanpx[x2][ton1]+tui2-xdmotor)*Km
                            if jisuanpx[x2][ton1]+tui2<-xdmotor:
                                F4[x2]-=(jisuanpx[x2][ton1]+tui2+xdmotor)*Km
                                F2[x2]-=(jisuanpx[x2][ton1]+tui2+xdmotor)*Km
                for ssx in range(2):
                    for xn in range(MTnumber):
                        
                        for ton1 in range(Nma[ssx][xn][0]):
                            if kinam[ssx][xn][0][ton1]==1 and kinbm[ssx][xn][0][ton1]==1:
                                dxnuma=numa[ssx][xn][0][ton1][0]-numa[ssx][xn][0][ton1][1]
                                for to2 in range(xn,MTnumber-1):
                                    dxnuma+=overlap[0][ssx][1][to2]-overlap[1][ssx][1][to2]
                                F2[0]+=Kpn5*dxnuma
                                F2[1]-=Kpn5*dxnuma
                        if dpn==0:
                            kua0=tui1;kua1=0
                        if dpn==1:
                            kua0=0;kua1=tui1
                        for ton1 in range(Nma[ssx][xn][1]):
                            if kinam[ssx][xn][1][ton1]==1 and kinbm[ssx][xn][1][ton1]==1:
                                dxnuma=numa[ssx][xn][1][ton1][0]-numa[ssx][xn][1][ton1][1]+kua0-kua1
                                for to2 in range(xn,MTnumber-1):
                                    dxnuma+=-overlap[0][ssx][2][to2]+overlap[1][ssx][2][to2]
                                F3[0]-=Kpn5*dxnuma
                                F3[1]+=Kpn5*dxnuma
                        for sik in range(2):
                            for ton1 in range(Nma1[sik][ssx][xn][0]):
                                if kinam1[sik][ssx][xn][0][ton1]==1 and kinbm1[sik][ssx][xn][0][ton1]==1:
                                    dxnuma1=numa1[sik][ssx][xn][0][ton1][0]-numa1[sik][ssx][xn][0][ton1][1]
                                    for to2 in range(xn,MTnumber-1):
                                        dxnuma1+=overlap[sik][ssx][0][to2]-overlap[sik][ssx][1][to2]
                                    F1[sik]+=Kpn5*dxnuma1
                                    F2[sik]-=Kpn5*dxnuma1
                            for ton1 in range(Nma1[sik][ssx][xn][1]):
                                if kinam1[sik][ssx][xn][1][ton1]==1 and kinbm1[sik][ssx][xn][1][ton1]==1:
                                    if dpn!=sik:
                                        dxnuma1=numa1[sik][ssx][xn][1][ton1][0]-numa1[sik][ssx][xn][1][ton1][1]
                                    if dpn==sik:
                                        dxnuma1=numa1[sik][ssx][xn][1][ton1][0]-numa1[sik][ssx][xn][1][ton1][1]+tui2-tui1
                                    for to2 in range(xn,MTnumber-1):
                                        dxnuma1+=-overlap[sik][ssx][3][to2]+overlap[sik][ssx][2][to2]
                                    F4[sik]-=Kpn5*dxnuma1
                                    F3[sik]+=Kpn5*dxnuma1

                Fcc=0
                for x2 in range(pair):
                    if abs(F1[x2])+abs(F2[x2])+abs(F3[x2])+abs(F4[x2])>0.01:
                        Fcc=1
                        break
                if Fcc==0 and abs(F0)<0.0001 and abs(F5)<0.00001 and abs(F6)<0.00001 and abs(F7)<0.00001:
                    de[2][dpn]+=tui1;de[4][dpn]+=tui2
                    for xxx in range(pair):
                        F1[xxx]=p1[xxx]
                        F2[xxx]=p2[xxx]
                        F3[xxx]=p3[xxx]
                        F4[xxx]=p4[xxx]
                    return de[0],de[1],de[2],de[3],de[4],de[5],de[6],de[7]

                jisuan1=[[] for i in range(pair)]
                jisuanp1=[[] for i in range(pair)]
                jisuanpx1=[[] for i in range(pair)]
                for x2 in range(pair):
                    if x2==dpn:
                        for ton1 in range(monum[x2]):
                            jisuan1[x2].append(jisuan[x2][ton1]-tui1)
                        for ton1 in range(monump[x2]):
                            jisuanp1[x2].append(jisuanp[x2][ton1]-tui1)
                        for ton1 in range(monumpx[x2]):
                            jisuanpx1[x2].append(jisuanpx[x2][ton1]+tui2)
                    if x2!=dpn:
                        for ton1 in range(monum[x2]):
                            jisuan1[x2].append(jisuan[x2][ton1])
                        for ton1 in range(monump[x2]):
                            jisuanp1[x2].append(jisuanp[x2][ton1])
                        for ton1 in range(monumpx[x2]):
                            jisuanpx1[x2].append(jisuanpx[x2][ton1])
                #print(jisuan1,jisuanp1,jisuanpx1,F0,F1,F2,F3,F4,F5,F6,F7,'cc2')
                tuf,de[0],de[1],de[2],de[3],de[4],de[5],de[6],de[7]=jiaocheck(jisuan1,jisuanp1,jisuanpx1,F0,F1,F2,F3,F4,F5,F6,F7)
                if tuf==1:
                    de[2][dpn]+=tui1
                    de[4][dpn]+=tui2
                    for xxx in range(pair):
                        F1[xxx]=p1[xxx]
                        F2[xxx]=p2[xxx]
                        F3[xxx]=p3[xxx]
                        F4[xxx]=p4[xxx]
                    return de[0],de[1],de[2],de[3],de[4],de[5],de[6],de[7]
                    break
    if dpn==0:
        kpn=1
    if dpn==1:
        kpn=0
    lastui1=-1000
    for xn in range(num1[dpn]+nump2[dpn]+num2[dpn]+nump1[dpn]+1):
        if xn < num1[dpn]:
            tui1=(jisuan[dpn][-num1[dpn]+xn]-xdmotor+0.1)
        if xn >= num1[dpn] and xn <num1[dpn]+nump2[dpn]:
            tui1=(jisuanp[dpn][nump2[dpn]-1-xn+num1[dpn]]+xdmotor-0.1)
        if xn >= num1[dpn]+nump2[dpn] and xn <num1[dpn]+nump2[dpn]+num2[dpn]:
            tui1=(jisuan[dpn][num2[dpn]-1-xn+num1[dpn]+nump2[dpn]]+xdmotor-0.1)
        if xn >= num1[dpn]+nump2[dpn]+num2[dpn] and xn <num1[dpn]+nump2[dpn]+num2[dpn]+nump1[dpn]:
            tui1=(jisuanp[dpn][monump[dpn]-nump1[dpn]+xn-num1[dpn]-nump2[dpn]-num2[dpn]]-xdmotor+0.1)
        if xn==num1[dpn]+nump2[dpn]+num2[dpn]+nump1[dpn]:
            tui1=0
        if abs(tui1-lastui1)<0.0001:
            continue
        lastui1=tui1
        lastui2=-1000
        for xn1 in range(numpx2[dpn]+numpx1[dpn]+1):#MT4
            if xn1 <numpx1[dpn]:
                tui2=(-jisuanpx[dpn][-numpx1[dpn]+xn1]+xdmotor-0.1)
            if xn1 >= numpx1[dpn] and xn1 <numpx1[dpn]+numpx2[dpn]:
                tui2=-(jisuanpx[dpn][numpx2[dpn]-1-xn1+numpx1[dpn]]+xdmotor-0.1)
            if xn1==numpx1[dpn]+numpx2[dpn]:
                tui2=0
            if abs(tui2-lastui2)<0.0001:
                continue
            lastui2=tui2
            lastui3=-1000
            for xn2 in range(num1[kpn]+nump2[kpn]+num2[kpn]+nump1[kpn]+1):
                if xn2 < num1[kpn]:
                    tui3=(jisuan[kpn][-num1[kpn]+xn2]-xdmotor+0.1)
                if xn2 >= num1[kpn] and xn2 <num1[kpn]+nump2[kpn]:
                    tui3=(jisuanp[kpn][nump2[kpn]-1-xn2+num1[kpn]]+xdmotor-0.1)
                if xn2 >= num1[kpn]+nump2[kpn] and xn2 <num1[kpn]+nump2[kpn]+num2[kpn]:
                    tui3=(jisuan[kpn][num2[kpn]-1-xn2+num1[kpn]+nump2[kpn]]+xdmotor-0.1)
                if xn2 >= num1[kpn]+nump2[kpn]+num2[kpn] and xn2 <num1[kpn]+nump2[kpn]+num2[kpn]+nump1[kpn]:
                    tui3=(jisuanp[kpn][monump[kpn]-nump1[kpn]+xn2-num1[kpn]-nump2[kpn]-num2[kpn]]-xdmotor+0.1)
                if xn2==num1[kpn]+nump2[kpn]+num2[kpn]+nump1[kpn]:
                    tui3=0
                if abs(tui3-lastui3)<0.0001:
                    continue
                lastui3=tui3
                lastui4=-1000
                for xn3 in range(numpx2[kpn]+numpx1[kpn]+1):#MT4
                    if xn3 <numpx1[kpn]:
                        tui4=(-jisuanpx[kpn][-numpx1[kpn]+xn3]+xdmotor-0.1)
                    if xn3 >= numpx1[kpn] and xn3 <numpx1[kpn]+numpx2[kpn]:
                        tui4=-(jisuanpx[kpn][numpx2[kpn]-1-xn3+numpx1[kpn]]+xdmotor-0.1)
                    if xn3==numpx1[kpn]+numpx2[kpn]:
                        tui4=0
                    if abs(tui4-lastui4)<0.0001 or abs(tui3)+abs(tui4)==0:
                        continue
                    lastui4=tui4
                    #print(tui1,tui2,tui3,tui4)
                    F0=-FPE
                    F7=FPE
                    F5=FPE
                    F6=-FPE
                    for x2 in range(pair):
                        if x2!=dpn and x2!=kpn:
                            F0+=Kp1*(l1l[x2]-Xpole)+Kp2*(l2l[x2]-Xpole)
                            F7+=Kp1*(l4r[x2]-Xpo)+Kp2*(l3r[x2]-Xpo)
                            F5+=Kp3*(l1r[x2]-Xkin)+Kp4*(Xkin1-Xkin-kdis)
                            F6+=Kp4*(Xkin-Xkin1+kdis)+Kp3*(l4l[x2]-Xkin1)
                            F3[x2]=Kp2*(Xpo-l3r[x2])
                            F1[x2]=Kp1*(l1l[x2]-Xpole)+Kp3*(l1r[x2]-Xkin)
                            F2[x2]=Kp2*(l2l[x2]-Xpole)
                            F4[x2]=Kp1*(Xpo-l4r[x2])+Kp3*(Xkin1-l4l[x2])
                            for ton1 in range(monum[x2]):
                                if jisuan[x2][ton1]>xdmotor:
                                    F3[x2]+=(jisuan[x2][ton1]-xdmotor)*Km
                                    F2[x2]+=(jisuan[x2][ton1]-xdmotor)*Km
                                if jisuan[x2][ton1]<-xdmotor:
                                    F3[x2]+=(jisuan[x2][ton1]+xdmotor)*Km
                                    F2[x2]+=(jisuan[x2][ton1]+xdmotor)*Km
                            for ton1 in range(monump[x2]):
                                if jisuanp[x2][ton1]>xdmotor:
                                    F3[x2]+=(jisuanp[x2][ton1]-xdmotor)*Km
                                    F1[x2]+=(jisuanp[x2][ton1]-xdmotor)*Km
                                if jisuanp[x2][ton1]<-xdmotor:
                                    F3[x2]+=(jisuanp[x2][ton1]+xdmotor)*Km
                                    F1[x2]+=(jisuanp[x2][ton1]+xdmotor)*Km
                            for ton1 in range(monumpx[x2]):
                                if jisuanpx[x2][ton1]>xdmotor:
                                    F4[x2]-=(jisuanpx[x2][ton1]-xdmotor)*Km
                                    F2[x2]-=(jisuanpx[x2][ton1]-xdmotor)*Km
                                if jisuanpx[x2][ton1]<-xdmotor:
                                    F4[x2]-=(jisuanpx[x2][ton1]+xdmotor)*Km
                                    F2[x2]-=(jisuanpx[x2][ton1]+xdmotor)*Km
                        if x2==dpn:
                            F0+=Kp1*(l1l[x2]-Xpole)+Kp2*(l2l[x2]-Xpole)
                            F7+=Kp1*(l4r[x2]+tui2-Xpo)+Kp2*(l3r[x2]+tui1-Xpo)
                            F5+=Kp3*(l1r[x2]-Xkin)+Kp4*(Xkin1-Xkin-kdis)
                            F6+=Kp4*(Xkin-Xkin1+kdis)+Kp3*(l4l[x2]+tui2-Xkin1)
                            F3[x2]=Kp2*(Xpo-l3r[x2]-tui1)
                            F1[x2]=Kp1*(l1l[x2]-Xpole)+Kp3*(l1r[x2]-Xkin)
                            F2[x2]=Kp2*(l2l[x2]-Xpole)
                            F4[x2]=Kp1*(Xpo-l4r[x2]-tui2)+Kp3*(Xkin1-l4l[x2]-tui2)
                            for ton1 in range(monum[x2]):
                                if jisuan[x2][ton1]-tui1>xdmotor:
                                    F3[x2]+=(jisuan[x2][ton1]-tui1-xdmotor)*Km
                                    F2[x2]+=(jisuan[x2][ton1]-tui1-xdmotor)*Km
                                if jisuan[x2][ton1]-tui1<-xdmotor:
                                    F3[x2]+=(jisuan[x2][ton1]-tui1+xdmotor)*Km
                                    F2[x2]+=(jisuan[x2][ton1]-tui1+xdmotor)*Km
                            for ton1 in range(monump[x2]):
                                if jisuanp[x2][ton1]-tui1>xdmotor:
                                    F3[x2]+=(jisuanp[x2][ton1]-tui1-xdmotor)*Km
                                    F1[x2]+=(jisuanp[x2][ton1]-tui1-xdmotor)*Km
                                if jisuanp[x2][ton1]-tui1<-xdmotor:
                                    F3[x2]+=(jisuanp[x2][ton1]-tui1+xdmotor)*Km
                                    F1[x2]+=(jisuanp[x2][ton1]-tui1+xdmotor)*Km
                            for ton1 in range(monumpx[x2]):
                                if jisuanpx[x2][ton1]+tui2>xdmotor:
                                    F4[x2]-=(jisuanpx[x2][ton1]+tui2-xdmotor)*Km
                                    F2[x2]-=(jisuanpx[x2][ton1]+tui2-xdmotor)*Km
                                if jisuanpx[x2][ton1]+tui2<-xdmotor:
                                    F4[x2]-=(jisuanpx[x2][ton1]+tui2+xdmotor)*Km
                                    F2[x2]-=(jisuanpx[x2][ton1]+tui2+xdmotor)*Km
                        if x2==kpn:
                            F0+=Kp1*(l1l[x2]-Xpole)+Kp2*(l2l[x2]-Xpole)
                            F7+=Kp1*(l4r[x2]+tui4-Xpo)+Kp2*(l3r[x2]+tui3-Xpo)
                            F5+=Kp3*(l1r[x2]-Xkin)+Kp4*(Xkin1-Xkin-kdis)
                            F6+=Kp4*(Xkin-Xkin1+kdis)+Kp3*(l4l[x2]+tui4-Xkin1)
                            F3[x2]=Kp2*(Xpo-l3r[x2]-tui3)
                            F1[x2]=Kp1*(l1l[x2]-Xpole)+Kp3*(l1r[x2]-Xkin)
                            F2[x2]=Kp2*(l2l[x2]-Xpole)
                            F4[x2]=Kp1*(Xpo-l4r[x2]-tui4)+Kp3*(Xkin1-l4l[x2]-tui4)
                            for ton1 in range(monum[x2]):
                                if jisuan[x2][ton1]-tui3>xdmotor:
                                    F3[x2]+=(jisuan[x2][ton1]-tui3-xdmotor)*Km
                                    F2[x2]+=(jisuan[x2][ton1]-tui3-xdmotor)*Km
                                if jisuan[x2][ton1]-tui3<-xdmotor:
                                    F3[x2]+=(jisuan[x2][ton1]-tui3+xdmotor)*Km
                                    F2[x2]+=(jisuan[x2][ton1]-tui3+xdmotor)*Km
                            for ton1 in range(monump[x2]):
                                if jisuanp[x2][ton1]-tui3>xdmotor:
                                    F3[x2]+=(jisuanp[x2][ton1]-tui3-xdmotor)*Km
                                    F1[x2]+=(jisuanp[x2][ton1]-tui3-xdmotor)*Km
                                if jisuanp[x2][ton1]-tui3<-xdmotor:
                                    F3[x2]+=(jisuanp[x2][ton1]-tui3+xdmotor)*Km
                                    F1[x2]+=(jisuanp[x2][ton1]-tui3+xdmotor)*Km
                            for ton1 in range(monumpx[x2]):
                                if jisuanpx[x2][ton1]+tui4>xdmotor:
                                    F4[x2]-=(jisuanpx[x2][ton1]+tui4-xdmotor)*Km
                                    F2[x2]-=(jisuanpx[x2][ton1]+tui4-xdmotor)*Km
                                if jisuanpx[x2][ton1]+tui4<-xdmotor:
                                    F4[x2]-=(jisuanpx[x2][ton1]+tui4+xdmotor)*Km
                                    F2[x2]-=(jisuanpx[x2][ton1]+tui4+xdmotor)*Km
                    for ssx in range(2):
                        for xn in range(MTnumber):
                           
                            for ton1 in range(Nma[ssx][xn][0]):
                                if kinam[ssx][xn][0][ton1]==1 and kinbm[ssx][xn][0][ton1]==1:
                                    dxnuma=numa[ssx][xn][0][ton1][0]-numa[ssx][xn][0][ton1][1]
                                    for to2 in range(xn,MTnumber-1):
                                        dxnuma+=overlap[0][ssx][1][to2]-overlap[1][ssx][1][to2]
                                    F2[0]+=Kpn5*dxnuma
                                    F2[1]-=Kpn5*dxnuma
                            if dpn==0:
                                kua0=tui1;kua1=tui3
                            if dpn==1:
                                kua0=tui3;kua1=tui1 
                            for ton1 in range(Nma[ssx][xn][1]):
                                if kinam[ssx][xn][1][ton1]==1 and kinbm[ssx][xn][1][ton1]==1:
                                    dxnuma=numa[ssx][xn][1][ton1][0]-numa[ssx][xn][1][ton1][1]+kua0-kua1
                                    for to2 in range(xn,MTnumber-1):
                                        dxnuma+=-overlap[0][ssx][2][to2]+overlap[1][ssx][2][to2]
                                    F3[0]-=Kpn5*dxnuma
                                    F3[1]+=Kpn5*dxnuma
                            for sik in range(2):
                                for ton1 in range(Nma1[sik][ssx][xn][0]):
                                    if kinam1[sik][ssx][xn][0][ton1]==1 and kinbm1[sik][ssx][xn][0][ton1]==1:
                                        dxnuma1=numa1[sik][ssx][xn][0][ton1][0]-numa1[sik][ssx][xn][0][ton1][1]
                                        for to2 in range(xn,MTnumber-1):
                                            dxnuma1+=overlap[sik][ssx][0][to2]-overlap[sik][ssx][1][to2]
                                        F1[sik]+=Kpn5*dxnuma1
                                        F2[sik]-=Kpn5*dxnuma1
                                for ton1 in range(Nma1[sik][ssx][xn][1]):
                                    if kinam1[sik][ssx][xn][1][ton1]==1 and kinbm1[sik][ssx][xn][1][ton1]==1:
                                        if dpn!=sik and kpn!=sik:
                                            dxnuma1=numa1[sik][ssx][xn][1][ton1][0]-numa1[sik][ssx][xn][1][ton1][1]
                                        if dpn==sik:
                                            dxnuma1=numa1[sik][ssx][xn][1][ton1][0]-numa1[sik][ssx][xn][1][ton1][1]+tui2-tui1
                                        if kpn==sik:
                                            dxnuma1=numa1[sik][ssx][xn][1][ton1][0]-numa1[sik][ssx][xn][1][ton1][1]+tui4-tui3
                                        for to2 in range(xn,MTnumber-1):
                                            dxnuma1+=-overlap[sik][ssx][3][to2]+overlap[sik][ssx][2][to2]
                                        F4[sik]-=Kpn5*dxnuma1
                                        F3[sik]+=Kpn5*dxnuma1
                   
    
                    Fcc=0
                    for x2 in range(pair):
                        if abs(F1[x2])+abs(F2[x2])+abs(F3[x2])+abs(F4[x2])>0.01:
                            Fcc=1
                            break
                    if Fcc==0 and abs(F0)<0.0001 and abs(F5)<0.00001 and abs(F6)<0.00001 and abs(F7)<0.00001:
                        de[2][dpn]+=tui1;de[4][dpn]+=tui2
                        de[2][kpn]+=tui3;de[4][kpn]+=tui4
                        for xxx in range(pair):
                            F1[xxx]=p1[xxx]
                            F2[xxx]=p2[xxx]
                            F3[xxx]=p3[xxx]
                            F4[xxx]=p4[xxx]
                        return de[0],de[1],de[2],de[3],de[4],de[5],de[6],de[7]

                    jisuan1=[[] for i in range(pair)]
                    jisuanp1=[[] for i in range(pair)]
                    jisuanpx1=[[] for i in range(pair)]
                    for x2 in range(pair):
                        if x2==dpn:
                            for ton1 in range(monum[x2]):
                                jisuan1[x2].append(jisuan[x2][ton1]-tui1)
                            for ton1 in range(monump[x2]):
                                jisuanp1[x2].append(jisuanp[x2][ton1]-tui1)
                            for ton1 in range(monumpx[x2]):
                                jisuanpx1[x2].append(jisuanpx[x2][ton1]+tui2)
                        if x2==kpn:
                            for ton1 in range(monum[x2]):
                                jisuan1[x2].append(jisuan[x2][ton1]-tui3)
                            for ton1 in range(monump[x2]):
                                jisuanp1[x2].append(jisuanp[x2][ton1]-tui3)
                            for ton1 in range(monumpx[x2]):
                                jisuanpx1[x2].append(jisuanpx[x2][ton1]+tui4)
                        if x2!=dpn and x2!=kpn:
                            for ton1 in range(monum[x2]):
                                jisuan1[x2].append(jisuan[x2][ton1])
                            for ton1 in range(monump[x2]):
                                jisuanp1[x2].append(jisuanp[x2][ton1])
                            for ton1 in range(monumpx[x2]):
                                jisuanpx1[x2].append(jisuanpx[x2][ton1])
                    #print(jisuan1,jisuanp1,jisuanpx1,F0,F1,F2,F3,F4,F5,F6,F7,'dd')
                    tuf,de[0],de[1],de[2],de[3],de[4],de[5],de[6],de[7]=jiaocheck(jisuan1,jisuanp1,jisuanpx1,F0,F1,F2,F3,F4,F5,F6,F7)
                    if tuf==1:
                        de[2][dpn]+=tui1
                        de[4][dpn]+=tui2
                        de[2][kpn]+=tui3;de[4][kpn]+=tui4
                        for xxx in range(pair):
                            F1[xxx]=p1[xxx]
                            F2[xxx]=p2[xxx]
                            F3[xxx]=p3[xxx]
                            F4[xxx]=p4[xxx]
                        return de[0],de[1],de[2],de[3],de[4],de[5],de[6],de[7]
    return de[0],de[1],de[2],de[3],de[4],de[5],de[6],de[7]


# In[5]:


def gaussian_elimination(A, b):
    #print(A,b)
    n = len(A)
 
  
    A = A.astype(np.float64)
    b = b.astype(np.float64)
    #print(A,b)
  
    for i in range(n - 1):
        max_idx = i
 
        for j in range(i + 1, n):
            if abs(A[j][i]) > abs(A[max_idx][i]):
                max_idx = j

        A[[i, max_idx]] = A[[max_idx, i]]
        b[[i, max_idx]] = b[[max_idx, i]]
 
        for j in range(i + 1, n):
            #
            multiplier = A[j][i] / A[i][i]
 
            # 
            A[j][i:] -= multiplier * A[i][i:]
            b[j] -= multiplier * b[i]
 
    
    #print(A,b)
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        if A[i][i]!=0 and abs(A[i][i])>1e-12:
            x[i] = (b[i] - np.dot(A[i][i + 1:], x[i + 1:])) / A[i][i]
 
    return x


# In[6]:


def jiaocheck(jisuan,jisuanp,jisuanpx,F0,F1,F2,F3,F4,F5,F6,F7):
    num3=[0 for i in range(pair)]
    num4=[0 for i in range(pair)]
    nump3=[0 for i in range(pair)]
    nump4=[0 for i in range(pair)]
    numpx3=[0 for i in range(pair)]
    numpx4=[0 for i in range(pair)]
    ji=[[] for i in range(pair)]
    fen0=[[] for i in range(pair)]
    fen1=[[] for i in range(pair)]
    fen2=[[] for i in range(pair)]
    fenp0=[[] for i in range(pair)]
    fenp1=[[] for i in range(pair)]
    fenp2=[[] for i in range(pair)]
    fenpx0=[[] for i in range(pair)]
    fenpx1=[[] for i in range(pair)]
    fenpx2=[[] for i in range(pair)]
    for x2 in range(pair):
        for ton1 in range(monum[x2]):
            if jisuan[x2][ton1]>xdmotor:
                num3[x2]+=1
            if jisuan[x2][ton1]<-xdmotor:
                num4[x2]+=1
        for ton1 in range(monump[x2]):
            if jisuanp[x2][ton1]>xdmotor:
                nump3[x2]+=1
            if jisuanp[x2][ton1]<-xdmotor:
                nump4[x2]+=1
        for ton1 in range(monumpx[x2]):
            if jisuanpx[x2][ton1]>xdmotor:
                numpx3[x2]+=1
            if jisuanpx[x2][ton1]<-xdmotor:
                numpx4[x2]+=1
        m1=[monum[x2]-num3[x2]]
        m0=[num4[x2]]
        m2=[0]
        if monum[x2]>0:
            ttt=jisuan[x2][0]
            for tt1 in range(monum[x2]):
                if abs(jisuan[x2][tt1]-ttt)>0.0001:
                    if jisuan[x2][tt1]<-xdmotor:
                        m2.append(tt1)
                    if jisuan[x2][tt1]>=-xdmotor and ttt<xdmotor:
                        m0.append(tt1)
                    if jisuan[x2][tt1]>xdmotor:
                        m1.append(tt1)
                    ttt=jisuan[x2][tt1]
            m2.append(num4[x2])
            m0.append(monum[x2]-num3[x2])
            m1.append(monum[x2])
        fen2[x2]=list(set(m2))
        fen1[x2]=list(set(m1))
        fen0[x2]=list(set(m0))
        fen2[x2].sort(key=m2.index)
        fen1[x2].sort(key=m1.index)
        fen0[x2].sort(key=m0.index)

        m1=[monump[x2]-nump3[x2]]
        m0=[nump4[x2]]
        m2=[0]
        if monump[x2]>0:
            ttt=jisuanp[x2][0]
            for tt1 in range(monump[x2]):
                if abs(jisuanp[x2][tt1]-ttt)>0.0001:
                    if jisuanp[x2][tt1]<-xdmotor:
                        m2.append(tt1)
                    if jisuanp[x2][tt1]>=-xdmotor and ttt<xdmotor:
                        m0.append(tt1)
                    if jisuanp[x2][tt1]>xdmotor:
                        m1.append(tt1)
                    ttt=jisuanp[x2][tt1]
            m2.append(nump4[x2])
            m0.append(monump[x2]-nump3[x2])
            m1.append(monump[x2])
        fenp2[x2]=list(set(m2))
        fenp1[x2]=list(set(m1))
        fenp0[x2]=list(set(m0))
        fenp2[x2].sort(key=m2.index)
        fenp1[x2].sort(key=m1.index)
        fenp0[x2].sort(key=m0.index)

        m1=[monumpx[x2]-numpx3[x2]]
        m0=[numpx4[x2]]
        m2=[0]
        if monumpx[x2]>0:
            ttt=jisuanpx[x2][0]
            for tt1 in range(monumpx[x2]):
                if abs(jisuanpx[x2][tt1]-ttt)>0.0001:
                    if jisuanpx[x2][tt1]<-xdmotor:
                        m2.append(tt1)
                    if jisuanpx[x2][tt1]>=-xdmotor and ttt<xdmotor:
                        m0.append(tt1)
                    if jisuanpx[x2][tt1]>xdmotor:
                        m1.append(tt1)
                    ttt=jisuanpx[x2][tt1]
            m2.append(numpx4[x2])
            m0.append(monumpx[x2]-numpx3[x2])
            m1.append(monumpx[x2])
        fenpx2[x2]=list(set(m2))
        fenpx1[x2]=list(set(m1))
        fenpx0[x2]=list(set(m0))
        fenpx2[x2].sort(key=m2.index)
        fenpx1[x2].sort(key=m1.index)
        fenpx0[x2].sort(key=m0.index)
    #########################################dzk,dz0
    dzk=[[[0 for xxn2 in range(len(fen0[0]))] for xxn1 in range(2)]]
    dz0=[[[0 for xxn2 in range(len(fen2[0]))],[0 for xxn1 in range(len(fen1[0]))]]]
    dzkp=[[[0 for xxn2 in range(len(fenp0[0]))] for xxn1 in range(2)]]
    dz0p=[[[0 for xxn2 in range(len(fenp1[0]))],[0 for xxn1 in range(len(fenp2[0]))]]]
    dzkpx=[[[0 for xxn2 in range(len(fenpx0[0]))] for xxn1 in range(2)]]
    dz0px=[[[0 for xxn2 in range(len(fenpx1[0]))],[0 for xxn1 in range(len(fenpx2[0]))]]]
    for x3 in range(1,pair):
        dzk.append([[0 for xxn2 in range(len(fen0[x3]))] for xxn1 in range(2)])
        dz0.append([[0 for xxn2 in range(len(fen2[x3]))],[0 for xxn1 in range(len(fen1[x3]))]])
        dzkp.append([[0 for xxn2 in range(len(fenp0[x3]))] for xxn1 in range(2)])
        dz0p.append([[0 for xxn2 in range(len(fenp1[x3]))],[0 for xxn1 in range(len(fenp2[x3]))]])
        dzkpx.append([[0 for xxn2 in range(len(fenpx0[x3]))] for xxn1 in range(2)])
        dz0px.append([[0 for xxn2 in range(len(fenpx1[x3]))],[0 for xxn1 in range(len(fenpx2[x3]))]])
    for x2 in range(pair):
        ta1=-1
        for xck in fen0[x2]:
            ta1+=1
            cnnk=monum[x2]-num3[x2]-fen0[x2][-ta1-1]
            chek=monum[x2]-num3[x2]-1
            for xxxn in range(cnnk):
                dzk[x2][0][ta1]+=jisuan[x2][chek-xxxn]-xdmotor
        ta1=-1
        for xck in fen0[x2]:
            ta1+=1
            cnnk=xck-num4[x2]
            chek=num4[x2]
            for xxxn in range(cnnk):
                dzk[x2][1][ta1]+=jisuan[x2][chek+xxxn]+xdmotor 
        ta2=-1
        for xckp in fenp0[x2]:
            ta2+=1
            cnnkp=xckp-nump4[x2]
            chekp=nump4[x2]
            for xxxn in range(cnnkp):
                dzkp[x2][0][ta2]+=jisuanp[x2][chekp+xxxn]+xdmotor
        ta2=-1
        for xckp in fenp0[x2]:
            ta2+=1
            cnnkp=monump[x2]-nump3[x2]-fenp0[x2][-ta2-1]
            chekp=monump[x2]-nump3[x2]-1 
            for xxxn in range(cnnkp):
                dzkp[x2][1][ta2]+=jisuanp[x2][chekp-xxxn]-xdmotor 
        ta2=-1
        for xckpx in fenpx0[x2]:
            ta2+=1
            cnnkpx=xckpx-numpx4[x2]
            chekpx=numpx4[x2]
            for xxxn in range(cnnkpx):
                dzkpx[x2][0][ta2]+=jisuanpx[x2][chekpx+xxxn]+xdmotor
        ta2=-1
        for xckpx in fenpx0[x2]:
            ta2+=1
            cnnkpx=monumpx[x2]-numpx3[x2]-fenpx0[x2][-ta2-1]
            chekpx=monumpx[x2]-numpx3[x2]-1 
            for xxxn in range(cnnkpx):
                dzkpx[x2][1][ta2]+=jisuanpx[x2][chekpx-xxxn]-xdmotor 
        ta3=-1
        for xc0 in fen2[x2]:
            ta3+=1
            cnn0=num4[x2]-fen2[x2][-ta3-1]
            che0=num4[x2]-1
            for xxxn in range(cnn0):
                dz0[x2][0][ta3]+=jisuan[x2][che0-xxxn]+xdmotor
        ta3=-1
        for xc0 in fen1[x2]:    
            ta3+=1
            cnn0=xc0-monum[x2]+num3[x2]
            che0=monum[x2]-num3[x2]
            for xxxn in range(cnn0):
                dz0[x2][1][ta3]+=jisuan[x2][che0+xxxn]-xdmotor
        ta4=-1
        for xc0p in fenp1[x2]:
            ta4+=1
            cnn0p=xc0p-monump[x2]+nump3[x2]
            che0p=monump[x2]-nump3[x2]
            for xxxn in range(cnn0p):
                dz0p[x2][0][ta4]+=jisuanp[x2][che0p+xxxn]-xdmotor
        ta4=-1
        for xc0p in fenp2[x2]:
            ta4+=1
            cnn0p=nump4[x2]-fenp2[x2][-ta4-1]
            che0p=nump4[x2]-1
            for xxxn in range(cnn0p):
                dz0p[x2][1][ta4]+=jisuanp[x2][che0p-xxxn]+xdmotor
        ta4=-1
        for xc0px in fenpx1[x2]:
            ta4+=1
            cnn0px=xc0px-monumpx[x2]+numpx3[x2]
            che0px=monumpx[x2]-numpx3[x2]
            for xxxn in range(cnn0px):
                dz0px[x2][0][ta4]+=jisuanpx[x2][che0px+xxxn]-xdmotor
        ta4=-1
        for xc0px in fenpx2[x2]:
            ta4+=1
            cnn0px=numpx4[x2]-fenpx2[x2][-ta4-1]
            che0px=numpx4[x2]-1
            for xxxn in range(cnn0px):
                dz0px[x2][1][ta4]+=jisuanpx[x2][che0px-xxxn]+xdmotor
   
    #print(round(F0),round(F1,2),round(F2,2),round(F3,2),round(F4,2),round(F5,2),round(F6,2),round(F7,2))
    for x2 in range(pair):
        for xx1 in range(2):
            ta1=-1
            for xck in fen0[x2]:
                ta1+=1
                if xx1==0: 
                    if ta1<len(dzk[x2][0]):
                        cnnk=monum[x2]-num3[x2]-fen0[x2][-ta1-1]
                    if ta1>=len(dzk[x2][0]):
                        break
                if xx1==1:
                    if ta1<len(dzk[x2][1]):
                        cnnk=xck-num4[x2]
                    if ta1>=len(dzk[x2][1]):
                        break
                for xx2 in range(2):
                    ta2=-1
                    for xckp in fenp0[x2]:
                        ta2+=1
                        if xx2==0:
                            if ta2<len(dzkp[x2][0]):
                                cnnkp=xckp-nump4[x2]
                            if ta2>=len(dzkp[x2][0]):
                                break
                        if xx2==1:
                            if ta2<len(dzkp[x2][1]):
                                cnnkp=monump[x2]-nump3[x2]-fenp0[x2][-ta2-1]
                            if ta2>=len(dzkp[x2][1]):
                                break
                        for xx3 in range(2):
                            ta5=-1
                            for xckpx in fenpx0[x2]:    
                                ta5+=1
                                if xx3==0:
                                    if ta5<len(dzkpx[x2][0]):
                                        cnnkpx=xckpx-numpx4[x2]
                                    if ta5>=len(dzkpx[x2][0]):
                                        break
                                if xx3==1:
                                    if ta5<len(dzkpx[x2][1]):
                                        cnnkpx=monumpx[x2]-numpx3[x2]-fenpx0[x2][-ta5-1]
                                    if ta5>=len(dzkpx[x2][1]):
                                        break
                                if xx1==0:
                                    xa3=fen2[x2]
                                if xx1==1:
                                    xa3=fen1[x2]
                                ta3=-1
                                for xc0 in xa3:
                                    #print(xqq,xc0,len(dz0[xqq][1]),len(dz0[xqq][0]),'3')
                                    ta3+=1  
                                    if xx1==0:
                                        if ta3<len(dz0[x2][0]):
                                            cnn0=num4[x2]-fen2[x2][-ta3-1]
                                        if ta3>=len(dz0[x2][0]):
                                            break
                                    if xx1==1:
                                        if ta3<len(dz0[x2][1]):
                                            cnn0=xc0-monum[x2]+num3[x2]
                                        if ta3>=len(dz0[x2][1]):
                                            break
                                    if xx2==0:
                                        xa4=fenp1[x2]
                                    if xx2==1:
                                        xa4=fenp2[x2]
                                    ta4=-1
                                    for xc0p in xa4:
                                        ta4+=1
                                        if xx2==0:
                                            if ta4<len(dz0p[x2][0]):
                                                cnn0p=xc0p-monump[x2]+nump3[x2]
                                            if ta4>=len(dz0p[x2][0]):
                                                break
                                        if xx2==1:
                                            if ta4<len(dz0p[x2][1]):
                                                cnn0p=nump4[x2]-fenp2[x2][-ta4-1]    
                                        if xx3==0:
                                            xa5=fenpx1[x2]
                                        if xx3==1:
                                            xa5=fenpx2[x2]
                                        ta6=-1
                                        for xc0px in xa5:
                                            ta6+=1
                                            if xx3==0:
                                                if ta6<len(dz0px[x2][0]):
                                                    cnn0px=xc0px-monumpx[x2]+numpx3[x2]
                                                if ta6>=len(dz0px[x2][0]):
                                                    break
                                            if xx3==1:
                                                if ta6<len(dz0px[x2][1]):
                                                    cnn0px=numpx4[x2]-fenpx2[x2][-ta6-1] 
                                                if ta6>len(dz0px[x2][1]):
                                                    break
                                            if cnn0+cnnk==0 and xx1!=0:
                                                continue
                                            if cnn0p+cnnkp==0 and xx2!=0:
                                                continue
                                            if cnn0px+cnnkpx==0 and xx3!=0:
                                                continue    
                                            """if cnn0+cnnk!=0:
                                                if xx1==0  and xx3==0 and F2[x2]>0.00001 and abs(F1[x2])<0.00001:
                                                    continue
                                                if xx1==1 and xx3==1 and F2[x2]<-0.00001 and abs(F1[x2])<0.00001:
                                                    continue
                                            if cnn0p+cnnkp!=0:
                                                if xx2==1 and F1[x2]>0.00001 and F3[x2]>=-0.00001:#dxcp增
                                                    continue
                                                if xx2==0 and F1[x2]<-0.00001 and F3[x2]<=0.00001:#dxcp减
                                                    continue
                                            if cnn0px+cnnkpx!=0:
                                                if xx3==0 and F4[x2]>0.00001 and F2[x2]>=-0.00001:#dxcpx减
                                                    continue
                                                if xx3==1 and F4[x2]<-0.00001 and F2[x2]<=0.00001:#dxcp增
                                                    continue"""
                                            ji[x2].append([cnn0,cnnk,cnn0p,cnnkp,cnn0px,cnnkpx,xx1,xx2,xx3,ta1,ta2,ta3,ta4,ta5,ta6])
    a00=round(2*(-Kp1-Kp2),3);a10=Kp2;a30=Kp1;a80=Kp2;a100=Kp1
    a21=Kp2;a41=Kp1;a71=round((-Kp1-Kp2)*2,3);a91=Kp2;a111a=Kp1
    a32=Kp3;a52=round((-Kp3-Kp4)*2,3);a62=round(Kp4*2,3);a102=Kp3
    a43=Kp3;a53=round(Kp4*2,3);a63=round((-Kp3-Kp4 )*2,3);a113=Kp3
    zq=[0 for i in range(pair)]
    cxx=[0 for i in range(pair)]
    for cx0 in range(len(ji[0])):
        cxx[0]=cx0
        if abs(sum(zq)-pair)<0.01:
            break
        for cx1 in range(len(ji[1])):
            cxx[1]=cx1
            if abs(sum(zq)-pair)<0.01:
                break

            cnn0=ji[0][cxx[0]][0]
            cnnk=ji[0][cxx[0]][1]
            cnn0p=ji[0][cxx[0]][2]
            cnnkp=ji[0][cxx[0]][3]
            cnn0px=ji[0][cxx[0]][4]
            cnnkpx=ji[0][cxx[0]][5]
            xx1=ji[0][cxx[0]][6]
            xx2=ji[0][cxx[0]][7]
            xx3=ji[0][cxx[0]][8]
            ta1=ji[0][cxx[0]][9]
            ta2=ji[0][cxx[0]][10]
            ta3=ji[0][cxx[0]][11]
            ta4=ji[0][cxx[0]][12]
            ta5=ji[0][cxx[0]][13]
            ta6=ji[0][cxx[0]][14]

            
            a04=-Kp1;a24=round(-(nump3[0]+nump4[0]+cnnkp-cnn0p)*Km,3);a34=round((nump3[0]+nump4[0]+cnnkp-cnn0p)*Km+Kp1+Kp3+Kpn5*nunum1[0][0],3)
            a54=-Kp3;a0104=round(-Kpn5*nunum1[0][0],3)
            a05=-Kp2;a15=round(((numpx3[0]+numpx4[0]+cnnkpx-cnn0px)+(num3[0]+num4[0]+cnnk-cnn0))*Km+Kp2+Kpn5*nunum[0]+Kpn5*nunum1[0][0],3);a85=round(-Kpn5*nunum[0],3)
            a25=round(-Km*(num3[0]+num4[0]+cnnk-cnn0),3);a35=round(-Kpn5*nunum1[0][0],3);a45=round(-(numpx3[0]+numpx4[0]+cnnkpx-cnn0px)*Km,3)
            a16=round((num3[0]+num4[0]+cnnk-cnn0)*Km,3);a26=round(-Km*(nump3[0]+nump4[0]+cnnkp-cnn0p+num3[0]+num4[0]+cnnk-cnn0)-Kp2-Kpn5*nunum[1]-Kpn5*nunum1[0][1],3)
            a36=round(Km*(nump3[0]+nump4[0]+cnnkp-cnn0p),3);a76=Kp2;a96=round(Kpn5*nunum[1],3);a46=round(Kpn5*nunum1[0][1],3)
            a17=round(Km*(numpx3[0]+numpx4[0]+cnnkpx-cnn0px),3);a47=round(-Km*(numpx3[0]+numpx4[0]+cnnkpx-cnn0px)-Kp1-Kp3-Kpn5*nunum1[0][1],3)
            a67=Kp3;a77=Kp1;a27=round(Kpn5*nunum1[0][1],3)
            b4=-Km*(dzkp[0][xx2][ta2]-dz0p[0][xx2][ta4])-F1[0]
            b5=-Km*(-dzkpx[0][xx3][ta5]+dz0px[0][xx3][ta6]+dzk[0][xx1][ta1]-dz0[0][xx1][ta3])-F2[0]
            b6=-Km*(dzkp[0][xx2][ta2]-dz0p[0][xx2][ta4]+dzk[0][xx1][ta1]-dz0[0][xx1][ta3])-F3[0]
            b7=Km*(dzkpx[0][xx3][ta5]-dz0px[0][xx3][ta6])-F4[0]
            cnn0=ji[1][cxx[1]][0]
            cnnk=ji[1][cxx[1]][1]
            cnn0p=ji[1][cxx[1]][2]
            cnnkp=ji[1][cxx[1]][3]
            cnn0px=ji[1][cxx[1]][4]
            cnnkpx=ji[1][cxx[1]][5]
            xx1=ji[1][cxx[1]][6]
            xx2=ji[1][cxx[1]][7]
            xx3=ji[1][cxx[1]][8]
            ta1=ji[1][cxx[1]][9]
            ta2=ji[1][cxx[1]][10]
            ta3=ji[1][cxx[1]][11]
            ta4=ji[1][cxx[1]][12]
            ta5=ji[1][cxx[1]][13]
            ta6=ji[1][cxx[1]][14]
            
            
            a08=-Kp1;a28=round(-(nump3[1]+nump4[1]+cnnkp-cnn0p)*Km,3);a38=round((nump3[1]+nump4[1]+cnnkp-cnn0p)*Km+Kp1+Kp3+Kpn5*nunum1[1][0],3)
            a58=-Kp3;a88=-round(Kpn5*nunum1[1][0],3)
            a09=-Kp2;a19=round(((numpx3[1]+numpx4[1]+cnnkpx-cnn0px)+(num3[1]+num4[1]+cnnk-cnn0))*Km+Kp2+Kpn5*nunum[0]+Kpn5*nunum1[1][0],3);a019=round(-Kpn5*nunum[0],3)
            a29=round(-Km*(num3[1]+num4[1]+cnnk-cnn0),3);a49=round(-(numpx3[1]+numpx4[1]+cnnkpx-cnn0px)*Km,3);a109=-round(Kpn5*nunum1[1][0],3)
            a110=round((num3[1]+num4[1]+cnnk-cnn0)*Km,3);a210=round(-Km*(nump3[1]+nump4[1]+cnnkp-cnn0p+num3[1]+num4[1]+cnnk-cnn0)-Kp2-Kpn5*nunum[1]-Kpn5*nunum1[1][1],3)
            a310=round(Km*(nump3[1]+nump4[1]+cnnkp-cnn0p),3);a710=Kp2;a0210=round(Kpn5*nunum[1],3);a1110=round(Kpn5*nunum1[1][1],3)
            a111=round(Km*(numpx3[1]+numpx4[1]+cnnkpx-cnn0px),3);a411=round(-Km*(numpx3[1]+numpx4[1]+cnnkpx-cnn0px)-Kp1-Kp3-Kpn5*nunum1[1][1],3)
            a611=Kp3;a711=Kp1;a911=round(Kpn5*nunum1[1][1],3)
            b8=-Km*(dzkp[1][xx2][ta2]-dz0p[1][xx2][ta4])-F1[1]
            b9=-Km*(-dzkpx[1][xx3][ta5]+dz0px[1][xx3][ta6]+dzk[1][xx1][ta1]-dz0[1][xx1][ta3])-F2[1]
            b10=-Km*(dzkp[1][xx2][ta2]-dz0p[1][xx2][ta4]+dzk[1][xx1][ta1]-dz0[1][xx1][ta3])-F3[1]
            b11=Km*(dzkpx[1][xx3][ta5]-dz0px[1][xx3][ta6])-F4[1] 

            b=np.array([round(-F0,14),round(-F7,14),round(-F5,14),round(-F6,14),round(b4,14),round(b5,14),round(b6,14),round(b7,14),round(b8,14),round(b9,14),round(b10,14),round(b11,14)])
            try:
                A=np.array([[a00,a10,0,a30,0,0,0,0,a80,0,a100,0],[0,0,a21,0,a41,0,0,a71,0,a91,0,a111a],
                             [0,0,0,a32,0,a52,a62,0,0,0,a102,0],[0,0,0,0,a43,a53,a63,0,0,0,0,a113],
                             [a04,a0104,a24,a34,0,a54,0,0,0,0,0,0],[a05,a15,a25,a35,a45,0,0,0,a85,0,0,0],
                             [0,a16,a26,a36,a46,0,0,a76,0,a96,0,0],[0,a17,a27,0,a47,0,a67,a77,0,0,0,0],
                             [a08,0,0,0,0,a58,0,0,a88,a28,a38,0],[a09,a019,0,0,0,0,0,0,a19,a29,a109,a49],
                             [0,0,a0210,0,0,0,0,a710,a110,a210,a310,a1110],[0,0,0,0,0,0,a611,a711,a111,a911,0,a411]])
                
                #b=np.array([-F0,-F7,-F5,-F6,b4,b5,b6,b7])

                mtui=np.linalg.solve(A,b)

            except:
                #print(A,b)
                mtui = gaussian_elimination(A,b)
                
                #mtui = np.linalg.pinv(A) @ b
            tuzx=(mtui[0]+mtui[7])/2
            for xn in range(12):
                mtui[xn]-=tuzx
            de=[mtui[0],[mtui[1],mtui[8]],[mtui[2],mtui[9]],[mtui[3],mtui[10]],[mtui[4],mtui[11]],mtui[5],mtui[6],mtui[7]]
            #print(de)
            chezq=0
            for x3 in range(pair):
                check0=-1#################由K到0
                checkk=-1################由0到K
                checkp0=-1#################由K到0
                checkpk=-1#################由0到K
                checkpx0=-1#################由K到0
                checkpxk=-1#################由0到K
                cnn0=ji[x3][cxx[x3]][0]
                cnnk=ji[x3][cxx[x3]][1]
                cnn0p=ji[x3][cxx[x3]][2]
                cnnkp=ji[x3][cxx[x3]][3]
                cnn0px=ji[x3][cxx[x3]][4]
                cnnkpx=ji[x3][cxx[x3]][5]
                xx1=ji[x3][cxx[x3]][6]
                xx2=ji[x3][cxx[x3]][7]
                xx3=ji[x3][cxx[x3]][8]
                #print(chezq)
                if cnn0+cnnk==0:
                    for ton1 in range(monum[x3]):
                        if abs(jisuan[x3][ton1])<=xdmotor and abs(jisuan[x3][ton1]+de[1][x3]-de[2][x3])>xdmotor:
                            chezq=-1
                            break
                        if abs(jisuan[x3][ton1])>xdmotor and abs(jisuan[x3][ton1]+de[1][x3]-de[2][x3])<=xdmotor:
                            chezq=-1
                            break
                #print(chezq)
                if cnn0+cnnk!=0:    
                    if xx1==0 and de[1][x3]-de[2][x3]>=0:
                        check0=0################
                        checkk=0#################
                        for ton1 in range(monum[x3]):
                            if jisuan[x3][ton1]<-xdmotor and abs(jisuan[x3][ton1]+de[1][x3]-de[2][x3])<=xdmotor:
                                check0+=1
                            if abs(jisuan[x3][ton1])<=xdmotor and jisuan[x3][ton1]+de[1][x3]-de[2][x3]>xdmotor:
                                checkk+=1
                    if xx1==1 and de[1][x3]-de[2][x3]<=0:
                        check0=0################
                        checkk=0##############
                        for ton1 in range(monum[x3]):
                            if abs(jisuan[x3][ton1])<=xdmotor and jisuan[x3][ton1]+de[1][x3]-de[2][x3]<-xdmotor:
                                checkk+=1
                            if jisuan[x3][ton1]>xdmotor and abs(jisuan[x3][ton1]+de[1][x3]-de[2][x3])<=xdmotor:
                                check0+=1
                    if check0!=cnn0 or checkk!=cnnk:
                        chezq=-1
                        break
                #print(chezq)
                if chezq==-1:
                    #print(x3)
                    break
                if cnn0p+cnnkp==0:
                    for ton1 in range(monump[x3]):
                        if abs(jisuanp[x3][ton1])<=xdmotor and abs(jisuanp[x3][ton1]+de[3][x3]-de[2][x3])>xdmotor:
                            chezq=-1
                            break
                        if abs(jisuanp[x3][ton1])>xdmotor and abs(jisuanp[x3][ton1]+de[3][x3]-de[2][x3])<=xdmotor:
                            chezq=-1
                            break
                #print(chezq)
                if cnn0p+cnnkp!=0:
                    if xx2==1 and de[3][x3]-de[2][x3]>=0:
                        checkp0=0#################
                        checkpk=0#################
                        for ton1 in range(monump[x3]):
                            if jisuanp[x3][ton1]<-xdmotor and abs(jisuanp[x3][ton1]+de[3][x3]-de[2][x3])<=xdmotor:
                                checkp0+=1
                            if abs(jisuanp[x3][ton1])<=xdmotor and jisuanp[x3][ton1]+de[3][x3]-de[2][x3]>xdmotor:
                                checkpk+=1
                    if xx2==0 and de[3][x3]-de[2][x3]<=0:
                        checkp0=0
                        checkpk=0
                        for ton1 in range(monump[x3]):
                            if abs(jisuanp[x3][ton1])<=xdmotor and jisuanp[x3][ton1]+de[3][x3]-de[2][x3]<-xdmotor:
                                checkpk+=1
                            if jisuanp[x3][ton1]>xdmotor and abs(jisuanp[x3][ton1]+de[3][x3]-de[2][x3])<=xdmotor:
                                checkp0+=1
                    if checkp0!=cnn0p or checkpk!=cnnkp:
                        chezq=-1
                        break
                #print(chezq)
                if chezq==-1:
                    #print(x3,'p')
                    break
                if cnn0px+cnnkpx==0:
                    for ton1 in range(monumpx[x3]):
                        if abs(jisuanpx[x3][ton1])<=xdmotor and abs(jisuanpx[x3][ton1]+de[4][x3]-de[1][x3])>xdmotor:
                            chezq=-1
                            break
                        if abs(jisuanpx[x3][ton1])>xdmotor and abs(jisuanpx[x3][ton1]+de[4][x3]-de[1][x3])<=xdmotor:
                            chezq=-1
                            break
                #print(chezq)
                if cnn0px+cnnkpx!=0:
                    if xx3==1 and de[4][x3]-de[1][x3]>=0:
                        checkpx0=0#################
                        checkpxk=0#################
                        for ton1 in range(monumpx[x3]):
                            if jisuanpx[x3][ton1]<-xdmotor and abs(jisuanpx[x3][ton1]+de[4][x3]-de[1][x3])<=xdmotor:
                                checkpx0+=1
                            if abs(jisuanpx[x3][ton1])<=xdmotor and jisuanpx[x3][ton1]+de[4][x3]-de[1][x3]>xdmotor:
                                checkpxk+=1
                    if xx3==0 and de[4][x3]-de[1][x3]<=0:
                        checkpx0=0#################
                        checkpxk=0#################
                        for ton1 in range(monumpx[x3]):
                            if abs(jisuanpx[x3][ton1])<=xdmotor and jisuanpx[x3][ton1]+de[4][x3]-de[1][x3]<-xdmotor:
                                checkpxk+=1
                            if jisuanpx[x3][ton1]>xdmotor and abs(jisuanpx[x3][ton1]+de[4][x3]-de[1][x3])<=xdmotor:
                                checkpx0+=1
                    if checkpx0!=cnn0px or checkpxk!=cnnkpx:
                        chezq=-1
                        break

                if chezq==-1:
                    break
            if chezq==-1:
                continue
            return 1,de[0],de[1],de[2],de[3],de[4],de[5],de[6],de[7]
    return 0,de[0],de[1],de[2],de[3],de[4],de[5],de[6],de[7]


# In[7]:


def energy(x1,i):
    ypsl11=0
    ypsl22=0
    for x2 in range(pair):
        ypsl11+=Kp3*(((Xkin+zj5[x1][i]-l1r[x2]-zj3[x1][i][x2])**2+(Xkin1+zj6[x1][i]-l4l[x2]-zj4[x1][i][x2])**2)/2)+Kp2*((Xpole+zj0[x1][i]-l2l[x2]-zj1[x1][i][x2])**2+(Xpo+zj7[x1][i]-l3r[x2]-zj2[x1][i][x2])**2)/2+Kp1*((Xpole+zj0[x1][i]-l1l[x2]-zj3[x1][i][x2])**2+(Xpo+zj7[x1][i]-l4r[x2]-zj4[x1][i][x2])**2)/2+Kp4*((Xkin1+zj6[x1][i]-Xkin-zj5[x1][i]-kdis)**2)/2
        ypsl22+=Kp3*(((Xkin+js5[x1][i]-l1r[x2]-js3[x1][i][x2])**2+(Xkin1+js6[x1][i]-l4l[x2]-js4[x1][i][x2])**2)/2)+Kp2*((Xpole+js0[x1][i]-l2l[x2]-js1[x1][i][x2])**2+(Xpo+js7[x1][i]-l3r[x2]-js2[x1][i][x2])**2)/2+Kp1*((Xpole+js0[x1][i]-l1l[x2]-js3[x1][i][x2])**2+(Xpo+js7[x1][i]-l4r[x2]-js4[x1][i][x2])**2)/2+Kp4*((Xkin1+js6[x1][i]-Xkin-js5[x1][i]-kdis)**2)/2
        ypsl11+=(FPE)*zj0[x1][i]-(FPE)*zj7[x1][i]-FPE*zj5[x1][i]+FPE*zj6[x1][i]
        ypsl22+=(FPE)*js0[x1][i]-(FPE)*js7[x1][i]-FPE*js5[x1][i]+FPE*js6[x1][i]
        for xn in range(nu[x2]):
            if kina[x2][xn]==1 and kinb[x2][xn]==1:
                if xn==i and x2==x1:
                    ppx=dx1+d+zj1[x1][i][x2]-zj2[x1][i][x2]
                    if ppx>xdmotor:
                        ypsl11+=Km*((ppx-xdmotor)**2)/2
                    if ppx<-xdmotor:
                        ypsl11+=Km*((ppx+xdmotor)**2)/2
                    ppx=dx1-d+js1[x1][i][x2]-js2[x1][i][x2]
                    if ppx>xdmotor:
                        ypsl22+=Km*((ppx-xdmotor)**2)/2
                    if ppx<-xdmotor:
                        ypsl22+=Km*((ppx+xdmotor)**2)/2
                if xn!=i or x2!=x1:
                    ppx=dxc[x2][xn]+zj1[x1][i][x2]-zj2[x1][i][x2]
                    if ppx>xdmotor:
                        ypsl11+=Km*((ppx-xdmotor)**2)/2
                    if ppx<-xdmotor:
                        ypsl11+=Km*((ppx+xdmotor)**2)/2
                    ppx=dxc[x2][xn]+js1[x1][i][x2]-js2[x1][i][x2]
                    if ppx>xdmotor:
                        ypsl22+=Km*((ppx-xdmotor)**2)/2
                    if ppx<-xdmotor:
                        ypsl22+=Km*((ppx+xdmotor)**2)/2
        for xn in range(nu1[x2]):
            if kinap[x2][xn]+kinbp[x2][xn]==2:
                ppx=motorp[x2][xn][0]-motorp[x2][xn][1]+zj3[x1][i][x2]-zj2[x1][i][x2]
                if ppx>xdmotor:
                    ypsl11+=Km*((ppx-xdmotor)**2)/2
                if ppx<-xdmotor:
                    ypsl11+=Km*((ppx+xdmotor)**2)/2
                ppx=motorp[x2][xn][0]-motorp[x2][xn][1]+js3[x1][i][x2]-js2[x1][i][x2]
                if ppx>xdmotor:
                    ypsl22+=Km*((ppx-xdmotor)**2)/2
                if ppx<-xdmotor:
                    ypsl22+=Km*((ppx+xdmotor)**2)/2
        for xn in range(nu1x[x2]):
            if kinapx[x2][xn]+kinbpx[x2][xn]==2:
                ppx=motorpx[x2][xn][0]-motorpx[x2][xn][1]+zj4[x1][i][x2]-zj1[x1][i][x2]
                if ppx>xdmotor:
                    ypsl11+=Km*((ppx-xdmotor)**2)/2
                if ppx<-xdmotor:
                    ypsl11+=Km*((ppx+xdmotor)**2)/2
                ppx=motorpx[x2][xn][0]-motorpx[x2][xn][1]+js4[x1][i][x2]-js1[x1][i][x2]
                if ppx>xdmotor:
                    ypsl22+=Km*((ppx-xdmotor)**2)/2
                if ppx<-xdmotor:
                    ypsl22+=Km*((ppx+xdmotor)**2)/2
    for ssx in range(2):
        for xn in range(MTnumber):
            for ton1 in range(Nma[ssx][xn][0]):
                if kinam[ssx][xn][0][ton1]==1 and kinbm[ssx][xn][0][ton1]==1:
                    dxnuma=numa[ssx][xn][0][ton1][0]-numa[ssx][xn][0][ton1][1]
                    for to2 in range(xn,MTnumber-1):
                        dxnuma+=overlap[0][ssx][1][to2]-overlap[1][ssx][1][to2]
                    ypsl11+=Kpn5*((dxnuma+zj1[x1][i][0]-zj1[x1][i][1])**2)/2
                    ypsl22+=Kpn5*((dxnuma+js1[x1][i][0]-js1[x1][i][1])**2)/2
            for ton1 in range(Nma[ssx][xn][1]):
                if kinam[ssx][xn][1][ton1]==1 and kinbm[ssx][xn][1][ton1]==1:
                    dxnuma=numa[ssx][xn][1][ton1][0]-numa[ssx][xn][1][ton1][1]
                    for to2 in range(xn,MTnumber-1):
                        dxnuma+=-overlap[0][ssx][2][to2]+overlap[1][ssx][2][to2]
                    ypsl11+=Kpn5*((dxnuma+zj2[x1][i][0]-zj2[x1][i][1])**2)/2
                    ypsl22+=Kpn5*((dxnuma+js2[x1][i][0]-js2[x1][i][1])**2)/2
            for sik in range(2):
                for ton1 in range(Nma1[sik][ssx][xn][0]):
                    if kinam1[sik][ssx][xn][0][ton1]==1 and kinbm1[sik][ssx][xn][0][ton1]==1:
                        dxnuma1=numa1[sik][ssx][xn][0][ton1][0]-numa1[sik][ssx][xn][0][ton1][1]
                        for to2 in range(xn,MTnumber-1):
                            dxnuma1+=overlap[sik][ssx][0][to2]-overlap[sik][ssx][1][to2]
                        ypsl11+=Kpn5*((dxnuma1+zj3[x1][i][sik]-zj1[x1][i][sik])**2)/2
                        ypsl22+=Kpn5*((dxnuma1+js3[x1][i][sik]-js1[x1][i][sik])**2)/2
                
                for ton1 in range(Nma1[sik][ssx][xn][1]):
                    if kinam1[sik][ssx][xn][1][ton1]==1 and kinbm1[sik][ssx][xn][1][ton1]==1:
                        dxnuma1=numa1[sik][ssx][xn][1][ton1][0]-numa1[sik][ssx][xn][1][ton1][1]
                        for to2 in range(xn,MTnumber-1):
                            dxnuma1+=-overlap[sik][ssx][3][to2]+overlap[sik][ssx][2][to2]
                        ypsl11+=Kpn5*((dxnuma1+zj4[x1][i][sik]-zj2[x1][i][sik])**2)/2
                        ypsl22+=Kpn5*((dxnuma1+js4[x1][i][sik]-js2[x1][i][sik])**2)/2
    
    return ypsl11,ypsl22


# In[8]:


def energyp(x1,i):
    ypsl11=0
    ypsl22=0
    for x2 in range(pair):
        ypsl11+=Kp3*(((Xkin+zj5p[x1][i]-l1r[x2]-zj3p[x1][i][x2])**2+(Xkin1+zj6p[x1][i]-l4l[x2]-zj4p[x1][i][x2])**2)/2)+Kp2*((Xpole+zj0p[x1][i]-l2l[x2]-zj1p[x1][i][x2])**2+(Xpo+zj7p[x1][i]-l3r[x2]-zj2p[x1][i][x2])**2)/2+Kp1*((Xpole+zj0p[x1][i]-l1l[x2]-zj3p[x1][i][x2])**2+(Xpo+zj7p[x1][i]-l4r[x2]-zj4p[x1][i][x2])**2)/2+Kp4*((Xkin1+zj6p[x1][i]-Xkin-zj5p[x1][i]-kdis)**2)/2
        ypsl22+=Kp3*(((Xkin+js5p[x1][i]-l1r[x2]-js3p[x1][i][x2])**2+(Xkin1+js6p[x1][i]-l4l[x2]-js4p[x1][i][x2])**2)/2)+Kp2*((Xpole+js0p[x1][i]-l2l[x2]-js1p[x1][i][x2])**2+(Xpo+js7p[x1][i]-l3r[x2]-js2p[x1][i][x2])**2)/2+Kp1*((Xpole+js0p[x1][i]-l1l[x2]-js3p[x1][i][x2])**2+(Xpo+js7p[x1][i]-l4r[x2]-js4p[x1][i][x2])**2)/2+Kp4*((Xkin1+js6p[x1][i]-Xkin-js5p[x1][i]-kdis)**2)/2
        ypsl11+=(FPE)*zj0p[x1][i]-(FPE)*zj7p[x1][i]-FPE*zj5p[x1][i]+FPE*zj6p[x1][i]
        ypsl22+=(FPE)*js0p[x1][i]-(FPE)*js7p[x1][i]-FPE*js5p[x1][i]+FPE*js6p[x1][i]
        for xn in range(nu[x2]):
            if kina[x2][xn]==1 and kinb[x2][xn]==1:
                ppx=dxc[x2][xn]+zj1p[x1][i][x2]-zj2p[x1][i][x2]
                if ppx>xdmotor:
                    ypsl11+=Km*((ppx-xdmotor)**2)/2
                if ppx<-xdmotor:
                    ypsl11+=Km*((ppx+xdmotor)**2)/2
                ppx=dxc[x2][xn]+js1p[x1][i][x2]-js2p[x1][i][x2]    
                if ppx>xdmotor:
                    ypsl22+=Km*((ppx-xdmotor)**2)/2
                if ppx<-xdmotor:
                    ypsl22+=Km*((ppx+xdmotor)**2)/2
        for xn in range(nu1[x2]):
            if xn==i and x2==x1:
                if kinap[x2][xn]+kinbp[x2][xn]==2:
                    ppx=dx1+d+zj3p[x1][i][x2]-zj2p[x1][i][x2]
                    if ppx>xdmotor:
                        ypsl11+=Km*((ppx-xdmotor)**2)/2
                    if ppx<-xdmotor:
                        ypsl11+=Km*((ppx+xdmotor)**2)/2
                    ppx=dx1-d+js3p[x1][i][x2]-js2p[x1][i][x2]
                    if ppx>xdmotor:
                        ypsl22+=Km*((ppx-xdmotor)**2)/2
                    if ppx<-xdmotor:
                        ypsl22+=Km*((ppx+xdmotor)**2)/2
            if xn!=i or x2!=x1:
                if kinap[x2][xn]+kinbp[x2][xn]==2:
                    ppx=motorp[x2][xn][0]-motorp[x2][xn][1]+zj3p[x1][i][x2]-zj2p[x1][i][x2]
                    if ppx>xdmotor:
                        ypsl11+=Km*((ppx-xdmotor)**2)/2
                    if ppx<-xdmotor:
                        ypsl11+=Km*((ppx+xdmotor)**2)/2
                    ppx=motorp[x2][xn][0]-motorp[x2][xn][1]+js3p[x1][i][x2]-js2p[x1][i][x2]
                    if ppx>xdmotor:
                        ypsl22+=Km*((ppx-xdmotor)**2)/2
                    if ppx<-xdmotor:
                        ypsl22+=Km*((ppx+xdmotor)**2)/2
        for xn in range(nu1x[x2]):
            if kinapx[x2][xn]+kinbpx[x2][xn]==2:
                ppx=motorpx[x2][xn][0]-motorpx[x2][xn][1]+zj4p[x1][i][x2]-zj1p[x1][i][x2]
                if ppx>xdmotor:
                    ypsl11+=Km*((ppx-xdmotor)**2)/2
                if ppx<-xdmotor:
                    ypsl11+=Km*((ppx+xdmotor)**2)/2
                ppx=motorpx[x2][xn][0]-motorpx[x2][xn][1]+js4p[x1][i][x2]-js1p[x1][i][x2]
                if ppx>xdmotor:
                    ypsl22+=Km*((ppx-xdmotor)**2)/2
                if ppx<-xdmotor:
                    ypsl22+=Km*((ppx+xdmotor)**2)/2
    for ssx in range(2):
        for xn in range(MTnumber):
            for ton1 in range(Nma[ssx][xn][0]):
                if kinam[ssx][xn][0][ton1]==1 and kinbm[ssx][xn][0][ton1]==1:
                    dxnuma=numa[ssx][xn][0][ton1][0]-numa[ssx][xn][0][ton1][1]
                    for to2 in range(xn,MTnumber-1):
                        dxnuma+=overlap[0][ssx][1][to2]-overlap[1][ssx][1][to2]
                    ypsl11+=Kpn5*((dxnuma+zj1p[x1][i][0]-zj1p[x1][i][1])**2)/2
                    ypsl22+=Kpn5*((dxnuma+js1p[x1][i][0]-js1p[x1][i][1])**2)/2
            for ton1 in range(Nma[ssx][xn][1]):
                if kinam[ssx][xn][1][ton1]==1 and kinbm[ssx][xn][1][ton1]==1:
                    dxnuma=numa[ssx][xn][1][ton1][0]-numa[ssx][xn][1][ton1][1]
                    for to2 in range(xn,MTnumber-1):
                        dxnuma+=-overlap[0][ssx][2][to2]+overlap[1][ssx][2][to2]
                    ypsl11+=Kpn5*((dxnuma+zj2p[x1][i][0]-zj2p[x1][i][1])**2)/2
                    ypsl22+=Kpn5*((dxnuma+js2p[x1][i][0]-js2p[x1][i][1])**2)/2
            for sik in range(2):
                for ton1 in range(Nma1[sik][ssx][xn][0]):
                    if kinam1[sik][ssx][xn][0][ton1]==1 and kinbm1[sik][ssx][xn][0][ton1]==1:
                        dxnuma1=numa1[sik][ssx][xn][0][ton1][0]-numa1[sik][ssx][xn][0][ton1][1]
                        for to2 in range(xn,MTnumber-1):
                            dxnuma1+=overlap[sik][ssx][0][to2]-overlap[sik][ssx][1][to2]
                        ypsl11+=Kpn5*((dxnuma1+zj3p[x1][i][sik]-zj1p[x1][i][sik])**2)/2
                        ypsl22+=Kpn5*((dxnuma1+js3p[x1][i][sik]-js1p[x1][i][sik])**2)/2
                
                for ton1 in range(Nma1[sik][ssx][xn][1]):
                    if kinam1[sik][ssx][xn][1][ton1]==1 and kinbm1[sik][ssx][xn][1][ton1]==1:
                        dxnuma1=numa1[sik][ssx][xn][1][ton1][0]-numa1[sik][ssx][xn][1][ton1][1]
                        for to2 in range(xn,MTnumber-1):
                            dxnuma1+=-overlap[sik][ssx][3][to2]+overlap[sik][ssx][2][to2]
                        ypsl11+=Kpn5*((dxnuma1+zj4p[x1][i][sik]-zj2p[x1][i][sik])**2)/2
                        ypsl22+=Kpn5*((dxnuma1+js4p[x1][i][sik]-js2p[x1][i][sik])**2)/2 
    return ypsl11,ypsl22


# In[9]:


def energypx(x1,i):
    ypsl11=0
    ypsl22=0
    for x2 in range(pair):
        ypsl11+=Kp3*(((Xkin+zj5px[x1][i]-l1r[x2]-zj3px[x1][i][x2])**2+(Xkin1+zj6px[x1][i]-l4l[x2]-zj4px[x1][i][x2])**2)/2)+Kp2*((Xpole+zj0px[x1][i]-l2l[x2]-zj1px[x1][i][x2])**2+(Xpo+zj7px[x1][i]-l3r[x2]-zj2px[x1][i][x2])**2)/2+Kp1*((Xpole+zj0px[x1][i]-l1l[x2]-zj3px[x1][i][x2])**2+(Xpo+zj7px[x1][i]-l4r[x2]-zj4px[x1][i][x2])**2)/2+Kp4*((Xkin1+zj6px[x1][i]-Xkin-zj5px[x1][i]-kdis)**2)/2+
        ypsl22+=Kp3*(((Xkin+js5px[x1][i]-l1r[x2]-js3px[x1][i][x2])**2+(Xkin1+js6px[x1][i]-l4l[x2]-js4px[x1][i][x2])**2)/2)+Kp2*((Xpole+js0px[x1][i]-l2l[x2]-js1px[x1][i][x2])**2+(Xpo+js7px[x1][i]-l3r[x2]-js2px[x1][i][x2])**2)/2+Kp1*((Xpole+js0px[x1][i]-l1l[x2]-js3px[x1][i][x2])**2+(Xpo+js7px[x1][i]-l4r[x2]-js4px[x1][i][x2])**2)/2+Kp4*((Xkin1+js6px[x1][i]-Xkin-js5px[x1][i]-kdis)**2)/2
        ypsl11+=(FPE)*zj0px[x1][i]-(FPE)*zj7px[x1][i]-FPE*zj5px[x1][i]+FPE*zj6px[x1][i]
        ypsl22+=(FPE)*js0px[x1][i]-(FPE)*js7px[x1][i]-FPE*js5px[x1][i]+FPE*js6px[x1][i]
        for xn in range(nu[x2]):
            if kina[x2][xn]==1 and kinb[x2][xn]==1:
                ppx=dxc[x2][xn]+zj1px[x1][i][x2]-zj2px[x1][i][x2]
                if ppx>xdmotor:
                    ypsl11+=Km*((ppx-xdmotor)**2)/2
                if ppx<-xdmotor:
                    ypsl11+=Km*((ppx+xdmotor)**2)/2
                ppx=dxc[x2][xn]+js1px[x1][i][x2]-js2px[x1][i][x2]
                if ppx>xdmotor:
                    ypsl22+=Km*((ppx-xdmotor)**2)/2
                if ppx<-xdmotor:
                    ypsl22+=Km*((ppx+xdmotor)**2)/2
        for xn in range(nu1[x2]):
            if kinap[x2][xn]+kinbp[x2][xn]==2:
                ppx=motorp[x2][xn][0]-motorp[x2][xn][1]+zj3px[x1][i][x2]-zj2px[x1][i][x2]
                if ppx>xdmotor:
                    ypsl11+=Km*((ppx-xdmotor)**2)/2
                if ppx<-xdmotor:
                    ypsl11+=Km*((ppx+xdmotor)**2)/2
                ppx=motorp[x2][xn][0]-motorp[x2][xn][1]+js3px[x1][i][x2]-js2px[x1][i][x2]
                if ppx>xdmotor:
                    ypsl22+=Km*((ppx-xdmotor)**2)/2
                if ppx<-xdmotor:
                    ypsl22+=Km*((ppx+xdmotor)**2)/2
        for xn in range(nu1x[x2]):
            if xn==i and x2==x1:
                if kinapx[x2][xn]+kinbpx[x2][xn]==2:
                    ppx=dx1+d+zj4px[x1][i][x2]-zj1px[x1][i][x2]
                    if ppx>xdmotor:
                        ypsl11+=Km*((ppx-xdmotor)**2)/2
                    if ppx<-xdmotor:
                        ypsl11+=Km*((ppx+xdmotor)**2)/2
                    ppx=dx1-d+js4px[x1][i][x2]-js1px[x1][i][x2]
                    if ppx>xdmotor:
                        ypsl22+=Km*((ppx-xdmotor)**2)/2
                    if ppx<-xdmotor:
                        ypsl22+=Km*((ppx+xdmotor)**2)/2
            if xn!=i or x2!=x1:
                if kinapx[x2][xn]+kinbpx[x2][xn]==2:
                    ppx=motorpx[x2][xn][0]-motorpx[x2][xn][1]+zj4px[x1][i][x2]-zj1px[x1][i][x2]
                    if ppx>xdmotor:
                        ypsl11+=Km*((ppx-xdmotor)**2)/2
                    if ppx<-xdmotor:
                        ypsl11+=Km*((ppx+xdmotor)**2)/2
                    ppx=motorpx[x2][xn][0]-motorpx[x2][xn][1]+js4px[x1][i][x2]-js1px[x1][i][x2]
                    if ppx>xdmotor:
                        ypsl22+=Km*((ppx-xdmotor)**2)/2
                    if ppx<-xdmotor:
                        ypsl22+=Km*((ppx+xdmotor)**2)/2
    for ssx in range(2):
        for xn in range(MTnumber):
            for ton1 in range(Nma[ssx][xn][0]):
                if kinam[ssx][xn][0][ton1]==1 and kinbm[ssx][xn][0][ton1]==1:
                    dxnuma=numa[ssx][xn][0][ton1][0]-numa[ssx][xn][0][ton1][1]
                    for to2 in range(xn,MTnumber-1):
                        dxnuma+=overlap[0][ssx][1][to2]-overlap[1][ssx][1][to2]
                    ypsl11+=Kpn5*((dxnuma+zj1px[x1][i][0]-zj1px[x1][i][1])**2)/2
                    ypsl22+=Kpn5*((dxnuma+js1px[x1][i][0]-js1px[x1][i][1])**2)/2
            for ton1 in range(Nma[ssx][xn][1]):
                if kinam[ssx][xn][1][ton1]==1 and kinbm[ssx][xn][1][ton1]==1:
                    dxnuma=numa[ssx][xn][1][ton1][0]-numa[ssx][xn][1][ton1][1]
                    for to2 in range(xn,MTnumber-1):
                        dxnuma+=-overlap[0][ssx][2][to2]+overlap[1][ssx][2][to2]
                    ypsl11+=Kpn5*((dxnuma+zj2px[x1][i][0]-zj2px[x1][i][1])**2)/2
                    ypsl22+=Kpn5*((dxnuma+js2px[x1][i][0]-js2px[x1][i][1])**2)/2
            for sik in range(2):
                for ton1 in range(Nma1[sik][ssx][xn][0]):
                    if kinam1[sik][ssx][xn][0][ton1]==1 and kinbm1[sik][ssx][xn][0][ton1]==1:
                        dxnuma1=numa1[sik][ssx][xn][0][ton1][0]-numa1[sik][ssx][xn][0][ton1][1]
                        for to2 in range(xn,MTnumber-1):
                            dxnuma1+=overlap[sik][ssx][0][to2]-overlap[sik][ssx][1][to2]
                        ypsl11+=Kpn5*((dxnuma1+zj3px[x1][i][sik]-zj1px[x1][i][sik])**2)/2
                        ypsl22+=Kpn5*((dxnuma1+js3px[x1][i][sik]-js1px[x1][i][sik])**2)/2
                
                for ton1 in range(Nma1[sik][ssx][xn][1]):
                    if kinam1[sik][ssx][xn][1][ton1]==1 and kinbm1[sik][ssx][xn][1][ton1]==1:
                        dxnuma1=numa1[sik][ssx][xn][1][ton1][0]-numa1[sik][ssx][xn][1][ton1][1]
                        for to2 in range(xn,MTnumber-1):
                            dxnuma1+=-overlap[sik][ssx][3][to2]+overlap[sik][ssx][2][to2]
                        ypsl11+=Kpn5*((dxnuma1+zj4px[x1][i][sik]-zj2px[x1][i][sik])**2)/2
                        ypsl22+=Kpn5*((dxnuma1+js4px[x1][i][sik]-js2px[x1][i][sik])**2)/2 
    
   
    return ypsl11,ypsl22


# In[10]:


def energy0():
    ypsl0=0
    for x2 in range(pair):
        ypsl0+=Kp3*(((Xkin-l1r[x2])**2+(Xkin1-l4l[x2])**2)/2)+Kp2*((Xpole-l2l[x2])**2+(Xpo-l3r[x2])**2)/2+Kp1*((Xpole-l1l[x2])**2+(Xpo-l4r[x2])**2)/2+Kp4*((Xkin1-Xkin-kdis)**2)/2
        for xn in range(nu[x2]):
            
            if kina[x2][xn]==1 and kinb[x2][xn]==1:
                ppx=motor[x2][xn][0]-motor[x2][xn][1]
                if ppx>xdmotor:
                    ypsl0+=Km*((ppx-xdmotor)**2)/2
                if ppx<-xdmotor:
                    ypsl0+=Km*((ppx+xdmotor)**2)/2
        for xn in range(nu1[x2]):
            if kinap[x2][xn]+kinbp[x2][xn]==2:
                ppx=motorp[x2][xn][0]-motorp[x2][xn][1]
                if ppx>xdmotor:
                    ypsl0+=Km*((ppx-xdmotor)**2)/2
                if ppx<-xdmotor:
                    ypsl0+=Km*((ppx+xdmotor)**2)/2
        for xn in range(nu1x[x2]):
            if kinapx[x2][xn]+kinbpx[x2][xn]==2:
                ppx=motorpx[x2][xn][0]-motorpx[x2][xn][1]
                if ppx>xdmotor:
                    ypsl0+=Km*((ppx-xdmotor)**2)/2
                if ppx<-xdmotor:
                    ypsl0+=Km*((ppx+xdmotor)**2)/2
    for ssx in range(2):
        for xn in range(MTnumber):
            for ton1 in range(Nma[ssx][xn][0]):
                if kinam[ssx][xn][0][ton1]==1 and kinbm[ssx][xn][0][ton1]==1:
                    dxnuma=numa[ssx][xn][0][ton1][0]-numa[ssx][xn][0][ton1][1]
                    for to2 in range(xn,MTnumber-1):
                        dxnuma+=overlap[0][ssx][1][to2]-overlap[1][ssx][1][to2]
                    ypsl0+=Kpn5*(dxnuma**2)/2
                
            for ton1 in range(Nma[ssx][xn][1]):
                if kinam[ssx][xn][1][ton1]==1 and kinbm[ssx][xn][1][ton1]==1:
                    dxnuma=numa[ssx][xn][1][ton1][0]-numa[ssx][xn][1][ton1][1]
                    for to2 in range(xn,MTnumber-1):
                        dxnuma+=-overlap[0][ssx][2][to2]+overlap[1][ssx][2][to2]
                    ypsl0+=Kpn5*(dxnuma**2)/2
            for sik in range(2):
                for ton1 in range(Nma1[sik][ssx][xn][0]):
                    if kinam1[sik][ssx][xn][0][ton1]==1 and kinbm1[sik][ssx][xn][0][ton1]==1:
                        dxnuma1=numa1[sik][ssx][xn][0][ton1][0]-numa1[sik][ssx][xn][0][ton1][1]
                        for to2 in range(xn,MTnumber-1):
                            dxnuma1+=overlap[sik][ssx][0][to2]-overlap[sik][ssx][1][to2]
                        ypsl0+=Kpn5*(dxnuma1**2)/2
                for ton1 in range(Nma1[sik][ssx][xn][1]):
                    if kinam1[sik][ssx][xn][1][ton1]==1 and kinbm1[sik][ssx][xn][1][ton1]==1:
                        dxnuma1=numa1[sik][ssx][xn][1][ton1][0]-numa1[sik][ssx][xn][1][ton1][1]
                        for to2 in range(xn,MTnumber-1):
                            dxnuma1+=-overlap[sik][ssx][3][to2]+overlap[sik][ssx][2][to2]
                        ypsl0+=Kpn5*(dxnuma1**2)/2
                        

                
    return ypsl0


# In[11]:


def checkF():
    F0=-FPE
    F7=FPE
    F5=FPE
    F6=-FPE
    Fcc=0
    for x2 in range(pair):
        F0+=Kp1*(l1l[x2]-Xpole)+Kp2*(l2l[x2]-Xpole)
        F7+=Kp1*(l4r[x2]-Xpo)+Kp2*(l3r[x2]-Xpo)
        F5+=Kp3*(l1r[x2]-Xkin)+Kp4*(Xkin1-Xkin-kdis)
        F6+=Kp4*(Xkin-Xkin1+kdis)+Kp3*(l4l[x2]-Xkin1)
        F3[x2]=Kp2*(Xpo-l3r[x2])
        F1[x2]=Kp1*(l1l[x2]-Xpole)+Kp3*(l1r[x2]-Xkin)
        F2[x2]=Kp2*(l2l[x2]-Xpole)
        F4[x2]=Kp1*(Xpo-l4r[x2])+Kp3*(Xkin1-l4l[x2])
        for ton1 in range(nu[x2]):
            if kina[x2][ton1]==1 and kinb[x2][ton1]==1:
                dxc[x2][ton1]=motor[x2][ton1][0]-motor[x2][ton1][1]
                if dxc[x2][ton1]>xdmotor:
                    F3[x2]+=(dxc[x2][ton1]-xdmotor)*Km
                    F2[x2]+=(dxc[x2][ton1]-xdmotor)*Km
                if dxc[x2][ton1]<-xdmotor:
                    F3[x2]+=(dxc[x2][ton1]+xdmotor)*Km
                    F2[x2]+=(dxc[x2][ton1]+xdmotor)*Km
            if kina[x2][ton1]==0 or kinb[x2][ton1]==0:
                dxc[x2][ton1]=0
        for ton1 in range(nu1[x2]):
            if kinap[x2][ton1]==1 and kinbp[x2][ton1]==1:
                dxcp[x2][ton1]=motorp[x2][ton1][0]-motorp[x2][ton1][1]
                if dxcp[x2][ton1]>xdmotor:
                    F3[x2]+=(dxcp[x2][ton1]-xdmotor)*Km
                    F1[x2]+=(dxcp[x2][ton1]-xdmotor)*Km
                if dxcp[x2][ton1]<-xdmotor:
                    F3[x2]+=(dxcp[x2][ton1]+xdmotor)*Km
                    F1[x2]+=(dxcp[x2][ton1]+xdmotor)*Km
            if kinap[x2][ton1]==0 or kinbp[x2][ton1]==0:
                dxcp[x2][ton1]=0
        for ton1 in range(nu1x[x2]):
            if kinapx[x2][ton1]==1 and kinbpx[x2][ton1]==1:
                dxcpx[x2][ton1]=motorpx[x2][ton1][0]-motorpx[x2][ton1][1]
                if dxcpx[x2][ton1]>xdmotor:
                    F4[x2]-=(dxcpx[x2][ton1]-xdmotor)*Km
                    F2[x2]-=(dxcpx[x2][ton1]-xdmotor)*Km
                if dxcpx[x2][ton1]<-xdmotor:
                    F4[x2]-=(dxcpx[x2][ton1]+xdmotor)*Km
                    F2[x2]-=(dxcpx[x2][ton1]+xdmotor)*Km
            if kinapx[x2][ton1]==0 or kinbpx[x2][ton1]==0:
                dxcpx[x2][ton1]=0
    for ssx in range(2):
        for xn in range(MTnumber):
            for ton1 in range(Nma[ssx][xn][0]):
                
                if kinam[ssx][xn][0][ton1]==1 and kinbm[ssx][xn][0][ton1]==1:
                    dxnuma=numa[ssx][xn][0][ton1][0]-numa[ssx][xn][0][ton1][1]
                    for to2 in range(xn,MTnumber-1):
                        dxnuma+=overlap[0][ssx][1][to2]-overlap[1][ssx][1][to2]
                    #print(dxnuma,'00')
                    F2[0]+=Kpn5*dxnuma
                    F2[1]-=Kpn5*dxnuma
            for ton1 in range(Nma[ssx][xn][1]):
                if kinam[ssx][xn][1][ton1]==1 and kinbm[ssx][xn][1][ton1]==1:
                    dxnuma=numa[ssx][xn][1][ton1][0]-numa[ssx][xn][1][ton1][1]
                    for to2 in range(xn,MTnumber-1):
                        dxnuma+=-overlap[0][ssx][2][to2]+overlap[1][ssx][2][to2]
                    #print(dxnuma,'0')
                    F3[0]-=Kpn5*dxnuma
                    F3[1]+=Kpn5*dxnuma
            for sik in range(2):
                for ton1 in range(Nma1[sik][ssx][xn][0]):
                    if kinam1[sik][ssx][xn][0][ton1]==1 and kinbm1[sik][ssx][xn][0][ton1]==1:
                        dxnuma1=numa1[sik][ssx][xn][0][ton1][0]-numa1[sik][ssx][xn][0][ton1][1]
                        for to2 in range(xn,MTnumber-1):
                            dxnuma1+=overlap[sik][ssx][0][to2]-overlap[sik][ssx][1][to2]
                        #print(dxnuma1,'10')
                        F1[sik]+=Kpn5*dxnuma1
                        F2[sik]-=Kpn5*dxnuma1
                for ton1 in range(Nma1[sik][ssx][xn][1]):
                    if kinam1[sik][ssx][xn][1][ton1]==1 and kinbm1[sik][ssx][xn][1][ton1]==1:
                        dxnuma1=numa1[sik][ssx][xn][1][ton1][0]-numa1[sik][ssx][xn][1][ton1][1]
                        for to2 in range(xn,MTnumber-1):
                            dxnuma1+=-overlap[sik][ssx][3][to2]+overlap[sik][ssx][2][to2]
                        #print(dxnuma1,'1')
                        F4[sik]-=Kpn5*dxnuma1
                        F3[sik]+=Kpn5*dxnuma1
              
    for x2 in range(pair):
        if abs(F1[x2])+abs(F2[x2])+abs(F3[x2])+abs(F4[x2])>0.0001:
            Fcc=1
    if abs(F0)+abs(F7)+abs(F5)+abs(F6)>0.0001 or Fcc==1:
        #print(F1,F2,F3,F4,F0,F7,F5,F6,a)
        #print(qq)
        de0,de1,de2,de3,de4,de5,de6,de7=jiao(dxc,dxcp,dxcpx,F1,F2,F3,F4,monum,monump,monumpx)
        return 1,de0,de1,de2,de3,de4,de5,de6,de7
    return 0,0,0,0,0,0,0,0,0


# In[12]:


def disnuma(FF):
    kin=1
    ran1=random.uniform(0,1)
    if ran1<koffn*math.exp(abs(FF)/Foffn)*h:
        kin=0
    return kin


# In[ ]:





# In[13]:


import random
import math
import numpy
import numpy as np
import pandas as pd
h = 0.001
Km = 0.55# pN/nm
d=8.2
dcc=8.2
Number=3
vp1=24
vpol=vp1/d
xdmotor=d+0.000001
nant=3
npar=1
pair=2
ka1=0.0004*nant
ka2=0.0004*nant
Kp2=0.1
Kp1=0.1
Kp3=0.1
Kp4=0.01#2/pair
lover=8003.2
kdis=500.2
llap=4001.6
llap1=4001.6
FPE=2#pN
koffn=0.02
Foffn=4
l1l=[-lover+FPE/Kp1 for i in range(pair)]
l1r=[-kdis/2+FPE/Kp4-FPE/Kp3 for i in range(pair)]
l2l=[-lover for i in range(pair)]
l2r=[llap ,llap1]
l3l=[-llap ,-llap1]
l3r=[lover for i in range(pair)]
l4l=[kdis/2-FPE/Kp4+FPE/Kp3 for i in range(pair)]
l4r=[lover-FPE/Kp1 for i in range(pair)]
Xpole=-lover
Xpo=lover
Xkin=-kdis/2+FPE/Kp4
Xkin1=kdis/2-FPE/Kp4
B=4
vp0=vp1/B
Fp0=1.85

dn=1
#MCAK
kon=0.0003
koff=0.003
konnu=0.0003
Kpn5=0.03
unu=1
kdif=82

vd=5
#stai=0.5
#stak=0.5
stad=0.5
##################
Ximt2=[0  for i in range(pair)]
Ximt3=[0  for i in range(pair)]
Xkmt1=[0  for i in range(pair)]
Xkmt4=[0  for i in range(pair)]
desi2=[0  for i in range(pair)]
desi3=[0  for i in range(pair)]
desk1=[0  for i in range(pair)]
desk4=[0  for i in range(pair)]
pos1=[0  for i in range(pair)]
pos4=[0  for i in range(pair)]
pos2=[0  for i in range(pair)]
desia2=[0  for i in range(pair)]
desia3=[0  for i in range(pair)]
deska1=[0  for i in range(pair)]
deska4=[0  for i in range(pair)]
posa1=[0  for i in range(pair)]
posa4=[0  for i in range(pair)]
posa2=[0  for i in range(pair)]
ximta2=[0  for i in range(pair)]
ximta3=[0  for i in range(pair)]
xkmta1=[0  for i in range(pair)]
xkmta4=[0  for i in range(pair)]
ads=1

nu=[0 for i in range(pair)]
nu1=[0 for i in range(pair)]
nu1x=[0 for i in range(pair)]
monum=[0 for i in range(pair)]
monump=[0 for i in range(pair)]
monumpx=[0 for i in range(pair)]

lxian=[0 for i in range(pair)]
lxianp=[0 for i in range(pair)]
lxianpx=[0 for i in range(pair)]
F1=[0 for i in range(pair)]
F2=[0 for i in range(pair)]
F3=[0 for i in range(pair)]
F4=[0 for i in range(pair)]
panx=0
pan1=1
site=round(lover/d)-1
parpair=2
kina =[[]for i in range(pair)]
kinb =[[]for i in range(pair)]
kinap =[[]for i in range(pair)]
kinbp =[[]for i in range(pair)]
kinapx=[[]for i in range(pair)]
kinbpx=[[]for i in range(pair)]

motor =[[]for i in range(pair)]
motorp=[[]for i in range(pair)]
motorpx=[[]for i in range(pair)]
motormc1=[[[] for i in range(2)]for i in range(pair)] 
motormc2=[[[] for i in range(2)]for i in range(pair)]
motormc3=[[[] for i in range(2)]for i in range(pair)]
motormc4=[[[] for i in range(2)]for i in range(pair)]
dxc =[[]for i in range(pair)]
dxcp =[[]for i in range(pair)]
dxcpx =[[]for i in range(pair)]
pan=[[]for i in range(pair)]
ypsl1=[[]for i in range(pair)]
ypsl2=[[]for i in range(pair)]
panp=[[]for i in range(pair)]
ypsl1p=[[]for i in range(pair)]
ypsl2p=[[]for i in range(pair)]
panpx=[[]for i in range(pair)]
ypsl1px=[[]for i in range(pair)]
ypsl2px=[[]for i in range(pair)]
zj0=[[] for i in range(pair)]
js0=[[]for i in range(pair)]
zj1=[[]for i in range(pair)]
js1=[[]for i in range(pair)]
zj2=[[]for i in range(pair)]
js2=[[]for i in range(pair)]
zj3=[[]for i in range(pair)]
js3=[[]for i in range(pair)]
zj4=[[]for i in range(pair)]
js4=[[]for i in range(pair)]
zj5=[[]for i in range(pair)]
js5=[[]for i in range(pair)]
zj6=[[]for i in range(pair)]
js6=[[]for i in range(pair)]
zj7=[[]for i in range(pair)]
js7=[[]for i in range(pair)]
zj0p=[[]for i in range(pair)]
js0p=[[]for i in range(pair)]
zj1p=[[]for i in range(pair)]
js1p=[[]for i in range(pair)]
zj2p=[[]for i in range(pair)]
js2p=[[]for i in range(pair)]
zj3p=[[]for i in range(pair)]
js3p=[[]for i in range(pair)]
zj4p=[[]for i in range(pair)]
js4p=[[]for i in range(pair)]
zj5p=[[]for i in range(pair)]
js5p=[[]for i in range(pair)]
zj6p=[[]for i in range(pair)]
js6p=[[]for i in range(pair)]
zj7p=[[]for i in range(pair)]
js7p=[[]for i in range(pair)]
zj0px=[[]for i in range(pair)]
js0px=[[]for i in range(pair)]
zj1px=[[]for i in range(pair)]
js1px=[[]for i in range(pair)]
zj2px=[[]for i in range(pair)]
js2px=[[]for i in range(pair)]
zj3px=[[]for i in range(pair)]
js3px=[[]for i in range(pair)]
zj4px=[[]for i in range(pair)]
js4px=[[]for i in range(pair)]
zj5px=[[]for i in range(pair)]
js5px=[[]for i in range(pair)]
zj6px=[[]for i in range(pair)]
js6px=[[]for i in range(pair)]
zj7px=[[]for i in range(pair)]
js7px=[[]for i in range(pair)]

for x1 in range(pair):
    xx=1/8
    for xn in range(2*7):
        xx+=1/2/8
        cx0=l3r[x1]-round((lover-llap)/d*random.uniform(0,xx))*d####??????
        motormc3[x1].append(cx0)
    xx=1/8
    for xn in range(2*7):
        xx+=1/2/8
        cx0=l1l[x1]+round((lover-llap)/d*random.uniform(0,xx))*d
        motormc1[x1].append(cx0)
    xx=1/8
    for xn in range(2*7):
        xx+=1/2/8
        cx0=l4r[x1]-round((lover-llap)/d*random.uniform(0,xx))*d
        motormc4[x1].append(cx0)
    xx=1/8
    for xn in range(2*7):
        xx+=1/2/8
        cx0=l2l[x1]+round((lover-llap)/d*random.uniform(0,xx))*d
        motormc2[x1].append(cx0)
    for xn in range(round(Number*random.uniform(nant*2,nant*2+1))):
        cx0=l3l[x1]+round(lover/d*random.uniform(0,1))*d
        motor[x1].append([cx0,cx0])
        kina[x1].append(round(random.uniform(0,1)))
        kinb[x1].append(round(random.uniform(0,1)))
        ypsl1[x1].append(0)
        dxc[x1].append(0)
        pan[x1].append(0)
        ypsl2[x1].append(0)
        zj0[x1].append(0)
        js0[x1].append(0)
        zj1[x1].append([0 for i in range(pair)])
        js1[x1].append([0 for i in range(pair)])
        zj2[x1].append([0 for i in range(pair)])
        js2[x1].append([0 for i in range(pair)])
        zj3[x1].append([0 for i in range(pair)])
        js3[x1].append([0 for i in range(pair)])
        zj4[x1].append([0 for i in range(pair)])
        js4[x1].append([0 for i in range(pair)])
        zj5[x1].append(0)
        js5[x1].append(0)
        zj6[x1].append(0)
        js6[x1].append(0)
        zj7[x1].append(0)
        js7[x1].append(0)

    for xn in range(round(Number*random.uniform(nant,nant+1))):
        cx0=l3l[x1]+round(lover/2/d*random.uniform(0,1))*d
        motorp[x1].append([cx0,cx0])
        kinap[x1].append(round(random.uniform(0,1)))
        kinbp[x1].append(round(random.uniform(0,1)))
        dxcp[x1].append(0)
        panp[x1].append(0)
        ypsl1p[x1].append(0)
        ypsl2p[x1].append(0)
        zj0p[x1].append(0)
        js0p[x1].append(0)
        zj1p[x1].append([0 for i in range(pair)])
        js1p[x1].append([0 for i in range(pair)])
        zj2p[x1].append([0 for i in range(pair)])
        js2p[x1].append([0 for i in range(pair)])
        zj3p[x1].append([0 for i in range(pair)])
        js3p[x1].append([0 for i in range(pair)])
        zj4p[x1].append([0 for i in range(pair)])
        js4p[x1].append([0 for i in range(pair)])
        zj5p[x1].append(0)
        js5p[x1].append(0)
        zj6p[x1].append(0)
        js6p[x1].append(0)
        zj7p[x1].append(0)
        js7p[x1].append(0)
    
    for xn in range(round(Number*random.uniform(nant,nant+1))):
        cx0=l4l[x1]+round(lover/2/d*random.uniform(0,1))*d
        motorpx[x1].append([cx0,cx0])
        kinapx[x1].append(round(random.uniform(0,1)))
        kinbpx[x1].append(round(random.uniform(0,1)))
        dxcpx[x1].append(0)
        panpx[x1].append(0)
        ypsl1px[x1].append(0)
        ypsl2px[x1].append(0)
        zj0px[x1].append(0)
        js0px[x1].append(0)
        zj1px[x1].append([0 for i in range(pair)])
        js1px[x1].append([0 for i in range(pair)])
        zj2px[x1].append([0 for i in range(pair)])
        js2px[x1].append([0 for i in range(pair)])
        zj3px[x1].append([0 for i in range(pair)])
        js3px[x1].append([0 for i in range(pair)])
        zj4px[x1].append([0 for i in range(pair)])
        js4px[x1].append([0 for i in range(pair)])
        zj5px[x1].append(0)
        js5px[x1].append(0)
        zj6px[x1].append(0)
        js6px[x1].append(0)
        zj7px[x1].append(0)
        js7px[x1].append(0)




for x1 in range(pair):
    nu[x1]=len(kina[x1])
    nu1[x1]=len(kinap[x1])
    nu1x[x1]=len(kinapx[x1])

for x1 in range(pair):
    monum[x1]=sum(kina[x1])
    for xn in range(nu[x1]):
        if kina[x1][xn]==1 and kinb[x1][xn]==0:
            monum[x1]-=1
    monump[x1]=sum(kinap[x1])
    for xn in range(nu1[x1]):
        if kinap[x1][xn]==1 and kinbp[x1][xn]==0:
            monump[x1]-=1
    monumpx[x1]=sum(kinapx[x1])
    for xn in range(nu1x[x1]):
        if kinapx[x1][xn]==1 and kinbpx[x1][xn]==0:
            monumpx[x1]-=1

lenn=0         
MTnumber=3
numa=[[[[] for i in range(parpair)] for i in range(MTnumber)] for i in range(2)]
kinam=[[[[]for i in range(parpair)] for i in range(MTnumber)] for i in range(2)]
kinbm=[[[[]for i in range(parpair)] for i in range(MTnumber)] for i in range(2)]
Nma=[[[0 for i in range(parpair)] for i in range(MTnumber)] for i in range(2)]
kinam1=[[[[[]for i in range(parpair)] for i in range(MTnumber)] for i in range(2)] for i in range(2)]
kinbm1=[[[[[]for i in range(parpair)] for i in range(MTnumber)] for i in range(2)] for i in range(2)]
Nma1=[[[[0 for i in range(parpair)] for i in range(MTnumber)] for i in range(2)] for i in range(2)]
numa1=[[[[[] for i in range(parpair)] for i in range(MTnumber)] for i in range(2)] for i in range(2)]

nunum1=[[0 for i in range(2)]for i in range(2)]
nunum=[0 for i in range(2)]
for ssx in range(2):
    for xn in range(MTnumber):
        for xbb in range(Nma[ssx][xn][0]):
            if kinam[ssx][xn][0][xbb]==1 and kinbm[ssx][xn][0][xbb]==1:
                nunum[0]+=1
        for xbb in range(Nma[ssx][xn][1]):
            if kinam[ssx][xn][1][xbb]==1 and kinbm[ssx][xn][1][xbb]==1:
                nunum[1]+=1
        for sik in range(2):
            for xbb in range(Nma1[sik][ssx][xn][0]):
                if kinam1[sik][ssx][xn][0][xbb]==1 and kinbm1[sik][ssx][xn][0][xbb]==1:
                    nunum1[sik][0]+=1
            for xbb in range(Nma1[sik][ssx][xn][1]):
                if kinam1[sik][ssx][xn][1][xbb]==1 and kinbm1[sik][ssx][xn][1][xbb]==1:
                    nunum1[sik][1]+=1
node1=[[[]for i in range(2)] for x1 in range(pair)]
for x1 in range(pair):#2pair
    for xn in range(2):
        node1[x1][xn]=[[l1l[x1]-lenn*(MTnumber-1)],[l1l[x1]-lenn*(MTnumber-1)],[l3r[x1]+lenn*(MTnumber-1)],[l3r[x1]+lenn*(MTnumber-1)]]
        for i in range(1,MTnumber):
            for xx in range(2):
                node1[x1][xn][xx].append(l1l[x1]-lenn*(MTnumber-1)+round(i*(lover-(llap)/2)/MTnumber/d)*d+lenn*i)
            for xx in [2,3]:
                node1[x1][xn][xx].append(l3r[x1]+lenn*(MTnumber-1)-round(i*(lover-(llap)/2)/MTnumber/d)*d-lenn*i)
        node1[x1][xn][0].append(l1r[x1])
        node1[x1][xn][1].append(l2r[x1])
        node1[x1][xn][2].append(l3l[x1])  
        node1[x1][xn][3].append(l4l[x1])
adeps1=[[[0 for i in range(MTnumber)] for i in range(2)]  for x1 in range(pair)]
adeps2=[[[0 for i in range(MTnumber)] for i in range(2)] for x1 in range(pair)]
adeps3=[[[0 for i in range(MTnumber)]  for i in range(2)]  for x1 in range(pair)]
adeps4=[[[0 for i in range(MTnumber)] for i in range(2)]  for x1 in range(pair)]
noind=[[[[0 for i in range(MTnumber)] for i in range(4)]  for i in range(2)]  for x1 in range(pair)]
overlap=[[[[lenn for i in range(MTnumber-1)] for i in range(4)] for i in range(2)]  for x1 in range(pair)]
hua1=[0,0]
hua4=[0,0]
Fxing=3.2
alp=10
pi1=0.1
numc1=[[0 for i in range(2)] for x1 in range(pair)]
numc2=[[0 for i in range(2)] for x1 in range(pair)]
numc3=[[0 for i in range(2)] for x1 in range(pair)]
numc4=[[0 for i in range(2)] for x1 in range(pair)]
ypsl0=energy0()
ypsl0p=ypsl0
ypsl0px=ypsl0
MTk1=[]
MTi1=[]
MTzn1=[]
MTzn2=[]
MTzn3=[]
MTzn4=[]
MTzn5=[]
MTzn6=[]
MTzn7=[]
MTzn8=[]
MTzn9=[]
MTzn10=[]
MTzn11=[]
MTzn12=[]
MTzn13=[]
MTzn14=[]
MTzn15=[]
MTzn16=[]
MTzn17=[]
MTzn18=[]
MTzn19=[]
MTzn20=[]
MTzn21=[]
MTzn22=[]
MTzn23=[]
MTzn24=[]
time1=[]
MTX1=[]
MTX2=[]
ttq=0


# In[ ]:


for a in range(0,20000000):

    for ssx in range(2):
        for xn in range(MTnumber):
            Nma[ssx][xn][0]=len(kinam[ssx][xn][0])
            Nma[ssx][xn][1]=len(kinam[ssx][xn][1])
            for sik in range(2):
                Nma1[sik][ssx][xn][0]=len(kinam1[sik][ssx][xn][0])
                Nma1[sik][ssx][xn][1]=len(kinam1[sik][ssx][xn][1])
    nunum1=[[0 for i in range(2)]for i in range(2)]
    nunum=[0 for i in range(2)]
    for ssx in range(2):
        for xn in range(MTnumber):
            for xbb in range(Nma[ssx][xn][0]):
                if kinam[ssx][xn][0][xbb]==1 and kinbm[ssx][xn][0][xbb]==1:
                    nunum[0]+=1
            for xbb in range(Nma[ssx][xn][1]):
                if kinam[ssx][xn][1][xbb]==1 and kinbm[ssx][xn][1][xbb]==1:
                    nunum[1]+=1
            for sik in range(2):
                for xbb in range(Nma1[sik][ssx][xn][0]):
                    if kinam1[sik][ssx][xn][0][xbb]==1 and kinbm1[sik][ssx][xn][0][xbb]==1:
                        nunum1[sik][0]+=1
                for xbb in range(Nma1[sik][ssx][xn][1]):
                    if kinam1[sik][ssx][xn][1][xbb]==1 and kinbm1[sik][ssx][xn][1][xbb]==1:
                        nunum1[sik][1]+=1
    xn=MTnumber-1
    ssx=0
    for sik in range(2):
        
        Fmt1=Kp1*(l1l[sik]-Xpole)
        Fmt4=Kp1*(Xpo-l4r[sik])
        
        for ssx in range(2):
            for xn in range(MTnumber-1):
                for ton1 in range(Nma1[sik][ssx][xn][0]):
                    if kinam1[sik][ssx][xn][0][ton1]==1 and kinbm1[sik][ssx][xn][0][ton1]==1:
                        dxnuma1=numa1[sik][ssx][xn][0][ton1][0]-numa1[sik][ssx][xn][0][ton1][1]
                        for to2 in range(xn,MTnumber-1):
                            dxnuma1+=overlap[sik][ssx][0][to2]-overlap[sik][ssx][1][to2]
                        Fmt1+=Kpn5*dxnuma1
                for ton1 in range(Nma1[sik][ssx][xn][1]):
                    if kinam1[sik][ssx][xn][1][ton1]==1 and kinbm1[sik][ssx][xn][1][ton1]==1:
                        dxnuma1=numa1[sik][ssx][xn][1][ton1][0]-numa1[sik][ssx][xn][1][ton1][1]
                        for to2 in range(xn,MTnumber-1):
                            dxnuma1+=-overlap[sik][ssx][3][to2]+overlap[sik][ssx][2][to2]
                        Fmt4-=Kpn5*dxnuma1
        
        vs=0
        if abs(Fmt1)-Fxing>0:
            vs=alp*(abs(Fmt1)-Fxing)
        ran1 = random.uniform(0, 1)
        if ran1 <vs*h/dn:
            if Fmt1<=0:
                for sn in range(2):
                    overlap[sik][sn][0][MTnumber-2]-=dn
                l1l[sik]-=dn
                hua1[sik]-=dn
                pan1=1
                panx=1
            if Fmt1>0:
                for sn in range(2):
                    overlap[sik][sn][0][MTnumber-2]+=dn
                l1l[sik]+=dn
                hua1[sik]+=dn
                pan1=1
                panx=1
        vs=alp*(abs(Fmt4)-Fxing)
        ran1 = random.uniform(0, 1)
        if ran1 <vs*h/dn:
            if Fmt4<=0:
                for sn in range(2):
                    overlap[sik][sn][3][MTnumber-2]-=dn
                l4r[sik]+=dn
                hua4[sik]+=dn
                pan1=1
                panx=1
            if Fmt4>0:
                for sn in range(2):
                    overlap[sik][sn][3][MTnumber-2]+=dn
                l4r[sik]-=dn
                hua4[sik]-=dn
                pan1=1
                panx=1
        if panx==1:   
            panx=0
            pan1=1
            ckF,de0,de1,de2,de3,de4,de5,de6,de7=checkF()
            if ckF==1:
                for x2 in range(pair):
                    for xn in range(nu[x2]):
                        if kina[x2][xn]==1:
                            motor[x2][xn][0]+=de1[x2]
                        if kinb[x2][xn]==1:
                            motor[x2][xn][1]+=de2[x2]
                    for xn in range(nu1[x2]):
                        if kinap[x2][xn]==1:
                            motorp[x2][xn][0]+=de3[x2]
                        if kinbp[x2][xn]==1:
                            motorp[x2][xn][1]+=de2[x2]
                    for xn in range(nu1x[x2]):
                        if kinapx[x2][xn]==1:
                            motorpx[x2][xn][0]+=de4[x2]
                        if kinbpx[x2][xn]==1:
                            motorpx[x2][xn][1]+=de1[x2]
                    for ssx in range(2):
                        for xn in range(numc1[x2][ssx]):
                            motormc1[x2][ssx][xn]+=de3[x2]
                        for xn in range(numc2[x2][ssx]):
                            motormc2[x2][ssx][xn]+=de1[x2]
                        for xn in range(numc3[x2][ssx]):
                            motormc3[x2][ssx][xn]+=de2[x2]
                        for xn in range(numc4[x2][ssx]):
                            motormc4[x2][ssx][xn]+=de4[x2]
                        for xn in range(MTnumber+1):
                            node1[x2][ssx][0][xn]+=de3[x2]
                            node1[x2][ssx][1][xn]+=de1[x2]
                            node1[x2][ssx][2][xn]+=de2[x2]
                            node1[x2][ssx][3][xn]+=de4[x2]

                    l2l[x2]+=de1[x2]
                    l2r[x2]+=de1[x2]
                    l3l[x2]+=de2[x2]
                    l3r[x2]+=de2[x2]
                    l1l[x2]+=de3[x2]
                    l1r[x2]+=de3[x2]
                    l4l[x2]+=de4[x2]
                    l4r[x2]+=de4[x2]
                    Ximt2[x2]+=de1[x2]
                    Ximt3[x2]+=de2[x2]
                    Xkmt1[x2]+=de3[x2]
                    Xkmt4[x2]+=de4[x2]

                for ssx in range(2):
                    for xn in range(MTnumber):
                        for ton1 in range(Nma[ssx][xn][0]):   
                            if kinam[ssx][xn][0][ton1]==1:
                                numa[ssx][xn][0][ton1][0]+=de1[0]
                            if kinbm[ssx][xn][0][ton1]==1:
                                numa[ssx][xn][0][ton1][1]+=de1[1]
                        for ton1 in range(Nma[ssx][xn][1]):   
                            if kinam[ssx][xn][1][ton1]==1:
                                numa[ssx][xn][1][ton1][0]+=de2[0]
                            if kinbm[ssx][xn][1][ton1]==1:
                                numa[ssx][xn][1][ton1][1]+=de2[1]
                        for sik in range(2):
                            for ton1 in range(Nma1[sik][ssx][xn][0]):   
                                if kinam1[sik][ssx][xn][0][ton1]==1:
                                    numa1[sik][ssx][xn][0][ton1][0]+=de3[sik]
                                if kinbm1[sik][ssx][xn][0][ton1]==1:
                                    numa1[sik][ssx][xn][0][ton1][1]+=de1[sik]
                            for ton1 in range(Nma1[sik][ssx][xn][1]):   
                                if kinam1[sik][ssx][xn][1][ton1]==1:
                                    numa1[sik][ssx][xn][1][ton1][0]+=de4[sik]
                                if kinbm1[sik][ssx][xn][1][ton1]==1:
                                    numa1[sik][ssx][xn][1][ton1][1]+=de2[sik]
                Xpole+=de0
                Xpo+=de7
                Xkin+=de5
                Xkin1+=de6
                ypsl0=energy0()
                ypsl0p=ypsl0
                ypsl0px=ypsl0
                ckF,de0,de1,de2,de3,de4,de5,de6,de7=checkF()
                if ckF==1:
                    for x2 in range(pair):
                        for xn in range(nu[x2]):
                            if kina[x2][xn]==1:
                                motor[x2][xn][0]+=de1[x2]
                            if kinb[x2][xn]==1:
                                motor[x2][xn][1]+=de2[x2]
                        for xn in range(nu1[x2]):
                            if kinap[x2][xn]==1:
                                motorp[x2][xn][0]+=de3[x2]
                            if kinbp[x2][xn]==1:
                                motorp[x2][xn][1]+=de2[x2]
                        for xn in range(nu1x[x2]):
                            if kinapx[x2][xn]==1:
                                motorpx[x2][xn][0]+=de4[x2]
                            if kinbpx[x2][xn]==1:
                                motorpx[x2][xn][1]+=de1[x2]


                        for ssx in range(2):
                            for xn in range(numc1[x2][ssx]):
                                motormc1[x2][ssx][xn]+=de3[x2]
                            for xn in range(numc2[x2][ssx]):
                                motormc2[x2][ssx][xn]+=de1[x2]
                            for xn in range(numc3[x2][ssx]):
                                motormc3[x2][ssx][xn]+=de2[x2]
                            for xn in range(numc4[x2][ssx]):
                                motormc4[x2][ssx][xn]+=de4[x2]
                            for xn in range(MTnumber+1):
                                node1[x2][ssx][0][xn]+=de3[x2]
                                node1[x2][ssx][1][xn]+=de1[x2]
                                node1[x2][ssx][2][xn]+=de2[x2]
                                node1[x2][ssx][3][xn]+=de4[x2]

                        l2l[x2]+=de1[x2]
                        l2r[x2]+=de1[x2]
                        l3l[x2]+=de2[x2]
                        l3r[x2]+=de2[x2]
                        l1l[x2]+=de3[x2]
                        l1r[x2]+=de3[x2]
                        l4l[x2]+=de4[x2]
                        l4r[x2]+=de4[x2]
                        Ximt2[x2]+=de1[x2]
                        Ximt3[x2]+=de2[x2]
                        Xkmt1[x2]+=de3[x2]
                        Xkmt4[x2]+=de4[x2]
                    for ssx in range(2):
                        for xn in range(MTnumber):
                            for ton1 in range(Nma[ssx][xn][0]):   
                                if kinam[ssx][xn][0][ton1]==1:
                                    numa[ssx][xn][0][ton1][0]+=de1[0]
                                if kinbm[ssx][xn][0][ton1]==1:
                                    numa[ssx][xn][0][ton1][1]+=de1[1]
                            for ton1 in range(Nma[ssx][xn][1]):   
                                if kinam[ssx][xn][1][ton1]==1:
                                    numa[ssx][xn][1][ton1][0]+=de2[0]
                                if kinbm[ssx][xn][1][ton1]==1:
                                    numa[ssx][xn][1][ton1][1]+=de2[1]
                            for sik in range(2):
                                for ton1 in range(Nma1[sik][ssx][xn][0]):   
                                    if kinam1[sik][ssx][xn][0][ton1]==1:
                                        numa1[sik][ssx][xn][0][ton1][0]+=de3[sik]
                                    if kinbm1[sik][ssx][xn][0][ton1]==1:
                                        numa1[sik][ssx][xn][0][ton1][1]+=de1[sik]
                                for ton1 in range(Nma1[sik][ssx][xn][1]):   
                                    if kinam1[sik][ssx][xn][1][ton1]==1:
                                        numa1[sik][ssx][xn][1][ton1][0]+=de4[sik]
                                    if kinbm1[sik][ssx][xn][1][ton1]==1:
                                        numa1[sik][ssx][xn][1][ton1][1]+=de2[sik]
                    Xpole+=de0
                    Xpo+=de7
                    Xkin+=de5
                    Xkin1+=de6
                    ypsl0=energy0()
                    ypsl0p=ypsl0
                    ypsl0px=ypsl0 
                    print(kk)
    for sn in range(2):
        for nn in range(MTnumber):
            if nn==MTnumber-1 and sn==1:
                continue
            ss1=min(node1[0][sn][1][nn+1]-node1[0][sn][1][nn],node1[1][sn][1][nn+1]-node1[1][sn][1][nn])#2MT
            ss2=min(node1[0][sn][2][nn]-node1[0][sn][2][nn+1],node1[1][sn][2][nn]-node1[1][sn][2][nn+1])#3Mt
            Nma[sn][nn][0]=len(numa[sn][nn][0])
            Nma[sn][nn][1]=len(numa[sn][nn][1])
    #############################NUma
            ran4 = random.uniform(0, 1)
            alp1=1
            if nn==MTnumber-1:
                alp1=pi1
            if ran4 < alp1*konnu*round(ss1/d-sum(kinam[sn][nn][0]))*h:
                cx0=node1[0][sn][1][nn]+round(ss1*random.uniform(0,1)/d)*d
                numa[sn][nn][0].append([cx0,cx0])
                kinam[sn][nn][0].append(1)
                kinbm[sn][nn][0].append(0)
                Nma[sn][nn][0]+=1

            ran4 = random.uniform(0, 1)
            if ran4 <  alp1*konnu*round(ss1/d-sum(kinbm[sn][nn][0]))*h:
                cx0=node1[1][sn][1][nn]+round(ss1*random.uniform(0,1)/d)*d
                numa[sn][nn][0].append([cx0,cx0])
                kinam[sn][nn][0].append(0)
                kinbm[sn][nn][0].append(1)
                Nma[sn][nn][0]+=1
            ran4 = random.uniform(0, 1)
            if ran4 <  alp1*konnu*round(ss2/d-sum(kinam[sn][nn][1]))*h:
                cx0=node1[0][sn][2][nn+1]+round(ss2*random.uniform(0,1)/d)*d
                numa[sn][nn][1].append([cx0,cx0])
                kinam[sn][nn][1].append(1)
                kinbm[sn][nn][1].append(0)
                Nma[sn][nn][1]+=1
            ran4 = random.uniform(0, 1)
            if ran4 <  alp1*konnu*round(ss2/d-sum(kinbm[sn][nn][1]))*h:
                cx0=node1[1][sn][2][nn+1]+round(ss2*random.uniform(0,1)/d)*d
                numa[sn][nn][1].append([cx0,cx0])
                kinam[sn][nn][1].append(0)
                kinbm[sn][nn][1].append(1)
                Nma[sn][nn][1]+=1
            for xbb in range(Nma[sn][nn][0]):
                if xbb>=Nma[sn][nn][0]-0.1:
                    continue
                if kinam[sn][nn][0][xbb]==1 or kinbm[sn][nn][0][xbb]==1:
                    if numa[sn][nn][0][xbb][0]>node1[0][sn][1][nn+1] or numa[sn][nn][0][xbb][0]<node1[0][sn][1][nn] or numa[sn][nn][0][xbb][1]>node1[1][sn][1][nn+1] or numa[sn][nn][0][xbb][1]<node1[1][sn][1][nn]:
                        if kinam[sn][nn][0][xbb]==1 and kinbm[sn][nn][0][xbb]==1:
                            kinam[sn][nn][0][xbb]=0;kinbm[sn][nn][0][xbb]=0
                            nunum[0]-=1
                            panx=1
                            pan1=1
                        Nma[sn][nn][0]-=1
                        del kinam[sn][nn][0][xbb]
                        del kinbm[sn][nn][0][xbb]
                        del numa[sn][nn][0][xbb]
                        continue
                if kinam[sn][nn][0][xbb]==1 and kinbm[sn][nn][0][xbb]==1:
                    ovx=0
                    for to2 in range(nn,MTnumber-1):
                        ovx+=overlap[0][sn][1][to2]-overlap[1][sn][1][to2]
                    F=Kpn5*(numa[sn][nn][0][xbb][0]-numa[sn][nn][0][xbb][1]+ovx)
                    kinam[sn][nn][0][xbb]=disnuma(F)
                    kinbm[sn][nn][0][xbb]=disnuma(F)
                    if kinam[sn][nn][0][xbb]+kinbm[sn][nn][0][xbb]<2:
                        nunum[0]-=1
                        panx=1
                        pan1=1
                if kinam[sn][nn][0][xbb]==1 and kinbm[sn][nn][0][xbb]==0:
                    kinam[sn][nn][0][xbb]=disnuma(0)
                    ran4 = random.uniform(0, 1)
                    if ran4 < unu*h and kinam[sn][nn][0][xbb]==1:
                        lian1=0
                        kinbm[sn][nn][0][xbb]=1
                        ovx=0
                        for to2 in range(nn,MTnumber-1):
                            ovx+=overlap[0][sn][1][to2]-overlap[1][sn][1][to2]
                        for xn in range(Nma[sn][nn][0]):
                            if kinbm[sn][nn][0][xn]==1 and xn!=xbb and abs(node1[1][sn][1][nn]+round((numa[sn][nn][0][xbb][0]-node1[1][sn][1][nn]+ovx)/d)*d-numa[sn][nn][0][xn][1])<1:
                                lian1=1
                                break
                        if lian1==1:
                            if node1[1][sn][1][nn+1]+round((numa[sn][nn][0][xbb][0]-node1[1][sn][1][nn]+ovx)/d)*d>=numa[sn][nn][0][xbb][0]:
                                la=(round((numa[sn][nn][0][xbb][0]-node1[1][sn][1][nn]+ovx)/d)-1)*d
                            if node1[1][sn][1][nn+1]+round((numa[sn][nn][0][xbb][0]-node1[1][sn][1][nn]+ovx)/d)*d<numa[sn][nn][0][xbb][0]:
                                la=(round((numa[sn][nn][0][xbb][0]-node1[1][sn][1][nn]+ovx)/d)+1)*d
                            for xn in range(Nma[sn][nn][0]):
                                if kinbm[sn][nn][0][xn]==1 and xn!=xbb and abs(node1[1][sn][1][nn]+la-numa[sn][nn][0][xn][1])<1:
                                    lian1=2
                                    break
                        if lian1==0:
                            numa[sn][nn][0][xbb][1]=node1[1][sn][1][nn]+round((numa[sn][nn][0][xbb][0]-node1[1][sn][1][nn]+ovx)/d)*d
                        if lian1==1:
                            numa[sn][nn][0][xbb][1]=node1[1][sn][1][nn]+la
                        if lian1==2:
                            kinbm[sn][nn][0][xbb]=0
                        if lian1==0 or lian1==1:
                            panx=1
                            nunum[0]+=1
                            pan1=1
                if kinam[sn][nn][0][xbb]==0 and kinbm[sn][nn][0][xbb]==1:
                    
                    kinbm[sn][nn][0][xbb]=disnuma(0)
                    ran4 = random.uniform(0, 1)
                    if ran4 < unu*h and kinbm[sn][nn][0][xbb]==1:
                        lian1=0
                        kinam[sn][nn][0][xbb]=1
                        ovx=0
                        for to2 in range(nn,MTnumber-1):
                            ovx+=overlap[0][sn][1][to2]-overlap[1][sn][1][to2]
                        for xn in range(Nma[sn][nn][0]):
                            if kinam[sn][nn][0][xn]==1 and xn!=xbb and abs(node1[0][sn][1][nn]+round((numa[sn][nn][0][xbb][1]-node1[0][sn][1][nn]-ovx)/d)*d-numa[sn][nn][0][xn][0])<1:
                                lian1=1
                                break
                        if lian1==1:
                            if node1[0][sn][1][nn]+round((numa[sn][nn][0][xbb][1]-node1[0][sn][1][nn]-ovx)/d)*d>=numa[sn][nn][0][xbb][1]:
                                la=(round((numa[sn][nn][0][xbb][1]-node1[0][sn][1][nn]-ovx)/d)-1)*d
                            if node1[0][sn][1][nn]+round((numa[sn][nn][0][xbb][1]-node1[0][sn][1][nn]-ovx)/d)*d<numa[sn][nn][0][xbb][1]:
                                la=(round((numa[sn][nn][0][xbb][1]-node1[0][sn][1][nn]-ovx)/d)+1)*d
                            for xn in range(Nma[sn][nn][0]):
                                if kinbm[sn][nn][0][xn]==1 and xn!=xbb and abs(node1[0][sn][1][nn]+la-numa[sn][nn][0][xn][0])<1:
                                    lian1=2
                                    break
                        if lian1==0:
                            numa[sn][nn][0][xbb][0]=node1[0][sn][1][nn]+round((numa[sn][nn][0][xbb][1]-node1[0][sn][1][nn]-ovx)/d)*d
                        if lian1==1:
                            numa[sn][nn][0][xbb][0]=node1[0][sn][1][nn]+la
                        if lian1==2:
                            kinam[sn][nn][0][xbb]=0
                        if lian1==0 or lian1==1:
                            panx=1
                            nunum[0]+=1
                            pan1=1
                if kinam[sn][nn][0][xbb]==0 and kinbm[sn][nn][0][xbb]==0:
                    Nma[sn][nn][0]-=1
                    del kinam[sn][nn][0][xbb]
                    del kinbm[sn][nn][0][xbb]
                    del numa[sn][nn][0][xbb]
                    continue
            for xbb in range(Nma[sn][nn][1]):
                if xbb>=Nma[sn][nn][1]-0.1:
                    continue
                if kinam[sn][nn][1][xbb]==1 or kinbm[sn][nn][1][xbb]==1:
                    if numa[sn][nn][1][xbb][0]>node1[0][sn][2][nn] or numa[sn][nn][1][xbb][0]<node1[0][sn][2][nn+1] or numa[sn][nn][1][xbb][1]>node1[1][sn][2][nn] or numa[sn][nn][1][xbb][1]<node1[1][sn][2][nn+1]:
                        if kinam[sn][nn][1][xbb]==1 and kinbm[sn][nn][1][xbb]==1:
                            kinam[sn][nn][1][xbb]=0;kinbm[sn][nn][1][xbb]=0
                            nunum[1]-=1
                            panx=1
                            pan1=1
                        Nma[sn][nn][1]-=1
                        del kinam[sn][nn][1][xbb]
                        del kinbm[sn][nn][1][xbb]
                        del numa[sn][nn][1][xbb]
                        continue
                if kinam[sn][nn][1][xbb]==1 and kinbm[sn][nn][1][xbb]==1:
                    ovx=0
                    for to2 in range(nn,MTnumber-1):
                        ovx+=-overlap[0][sn][2][to2]+overlap[1][sn][2][to2]
                    F=Kpn5*(numa[sn][nn][1][xbb][0]-numa[sn][nn][1][xbb][1]+ovx)
                    kinam[sn][nn][1][xbb]=disnuma(F)
                    kinbm[sn][nn][1][xbb]=disnuma(F)
                    if kinam[sn][nn][1][xbb]+kinbm[sn][nn][1][xbb]<2:
                        nunum[1]-=1
                        panx=1
                        pan1=1
                if kinam[sn][nn][1][xbb]==1 and kinbm[sn][nn][1][xbb]==0:
                    kinam[sn][nn][1][xbb]=disnuma(0)
                    ran4 = random.uniform(0, 1)
                    if ran4 < unu*h and kinam[sn][nn][1][xbb]==1:
                        kinbm[sn][nn][1][xbb]=1
                        lian1=0
                        ovx=0
                        for to2 in range(nn,MTnumber-1):
                            ovx+=-overlap[0][sn][2][to2]+overlap[1][sn][2][to2]
                        for xn in range(Nma[sn][nn][1]):
                            if kinbm[sn][nn][1][xn]==1 and xn!=xbb and abs(node1[1][sn][2][nn+1]+round((numa[sn][nn][1][xbb][0]-node1[1][sn][2][nn+1]+ovx)/d)*d-numa[sn][nn][1][xn][1])<1:
                                lian1=1
                                break
                        if lian1==1:
                            if l3l[1]+round((numa[sn][nn][1][xbb][0]-node1[1][sn][2][nn+1]+ovx)/d)*d>=numa[sn][nn][1][xbb][0]:
                                la=(round((numa[sn][nn][1][xbb][0]-node1[1][sn][2][nn+1]+ovx)/d)-1)*d
                            if l3l[1]+round((numa[sn][nn][1][xbb][0]-node1[1][sn][2][nn+1]+ovx)/d)*d<numa[sn][nn][1][xbb][0]:
                                la=(round((numa[sn][nn][1][xbb][0]-node1[1][sn][2][nn+1]+ovx)/d)+1)*d
                            for xn in range(Nma[sn][nn][1]):
                                if kinbm[sn][nn][1][xn]==1 and xn!=xbb and abs(node1[1][sn][2][nn+1]+la-numa[sn][nn][1][xn][1])<1:
                                    lian1=2
                                    break
                        if lian1==0:
                            numa[sn][nn][1][xbb][1]=node1[1][sn][2][nn+1]+round((numa[sn][nn][1][xbb][0]-l3l[1]+ovx)/d)*d
                        if lian1==1:
                            numa[sn][nn][1][xbb][1]=node1[1][sn][2][nn+1]+la
                        if lian1==2:
                            kinbm[sn][nn][1][xbb]=0
                        if lian1==0 or lian1==1:
                            panx=1
                            nunum[1]+=1
                            pan1=1
                if kinam[sn][nn][1][xbb]==0 and kinbm[sn][nn][1][xbb]==1:
                    kinbm[sn][nn][1][xbb]=disnuma(0)
                    ran4 = random.uniform(0, 1)
                    if ran4 < unu*h and kinbm[sn][nn][1][xbb]==1:
                        kinam[sn][nn][1][xbb]=1
                        lian1=0
                        ovx=0
                        for to2 in range(nn,MTnumber-1):
                            ovx+=-overlap[0][sn][2][to2]+overlap[1][sn][2][to2]
                        for xn in range(Nma[sn][nn][1]):
                            if kinam[sn][nn][1][xn]==1 and xn!=xbb and abs(node1[0][sn][2][nn+1]+round((numa[sn][nn][1][xbb][1]-node1[0][sn][2][nn+1]-ovx)/d)*d-numa[sn][nn][1][xn][0])<1:
                                lian1=1
                                break
                        if lian1==1:
                            if node1[0][sn][2][nn+1]+round((numa[sn][nn][1][xbb][1]-node1[0][sn][2][nn+1]-ovx)/d)*d>=numa[sn][nn][1][xbb][1]:
                                la=(round((numa[sn][nn][1][xbb][1]-node1[0][sn][2][nn+1]-ovx)/d)-1)*d
                            if node1[0][sn][2][nn+1]+round((numa[sn][nn][1][xbb][1]-node1[0][sn][2][nn+1]-ovx)/d)*d<numa[sn][nn][1][xbb][1]:
                                la=(round((numa[sn][nn][1][xbb][1]-node1[0][sn][2][nn+1]-ovx)/d)+1)*d
                            for xn in range(Nma[sn][nn][1]):
                                if kinbm[sn][nn][1][xn]==1 and xn!=xbb and abs(node1[0][sn][2][nn+1]+la-numa[sn][nn][1][xn][0])<1:
                                    lian1=2
                                    break
                        if lian1==0:
                            numa[sn][nn][1][xbb][0]=node1[0][sn][2][nn+1]+round((numa[sn][nn][1][xbb][1]-node1[0][sn][2][nn+1]-ovx)/d)*d
                        if lian1==1:
                            numa[sn][nn][1][xbb][0]=node1[0][sn][2][nn+1]+la
                        if lian1==2:
                            kinam[sn][nn][1][xbb]=0
                        if lian1==0 or lian1==1:
                            panx=1
                            nunum[1]+=1
                            pan1=1
                if kinam[sn][nn][1][xbb]==0 and kinbm[sn][nn][1][xbb]==0:
                    Nma[sn][nn][1]-=1
                    del kinam[sn][nn][1][xbb]
                    del kinbm[sn][nn][1][xbb]
                    del numa[sn][nn][1][xbb]
                    continue
            alp1=1
            if nn==MTnumber-1:
                alp1=pi1
            for sik in range(2):
                ss1=min(node1[sik][sn][0][nn+1]-node1[sik][sn][0][nn],node1[sik][sn][1][nn+1]-node1[sik][sn][1][nn])#1MT
                ss2=min(node1[sik][sn][3][nn]-node1[sik][sn][3][nn+1],node1[sik][sn][2][nn]-node1[sik][sn][2][nn+1])#4Mt
                Nma1[sik][sn][nn][0]=len(numa1[sik][sn][nn][0])
                Nma1[sik][sn][nn][1]=len(numa1[sik][sn][nn][1])
                ################################################################
                ran4 = random.uniform(0, 1)
            
                if ran4 < alp1*konnu*round(ss1/d-sum(kinam1[sik][sn][nn][0]))*h:
                    cx0=node1[sik][sn][0][nn]+round((node1[sik][sn][0][nn+1]-node1[sik][sn][0][nn])*random.uniform(0,1)/d)*d
                    numa1[sik][sn][nn][0].append([cx0,cx0])
                    kinam1[sik][sn][nn][0].append(1)
                    kinbm1[sik][sn][nn][0].append(0)
                    Nma1[sik][sn][nn][0]+=1
                ran4 = random.uniform(0, 1)
                if ran4 < alp1*konnu*round(ss1/d-sum(kinam1[sik][sn][nn][0]))*h:
                    cx0=node1[sik][sn][1][nn]+round((node1[sik][sn][1][nn+1]-node1[sik][sn][1][nn])*random.uniform(0,1)/d)*d
                    numa1[sik][sn][nn][0].append([cx0,cx0])
                    kinam1[sik][sn][nn][0].append(0)
                    kinbm1[sik][sn][nn][0].append(1)
                    Nma1[sik][sn][nn][0]+=1
                ran4 = random.uniform(0, 1)
                if ran4 < alp1*konnu*round(ss2/d-sum(kinam1[sik][sn][nn][1]))*h:
                    cx0=node1[sik][sn][3][nn+1]+round((node1[sik][sn][3][nn]-node1[sik][sn][3][nn+1])*random.uniform(0,1)/d)*d
                    numa1[sik][sn][nn][1].append([cx0,cx0])
                    kinam1[sik][sn][nn][1].append(1)
                    kinbm1[sik][sn][nn][1].append(0)
                    Nma1[sik][sn][nn][1]+=1
                ran4 = random.uniform(0, 1)
                if ran4 < alp1*konnu*round(ss2/d-sum(kinam1[sik][sn][nn][1]))*h:
                    cx0=node1[sik][sn][2][nn+1]+round((node1[sik][sn][2][nn]-node1[sik][sn][2][nn+1])*random.uniform(0,1)/d)*d
                    numa1[sik][sn][nn][1].append([cx0,cx0])
                    kinam1[sik][sn][nn][1].append(0)
                    kinbm1[sik][sn][nn][1].append(1)
                    Nma1[sik][sn][nn][1]+=1
                for xbb in range(Nma1[sik][sn][nn][0]):
                    if xbb>=Nma1[sik][sn][nn][0]-0.1:
                        continue
                    if kinam1[sik][sn][nn][0][xbb]==1 or kinbm1[sik][sn][nn][0][xbb]==1:
                        if numa1[sik][sn][nn][0][xbb][0]>node1[sik][sn][0][nn+1] or numa1[sik][sn][nn][0][xbb][0]<node1[sik][sn][0][nn] or numa1[sik][sn][nn][0][xbb][1]>node1[sik][sn][1][nn+1] or numa1[sik][sn][nn][0][xbb][1]<node1[sik][sn][1][nn]:
                            
                            if kinam1[sik][sn][nn][0][xbb]==1 and kinbm1[sik][sn][nn][0][xbb]==1:
                                kinam1[sik][sn][nn][0][xbb]=0;kinbm1[sik][sn][nn][0][xbb]=0
                                nunum1[sik][0]-=1
                                panx=1
                                pan1=1
                            Nma1[sik][sn][nn][0]-=1
                            del kinam1[sik][sn][nn][0][xbb]
                            del kinbm1[sik][sn][nn][0][xbb]
                            del numa1[sik][sn][nn][0][xbb]
                            continue
                    
                    if kinam1[sik][sn][nn][0][xbb]==1 and kinbm1[sik][sn][nn][0][xbb]==1:
                        ovx=0
                        for to2 in range(nn,MTnumber-1):
                            ovx+=overlap[sik][sn][0][to2]-overlap[sik][sn][1][to2]
                        F=Kpn5*(numa1[sik][sn][nn][0][xbb][0]-numa1[sik][sn][nn][0][xbb][1]+ovx)
                        kinam1[sik][sn][nn][0][xbb]=disnuma(F)
                        kinbm1[sik][sn][nn][0][xbb]=disnuma(F)
                        if kinam1[sik][sn][nn][0][xbb]+kinbm1[sik][sn][nn][0][xbb]<2:
                            nunum1[sik][0]-=1
                            panx=1
                            pan1=1
                    if kinam1[sik][sn][nn][0][xbb]==0 and kinbm1[sik][sn][nn][0][xbb]==0:
                        Nma1[sik][sn][nn][0]-=1
                        del kinam1[sik][sn][nn][0][xbb]
                        del kinbm1[sik][sn][nn][0][xbb]
                        del numa1[sik][sn][nn][0][xbb]
                        continue
                    if kinam1[sik][sn][nn][0][xbb]==1 and kinbm1[sik][sn][nn][0][xbb]==0:
                        kinam1[sik][sn][nn][0][xbb]=disnuma(0)
                        ran4 = random.uniform(0, 1)
                        if ran4 < unu*h and kinam1[sik][sn][nn][0][xbb]==1:
                            lian1=0
                            kinbm1[sik][sn][nn][0][xbb]=1
                            ovx=0
                            for to2 in range(nn,MTnumber-1):
                                ovx+=overlap[sik][sn][0][to2]-overlap[sik][sn][1][to2]
                            for xn in range(Nma1[sik][sn][nn][0]):
                                if kinbm1[sik][sn][nn][0][xn]==1 and xn!=xbb and abs(node1[sik][sn][1][nn]+round((numa1[sik][sn][nn][0][xbb][0]-node1[sik][sn][1][nn]+ovx)/d)*d-numa1[sik][sn][nn][0][xn][1])<1:
                                    lian1=1
                                    break
                            if lian1==1:
                                if node1[sik][sn][1][nn]+round((numa1[sik][sn][nn][0][xbb][0]-node1[sik][sn][1][nn]+ovx)/d)*d>=numa1[sik][sn][nn][0][xbb][0]:
                                    la=(round((numa1[sik][sn][nn][0][xbb][0]-node1[sik][sn][1][nn]+ovx)/d)-1)*d
                                if node1[sik][sn][1][nn]+round((numa1[sik][sn][nn][0][xbb][0]-node1[sik][sn][1][nn]+ovx)/d)*d<numa1[sik][sn][nn][0][xbb][0]:
                                    la=(round((numa1[sik][sn][nn][0][xbb][0]-node1[sik][sn][1][nn]+ovx)/d)+1)*d
                                for xn in range(Nma1[sik][sn][nn][0]):
                                    if kinbm1[sik][sn][nn][0][xn]==1 and xn!=xbb and abs(node1[sik][sn][1][nn]+la-numa1[sik][sn][nn][0][xn][1])<1:
                                        lian1=2
                                        break
                            if lian1==0:
                                numa1[sik][sn][nn][0][xbb][1]=node1[sik][sn][1][nn]+round((numa1[sik][sn][nn][0][xbb][0]-node1[sik][sn][1][nn]+ovx)/d)*d
                            if lian1==1:
                                numa1[sik][sn][nn][0][xbb][1]=node1[sik][sn][1][nn]+la
                            if lian1==2:
                                kinbm1[sik][sn][nn][0][xbb]=0
                            if lian1==0 or lian1==1:
                                panx=1
                                nunum1[sik][0]+=1
                                pan1=1
                                #print(numa1[sik][sn][nn][0][xbb][0]-numa1[sik][sn][nn][0][xbb][1]+ovx,'11')
                    if kinam1[sik][sn][nn][0][xbb]==0 and kinbm1[sik][sn][nn][0][xbb]==1:
                        kinbm1[sik][sn][nn][0][xbb]=disnuma(0)
                        ran4 = random.uniform(0, 1)
                        if ran4 < unu*h and kinbm1[sik][sn][nn][0][xbb]==1:
                            lian1=0
                            kinam1[sik][sn][nn][0][xbb]=1
                            ovx=0
                            for to2 in range(nn,MTnumber-1):
                                ovx+=overlap[sik][sn][0][to2]-overlap[sik][sn][1][to2]
                            for xn in range(Nma1[sik][sn][nn][0]):
                                if kinam1[sik][sn][nn][0][xn]==1 and xn!=xbb and abs(node1[sik][sn][0][nn]+round((numa1[sik][sn][nn][0][xbb][1]-node1[sik][sn][0][nn]-ovx)/d)*d-numa1[sik][sn][nn][0][xn][0])<1:
                                    lian1=1
                                    break
                            if lian1==1:
                                if node1[sik][sn][0][nn]+round((numa1[sik][sn][nn][0][xbb][1]-node1[sik][sn][0][nn]-ovx)/d)*d>=numa1[sik][sn][nn][0][xbb][1]:
                                    la=(round((numa1[sik][sn][nn][0][xbb][1]-node1[sik][sn][0][nn]-ovx)/d)-1)*d
                                if node1[sik][sn][0][nn]+round((numa1[sik][sn][nn][0][xbb][1]-node1[sik][sn][0][nn]-ovx)/d)*d<numa1[sik][sn][nn][0][xbb][1]:
                                    la=(round((numa1[sik][sn][nn][0][xbb][1]-node1[sik][sn][0][nn]-ovx)/d)+1)*d
                                for xn in range(Nma1[sik][sn][nn][0]):
                                    if kinbm1[sik][sn][nn][0][xn]==1 and xn!=xbb and abs(node1[sik][sn][0][nn]+la-numa1[sik][sn][nn][0][xn][0])<1:
                                        lian1=2
                                        break
                            if lian1==0:
                                numa1[sik][sn][nn][0][xbb][0]=node1[sik][sn][0][nn]+round((numa1[sik][sn][nn][0][xbb][1]-node1[sik][sn][0][nn]-ovx)/d)*d
                            if lian1==1:
                                numa1[sik][sn][nn][0][xbb][0]=node1[sik][sn][0][nn]+la
                            if lian1==2:
                                kinam1[sik][sn][nn][0][xbb]=0
                            if lian1==0 or lian1==1:
                                panx=1
                                nunum1[sik][0]+=1
                                pan1=1
                                #print(numa1[sik][sn][nn][0][xbb][0]-numa1[sik][sn][nn][0][xbb][1]+ovx,'12')
                for xbb in range(Nma1[sik][sn][nn][1]):
                    if xbb>=Nma1[sik][sn][nn][1]-0.1:
                        continue
                    if kinam1[sik][sn][nn][1][xbb]==1 or kinbm1[sik][sn][nn][1][xbb]==1:
                        if numa1[sik][sn][nn][1][xbb][0]>node1[sik][sn][3][nn] or numa1[sik][sn][nn][1][xbb][0]<node1[sik][sn][3][nn+1] or numa1[sik][sn][nn][1][xbb][1]>node1[sik][sn][2][nn] or numa1[sik][sn][nn][1][xbb][1]<node1[sik][sn][2][nn+1]:
                            
                            if kinam1[sik][sn][nn][1][xbb]==1 and kinbm1[sik][sn][nn][1][xbb]==1:
                                kinam1[sik][sn][nn][1][xbb]=0;kinbm1[sik][sn][nn][1][xbb]=0
                                nunum1[sik][1]-=1
                                panx=1
                                pan1=1
                            Nma1[sik][sn][nn][1]-=1
                            del kinam1[sik][sn][nn][1][xbb]
                            del kinbm1[sik][sn][nn][1][xbb]
                            del numa1[sik][sn][nn][1][xbb]
                            continue
                    if kinam1[sik][sn][nn][1][xbb]==1 and kinbm1[sik][sn][nn][1][xbb]==1:
                        ovx=0
                        for to2 in range(nn,MTnumber-1):
                            ovx+=-overlap[sik][sn][3][to2]+overlap[sik][sn][2][to2]
                        F=Kpn5*(numa1[sik][sn][nn][1][xbb][0]-numa1[sik][sn][nn][1][xbb][1]+ovx)
                        kinam1[sik][sn][nn][1][xbb]=disnuma(F)
                        kinbm1[sik][sn][nn][1][xbb]=disnuma(F)
                        if kinam1[sik][sn][nn][1][xbb]+kinbm1[sik][sn][nn][1][xbb]<2:
                            nunum1[sik][1]-=1
                            panx=1
                            pan1=1
                    if kinam1[sik][sn][nn][1][xbb]==0 and kinbm1[sik][sn][nn][1][xbb]==0:
                        Nma1[sik][sn][nn][1]-=1
                        del kinam1[sik][sn][nn][1][xbb]
                        del kinbm1[sik][sn][nn][1][xbb]
                        del numa1[sik][sn][nn][1][xbb]
                        continue
                    if kinam1[sik][sn][nn][1][xbb]==1 and kinbm1[sik][sn][nn][1][xbb]==0:
                        kinam1[sik][sn][nn][1][xbb]=disnuma(0)
                        ran4 = random.uniform(0, 1)
                        if ran4 < unu*h and kinam1[sik][sn][nn][1][xbb]==1:
                            kinbm1[sik][sn][nn][1][xbb]=1
                            lian1=0
                            ovx=0
                            for to2 in range(nn,MTnumber-1):
                                ovx+=-overlap[sik][sn][3][to2]+overlap[sik][sn][2][to2]
                            for xn in range(Nma1[sik][sn][nn][1]):
                                if kinbm1[sik][sn][nn][1][xn]==1 and xn!=xbb and abs(node1[sik][sn][2][nn+1]+round((numa1[sik][sn][nn][1][xbb][0]-node1[sik][sn][2][nn+1]+ovx)/d)*d-numa1[sik][sn][nn][1][xn][1])<1:
                                    lian1=1
                                    break
                            if lian1==1:
                                if node1[sik][sn][2][nn+1]+round((numa1[sik][sn][nn][1][xbb][0]-node1[sik][sn][2][nn+1]+ovx)/d)*d>=numa1[sik][sn][nn][1][xbb][0]:
                                    la=(round((numa1[sik][sn][nn][1][xbb][0]-node1[sik][sn][2][nn+1]+ovx)/d)-1)*d
                                if node1[sik][sn][2][nn+1]+round((numa1[sik][sn][nn][1][xbb][0]-node1[sik][sn][2][nn+1]+ovx)/d)*d<numa1[sik][sn][nn][1][xbb][0]:
                                    la=(round((numa1[sik][sn][nn][1][xbb][0]-node1[sik][sn][2][nn+1]+ovx)/d)+1)*d
                                for xn in range(Nma1[sik][sn][nn][1]):
                                    if kinbm1[sik][sn][nn][1][xn]==1 and xn!=xbb and abs(node1[sik][sn][2][nn+1]+la-numa1[sik][sn][nn][1][xn][1])<1:
                                        lian1=2
                                        break
                            if lian1==0:
                                numa1[sik][sn][nn][1][xbb][1]=node1[sik][sn][2][nn+1]+round((numa1[sik][sn][nn][1][xbb][0]-node1[sik][sn][2][nn+1]+ovx)/d)*d
                            if lian1==1:
                                numa1[sik][sn][nn][1][xbb][1]=node1[sik][sn][2][nn+1]+la
                            if lian1==2:
                                kinbm1[sik][sn][nn][1][xbb]=0
                            if lian1==0 or lian1==1:
                                panx=1
                                nunum1[sik][1]+=1
                                pan1=1
                                #print(numa1[sik][sn][nn][1][xbb][0]-numa1[sik][sn][nn][1][xbb][1]+ovx,'13')
                    if kinam1[sik][sn][nn][1][xbb]==0 and kinbm1[sik][sn][nn][1][xbb]==1:
                        kinbm1[sik][sn][nn][1][xbb]=disnuma(0)
                        ran4 = random.uniform(0, 1)
                        if ran4 < unu*h and kinbm1[sik][sn][nn][1][xbb]==1:
                            kinam1[sik][sn][nn][1][xbb]=1
                            lian1=0
                            ovx=0
                            for to2 in range(nn,MTnumber-1):
                                ovx+=-overlap[sik][sn][3][to2]+overlap[sik][sn][2][to2]
                            for xn in range(Nma1[sik][sn][nn][1]):
                                if kinam1[sik][sn][nn][1][xn]==1 and xn!=xbb and abs(node1[sik][sn][3][nn+1]+round((numa1[sik][sn][nn][1][xbb][1]-node1[sik][sn][3][nn+1]-ovx)/d)*d-numa1[sik][sn][nn][1][xn][0])<1:
                                    lian1=1
                                    break
                            if lian1==1:
                                if node1[sik][sn][3][nn+1]+round((numa1[sik][sn][nn][1][xbb][1]-node1[sik][sn][3][nn+1]-ovx)/d)*d>=numa1[sik][sn][nn][1][xbb][1]:
                                    la=(round((numa1[sik][sn][nn][1][xbb][1]-node1[sik][sn][3][nn+1]-ovx)/d)-1)*d
                                if node1[sik][sn][3][nn+1]+round((numa1[sik][sn][nn][1][xbb][1]-node1[sik][sn][3][nn+1]-ovx)/d)*d<numa1[sik][sn][nn][1][xbb][1]:
                                    la=(round((numa1[sik][sn][nn][1][xbb][1]-node1[sik][sn][3][nn+1]-ovx)/d)+1)*d
                                for xn in range(Nma1[sik][sn][nn][1]):
                                    if kinbm1[sik][sn][nn][1][xn]==1 and xn!=xbb and abs(node1[sik][sn][3][nn+1]+la-numa1[sik][sn][nn][1][xn][0])<1:
                                        lian1=2
                                        break
                            if lian1==0:
                                numa1[sik][sn][nn][1][xbb][0]=node1[sik][sn][3][nn+1]+round((numa1[sik][sn][nn][1][xbb][1]-node1[sik][sn][3][nn+1]-ovx)/d)*d
                            if lian1==1:
                                numa1[sik][sn][nn][1][xbb][0]=node1[sik][sn][3][nn+1]+la
                            if lian1==2:
                                kinam1[sik][sn][nn][1][xbb]=0
                            if lian1==0 or lian1==1:
                                panx=1
                                nunum1[sik][1]+=1
                                pan1=1
                                #print(numa1[sik][sn][nn][1][xbb][0]-numa1[sik][sn][nn][1][xbb][1]+ovx,'14')


            if panx==1:   
                panx=0
                pan1=1
                ckF,de0,de1,de2,de3,de4,de5,de6,de7=checkF()
                if ckF==1:
                    for x2 in range(pair):
                        for xn in range(nu[x2]):
                            if kina[x2][xn]==1:
                                motor[x2][xn][0]+=de1[x2]
                            if kinb[x2][xn]==1:
                                motor[x2][xn][1]+=de2[x2]
                        for xn in range(nu1[x2]):
                            if kinap[x2][xn]==1:
                                motorp[x2][xn][0]+=de3[x2]
                            if kinbp[x2][xn]==1:
                                motorp[x2][xn][1]+=de2[x2]
                        for xn in range(nu1x[x2]):
                            if kinapx[x2][xn]==1:
                                motorpx[x2][xn][0]+=de4[x2]
                            if kinbpx[x2][xn]==1:
                                motorpx[x2][xn][1]+=de1[x2]
                        for ssx in range(2):
                            for xn in range(numc1[x2][ssx]):
                                motormc1[x2][ssx][xn]+=de3[x2]
                            for xn in range(numc2[x2][ssx]):
                                motormc2[x2][ssx][xn]+=de1[x2]
                            for xn in range(numc3[x2][ssx]):
                                motormc3[x2][ssx][xn]+=de2[x2]
                            for xn in range(numc4[x2][ssx]):
                                motormc4[x2][ssx][xn]+=de4[x2]
                            for xn in range(MTnumber+1):
                                node1[x2][ssx][0][xn]+=de3[x2]
                                node1[x2][ssx][1][xn]+=de1[x2]
                                node1[x2][ssx][2][xn]+=de2[x2]
                                node1[x2][ssx][3][xn]+=de4[x2]
                        
                        l2l[x2]+=de1[x2]
                        l2r[x2]+=de1[x2]
                        l3l[x2]+=de2[x2]
                        l3r[x2]+=de2[x2]
                        l1l[x2]+=de3[x2]
                        l1r[x2]+=de3[x2]
                        l4l[x2]+=de4[x2]
                        l4r[x2]+=de4[x2]
                        Ximt2[x2]+=de1[x2]
                        Ximt3[x2]+=de2[x2]
                        Xkmt1[x2]+=de3[x2]
                        Xkmt4[x2]+=de4[x2]
                    
                    for ssx in range(2):
                        for xn in range(MTnumber):
                            for ton1 in range(Nma[ssx][xn][0]):   
                                if kinam[ssx][xn][0][ton1]==1:
                                    numa[ssx][xn][0][ton1][0]+=de1[0]
                                if kinbm[ssx][xn][0][ton1]==1:
                                    numa[ssx][xn][0][ton1][1]+=de1[1]
                            for ton1 in range(Nma[ssx][xn][1]):   
                                if kinam[ssx][xn][1][ton1]==1:
                                    numa[ssx][xn][1][ton1][0]+=de2[0]
                                if kinbm[ssx][xn][1][ton1]==1:
                                    numa[ssx][xn][1][ton1][1]+=de2[1]
                            for sik in range(2):
                                for ton1 in range(Nma1[sik][ssx][xn][0]):   
                                    if kinam1[sik][ssx][xn][0][ton1]==1:
                                        numa1[sik][ssx][xn][0][ton1][0]+=de3[sik]
                                    if kinbm1[sik][ssx][xn][0][ton1]==1:
                                        numa1[sik][ssx][xn][0][ton1][1]+=de1[sik]
                                for ton1 in range(Nma1[sik][ssx][xn][1]):   
                                    if kinam1[sik][ssx][xn][1][ton1]==1:
                                        numa1[sik][ssx][xn][1][ton1][0]+=de4[sik]
                                    if kinbm1[sik][ssx][xn][1][ton1]==1:
                                        numa1[sik][ssx][xn][1][ton1][1]+=de2[sik]
                    Xpole+=de0
                    Xpo+=de7
                    Xkin+=de5
                    Xkin1+=de6
                    ypsl0=energy0()
                    ypsl0p=ypsl0
                    ypsl0px=ypsl0
                    ckF,de0,de1,de2,de3,de4,de5,de6,de7=checkF()
                    if ckF==1:
                        for x2 in range(pair):
                            for xn in range(nu[x2]):
                                if kina[x2][xn]==1:
                                    motor[x2][xn][0]+=de1[x2]
                                if kinb[x2][xn]==1:
                                    motor[x2][xn][1]+=de2[x2]
                            for xn in range(nu1[x2]):
                                if kinap[x2][xn]==1:
                                    motorp[x2][xn][0]+=de3[x2]
                                if kinbp[x2][xn]==1:
                                    motorp[x2][xn][1]+=de2[x2]
                            for xn in range(nu1x[x2]):
                                if kinapx[x2][xn]==1:
                                    motorpx[x2][xn][0]+=de4[x2]
                                if kinbpx[x2][xn]==1:
                                    motorpx[x2][xn][1]+=de1[x2]


                            for ssx in range(2):
                                for xn in range(numc1[x2][ssx]):
                                    motormc1[x2][ssx][xn]+=de3[x2]
                                for xn in range(numc2[x2][ssx]):
                                    motormc2[x2][ssx][xn]+=de1[x2]
                                for xn in range(numc3[x2][ssx]):
                                    motormc3[x2][ssx][xn]+=de2[x2]
                                for xn in range(numc4[x2][ssx]):
                                    motormc4[x2][ssx][xn]+=de4[x2]
                                for xn in range(MTnumber+1):
                                    node1[x2][ssx][0][xn]+=de3[x2]
                                    node1[x2][ssx][1][xn]+=de1[x2]
                                    node1[x2][ssx][2][xn]+=de2[x2]
                                    node1[x2][ssx][3][xn]+=de4[x2]
                            
                            l2l[x2]+=de1[x2]
                            l2r[x2]+=de1[x2]
                            l3l[x2]+=de2[x2]
                            l3r[x2]+=de2[x2]
                            l1l[x2]+=de3[x2]
                            l1r[x2]+=de3[x2]
                            l4l[x2]+=de4[x2]
                            l4r[x2]+=de4[x2]
                            Ximt2[x2]+=de1[x2]
                            Ximt3[x2]+=de2[x2]
                            Xkmt1[x2]+=de3[x2]
                            Xkmt4[x2]+=de4[x2]
                        for ssx in range(2):
                            for xn in range(MTnumber):
                                for ton1 in range(Nma[ssx][xn][0]):   
                                    if kinam[ssx][xn][0][ton1]==1:
                                        numa[ssx][xn][0][ton1][0]+=de1[0]
                                    if kinbm[ssx][xn][0][ton1]==1:
                                        numa[ssx][xn][0][ton1][1]+=de1[1]
                                for ton1 in range(Nma[ssx][xn][1]):   
                                    if kinam[ssx][xn][1][ton1]==1:
                                        numa[ssx][xn][1][ton1][0]+=de2[0]
                                    if kinbm[ssx][xn][1][ton1]==1:
                                        numa[ssx][xn][1][ton1][1]+=de2[1]
                                for sik in range(2):
                                    for ton1 in range(Nma1[sik][ssx][xn][0]):   
                                        if kinam1[sik][ssx][xn][0][ton1]==1:
                                            numa1[sik][ssx][xn][0][ton1][0]+=de3[sik]
                                        if kinbm1[sik][ssx][xn][0][ton1]==1:
                                            numa1[sik][ssx][xn][0][ton1][1]+=de1[sik]
                                    for ton1 in range(Nma1[sik][ssx][xn][1]):   
                                        if kinam1[sik][ssx][xn][1][ton1]==1:
                                            numa1[sik][ssx][xn][1][ton1][0]+=de4[sik]
                                        if kinbm1[sik][ssx][xn][1][ton1]==1:
                                            numa1[sik][ssx][xn][1][ton1][1]+=de2[sik]
                        Xpole+=de0
                        Xpo+=de7
                        Xkin+=de5
                        Xkin1+=de6
                        ypsl0=energy0()
                        ypsl0p=ypsl0
                        ypsl0px=ypsl0
                        ckF,de0,de1,de2,de3,de4,de5,de6,de7=checkF()
                        if ckF==1:
                            for x2 in range(pair):
                                for xn in range(nu[x2]):
                                    if kina[x2][xn]==1:
                                        motor[x2][xn][0]+=de1[x2]
                                    if kinb[x2][xn]==1:
                                        motor[x2][xn][1]+=de2[x2]
                                for xn in range(nu1[x2]):
                                    if kinap[x2][xn]==1:
                                        motorp[x2][xn][0]+=de3[x2]
                                    if kinbp[x2][xn]==1:
                                        motorp[x2][xn][1]+=de2[x2]
                                for xn in range(nu1x[x2]):
                                    if kinapx[x2][xn]==1:
                                        motorpx[x2][xn][0]+=de4[x2]
                                    if kinbpx[x2][xn]==1:
                                        motorpx[x2][xn][1]+=de1[x2]


                                for ssx in range(2):
                                    for xn in range(numc1[x2][ssx]):
                                        motormc1[x2][ssx][xn]+=de3[x2]
                                    for xn in range(numc2[x2][ssx]):
                                        motormc2[x2][ssx][xn]+=de1[x2]
                                    for xn in range(numc3[x2][ssx]):
                                        motormc3[x2][ssx][xn]+=de2[x2]
                                    for xn in range(numc4[x2][ssx]):
                                        motormc4[x2][ssx][xn]+=de4[x2]
                                    for xn in range(MTnumber+1):
                                        node1[x2][ssx][0][xn]+=de3[x2]
                                        node1[x2][ssx][1][xn]+=de1[x2]
                                        node1[x2][ssx][2][xn]+=de2[x2]
                                        node1[x2][ssx][3][xn]+=de4[x2]

                                l2l[x2]+=de1[x2]
                                l2r[x2]+=de1[x2]
                                l3l[x2]+=de2[x2]
                                l3r[x2]+=de2[x2]
                                l1l[x2]+=de3[x2]
                                l1r[x2]+=de3[x2]
                                l4l[x2]+=de4[x2]
                                l4r[x2]+=de4[x2]
                                Ximt2[x2]+=de1[x2]
                                Ximt3[x2]+=de2[x2]
                                Xkmt1[x2]+=de3[x2]
                                Xkmt4[x2]+=de4[x2]
                            for ssx in range(2):
                                for xn in range(MTnumber):
                                    for ton1 in range(Nma[ssx][xn][0]):   
                                        if kinam[ssx][xn][0][ton1]==1:
                                            numa[ssx][xn][0][ton1][0]+=de1[0]
                                        if kinbm[ssx][xn][0][ton1]==1:
                                            numa[ssx][xn][0][ton1][1]+=de1[1]
                                    for ton1 in range(Nma[ssx][xn][1]):   
                                        if kinam[ssx][xn][1][ton1]==1:
                                            numa[ssx][xn][1][ton1][0]+=de2[0]
                                        if kinbm[ssx][xn][1][ton1]==1:
                                            numa[ssx][xn][1][ton1][1]+=de2[1]
                                    for sik in range(2):
                                        for ton1 in range(Nma1[sik][ssx][xn][0]):   
                                            if kinam1[sik][ssx][xn][0][ton1]==1:
                                                numa1[sik][ssx][xn][0][ton1][0]+=de3[sik]
                                            if kinbm1[sik][ssx][xn][0][ton1]==1:
                                                numa1[sik][ssx][xn][0][ton1][1]+=de1[sik]
                                        for ton1 in range(Nma1[sik][ssx][xn][1]):   
                                            if kinam1[sik][ssx][xn][1][ton1]==1:
                                                numa1[sik][ssx][xn][1][ton1][0]+=de4[sik]
                                            if kinbm1[sik][ssx][xn][1][ton1]==1:
                                                numa1[sik][ssx][xn][1][ton1][1]+=de2[sik]
                            Xpole+=de0
                            Xpo+=de7
                            Xkin+=de5
                            Xkin1+=de6
                            ypsl0=energy0()
                            ypsl0p=ypsl0
                            ypsl0px=ypsl0
                            print(kk)
#################################################################判断是否有新的Eg5连接
    for x1 in range(pair):
        
        for sn in range(2):
        
            numc1[x1][sn]=len(motormc1[x1][sn])
            numc2[x1][sn]=len(motormc2[x1][sn])
            numc3[x1][sn]=len(motormc3[x1][sn])
            numc4[x1][sn]=len(motormc4[x1][sn])

            for nn in range(MTnumber):
                if nn==MTnumber-1 and sn==1:
                    continue
                if nn==MTnumber-1:
                    lspa1=min(l3l[x1]-node1[x1][sn][0][nn],node1[x1][sn][0][nn+1]-node1[x1][sn][0][nn])#,Xkin-node1[x1][sn][0][nn])##1MT
                    lspa2=min(l3l[x1]-node1[x1][sn][1][nn],node1[x1][sn][1][nn+1]-node1[x1][sn][1][nn])##2MT
                    lspa3=min(node1[x1][sn][2][nn]-l2r[x1],node1[x1][sn][2][nn]-node1[x1][sn][2][nn+1])#3MT
                    lspa4=min(node1[x1][sn][3][nn]-l2r[x1],node1[x1][sn][3][nn]-node1[x1][sn][3][nn+1])#,node1[x1][sn][3][nn]-Xkin1)
                if nn!=MTnumber-1:
                    lspa1=node1[x1][sn][0][nn+1]-node1[x1][sn][0][nn]##1MT
                    lspa2=node1[x1][sn][1][nn+1]-node1[x1][sn][1][nn]##2MT
                    lspa3=node1[x1][sn][2][nn]-node1[x1][sn][2][nn+1]#3MT
                    lspa4=node1[x1][sn][3][nn]-node1[x1][sn][3][nn+1]
                nn1=0
                nn2=0
                nn3=0
                nmc1=0
                for xn in range(numc1[x1][sn]):
                    if motormc1[x1][sn][xn]>=node1[x1][sn][0][nn]-1 and motormc1[x1][sn][xn]<=node1[x1][sn][0][nn+1]+1:
                        if motormc1[x1][sn][xn]<node1[x1][sn][0][nn]+1000 and motormc1[x1][sn][xn]<node1[x1][sn][0][nn]:
                            nn1+=1
                        if motormc1[x1][sn][xn]>=node1[x1][sn][0][nn]+1000 and motormc1[x1][sn][xn]<node1[x1][sn][0][nn]+2000:
                            nn2+=1
                        if motormc1[x1][sn][xn]>=node1[x1][sn][0][nn]+2000 and motormc1[x1][sn][xn]<node1[x1][sn][0][nn]+3000:
                            nn3+=1
                        nmc1+=1
                if lspa1>1000:
                    ran5 = random.uniform(0, 1)
                    if ran5<kon*(1000-nn1*d)*h:
                        cx0=node1[x1][sn][0][nn]+round(1000/d*random.uniform(0,1))*d
                        it=0
                        while it <numc1[x1][sn]:
                            if abs(cx0-motormc1[x1][sn][it])<1:
                                cx0+=d
                                it=-1
                            it+=1
                        motormc1[x1][sn].append(cx0) 
                if lspa1>2000:
                    ran5 = random.uniform(0, 1)
                    if ran5<kon*(1000-nn2*d)*h:
                        cx0=node1[x1][sn][0][nn]+round(2000/d*random.uniform(0.5,1))*d
                        it=0
                        while it <numc1[x1][sn]:
                            if abs(cx0-motormc1[x1][sn][it])<1:
                                cx0+=d
                                it=-1
                            it+=1
                        motormc1[x1][sn].append(cx0) 
                if lspa1>3000:
                    ran5 = random.uniform(0, 1)
                    if ran5<kon*(1000-nn3*d)*h:
                        cx0=node1[x1][sn][0][nn]+round(3000/d*random.uniform(0.67,1))*d
                        it=0
                        while it <numc1[x1][sn]:
                            if abs(cx0-motormc1[x1][sn][it])<1:
                                cx0+=d
                                it=-1
                            it+=1
                        motormc1[x1][sn].append(cx0)
                if lspa1<=1000:
                    nc1=nmc1
                    ld=lspa1
                if lspa1<=2000 and lspa1>1000:
                    nc1=nmc1-nn1
                    ld=lspa1-1000
                if lspa1<=3000 and lspa1>2000:
                    nc1=nmc1-nn1-nn2
                    ld=lspa1-2000
                if lspa1>3000:
                    nc1=nmc1-nn1-nn2-nn3
                    ld=lspa1-3000
                ran5 = random.uniform(0, 1)
                if ran5<kon*(ld-nc1*d)*h:
                    cx0=node1[x1][sn][0][nn]+round(lspa1/d*random.uniform(1-ld/lspa1,1))*d
                    it=0
                    while it <numc1[x1][sn]:
                        if abs(cx0-motormc1[x1][sn][it])<1:
                            cx0+=d
                            it=-1
                        it+=1
                    motormc1[x1][sn].append(cx0)
                nn1=0
                nn2=0
                nn3=0
                nmc2=0
                for xn in range(numc2[x1][sn]):
                    if motormc2[x1][sn][xn]>=node1[x1][sn][1][nn]-1 and motormc2[x1][sn][xn]<=node1[x1][sn][1][nn+1]+1:
                        if motormc2[x1][sn][xn]<node1[x1][sn][1][nn]+1000:
                            nn1+=1
                        if motormc2[x1][sn][xn]>=node1[x1][sn][1][nn]+1000 and motormc2[x1][sn][xn]<node1[x1][sn][1][nn]+2000:
                            nn2+=1
                        if motormc2[x1][sn][xn]>=node1[x1][sn][1][nn]+2000 and motormc2[x1][sn][xn]<node1[x1][sn][1][nn]+3000:
                            nn3+=1
                        nmc2+=1
                if lspa2>1000:
                    ran5 = random.uniform(0, 1)
                    if ran5<kon*(1000-nn1*d)*h:
                        cx0=node1[x1][sn][1][nn]+round(1000/d*random.uniform(0,1))*d
                        it=0
                        while it <numc2[x1][sn]:
                            if abs(cx0-motormc2[x1][sn][it])<1:
                                cx0+=d
                                it=-1
                            it+=1
                        motormc2[x1][sn].append(cx0) 
                if lspa2>2000:
                    ran5 = random.uniform(0, 1)
                    if ran5<kon*(1000-nn2*d)*h:
                        cx0=node1[x1][sn][1][nn]+round(2000/d*random.uniform(0.5,1))*d
                        it=0
                        while it <numc2[x1][sn]:
                            if abs(cx0-motormc2[x1][sn][it])<1:
                                cx0+=d
                                it=-1
                            it+=1
                        motormc2[x1][sn].append(cx0) 
                if lspa2>3000:
                    ran5 = random.uniform(0, 1)
                    if ran5<kon*(1000-nn3*d)*h:
                        cx0=node1[x1][sn][1][nn]+round(3000/d*random.uniform(0.67,1))*d
                        it=0
                        while it <numc2[x1][sn]:
                            if abs(cx0-motormc2[x1][sn][it])<0:
                                cx0+=d
                                it=-1
                            it+=1
                        motormc2[x1][sn].append(cx0)
                if lspa2<=1000:
                    nc1=nmc2
                    ld=lspa2
                if lspa2<=2000 and lspa2>1000:
                    nc1=nmc2-nn1
                    ld=lspa2-1000
                if lspa2<=3000 and lspa2>2000:
                    nc1=nmc2-nn1-nn2
                    ld=lspa2-2000
                if lspa2>3000:
                    nc1=nmc2-nn1-nn2-nn3
                    ld=lspa2-3000
                ran5 = random.uniform(0, 1)
                if ran5<kon*(ld-nc1*d)*h:
                    cx0=node1[x1][sn][1][nn]+round(lspa2/d*random.uniform(1-ld/lspa2,1))*d
                    it=0
                    while it <numc2[x1][sn]:
                        if abs(cx0-motormc2[x1][sn][it])<1:
                            cx0+=d
                            it=-1
                        it+=1
                    motormc2[x1][sn].append(cx0)
                nn1=0
                nn2=0
                nn3=0
                nmc3=0
                for xn in range(numc3[x1][sn]):
                    if motormc3[x1][sn][xn]<=node1[x1][sn][2][nn]+1 and motormc3[x1][sn][xn]>=node1[x1][sn][2][nn+1]-1:
                        if motormc3[x1][sn][xn]>node1[x1][sn][2][nn]-1000:
                            nn1+=1
                        if motormc3[x1][sn][xn]<=node1[x1][sn][2][nn]-1000 and motormc3[x1][sn][xn]>node1[x1][sn][2][nn]-2000:
                            nn2+=1
                        if motormc3[x1][sn][xn]<=node1[x1][sn][2][nn]-2000 and motormc3[x1][sn][xn]>node1[x1][sn][2][nn]-3000:
                            nn3+=1
                        nmc3+=1
                if lspa3>1000:
                    ran5 = random.uniform(0, 1)
                    if ran5<kon*(1000-nn1*d)*h:
                        cx0=node1[x1][sn][2][nn]-round(1000/d*random.uniform(0,1))*d
                        it=0
                        while it <numc3[x1][sn]:
                            if abs(cx0-motormc3[x1][sn][it])<1:
                                cx0-=d
                                it=-1
                            it+=1
                        motormc3[x1][sn].append(cx0) 
                if lspa3>2000:
                    ran5 = random.uniform(0, 1)
                    if ran5<kon*(1000-nn2*d)*h:
                        cx0=node1[x1][sn][2][nn]-round(2000/d*random.uniform(0.5,1))*d
                        it=0
                        while it <numc3[x1][sn]:
                            if abs(cx0-motormc3[x1][sn][it])<1:
                                cx0-=d
                                it=-1
                            it+=1
                        motormc3[x1][sn].append(cx0) 
                if lspa3>3000:
                    ran5 = random.uniform(0, 1)
                    if ran5<kon*(1000-nn3*d)*h:
                        cx0=node1[x1][sn][2][nn]-round(3000/d*random.uniform(0.67,1))*d
                        it=0
                        while it <numc3[x1][sn]:
                            if abs(cx0-motormc3[x1][sn][it])<1:
                                cx0-=d
                                it=-1
                            it+=1
                        motormc3[x1][sn].append(cx0)
                if lspa3<=1000:
                    nc1=nmc3
                    ld=lspa3
                if lspa3<=2000 and lspa3>1000:
                    nc1=nmc3-nn1
                    ld=lspa3-1000
                if lspa3<=3000 and lspa3>2000:
                    nc1=nmc3-nn1-nn2
                    ld=lspa3-2000
                if lspa3>3000:
                    nc1=nmc3-nn1-nn2-nn3
                    ld=lspa3-3000
                ran4 = random.uniform(0, 1)
                if ran4<kon*(ld-nc1*d)*h:
                    cx0=node1[x1][sn][2][nn]-round(lspa3/d*random.uniform(1-ld/lspa3,1))*d
                    it=0
                    while it <numc3[x1][sn]:
                        if abs(cx0-motormc3[x1][sn][it])<1:
                            cx0-=d
                            it=-1
                        it+=1
                    motormc3[x1][sn].append(cx0)
                nn1=0
                nn2=0
                nn3=0
                nmc4=0
                for xn in range(numc4[x1][sn]):
                    if motormc4[x1][sn][xn]<=node1[x1][sn][3][nn]+1 and motormc4[x1][sn][xn]>=node1[x1][sn][3][nn+1]-1:
                        if motormc4[x1][sn][xn]>node1[x1][sn][3][nn]-1000:
                            nn1+=1
                        if motormc4[x1][sn][xn]<=node1[x1][sn][3][nn]-1000 and motormc4[x1][sn][xn]>node1[x1][sn][3][nn]-2000:
                            nn2+=1
                        if motormc4[x1][sn][xn]<=node1[x1][sn][3][nn]-2000 and motormc4[x1][sn][xn]>node1[x1][sn][3][nn]-3000:
                            nn3+=1
                        nmc4+=1
                if lspa4>1000:
                    ran5 = random.uniform(0, 1)
                    if ran5<kon*(1000-nn1*d)*h:
                        cx0=node1[x1][sn][3][nn]-round(1000/d*random.uniform(0,1))*d
                        it=0
                        while it <numc4[x1][sn]:
                            if abs(cx0-motormc4[x1][sn][it])<1:
                                cx0-=d
                                it=-1
                            it+=1
                        motormc4[x1][sn].append(cx0) 
                if lspa4>2000:
                    ran5 = random.uniform(0, 1)
                    if ran5<kon*(1000-nn2*d)*h:
                        cx0=node1[x1][sn][3][nn]-round(2000/d*random.uniform(0.5,1))*d
                        it=0
                        while it <numc4[x1][sn]:
                            if abs(cx0-motormc4[x1][sn][it])<1:
                                cx0-=d
                                it=-1
                            it+=1
                        motormc4[x1][sn].append(cx0) 
                if lspa4>3000:
                    ran5 = random.uniform(0, 1)
                    if ran5<kon*(1000-nn3*d)*h:
                        cx0=node1[x1][sn][3][nn]-round(3000/d*random.uniform(0.67,1))*d
                        it=0
                        while it <numc4[x1][sn]:
                            if abs(cx0-motormc4[x1][sn][it])<1:
                                cx0-=d
                                it=-1
                            it+=1
                        motormc4[x1][sn].append(cx0)
                if lspa4<=1000:
                    nc1=nmc4
                    ld=lspa4
                if lspa4<=2000 and lspa4>1000:
                    nc1=nmc4-nn1
                    ld=lspa4-1000
                if lspa4<=3000 and lspa4>2000:
                    nc1=nmc4-nn1-nn2
                    ld=lspa4-2000
                if lspa4>3000:
                    nc1=nmc4-nn1-nn2-nn3
                    ld=lspa4-3000
                ran4 = random.uniform(0, 1)
                if ran4<kon*(ld-nc1*d)*h:
                    cx0=node1[x1][sn][3][nn]-round(lspa4/d*random.uniform(1-ld/lspa4,1))*d
                    it=0
                    while it <numc4[x1][sn]:
                        if abs(cx0-motormc4[x1][sn][it])<1:
                            cx0-=d
                            it=-1
                        it+=1
                    motormc4[x1][sn].append(cx0)
        
        
##############################################################
        lxian[x1]=l2r[x1]-l3l[x1]
        lxianp[x1]=l1r[x1]-l3l[x1]
        lxianpx[x1]=l2r[x1]-l4l[x1]
        lspa=l2r[x1]-l3l[x1]
        ran4 = random.uniform(0, 1)
        ran5 = random.uniform(0, 1)
        if ran4 < ka1* (round(lspa/d)-1-sum(kina[x1]))* h:
            cx0=l2r[x1]-(round(lspa*random.uniform(0,1)/d)-1)*d
            motor[x1].append([cx0,cx0])
            kina[x1].append(1)
            kinb[x1].append(0)
            ypsl1[x1].append(0)
            dxc[x1].append(0)
            ypsl2[x1].append(0)
            zj0[x1].append(0)
            js0[x1].append(0)
            zj1[x1].append([0 for i in range(pair)])
            js1[x1].append([0 for i in range(pair)])
            zj2[x1].append([0 for i in range(pair)])
            js2[x1].append([0 for i in range(pair)])
            zj3[x1].append([0 for i in range(pair)])
            js3[x1].append([0 for i in range(pair)])
            zj4[x1].append([0 for i in range(pair)])
            js4[x1].append([0 for i in range(pair)])
            zj5[x1].append(0)
            js5[x1].append(0)
            zj6[x1].append(0)
            js6[x1].append(0)
            zj7[x1].append(0)
            js7[x1].append(0)
            pan[x1].append(0)
            nu[x1]+=1
        if ran5 < ka1* (round(lspa/d)-1-sum(kinb[x1]))* h:
            dxc[x1].append(0)
            kina[x1].append(0)
            kinb[x1].append(1)
            cx0=l3l[x1]+(round(lspa*random.uniform(0,1)/d)-1)*d
            motor[x1].append([cx0,cx0])
            ypsl1[x1].append(0)
            ypsl2[x1].append(0)
            zj0[x1].append(0)
            js0[x1].append(0)
            zj1[x1].append([0 for i in range(pair)])
            js1[x1].append([0 for i in range(pair)])
            zj2[x1].append([0 for i in range(pair)])
            js2[x1].append([0 for i in range(pair)])
            zj3[x1].append([0 for i in range(pair)])
            js3[x1].append([0 for i in range(pair)])
            zj4[x1].append([0 for i in range(pair)])
            js4[x1].append([0 for i in range(pair)])
            zj5[x1].append(0)
            js5[x1].append(0)
            zj6[x1].append(0)
            js6[x1].append(0)
            zj7[x1].append(0)
            js7[x1].append(0)
            pan[x1].append(0)
            nu[x1]+=1
        ran4 = random.uniform(0, 1)
        ran5 = random.uniform(0, 1)
        if ran4 < ka2* (round(lxianp[x1]/d)-1-sum(kinap[x1]))* h:
            cx0=l1r[x1]-(round(lxianp[x1]*random.uniform(0,1)/d)-1)*d
            motorp[x1].append([cx0,cx0])
            kinap[x1].append(1)
            kinbp[x1].append(0)
            dxcp[x1].append(0)
            ypsl1p[x1].append(0)
            ypsl2p[x1].append(0)
            zj0p[x1].append(0)
            js0p[x1].append(0)
            zj1p[x1].append([0 for i in range(pair)])
            js1p[x1].append([0 for i in range(pair)])
            zj2p[x1].append([0 for i in range(pair)])
            js2p[x1].append([0 for i in range(pair)])
            zj3p[x1].append([0 for i in range(pair)])
            js3p[x1].append([0 for i in range(pair)])
            zj4p[x1].append([0 for i in range(pair)])
            js4p[x1].append([0 for i in range(pair)])
            zj5p[x1].append(0)
            js5p[x1].append(0)
            zj6p[x1].append(0)
            js6p[x1].append(0)
            zj7p[x1].append(0)
            js7p[x1].append(0)
            panp[x1].append(0)
            nu1[x1]+=1
        if ran5 < ka2* (round(lxianp[x1]/d)-1-sum(kinbp[x1]))* h:
            cx0=l3l[x1]+(round(lxianp[x1]*random.uniform(0,1)/d)-1)*d
            motorp[x1].append([cx0,cx0])
            kinap[x1].append(0)
            kinbp[x1].append(1)
            dxcp[x1].append(0)
            ypsl1p[x1].append(0)
            ypsl2p[x1].append(0)               
            panp[x1].append(0)
            zj0p[x1].append(0)
            js0p[x1].append(0)
            zj1p[x1].append([0 for i in range(pair)])
            js1p[x1].append([0 for i in range(pair)])
            zj2p[x1].append([0 for i in range(pair)])
            js2p[x1].append([0 for i in range(pair)])
            zj3p[x1].append([0 for i in range(pair)])
            js3p[x1].append([0 for i in range(pair)])
            zj4p[x1].append([0 for i in range(pair)])
            js4p[x1].append([0 for i in range(pair)])
            zj5p[x1].append(0)
            js5p[x1].append(0)
            zj6p[x1].append(0)
            js6p[x1].append(0)
            zj7p[x1].append(0)
            js7p[x1].append(0)
            nu1[x1]+=1
        ran4 = random.uniform(0, 1)
        ran5 = random.uniform(0, 1)
        if ran4 < ka2* (round(lxianpx[x1]/d)-1-sum(kinapx[x1]))* h:
            cx0=l4l[x1]+(round(lxianpx[x1]*random.uniform(0,1)/d)-1)*d
            motorpx[x1].append([cx0,cx0])
            kinapx[x1].append(1)
            kinbpx[x1].append(0)
            dxcpx[x1].append(0)
            ypsl1px[x1].append(0)
            ypsl2px[x1].append(0)
            zj0px[x1].append(0)
            js0px[x1].append(0)
            zj1px[x1].append([0 for i in range(pair)])
            js1px[x1].append([0 for i in range(pair)])
            zj2px[x1].append([0 for i in range(pair)])
            js2px[x1].append([0 for i in range(pair)])
            zj3px[x1].append([0 for i in range(pair)])
            js3px[x1].append([0 for i in range(pair)])
            zj4px[x1].append([0 for i in range(pair)])
            js4px[x1].append([0 for i in range(pair)])
            zj5px[x1].append(0)
            js5px[x1].append(0)
            zj6px[x1].append(0)
            js6px[x1].append(0)
            zj7px[x1].append(0)
            js7px[x1].append(0)
            panpx[x1].append(0)
            nu1x[x1]+=1
        if ran5 < ka2* (round(lxianpx[x1]/d)-1-sum(kinbpx[x1]))* h:
            cx0=l2r[x1]-(round(lxianpx[x1]*random.uniform(0,1)/d)-1)*d
            motorpx[x1].append([cx0,cx0])
            kinapx[x1].append(0)
            kinbpx[x1].append(1)
            dxcpx[x1].append(0)
            ypsl1px[x1].append(0)
            ypsl2px[x1].append(0)
            panpx[x1].append(0)
            zj0px[x1].append(0)
            js0px[x1].append(0)
            zj1px[x1].append([0 for i in range(pair)])
            js1px[x1].append([0 for i in range(pair)])
            zj2px[x1].append([0 for i in range(pair)])
            js2px[x1].append([0 for i in range(pair)])
            zj3px[x1].append([0 for i in range(pair)])
            js3px[x1].append([0 for i in range(pair)])
            zj4px[x1].append([0 for i in range(pair)])
            js4px[x1].append([0 for i in range(pair)])
            zj5px[x1].append(0)
            js5px[x1].append(0)
            zj6px[x1].append(0)
            js6px[x1].append(0)
            zj7px[x1].append(0)
            js7px[x1].append(0)
            nu1x[x1]+=1
################################################################是否有新的tubulin连接
    for x1 in range(pair):
        for sn in range(2):
            motormc3[x1][sn].sort()
            motormc1[x1][sn].sort()
            motormc2[x1][sn].sort()
            motormc4[x1][sn].sort()
            numc1[x1][sn]=len(motormc1[x1][sn])
            numc2[x1][sn]=len(motormc2[x1][sn])
            numc3[x1][sn]=len(motormc3[x1][sn])
            numc4[x1][sn]=len(motormc4[x1][sn])
            for xxx in range(MTnumber):
                if xxx==MTnumber-1 and sn==1:
                    continue
                zq1=0
                for xn in range(numc1[x1][sn]):
                    if abs(motormc1[x1][sn][xn]-node1[x1][sn][0][xxx])<3/2*d and motormc1[x1][sn][xn]>=node1[x1][sn][0][xxx]-0.1:
                        zq1=1
                        noind[x1][sn][0][xxx]=xn
                        break
                if zq1<0.5:
                    #if adeps1[xxx]>0:
                    #    print(qq)
                    adeps1[x1][sn][xxx]=0
                if zq1==1:
                    adeps1[x1][sn][xxx]+=1
                zq2=0
                for xn in range(numc2[x1][sn]):
                    if abs(motormc2[x1][sn][xn]-node1[x1][sn][1][xxx])<3/2*d and motormc2[x1][sn][xn]>=node1[x1][sn][1][xxx]-0.1:
                        zq2=1
                        noind[x1][sn][1][xxx]=xn
                        break
                if zq2==0:
                    #if adeps2[xxx]>0:
                    #    print(qq)
                    adeps2[x1][sn][xxx]=0
                if zq2==1:
                    adeps2[x1][sn][xxx]+=1
                zq3=0
                for xn in range(numc3[x1][sn]):
                    if abs(motormc3[x1][sn][xn]-node1[x1][sn][2][xxx])<3/2*d and motormc3[x1][sn][xn]<=node1[x1][sn][2][xxx]+0.1:
                        zq3=1
                        noind[x1][sn][2][xxx]=xn
                        break
                if zq3==0:
                    #if adeps3[xxx]>0:
                     #   print(qq)
                    adeps3[x1][sn][xxx]=0
                if zq3==1:
                    adeps3[x1][sn][xxx]+=1
                zq4=0
                for xn in range(numc4[x1][sn]):
                    if abs(motormc4[x1][sn][xn]-node1[x1][sn][3][xxx])<3/2*d and motormc4[x1][sn][xn]<=node1[x1][sn][3][xxx]+0.1:
                        zq4=1
                        noind[x1][sn][3][xxx]=xn
                        break
                if zq4==0:
                    #if adeps4[xxx]>0:
                    #    print(qq)
                    adeps4[x1][sn][xxx]=0
                if zq4==1:
                    adeps4[x1][sn][xxx]+=1
            for i in range(numc3[x1][sn]):
                ran4=random.uniform(0, 1)
                zq=0
                for xxx in range(MTnumber):
                    if abs(motormc3[x1][sn][i]-node1[x1][sn][2][xxx])<3/2*d and motormc3[x1][sn][i]<=node1[x1][sn][2][xxx]+0.1:
                        zq=1
                        break
                if zq==1:
                    continue
                if ran4<kdif*h:
                    zq=0
                    for xxx in range(MTnumber):
                        if adeps3[x1][sn][xxx]!=0:
                            if motormc3[x1][sn][i]+d>=motormc3[x1][sn][noind[x1][sn][2][xxx]]-0.1 and  motormc3[x1][sn][i]<motormc3[x1][sn][noind[x1][sn][2][xxx]]-0.1:
                                zq=3
                        if motormc3[x1][sn][i]+d>=node1[x1][sn][2][xxx]-0.1 and  motormc3[x1][sn][i]<node1[x1][sn][2][xxx]-0.1 :
                            zq=3
                    if motormc3[x1][sn][i]+d>node1[x1][sn][2][0]:#l3r:
                        zq=3
                    for xn in range(numc3[x1][sn]):
                        if motormc3[x1][sn][i]+d>=motormc3[x1][sn][xn]-0.1 and  motormc3[x1][sn][i]<motormc3[x1][sn][xn]-0.1:
                            zq=3
                    if zq==0:
                        motormc3[x1][sn][i]+=d
                ran4=random.uniform(0, 1)
                if ran4<kdif*h:
                    zq=0
                    for xxx in range(MTnumber):
                        if motormc3[x1][sn][i]-d<=node1[x1][sn][2][xxx]+0.1 and  motormc3[x1][sn][i]>node1[x1][sn][2][xxx]+0.1 :
                            zq=3
                    if motormc3[x1][sn][i]-d<node1[x1][sn][1][MTnumber]:#l2r:
                        zq=3
                    for xn in range(numc3[x1][sn]):
                        if motormc3[x1][sn][i]-d<=motormc3[x1][sn][xn]+0.1 and  motormc3[x1][sn][i]>motormc3[x1][sn][xn]+0.1:
                            zq=3
                    if zq==0:
                        motormc3[x1][sn][i]-=d
            for i in range(numc1[x1][sn]):
                zq=0
                for xxx in range(MTnumber):
                    if abs(motormc1[x1][sn][i]-node1[x1][sn][0][xxx])<3/2*d and motormc1[x1][sn][i]>=node1[x1][sn][0][xxx]-0.1:
                        zq=1
                        break
                if zq==1:
                    continue
                ran4=random.uniform(0, 1)
                if ran4<kdif*h:
                    zq=0
                    for xxx in range(MTnumber):
                        if motormc1[x1][sn][i]+d>=node1[x1][sn][0][xxx]-0.1 and  motormc1[x1][sn][i]<node1[x1][sn][0][xxx]-0.1 :
                            zq=3
                    if motormc1[x1][sn][i]+d>node1[x1][sn][2][MTnumber] or motormc1[x1][sn][i]+d>Xkin:#l3l
                        zq=3
                    for xn in range(numc1[x1][sn]):
                        if motormc1[x1][sn][i]+d>=motormc1[x1][sn][xn]-0.1 and  motormc1[x1][sn][i]<motormc1[x1][sn][xn]-0.1:
                            zq=3
                    if zq==0:
                        motormc1[x1][sn][i]+=d
                ran4=random.uniform(0, 1)
                if ran4<kdif*h:
                    zq=0
                    for xxx in range(MTnumber):
                        if adeps1[x1][sn][xxx]!=0:
                            if motormc1[x1][sn][i]-d<=motormc1[x1][sn][noind[x1][sn][0][xxx]]+0.1 and  motormc1[x1][sn][i]>motormc1[x1][sn][noind[x1][sn][0][xxx]]+0.1:
                                zq=3
                        if motormc1[x1][sn][i]-d<=node1[x1][sn][0][xxx]+0.1 and  motormc1[x1][sn][i]>node1[x1][sn][0][xxx]+0.1 :
                            zq=3
                    if motormc1[x1][sn][i]-d<=node1[x1][sn][0][0]:#l1l:
                        zq=3
                    for xn in range(numc1[x1][sn]):
                        if motormc1[x1][sn][i]-d<=motormc1[x1][sn][xn]+0.1 and  motormc1[x1][sn][i]>motormc1[x1][sn][xn]+0.1:
                            zq=3
                    if zq==0:
                        motormc1[x1][sn][i]-=d
            for i in range(numc4[x1][sn]):
                zq=0
                for xxx in range(MTnumber):
                    if abs(motormc4[x1][sn][i]-node1[x1][sn][3][xxx])<3/2*d and motormc4[x1][sn][i]<=node1[x1][sn][3][xxx]+0.1:
                        zq=1
                        break
                if zq==1:
                    continue
                ran4=random.uniform(0, 1)
                if ran4<kdif*h:
                    zq=0
                    for xxx in range(MTnumber):
                        if adeps4[x1][sn][xxx]!=0:
                            if motormc4[x1][sn][i]+d>=motormc4[x1][sn][noind[x1][sn][3][xxx]]-0.1 and  motormc4[x1][sn][i]<motormc4[x1][sn][noind[x1][sn][3][xxx]]-0.1:
                                zq=3
                        if motormc4[x1][sn][i]+d>=node1[x1][sn][3][xxx]-0.1 and  motormc4[x1][sn][i]<node1[x1][sn][3][xxx]-0.1 :
                            zq=3

                    if motormc4[x1][sn][i]+d>node1[x1][sn][3][0]:#l4r:
                        zq=3
                    for xn in range(numc4[x1][sn]):
                        if motormc4[x1][sn][i]+d>=motormc4[x1][sn][xn]-0.1 and  motormc4[x1][sn][i]<motormc4[x1][sn][xn]-0.1:
                            zq=3
                    if zq==0:
                        motormc4[x1][sn][i]+=d
                ran4=random.uniform(0, 1)
                if ran4<kdif*h:
                    zq=0
                    for xxx in range(MTnumber):
                        if motormc4[x1][sn][i]-d<=node1[x1][sn][3][xxx]+0.1 and  motormc4[x1][sn][i]>node1[x1][sn][3][xxx]+0.1 :
                            zq=3
                    if motormc4[x1][sn][i]-d<node1[x1][sn][1][MTnumber] or motormc4[x1][sn][i]-d<Xkin1:#l2r
                        zq=3
                    for xn in range(numc4[x1][sn]):
                        if motormc4[x1][sn][i]-d<=motormc4[x1][sn][xn]+0.1 and  motormc4[x1][sn][i]>motormc4[x1][sn][xn]+0.1:
                            zq=3
                    if zq==0:
                        motormc4[x1][sn][i]-=d
            for i in range(numc2[x1][sn]):
                zq=0
                for xxx in range(MTnumber):
                    if abs(motormc2[x1][sn][i]-node1[x1][sn][1][xxx])<3/2*d and motormc2[x1][sn][i]>=node1[x1][sn][1][xxx]-0.1:
                        zq=1
                        break
                if zq==1:
                    continue
                ran4=random.uniform(0, 1)
                if ran4<kdif*h:
                    zq=0
                    for xxx in range(MTnumber):
                        if motormc2[x1][sn][i]+d>=node1[x1][sn][1][xxx]-0.1 and  motormc2[x1][sn][i]<node1[x1][sn][1][xxx]-0.1 :
                            zq=3
                    if motormc2[x1][sn][i]+d>node1[x1][sn][2][MTnumber]:#l3l
                        zq=3
                    for xn in range(numc2[x1][sn]):
                        if motormc2[x1][sn][i]+d>=motormc2[x1][sn][xn]-0.1 and  motormc2[x1][sn][i]<motormc2[x1][sn][xn]-0.1:
                            zq=3
                    if zq==0:
                        motormc2[x1][sn][i]+=d
                ran4=random.uniform(0, 1)
                if ran4<kdif*h:
                    zq=0
                    for xxx in range(MTnumber):
                        if adeps2[x1][sn][xxx]!=0:
                            if motormc2[x1][sn][i]-d<=motormc2[x1][sn][noind[x1][sn][1][xxx]]+0.1 and  motormc2[x1][sn][i]>motormc2[x1][sn][noind[x1][sn][1][xxx]]+0.1  :
                                zq=3
                        if motormc2[x1][sn][i]-d<=node1[x1][sn][1][xxx]+0.1 and  motormc2[x1][sn][i]>node1[x1][sn][1][xxx]+0.1 :
                            zq=3
                    if motormc2[x1][sn][i]-d<node1[x1][sn][1][0]:#l2l
                        zq=3
                    for xn in range(numc2[x1][sn]):
                        if motormc2[x1][sn][i]-d<=motormc2[x1][sn][xn]+0.1 and  motormc2[x1][sn][i]>motormc2[x1][sn][xn]+0.1:
                            zq=3
                    if zq==0:
                        motormc2[x1][sn][i]-=d
    for x1 in range(pair):
        for sn in range(2):
            for xxx in range(MTnumber):
                if xxx==MTnumber-1 and sn==1:
                    continue
                if numc3[x1][sn]>0:#MT3,de2
                    if adeps3[x1][sn][xxx]>0 and node1[x1][sn][2][xxx]>node1[x1][sn][2][xxx+1]+1:
                        ran4=random.uniform(0, 1)

                        if ran4<vd*h:
                            motormc3[x1][sn][noind[x1][sn][2][xxx]]-=d        
                            for x3 in range(0,xxx+1):
                                node1[x1][sn][2][x3]-=d
                            for xn in range(xxx):
                                for ton1 in range(Nma[sn][xn][1]):   
                                    numa[sn][xn][1][ton1][x1]-=d
                                for ton1 in range(Nma1[x1][sn][xn][1]):   
                                    numa1[x1][sn][xn][1][ton1][1]-=d
                            
                            for x2 in range(noind[x1][sn][2][xxx]+1,numc3[x1][sn]):
                                motormc3[x1][sn][x2]-=d
                            x3=0
                            while x3<numc3[x1][sn]:
                                if x3!=noind[x1][sn][2][xxx] and abs(motormc3[x1][sn][noind[x1][sn][2][xxx]]-motormc3[x1][sn][x3])<1:
                                    del motormc3[x1][sn][x3]
                                    numc3[x1][sn]-=1
                                    for x2 in range(MTnumber):
                                        for xn in range(numc3[x1][sn]):
                                            if abs(motormc3[x1][sn][xn]-node1[x1][sn][2][x2])<3/2*d and motormc3[x1][sn][xn]<=node1[x1][sn][2][x2]+0.1:
                                                noind[x1][sn][2][x2]=xn
                                                break
                                    break    
                                x3+=1
                            if xxx==0:
                                if MTnumber==1:
                                    l3r[x1]-=d/2
                                    desi3[x1]+=d/2
                                l3r[x1]-=d/2
                                desi3[x1]+=d/2
                                pan1=1
                                panx=1
                            if xxx!=0:
                                overlap[x1][sn][2][xxx-1]-=d
                                if xxx==MTnumber-1:
                                    overlap[x1][1][2][xxx-1]-=d
                                    for x3 in range(0,xxx+1):
                                        node1[x1][1][2][x3]-=d
                                    for xn in range(xxx):
                                        for ton1 in range(Nma[1][xn][1]):   
                                            numa[1][xn][1][ton1][x1]-=d
                                        for ton1 in range(Nma1[x1][1][xn][1]):   
                                            numa1[x1][1][xn][1][ton1][1]-=d
                                    for x2 in range(0,numc3[x1][1]):
                                        motormc3[x1][1][x2]-=d
           
                        ran4=random.uniform(0, 1)
                        if ran4<stad*h:

                            motormc3[x1][sn].pop(noind[x1][sn][2][xxx])
                            adeps3[x1][sn][xxx]=0
                            numc3[x1][sn]-=1
                            for x2 in range(MTnumber):
                                for xn in range(numc3[x1][sn]):
                                    if abs(motormc3[x1][sn][xn]-node1[x1][sn][2][x2])<3/2*d and motormc3[x1][sn][xn]<=node1[x1][sn][2][x2]+0.1:
                                        noind[x1][sn][2][x2]=xn
                                        break
                if numc1[x1][sn]>0:

                    if adeps1[x1][sn][xxx]>0 and node1[x1][sn][0][xxx]<node1[x1][sn][0][xxx+1]-1:
                        ran4=random.uniform(0, 1)
                        if ran4<vd*h:
                            motormc1[x1][sn][noind[x1][sn][0][xxx]]+=d

                            for x3 in range(0,xxx+1):
                                node1[x1][sn][0][x3]+=d
                            for xn in range(xxx):
                                
                                for ton1 in range(Nma1[x1][sn][xn][0]):   
                                    numa1[x1][sn][xn][0][ton1][0]+=d
                            for x2 in range(0,noind[x1][sn][0][xxx]):
                                motormc1[x1][sn][x2]+=d
                            x3=0
                            while x3<numc1[x1][sn]:
                                if x3!=noind[x1][sn][0][xxx] and abs(motormc1[x1][sn][noind[x1][sn][0][xxx]]-motormc1[x1][sn][x3])<1:
                                    #print(motormc1[noind[0][xxx]],motormc1[x3],x3,noind[0][xxx])
                                    del motormc1[x1][sn][x3]
                                    numc1[x1][sn]-=1
                                    for x2 in range(MTnumber):
                                        for xn in range(numc1[x1][sn]):
                                            if abs(motormc1[x1][sn][xn]-node1[x1][sn][0][x2])<3/2*d and motormc1[x1][sn][xn]>=node1[x1][sn][0][x2]-0.1:
                                                noind[x1][sn][0][x2]=xn
                                                break
                                    break
                                x3+=1
                            if xxx==0:
                                if MTnumber==1:
                                    l1l[x1]+=d/2#polechu,2MT
                                
                                    desk1[x1]+=d/2
                                l1l[x1]+=d/2#polechu,2MT
                                pan1=1
                                desk1[x1]+=d/2
                                panx=1
                            if xxx!=0:
                                overlap[x1][sn][0][xxx-1]-=d
                                if xxx==MTnumber-1:
                                    overlap[x1][1][0][xxx-1]-=d
                                    for x3 in range(0,xxx+1):
                                        node1[x1][1][0][x3]+=d
                                    for xn in range(xxx):
                                
                                        for ton1 in range(Nma1[x1][1][xn][0]):   
                                            numa1[x1][1][xn][0][ton1][0]+=d
                                    for x2 in range(0,numc1[x1][1]):
                                        motormc1[x1][1][x2]+=d
                                #ckF,de0,de1,de2,de3,de4,de5,de6,de7=checkF()
                                #if ckF==1 and panx!=1:
                                #    print(kk)
                        ran4=random.uniform(0, 1)
                        if ran4<stad*h:
                            motormc1[x1][sn].pop(noind[x1][sn][0][xxx])

                            adeps1[x1][sn][xxx]=0
                            numc1[x1][sn]-=1
                            for x2 in range(MTnumber):
                                for xn in range(numc1[x1][sn]):
                                    if abs(motormc1[x1][sn][xn]-node1[x1][sn][0][x2])<3/2*d and motormc1[x1][sn][xn]>=node1[x1][sn][0][x2]-0.1:
                                        noind[x1][sn][0][x2]=xn
                                        break
                if numc4[x1][sn]>0: 

                    if adeps4[x1][sn][xxx]>0 and node1[x1][sn][3][xxx]>node1[x1][sn][3][xxx+1]+1+d:
                        ran4=random.uniform(0, 1)
                        if ran4<vd*h:

                            motormc4[x1][sn][noind[x1][sn][3][xxx]]-=d
                            for x3 in range(0,xxx+1):
                                node1[x1][sn][3][x3]-=d
                            for xn in range(xxx):  
                                for ton1 in range(Nma1[x1][sn][xn][1]):   
                                    numa1[x1][sn][xn][1][ton1][0]-=d
                            for x2 in range(noind[x1][sn][3][xxx]+1,numc4[x1][sn]):
                                motormc4[x1][sn][x2]-=d
                            x3=0
                            while x3<numc4[x1][sn]:
                                if x3!=noind[x1][sn][3][xxx] and abs(motormc4[x1][sn][noind[x1][sn][3][xxx]]-motormc4[x1][sn][x3])<1:
                                    #print(motormc4[noind[3][xxx]],motormc4[x3],x3,noind[3][xxx])
                                    del motormc4[x1][sn][x3]
                                    numc4[x1][sn]-=1
                                    for x2 in range(MTnumber):
                                        for xn in range(numc4[x1][sn]):
                                            if abs(motormc4[x1][sn][xn]-node1[x1][sn][3][x2])<3/2*d and motormc4[x1][sn][xn]<=node1[x1][sn][3][x2]+0.1:
                                                noind[x1][sn][3][x2]=xn
                                                break
                                    break
                                x3+=1
                            if xxx==0:
                                if MTnumber==1:
                                    l4r[x1]-=d/2
                                    desk4[x1]+=d/2
                                l4r[x1]-=d/2
                                desk4[x1]+=d/2
                                pan1=1
                                panx=1
                            if xxx!=0:
                                overlap[x1][sn][3][xxx-1]-=d
                                if xxx==MTnumber-1:
                                    overlap[x1][1][3][xxx-1]-=d
                                    for x3 in range(0,xxx+1):
                                        node1[x1][1][3][x3]-=d
                                    for xn in range(xxx):  
                                        for ton1 in range(Nma1[x1][1][xn][1]):   
                                            numa1[x1][1][xn][1][ton1][0]-=d
                                    for x2 in range(0,numc4[x1][1]):
                                        motormc4[x1][1][x2]-=d
                                ckF,de0,de1,de2,de3,de4,de5,de6,de7=checkF()
                                if ckF==1 and panx!=1:
                                    print(kk)
                        ran4=random.uniform(0, 1)
                        if ran4<stad*h:

                            motormc4[x1][sn].pop(noind[x1][sn][3][xxx])
                            adeps4[x1][sn][xxx]=0
                            numc4[x1][sn]-=1
                            for x2 in range(MTnumber):
                                for xn in range(numc4[x1][sn]):
                                    if abs(motormc4[x1][sn][xn]-node1[x1][sn][3][x2])<3/2*d and motormc4[x1][sn][xn]<=node1[x1][sn][3][x2]+0.1:
                                        noind[x1][sn][3][x2]=xn
                                        break

                if numc2[x1][sn]>0:
                    if adeps2[x1][sn][xxx]>0 and node1[x1][sn][1][xxx]<node1[x1][sn][1][xxx+1]-1-d:
                        ran4=random.uniform(0, 1)
                        if ran4<vd*h:
                            motormc2[x1][sn][noind[x1][sn][1][xxx]]+=d
                            for x3 in range(0,xxx+1):
                                node1[x1][sn][1][x3]+=d
                            for xn in range(xxx):
                                for ton1 in range(Nma[sn][xn][0]):   
                                    numa[sn][xn][0][ton1][x1]+=d
                                for ton1 in range(Nma1[x1][sn][xn][0]):   
                                    numa1[x1][sn][xn][0][ton1][1]+=d
                            for x2 in range(0,noind[x1][sn][1][xxx]):
                                motormc2[x1][sn][x2]+=d 
                            x3=0
                            while x3<numc2[x1][sn]:
                                if x3!=noind[x1][sn][1][xxx] and abs(motormc2[x1][sn][noind[x1][sn][1][xxx]]-motormc2[x1][sn][x3])<1:
                                    del motormc2[x1][sn][x3]
                                    numc2[x1][sn]-=1
                                    for x2 in range(MTnumber):
                                        for xn in range(numc2[x1][sn]):
                                            if abs(motormc2[x1][sn][xn]-node1[x1][sn][1][x2])<3/2*d and motormc2[x1][sn][xn]>=node1[x1][sn][1][x2]-0.1:
                                                noind[x1][sn][1][x2]=xn
                                                break
                                    break
                                x3+=1
                            if xxx==0:
                                if MTnumber==1:
                                    l2l[x1]+=d/2
                                
                                    desi2[x1]+=d/2
                                l2l[x1]+=d/2
                                pan1=1
                                desi2[x1]+=d/2
                                panx=1
                            if xxx!=0:
                                
                                overlap[x1][sn][1][xxx-1]-=d
                                if xxx==MTnumber-1:
                                    overlap[x1][1][1][xxx-1]-=d
                                    for x3 in range(0,xxx+1):
                                        node1[x1][1][1][x3]+=d
                                    for xn in range(xxx):
                                        for ton1 in range(Nma[1][xn][0]):   
                                            numa[1][xn][0][ton1][x1]+=d
                                        for ton1 in range(Nma1[x1][1][xn][0]):   
                                            numa1[x1][1][xn][0][ton1][1]+=d
                                    for x2 in range(0,numc2[x1][1]):
                                        motormc2[x1][1][x2]+=d 
                                #ckF,de0,de1,de2,de3,de4,de5,de6,de7=checkF()
                                #if ckF==1 and panx!=1:
                                #    print(kk)
                        ran4=random.uniform(0, 1)
                        if ran4<stad*h:

                            motormc2[x1][sn].pop(noind[x1][sn][1][xxx])
                            adeps2[x1][sn][xxx]=0
                            numc2[x1][sn]-=1
                            for x2 in range(MTnumber):
                                for xn in range(numc2[x1][sn]):
                                    if abs(motormc2[x1][sn][xn]-node1[x1][sn][1][x2])<3/2*d and motormc2[x1][sn][xn]>=node1[x1][sn][1][x2]-0.1:
                                        noind[x1][sn][1][x2]=xn
                                        break

        
                
                if panx==1:   
                    panx=0
                    pan1=1
                    ckF,de0,de1,de2,de3,de4,de5,de6,de7=checkF()
                    if ckF==1:
                        for x2 in range(pair):
                            for xn in range(nu[x2]):
                                if kina[x2][xn]==1:
                                    motor[x2][xn][0]+=de1[x2]
                                if kinb[x2][xn]==1:
                                    motor[x2][xn][1]+=de2[x2]
                            for xn in range(nu1[x2]):
                                if kinap[x2][xn]==1:
                                    motorp[x2][xn][0]+=de3[x2]
                                if kinbp[x2][xn]==1:
                                    motorp[x2][xn][1]+=de2[x2]
                            for xn in range(nu1x[x2]):
                                if kinapx[x2][xn]==1:
                                    motorpx[x2][xn][0]+=de4[x2]
                                if kinbpx[x2][xn]==1:
                                    motorpx[x2][xn][1]+=de1[x2]

                            for ssx in range(2):
                                for xn in range(numc1[x2][ssx]):
                                    motormc1[x2][ssx][xn]+=de3[x2]
                                for xn in range(numc2[x2][ssx]):
                                    motormc2[x2][ssx][xn]+=de1[x2]
                                for xn in range(numc3[x2][ssx]):
                                    motormc3[x2][ssx][xn]+=de2[x2]
                                for xn in range(numc4[x2][ssx]):
                                    motormc4[x2][ssx][xn]+=de4[x2]
                                for xn in range(MTnumber+1):
                                    node1[x2][ssx][0][xn]+=de3[x2]
                                    node1[x2][ssx][1][xn]+=de1[x2]
                                    node1[x2][ssx][2][xn]+=de2[x2]
                                    node1[x2][ssx][3][xn]+=de4[x2]

                            l2l[x2]+=de1[x2]
                            l2r[x2]+=de1[x2]
                            l3l[x2]+=de2[x2]
                            l3r[x2]+=de2[x2]
                            l1l[x2]+=de3[x2]
                            l1r[x2]+=de3[x2]
                            l4l[x2]+=de4[x2]
                            l4r[x2]+=de4[x2]
                            Ximt2[x2]+=de1[x2]
                            Ximt3[x2]+=de2[x2]
                            Xkmt1[x2]+=de3[x2]
                            Xkmt4[x2]+=de4[x2]
                        for ssx in range(2):
                            for xn in range(MTnumber):
                                for ton1 in range(Nma[ssx][xn][0]):   
                                    if kinam[ssx][xn][0][ton1]==1:
                                        numa[ssx][xn][0][ton1][0]+=de1[0]
                                    if kinbm[ssx][xn][0][ton1]==1:
                                        numa[ssx][xn][0][ton1][1]+=de1[1]
                                for ton1 in range(Nma[ssx][xn][1]):   
                                    if kinam[ssx][xn][1][ton1]==1:
                                        numa[ssx][xn][1][ton1][0]+=de2[0]
                                    if kinbm[ssx][xn][1][ton1]==1:
                                        numa[ssx][xn][1][ton1][1]+=de2[1]
                                for sik in range(2):
                                    for ton1 in range(Nma1[sik][ssx][xn][0]):   
                                        if kinam1[sik][ssx][xn][0][ton1]==1:
                                            numa1[sik][ssx][xn][0][ton1][0]+=de3[sik]
                                        if kinbm1[sik][ssx][xn][0][ton1]==1:
                                            numa1[sik][ssx][xn][0][ton1][1]+=de1[sik]
                                    for ton1 in range(Nma1[sik][ssx][xn][1]):   
                                        if kinam1[sik][ssx][xn][1][ton1]==1:
                                            numa1[sik][ssx][xn][1][ton1][0]+=de4[sik]
                                        if kinbm1[sik][ssx][xn][1][ton1]==1:
                                            numa1[sik][ssx][xn][1][ton1][1]+=de2[sik]
                        Xpole+=de0
                        Xpo+=de7
                        Xkin+=de5
                        Xkin1+=de6
                        ypsl0=energy0()
                        ypsl0p=ypsl0
                        ypsl0px=ypsl0
                        ckF,de0,de1,de2,de3,de4,de5,de6,de7=checkF()
                        if ckF==1:
                            #print('14depo',kk)
                            for x2 in range(pair):
                                for xn in range(nu[x2]):
                                    if kina[x2][xn]==1:
                                        motor[x2][xn][0]+=de1[x2]
                                    if kinb[x2][xn]==1:
                                        motor[x2][xn][1]+=de2[x2]
                                for xn in range(nu1[x2]):
                                    if kinap[x2][xn]==1:
                                        motorp[x2][xn][0]+=de3[x2]
                                    if kinbp[x2][xn]==1:
                                        motorp[x2][xn][1]+=de2[x2]
                                for xn in range(nu1x[x2]):
                                    if kinapx[x2][xn]==1:
                                        motorpx[x2][xn][0]+=de4[x2]
                                    if kinbpx[x2][xn]==1:
                                        motorpx[x2][xn][1]+=de1[x2]


                                for ssx in range(2):
                                    for xn in range(numc1[x2][ssx]):
                                        motormc1[x2][ssx][xn]+=de3[x2]
                                    for xn in range(numc2[x2][ssx]):
                                        motormc2[x2][ssx][xn]+=de1[x2]
                                    for xn in range(numc3[x2][ssx]):
                                        motormc3[x2][ssx][xn]+=de2[x2]
                                    for xn in range(numc4[x2][ssx]):
                                        motormc4[x2][ssx][xn]+=de4[x2]
                                    for xn in range(MTnumber+1):
                                        node1[x2][ssx][0][xn]+=de3[x2]
                                        node1[x2][ssx][1][xn]+=de1[x2]
                                        node1[x2][ssx][2][xn]+=de2[x2]
                                        node1[x2][ssx][3][xn]+=de4[x2]

                                l2l[x2]+=de1[x2]
                                l2r[x2]+=de1[x2]
                                l3l[x2]+=de2[x2]
                                l3r[x2]+=de2[x2]
                                l1l[x2]+=de3[x2]
                                l1r[x2]+=de3[x2]
                                l4l[x2]+=de4[x2]
                                l4r[x2]+=de4[x2]
                                Ximt2[x2]+=de1[x2]
                                Ximt3[x2]+=de2[x2]
                                Xkmt1[x2]+=de3[x2]
                                Xkmt4[x2]+=de4[x2]
                            for ssx in range(2):
                                for xn in range(MTnumber):
                                    for ton1 in range(Nma[ssx][xn][0]):   
                                        if kinam[ssx][xn][0][ton1]==1:
                                            numa[ssx][xn][0][ton1][0]+=de1[0]
                                        if kinbm[ssx][xn][0][ton1]==1:
                                            numa[ssx][xn][0][ton1][1]+=de1[1]
                                    for ton1 in range(Nma[ssx][xn][1]):   
                                        if kinam[ssx][xn][1][ton1]==1:
                                            numa[ssx][xn][1][ton1][0]+=de2[0]
                                        if kinbm[ssx][xn][1][ton1]==1:
                                            numa[ssx][xn][1][ton1][1]+=de2[1]
                                    for sik in range(2):
                                        for ton1 in range(Nma1[sik][ssx][xn][0]):   
                                            if kinam1[sik][ssx][xn][0][ton1]==1:
                                                numa1[sik][ssx][xn][0][ton1][0]+=de3[sik]
                                            if kinbm1[sik][ssx][xn][0][ton1]==1:
                                                numa1[sik][ssx][xn][0][ton1][1]+=de1[sik]
                                        for ton1 in range(Nma1[sik][ssx][xn][1]):   
                                            if kinam1[sik][ssx][xn][1][ton1]==1:
                                                numa1[sik][ssx][xn][1][ton1][0]+=de4[sik]
                                            if kinbm1[sik][ssx][xn][1][ton1]==1:
                                                numa1[sik][ssx][xn][1][ton1][1]+=de2[sik]
                            Xpole+=de0
                            Xpo+=de7
                            Xkin+=de5
                            Xkin1+=de6
                            ypsl0=energy0()
                            ypsl0p=ypsl0
                            ypsl0px=ypsl0

            if sn==0:#############只算MTnumber
                ran5 = random.uniform(0, 1)
                vpolkmt=vp0*(1+(Kp3*(Xkin-l1r[x1])/Fp0))/d
                if ran5<abs(vpolkmt)*h:
                    if vpolkmt>0:
                        node1[x1][sn][0][MTnumber]+=d
                        l1r[x1]+=d
                        pos1[x1]+=d
                    if vpolkmt<0:
                        node1[x1][sn][0][MTnumber]-=d
                        l1r[x1]-=d
                        pos1[x1]-=d
                    pan1=1
                    panx=1
                ran5 = random.uniform(0, 1)
                vpolkmt=vp0*(1+(Kp3*(l4l[x1]-Xkin1)/Fp0))/d
                if ran5<abs(vpolkmt)*h:
                    if vpolkmt>0:
                        node1[x1][sn][3][MTnumber]-=d
                        l4l[x1]-=d
                        pos4[x1]-=d
                    if vpolkmt<0:
                        node1[x1][sn][3][MTnumber]+=d
                        pos4[x1]+=d
                        l4l[x1]+=d
                    pan1=1
                    panx=1
            if panx==1:   
                panx=0
                pan1=1
                ckF,de0,de1,de2,de3,de4,de5,de6,de7=checkF()
                if ckF==1:
                    for x2 in range(pair):
                        for xn in range(nu[x2]):
                            if kina[x2][xn]==1:
                                motor[x2][xn][0]+=de1[x2]
                            if kinb[x2][xn]==1:
                                motor[x2][xn][1]+=de2[x2]
                        for xn in range(nu1[x2]):
                            if kinap[x2][xn]==1:
                                motorp[x2][xn][0]+=de3[x2]
                            if kinbp[x2][xn]==1:
                                motorp[x2][xn][1]+=de2[x2]
                        for xn in range(nu1x[x2]):
                            if kinapx[x2][xn]==1:
                                motorpx[x2][xn][0]+=de4[x2]
                            if kinbpx[x2][xn]==1:
                                motorpx[x2][xn][1]+=de1[x2]

                        for ssx in range(2):
                            for xn in range(numc1[x2][ssx]):
                                motormc1[x2][ssx][xn]+=de3[x2]
                            for xn in range(numc2[x2][ssx]):
                                motormc2[x2][ssx][xn]+=de1[x2]
                            for xn in range(numc3[x2][ssx]):
                                motormc3[x2][ssx][xn]+=de2[x2]
                            for xn in range(numc4[x2][ssx]):
                                motormc4[x2][ssx][xn]+=de4[x2]
                            for xn in range(MTnumber+1):
                                node1[x2][ssx][0][xn]+=de3[x2]
                                node1[x2][ssx][1][xn]+=de1[x2]
                                node1[x2][ssx][2][xn]+=de2[x2]
                                node1[x2][ssx][3][xn]+=de4[x2]
                        
                        l2l[x2]+=de1[x2]
                        l2r[x2]+=de1[x2]
                        l3l[x2]+=de2[x2]
                        l3r[x2]+=de2[x2]
                        l1l[x2]+=de3[x2]
                        l1r[x2]+=de3[x2]
                        l4l[x2]+=de4[x2]
                        l4r[x2]+=de4[x2]
                        Ximt2[x2]+=de1[x2]
                        Ximt3[x2]+=de2[x2]
                        Xkmt1[x2]+=de3[x2]
                        Xkmt4[x2]+=de4[x2]
                    for ssx in range(2):
                        for xn in range(MTnumber):
                            for ton1 in range(Nma[ssx][xn][0]):   
                                if kinam[ssx][xn][0][ton1]==1:
                                    numa[ssx][xn][0][ton1][0]+=de1[0]
                                if kinbm[ssx][xn][0][ton1]==1:
                                    numa[ssx][xn][0][ton1][1]+=de1[1]
                            for ton1 in range(Nma[ssx][xn][1]):   
                                if kinam[ssx][xn][1][ton1]==1:
                                    numa[ssx][xn][1][ton1][0]+=de2[0]
                                if kinbm[ssx][xn][1][ton1]==1:
                                    numa[ssx][xn][1][ton1][1]+=de2[1]
                            for sik in range(2):
                                for ton1 in range(Nma1[sik][ssx][xn][0]):   
                                    if kinam1[sik][ssx][xn][0][ton1]==1:
                                        numa1[sik][ssx][xn][0][ton1][0]+=de3[sik]
                                    if kinbm1[sik][ssx][xn][0][ton1]==1:
                                        numa1[sik][ssx][xn][0][ton1][1]+=de1[sik]
                                for ton1 in range(Nma1[sik][ssx][xn][1]):   
                                    if kinam1[sik][ssx][xn][1][ton1]==1:
                                        numa1[sik][ssx][xn][1][ton1][0]+=de4[sik]
                                    if kinbm1[sik][ssx][xn][1][ton1]==1:
                                        numa1[sik][ssx][xn][1][ton1][1]+=de2[sik]
                    Xpole+=de0
                    Xpo+=de7
                    Xkin+=de5
                    Xkin1+=de6
                    ypsl0=energy0()
                    ypsl0p=ypsl0
                    ypsl0px=ypsl0
                    ckF,de0,de1,de2,de3,de4,de5,de6,de7=checkF()
                    if ckF==1:
                        #print('1474depo')
                        for x2 in range(pair):
                            for xn in range(nu[x2]):
                                if kina[x2][xn]==1:
                                    motor[x2][xn][0]+=de1[x2]
                                if kinb[x2][xn]==1:
                                    motor[x2][xn][1]+=de2[x2]
                            for xn in range(nu1[x2]):
                                if kinap[x2][xn]==1:
                                    motorp[x2][xn][0]+=de3[x2]
                                if kinbp[x2][xn]==1:
                                    motorp[x2][xn][1]+=de2[x2]
                            for xn in range(nu1x[x2]):
                                if kinapx[x2][xn]==1:
                                    motorpx[x2][xn][0]+=de4[x2]
                                if kinbpx[x2][xn]==1:
                                    motorpx[x2][xn][1]+=de1[x2]


                            for ssx in range(2):
                                for xn in range(numc1[x2][ssx]):
                                    motormc1[x2][ssx][xn]+=de3[x2]
                                for xn in range(numc2[x2][ssx]):
                                    motormc2[x2][ssx][xn]+=de1[x2]
                                for xn in range(numc3[x2][ssx]):
                                    motormc3[x2][ssx][xn]+=de2[x2]
                                for xn in range(numc4[x2][ssx]):
                                    motormc4[x2][ssx][xn]+=de4[x2]
                                for xn in range(MTnumber+1):
                                    node1[x2][ssx][0][xn]+=de3[x2]
                                    node1[x2][ssx][1][xn]+=de1[x2]
                                    node1[x2][ssx][2][xn]+=de2[x2]
                                    node1[x2][ssx][3][xn]+=de4[x2]
                            
                            l2l[x2]+=de1[x2]
                            l2r[x2]+=de1[x2]
                            l3l[x2]+=de2[x2]
                            l3r[x2]+=de2[x2]
                            l1l[x2]+=de3[x2]
                            l1r[x2]+=de3[x2]
                            l4l[x2]+=de4[x2]
                            l4r[x2]+=de4[x2]
                            Ximt2[x2]+=de1[x2]
                            Ximt3[x2]+=de2[x2]
                            Xkmt1[x2]+=de3[x2]
                            Xkmt4[x2]+=de4[x2]
                        for ssx in range(2):
                            for xn in range(MTnumber):
                                for ton1 in range(Nma[ssx][xn][0]):   
                                    if kinam[ssx][xn][0][ton1]==1:
                                        numa[ssx][xn][0][ton1][0]+=de1[0]
                                    if kinbm[ssx][xn][0][ton1]==1:
                                        numa[ssx][xn][0][ton1][1]+=de1[1]
                                for ton1 in range(Nma[ssx][xn][1]):   
                                    if kinam[ssx][xn][1][ton1]==1:
                                        numa[ssx][xn][1][ton1][0]+=de2[0]
                                    if kinbm[ssx][xn][1][ton1]==1:
                                        numa[ssx][xn][1][ton1][1]+=de2[1]
                                for sik in range(2):
                                    for ton1 in range(Nma1[sik][ssx][xn][0]):   
                                        if kinam1[sik][ssx][xn][0][ton1]==1:
                                            numa1[sik][ssx][xn][0][ton1][0]+=de3[sik]
                                        if kinbm1[sik][ssx][xn][0][ton1]==1:
                                            numa1[sik][ssx][xn][0][ton1][1]+=de1[sik]
                                    for ton1 in range(Nma1[sik][ssx][xn][1]):   
                                        if kinam1[sik][ssx][xn][1][ton1]==1:
                                            numa1[sik][ssx][xn][1][ton1][0]+=de4[sik]
                                        if kinbm1[sik][ssx][xn][1][ton1]==1:
                                            numa1[sik][ssx][xn][1][ton1][1]+=de2[sik]
                        Xpole+=de0
                        Xpo+=de7
                        Xkin+=de5
                        Xkin1+=de6
                        ypsl0=energy0()
                        ypsl0p=ypsl0
                        ypsl0px=ypsl0

        
        
        
        ########################################polymerization
    for x1 in range(pair):
        for sn in range(2):
            for xn in range(1,MTnumber+1):
                if xn==MTnumber and sn==1:
                    continue
                ran4=random.uniform(0, 1)
                if ran4<vpol*h:#MT2
                    if node1[x1][sn][1][MTnumber]<node1[x1][sn][2][0]:
                        #ttq=1
                        if xn ==MTnumber:
                            node1[x1][sn][1][xn]+=d
                            l2r[x1]+=d
                            pos2[x1]+=d
                        if xn < MTnumber:

                            for xx in range(numc2[x1][sn]):
                                if motormc2[x1][sn][xx]<node1[x1][sn][1][xn]-1:
                                    motormc2[x1][sn][xx]-=d

                            for xx in range(xn):
                                node1[x1][sn][1][xx]-=d
                            for xx in range(xn):
                                for ton1 in range(Nma[sn][xx][0]):   
                                    numa[sn][xx][0][ton1][x1]-=d
                                for ton1 in range(Nma1[x1][sn][xx][0]):   
                                    numa1[x1][sn][xx][0][ton1][1]-=d
                            overlap[x1][sn][1][xn-1]+=d
    

                ran4=random.uniform(0, 1)
                if ran4<vpol*h:
                    if node1[x1][sn][2][MTnumber]>node1[x1][sn][1][0]:
                        #ttq=2
                        if xn ==MTnumber:
                            node1[x1][sn][2][xn]-=d
                            l3l[x1]-=d
                        if xn < MTnumber:
                            for xx in range(numc3[x1][sn]):
                                if motormc3[x1][sn][xx]>node1[x1][sn][2][xn]+1:
                                    motormc3[x1][sn][xx]+=d
                            for xx in range(xn):
                                node1[x1][sn][2][xx]+=d
                            for xx in range(xn):
                                for ton1 in range(Nma[sn][xx][1]):   
                                    numa[sn][xx][1][ton1][x1]+=d
                                for ton1 in range(Nma1[x1][sn][xx][1]):   
                                    numa1[x1][sn][xx][1][ton1][1]+=d
                            overlap[x1][sn][2][xn-1]+=d

                if xn <MTnumber:
                    ran5 = random.uniform(0, 1)
                    if ran5<vpol*h:#MT1
                        #ttq=3
                        for xx in range(numc1[x1][sn]):
                            if motormc1[x1][sn][xx]<node1[x1][sn][0][xn]-1:
                                motormc1[x1][sn][xx]-=d
                        for xx in range(xn):
                            node1[x1][sn][0][xx]-=d
                        for xx in range(xn):
                            for ton1 in range(Nma1[x1][sn][xx][0]):   
                                numa1[x1][sn][xx][0][ton1][0]-=d
                        overlap[x1][sn][0][xn-1]+=d

                    ran5 = random.uniform(0, 1)
                    if ran5<vpol*h:#MT4
                        #ttq=4
                        for xx in range(numc4[x1][sn]):
                            if motormc4[x1][sn][xx]>node1[x1][sn][3][xn]+1:
                                motormc4[x1][sn][xx]+=d
                        for xx in range(xn):
                            node1[x1][sn][3][xx]+=d
                        for xx in range(xn):
                            for ton1 in range(Nma1[x1][sn][xx][1]):   
                                numa1[x1][sn][xx][1][ton1][0]+=d
                        overlap[x1][sn][3][xn-1]+=d
                        
                

        for sn in range(2):
            i=0
            while i < numc1[x1][sn]:
                zq=0
                for x2 in range(MTnumber):
                    if abs(motormc1[x1][sn][i]-node1[x1][sn][0][x2])<3/2*d and motormc1[x1][sn][i]>=node1[x1][sn][0][x2]-0.1:
                        zq=1
                        break
                if zq==1:
                    i+=1
                    continue
                ran4=random.uniform(0, 1)
                if ran4<koff*h:
                    del motormc1[x1][sn][i]
                    numc1[x1][sn]-=1
                    continue
                if motormc1[x1][sn][i]<node1[x1][sn][0][0]-0.1 or motormc1[x1][sn][i]>l1r[x1]+0.1:
                    del motormc1[x1][sn][i]
                    numc1[x1][sn]-=1
                    i-=1
                i+=1
            i=0
            while i < numc3[x1][sn]:
                zq=0
                for x2 in range(MTnumber):
                    if abs(motormc3[x1][sn][i]-node1[x1][sn][2][x2])<3/2*d and motormc3[x1][sn][i]<=node1[x1][sn][2][x2]+0.1:
                        zq=1
                        break
                if zq==1:
                    i+=1
                    continue
                ran4=random.uniform(0, 1)
                if ran4<koff*h:
                    del motormc3[x1][sn][i]
                    numc3[x1][sn]-=1
                    continue
                if motormc3[x1][sn][i]<l3l[x1]-0.1 or motormc3[x1][sn][i]>node1[x1][sn][2][0]+0.1:
                    del motormc3[x1][sn][i]
                    numc3[x1][sn]-=1
                    i-=1
                i+=1

            i=0
            while i < numc2[x1][sn]:
                zq=0
                for x2 in range(MTnumber):
                    if abs(motormc2[x1][sn][i]-node1[x1][sn][1][x2])<3/2*d and motormc2[x1][sn][i]>=node1[x1][sn][1][x2]-0.1:
                        zq=1
                        break
                if zq==1:
                    i+=1
                    continue
                ran4=random.uniform(0, 1)
                if ran4<koff*h:
                    del motormc2[x1][sn][i]
                    numc2[x1][sn]-=1
                    continue
                if motormc2[x1][sn][i]<node1[x1][sn][1][0]-0.1 or motormc2[x1][sn][i]>l2r[x1]+0.1:
                    del motormc2[x1][sn][i]
                    numc2[x1][sn]-=1
                    i-=1
                i+=1
            i=0
            while i < numc4[x1][sn]:
                zq=0
                for x2 in range(MTnumber):
                    if abs(motormc4[x1][sn][i]-node1[x1][sn][3][x2])<3/2*d and motormc4[x1][sn][i]<=node1[x1][sn][3][x2]+0.1:
                        zq=1
                        break
                if zq==1:
                    i+=1
                    continue
                ran4=random.uniform(0, 1)
                if ran4<koff*h:
                    del motormc4[x1][sn][i]
                    numc4[x1][sn]-=1
                    continue
                if motormc4[x1][sn][i]<l4l[x1]-0.1 or motormc4[x1][sn][i]>node1[x1][sn][3][0]+0.1:
                    del motormc4[x1][sn][i]
                    numc4[x1][sn]-=1
                    i-=1
                i+=1
                
#########################################################################Eg5 stepping               
    
    if pan1==1:
        for x1 in range(pair):
            nu[x1]=len(kina[x1])
            nu1[x1]=len(kinap[x1])
            nu1x[x1]=len(kinapx[x1])
            monum[x1]=sum(kina[x1])
            for xn in range(nu[x1]):
                if kina[x1][xn]==1 and kinb[x1][xn]==0:
                    monum[x1]-=1
            monump[x1]=sum(kinap[x1])
            for xn in range(nu1[x1]):
                if kinap[x1][xn]==1 and kinbp[x1][xn]==0:
                    monump[x1]-=1
            monumpx[x1]=sum(kinapx[x1])
            for xn in range(nu1x[x1]):
                if kinapx[x1][xn]==1 and kinbpx[x1][xn]==0:
                    monumpx[x1]-=1
    for x1 in range(pair):
        for i in range(0,nu[x1]):
            if kina[x1][i]+kinb[x1][i]<2:
                if pan1==1:
                    pan[x1][i]=0
                if kina[x1][i]==1 and kinb[x1][i]==0:
                    na=stepnum(0,0,0)
                    if na==1:
                        motor[x1][i][0]+=d
                    if na==-1:
                        motor[x1][i][0]-=d
                if kina[x1][i]==0 and kinb[x1][i]==1:
                    nb=stepnum(0,0,0)
                    if nb==1:
                        motor[x1][i][1]-=d
                    if nb==-1:
                        motor[x1][i][1]+=d
            if kina[x1][i]==1 and kinb[x1][i]==1:
                if pan1!=0:
                    dx1=(motor[x1][i][0]-motor[x1][i][1])
                    for x2 in range(pair):
                        F3[x2]=Kp2*(Xpo-l3r[x2])
                        F1[x2]=Kp1*(l1l[x2]-Xpole)+Kp3*(l1r[x2]-Xkin)
                        F2[x2]=Kp2*(l2l[x2]-Xpole)
                        F4[x2]=Kp1*(Xpo-l4r[x2])+Kp3*(Xkin1-l4l[x2])
                        for ton1 in range(nu[x2]):
                            if kina[x2][ton1]==1 and kinb[x2][ton1]==1:
                                dxc[x2][ton1]=motor[x2][ton1][0]-motor[x2][ton1][1]
                                if x1==x2 and i==ton1:
                                    dxc[x2][ton1]+=d
                                if dxc[x2][ton1]>xdmotor:
                                    F3[x2]+=(dxc[x2][ton1]-xdmotor)*Km
                                    F2[x2]+=(dxc[x2][ton1]-xdmotor)*Km
                                if dxc[x2][ton1]<-xdmotor:
                                    F3[x2]+=(dxc[x2][ton1]+xdmotor)*Km
                                    F2[x2]+=(dxc[x2][ton1]+xdmotor)*Km
                            if kina[x2][ton1]==0 or kinb[x2][ton1]==0:
                                dxc[x2][ton1]=0
                        for ton1 in range(nu1[x2]):
                            if kinap[x2][ton1]==1 and kinbp[x2][ton1]==1:
                                dxcp[x2][ton1]=motorp[x2][ton1][0]-motorp[x2][ton1][1]
                                if dxcp[x2][ton1]>xdmotor:
                                    F3[x2]+=(dxcp[x2][ton1]-xdmotor)*Km
                                    F1[x2]+=(dxcp[x2][ton1]-xdmotor)*Km
                                if dxcp[x2][ton1]<-xdmotor:
                                    F3[x2]+=(dxcp[x2][ton1]+xdmotor)*Km
                                    F1[x2]+=(dxcp[x2][ton1]+xdmotor)*Km
                            if kinap[x2][ton1]==0 or kinbp[x2][ton1]==0:
                                dxcp[x2][ton1]=0
                        for ton1 in range(nu1x[x2]):
                            if kinapx[x2][ton1]==1 and kinbpx[x2][ton1]==1:
                                dxcpx[x2][ton1]=motorpx[x2][ton1][0]-motorpx[x2][ton1][1]
                                if dxcpx[x2][ton1]>xdmotor:
                                    F4[x2]-=(dxcpx[x2][ton1]-xdmotor)*Km
                                    F2[x2]-=(dxcpx[x2][ton1]-xdmotor)*Km
                                if dxcpx[x2][ton1]<-xdmotor:
                                    F4[x2]-=(dxcpx[x2][ton1]+xdmotor)*Km
                                    F2[x2]-=(dxcpx[x2][ton1]+xdmotor)*Km
                            if kinapx[x2][ton1]==0 or kinbpx[x2][ton1]==0:
                                dxcpx[x2][ton1]=0
                    for ssx in range(2):
                        for xn in range(MTnumber):
                            for ton1 in range(Nma[ssx][xn][0]):
                                if kinam[ssx][xn][0][ton1]==1 and kinbm[ssx][xn][0][ton1]==1:
                                    dxnuma=numa[ssx][xn][0][ton1][0]-numa[ssx][xn][0][ton1][1]
                                    for to2 in range(xn,MTnumber-1):
                                        dxnuma+=overlap[0][ssx][1][to2]-overlap[1][ssx][1][to2]
                                    F2[0]+=Kpn5*dxnuma
                                    F2[1]-=Kpn5*dxnuma
                            for ton1 in range(Nma[ssx][xn][1]):
                                if kinam[ssx][xn][1][ton1]==1 and kinbm[ssx][xn][1][ton1]==1:
                                    dxnuma=numa[ssx][xn][1][ton1][0]-numa[ssx][xn][1][ton1][1]
                                    for to2 in range(xn,MTnumber-1):
                                        dxnuma+=-overlap[0][ssx][2][to2]+overlap[1][ssx][2][to2]
                                    F3[0]-=Kpn5*dxnuma
                                    F3[1]+=Kpn5*dxnuma
                            for sik in range(2):
                                for ton1 in range(Nma1[sik][ssx][xn][0]):
                                    if kinam1[sik][ssx][xn][0][ton1]==1 and kinbm1[sik][ssx][xn][0][ton1]==1:
                                        dxnuma1=numa1[sik][ssx][xn][0][ton1][0]-numa1[sik][ssx][xn][0][ton1][1]
                                        for to2 in range(xn,MTnumber-1):
                                            dxnuma1+=overlap[sik][ssx][0][to2]-overlap[sik][ssx][1][to2]
                                        F1[sik]+=Kpn5*dxnuma1
                                        F2[sik]-=Kpn5*dxnuma1
                                for ton1 in range(Nma1[sik][ssx][xn][1]):
                                    if kinam1[sik][ssx][xn][1][ton1]==1 and kinbm1[sik][ssx][xn][1][ton1]==1:
                                        dxnuma1=numa1[sik][ssx][xn][1][ton1][0]-numa1[sik][ssx][xn][1][ton1][1]
                                        for to2 in range(xn,MTnumber-1):
                                            dxnuma1+=-overlap[sik][ssx][3][to2]+overlap[sik][ssx][2][to2]
                                        F4[sik]-=Kpn5*dxnuma1
                                        F3[sik]+=Kpn5*dxnuma1
                    
                                               
                    zj0[x1][i],zj1[x1][i],zj2[x1][i],zj3[x1][i],zj4[x1][i],zj5[x1][i],zj6[x1][i],zj7[x1][i]=jiao(dxc,dxcp,dxcpx,F1,F2,F3,F4,monum,monump,monumpx)
                    dxc[x1][i]=dx1-d
                    if dx1+d>xdmotor:
                        F3[x1]-=(dx1+d-xdmotor)*Km
                        F2[x1]-=(dx1+d-xdmotor)*Km
                    if dx1+d<-xdmotor:
                        F3[x1]-=(dx1+d+xdmotor)*Km
                        F2[x1]-=(dx1+d+xdmotor)*Km
                    if dx1-d>xdmotor:
                        F3[x1]+=(dx1-d-xdmotor)*Km
                        F2[x1]+=(dx1-d-xdmotor)*Km
                    if dx1-d<-xdmotor:
                        F3[x1]+=(dx1-d+xdmotor)*Km
                        F2[x1]+=(dx1-d+xdmotor)*Km
                    #print(F1,F2,F3,F4)
                    js0[x1][i],js1[x1][i],js2[x1][i],js3[x1][i],js4[x1][i],js5[x1][i],js6[x1][i],js7[x1][i]=jiao(dxc,dxcp,dxcpx,F1,F2,F3,F4,monum,monump,monumpx)
                    ypsl1[x1][i],ypsl2[x1][i]=energy(x1,i)

                na=stepnum(ypsl0,ypsl1[x1][i],ypsl2[x1][i])
                nb=stepnum(ypsl0,ypsl1[x1][i],ypsl2[x1][i])
                if motor[x1][i][0]+d>l2r[x1] and na==1:
                    na=0
                if motor[x1][i][1]-d<l3l[x1] and nb==1:
                    nb=0
                if abs(na)>0.9 and abs(nb)>0.9:
                    if na+nb>=-1:
                        na=min(1,round(na+nb))
                    if na+nb<-1:
                        na=-1
                    nb=0
                if na>0.9:
                    zq=0
                    for xn in range(nu[x1]):
                        if motor[x1][i][0]+d>=motor[x1][xn][0]-0.1 and  motor[x1][i][0]<motor[x1][xn][0] and kina[x1][xn]==1:
                            zq=3
                    if zq==0:
                        motor[x1][i][0]+=d
                        pan1=1
                        pan[x1][i]=1
                if na<-0.9:
                    zq=0
                    for xn in range(nu[x1]):
                        if motor[x1][i][0]-d<=motor[x1][xn][0] and motor[x1][i][0]>motor[x1][xn][0] and kina[x1][xn]==1:
                            zq=3
                    if zq==0:
                        motor[x1][i][0]-=d
                        pan1=1
                        pan[x1][i]=1
                if nb>0.9 and na==0:
                    zq=0
                    for xn in range(nu[x1]):
                        if motor[x1][i][1]-d<=motor[x1][xn][1] and  motor[x1][i][1]>motor[x1][xn][1] and kinb[x1][xn]==1:
                            zq=3
                    if zq==0:
                        motor[x1][i][1]-=d
                        pan1=1
                        pan[x1][i]=1
                if nb<-0.9 and na==0:
                    zq=0
                    for xn in range(nu[x1]):
                        if motor[x1][i][1]+d>=motor[x1][xn][1] and  motor[x1][i][1]<motor[x1][xn][1] and kinb[x1][xn]==1:
                            zq=3
                    if zq==0:
                        motor[x1][i][1]+=d
                        pan1=1
                        pan[x1][i]=1
                if pan[x1][i]==1 and zq==0:
                    #print('mz',ypsl0,ypsl1[i],ypsl2[i])
                    if na>0.1 or nb>0.1:
                        for x2 in range(pair):
                            for xn in range(nu[x2]):
                                if kina[x2][xn]==1:
                                    motor[x2][xn][0]+=zj1[x1][i][x2]
                                if kinb[x2][xn]==1:
                                    motor[x2][xn][1]+=zj2[x1][i][x2]
                            for xn in range(nu1[x2]):
                                if kinap[x2][xn]==1:
                                    motorp[x2][xn][0]+=zj3[x1][i][x2]
                                if kinbp[x2][xn]==1:
                                    motorp[x2][xn][1]+=zj2[x1][i][x2]
                            for xn in range(nu1x[x2]):
                                if kinapx[x2][xn]==1:
                                    motorpx[x2][xn][0]+=zj4[x1][i][x2]
                                if kinbpx[x2][xn]==1:
                                    motorpx[x2][xn][1]+=zj1[x1][i][x2]
                            
                            for ssx in range(2):
                                for xn in range(numc1[x2][ssx]):
                                    motormc1[x2][ssx][xn]+=zj3[x1][i][x2]
                                for xn in range(numc2[x2][ssx]):
                                    motormc2[x2][ssx][xn]+=zj1[x1][i][x2]
                                for xn in range(numc3[x2][ssx]):
                                    motormc3[x2][ssx][xn]+=zj2[x1][i][x2]
                                for xn in range(numc4[x2][ssx]):
                                    motormc4[x2][ssx][xn]+=zj4[x1][i][x2]
                                for xn in range(MTnumber+1):
                                    node1[x2][ssx][0][xn]+=zj3[x1][i][x2]
                                    node1[x2][ssx][1][xn]+=zj1[x1][i][x2]
                                    node1[x2][ssx][2][xn]+=zj2[x1][i][x2]
                                    node1[x2][ssx][3][xn]+=zj4[x1][i][x2]
                            
                            l2l[x2]+=zj1[x1][i][x2]
                            l2r[x2]+=zj1[x1][i][x2]
                            l3l[x2]+=zj2[x1][i][x2]
                            l3r[x2]+=zj2[x1][i][x2]
                            l1l[x2]+=zj3[x1][i][x2]
                            l1r[x2]+=zj3[x1][i][x2]
                            l4l[x2]+=zj4[x1][i][x2]
                            l4r[x2]+=zj4[x1][i][x2]
                            Ximt2[x2]+=zj1[x1][i][x2]
                            Ximt3[x2]+=zj2[x1][i][x2]
                            Xkmt1[x2]+=zj3[x1][i][x2]
                            Xkmt4[x2]+=zj4[x1][i][x2]
                        
                        Xpole+=zj0[x1][i]
                        Xpo+=zj7[x1][i]
                        Xkin+=zj5[x1][i]
                        Xkin1+=zj6[x1][i]
                        for ssx in range(2):
                            for xn in range(MTnumber):
                                for ton1 in range(Nma[ssx][xn][0]):   
                                    if kinam[ssx][xn][0][ton1]==1:
                                        numa[ssx][xn][0][ton1][0]+=zj1[x1][i][0]
                                    if kinbm[ssx][xn][0][ton1]==1:
                                        numa[ssx][xn][0][ton1][1]+=zj1[x1][i][1]
                                for ton1 in range(Nma[ssx][xn][1]):   
                                    if kinam[ssx][xn][1][ton1]==1:
                                        numa[ssx][xn][1][ton1][0]+=zj2[x1][i][0]
                                    if kinbm[ssx][xn][1][ton1]==1:
                                        numa[ssx][xn][1][ton1][1]+=zj2[x1][i][1]
                                for sik in range(2):
                                    for ton1 in range(Nma1[sik][ssx][xn][0]):   
                                        if kinam1[sik][ssx][xn][0][ton1]==1:
                                            numa1[sik][ssx][xn][0][ton1][0]+=zj3[x1][i][sik]
                                        if kinbm1[sik][ssx][xn][0][ton1]==1:
                                            numa1[sik][ssx][xn][0][ton1][1]+=zj1[x1][i][sik]
                                    for ton1 in range(Nma1[sik][ssx][xn][1]):   
                                        if kinam1[sik][ssx][xn][1][ton1]==1:
                                            numa1[sik][ssx][xn][1][ton1][0]+=zj4[x1][i][sik]
                                        if kinbm1[sik][ssx][xn][1][ton1]==1:
                                            numa1[sik][ssx][xn][1][ton1][1]+=zj2[x1][i][sik]
                    if na<-0.1 or nb<-0.1:
                        for x2 in range(pair):
                            for xn in range(nu[x2]):
                                if kina[x2][xn]==1:
                                    motor[x2][xn][0]+=js1[x1][i][x2]
                                if kinb[x2][xn]==1:
                                    motor[x2][xn][1]+=js2[x1][i][x2]
                            for xn in range(nu1[x2]):
                                if kinap[x2][xn]==1:
                                    motorp[x2][xn][0]+=js3[x1][i][x2]
                                if kinbp[x2][xn]==1:
                                    motorp[x2][xn][1]+=js2[x1][i][x2]
                            for xn in range(nu1x[x2]):
                                if kinapx[x2][xn]==1:
                                    motorpx[x2][xn][0]+=js4[x1][i][x2]
                                if kinbpx[x2][xn]==1:
                                    motorpx[x2][xn][1]+=js1[x1][i][x2]
                            
                            for ssx in range(2):
                                for xn in range(numc1[x2][ssx]):
                                    motormc1[x2][ssx][xn]+=js3[x1][i][x2]
                                for xn in range(numc2[x2][ssx]):
                                    motormc2[x2][ssx][xn]+=js1[x1][i][x2]
                                for xn in range(numc3[x2][ssx]):
                                    motormc3[x2][ssx][xn]+=js2[x1][i][x2]
                                for xn in range(numc4[x2][ssx]):
                                    motormc4[x2][ssx][xn]+=js4[x1][i][x2]
                                for xn in range(MTnumber+1):
                                    node1[x2][ssx][0][xn]+=js3[x1][i][x2]
                                    node1[x2][ssx][1][xn]+=js1[x1][i][x2]
                                    node1[x2][ssx][2][xn]+=js2[x1][i][x2]
                                    node1[x2][ssx][3][xn]+=js4[x1][i][x2]
                            
                            l2l[x2]+=js1[x1][i][x2]
                            l2r[x2]+=js1[x1][i][x2]
                            l3l[x2]+=js2[x1][i][x2]
                            l3r[x2]+=js2[x1][i][x2]
                            l1l[x2]+=js3[x1][i][x2]
                            l1r[x2]+=js3[x1][i][x2]
                            l4l[x2]+=js4[x1][i][x2]
                            l4r[x2]+=js4[x1][i][x2]
                            Ximt2[x2]+=js1[x1][i][x2]
                            Ximt3[x2]+=js2[x1][i][x2]
                            Xkmt1[x2]+=js3[x1][i][x2]
                            Xkmt4[x2]+=js4[x1][i][x2]
                        Xpole+=js0[x1][i]
                        Xpo+=js7[x1][i]
                        Xkin+=js5[x1][i]
                        Xkin1+=js6[x1][i]
                        for ssx in range(2):
                            for xn in range(MTnumber):
                                for ton1 in range(Nma[ssx][xn][0]):   
                                    if kinam[ssx][xn][0][ton1]==1:
                                        numa[ssx][xn][0][ton1][0]+=js1[x1][i][0]
                                    if kinbm[ssx][xn][0][ton1]==1:
                                        numa[ssx][xn][0][ton1][1]+=js1[x1][i][1]
                                for ton1 in range(Nma[ssx][xn][1]):   
                                    if kinam[ssx][xn][1][ton1]==1:
                                        numa[ssx][xn][1][ton1][0]+=js2[x1][i][0]
                                    if kinbm[ssx][xn][1][ton1]==1:
                                        numa[ssx][xn][1][ton1][1]+=js2[x1][i][1]
                                for sik in range(2):
                                    for ton1 in range(Nma1[sik][ssx][xn][0]):   
                                        if kinam1[sik][ssx][xn][0][ton1]==1:
                                            numa1[sik][ssx][xn][0][ton1][0]+=js3[x1][i][sik]
                                        if kinbm1[sik][ssx][xn][0][ton1]==1:
                                            numa1[sik][ssx][xn][0][ton1][1]+=js1[x1][i][sik]
                                    for ton1 in range(Nma1[sik][ssx][xn][1]):   
                                        if kinam1[sik][ssx][xn][1][ton1]==1:
                                            numa1[sik][ssx][xn][1][ton1][0]+=js4[x1][i][sik]
                                        if kinbm1[sik][ssx][xn][1][ton1]==1:
                                            numa1[sik][ssx][xn][1][ton1][1]+=js2[x1][i][sik]
                                
                    ypsl0=energy0()
                    ypsl0p=ypsl0
                    ypsl0px=ypsl0
                    ckF,de0,de1,de2,de3,de4,de5,de6,de7=checkF()
                    if ckF==1:
                        #print(kk)
                        for x2 in range(pair):
                            for xn in range(nu[x2]):
                                if kina[x2][xn]==1:
                                    motor[x2][xn][0]+=de1[x2]
                                if kinb[x2][xn]==1:
                                    motor[x2][xn][1]+=de2[x2]
                            for xn in range(nu1[x2]):
                                if kinap[x2][xn]==1:
                                    motorp[x2][xn][0]+=de3[x2]
                                if kinbp[x2][xn]==1:
                                    motorp[x2][xn][1]+=de2[x2]
                            for xn in range(nu1x[x2]):
                                if kinapx[x2][xn]==1:
                                    motorpx[x2][xn][0]+=de4[x2]
                                if kinbpx[x2][xn]==1:
                                    motorpx[x2][xn][1]+=de1[x2]


                            for ssx in range(2):
                                for xn in range(numc1[x2][ssx]):
                                    motormc1[x2][ssx][xn]+=de3[x2]
                                for xn in range(numc2[x2][ssx]):
                                    motormc2[x2][ssx][xn]+=de1[x2]
                                for xn in range(numc3[x2][ssx]):
                                    motormc3[x2][ssx][xn]+=de2[x2]
                                for xn in range(numc4[x2][ssx]):
                                    motormc4[x2][ssx][xn]+=de4[x2]
                                for xn in range(MTnumber+1):
                                    node1[x2][ssx][0][xn]+=de3[x2]
                                    node1[x2][ssx][1][xn]+=de1[x2]
                                    node1[x2][ssx][2][xn]+=de2[x2]
                                    node1[x2][ssx][3][xn]+=de4[x2]
                            
                            l2l[x2]+=de1[x2]
                            l2r[x2]+=de1[x2]
                            l3l[x2]+=de2[x2]
                            l3r[x2]+=de2[x2]
                            l1l[x2]+=de3[x2]
                            l1r[x2]+=de3[x2]
                            l4l[x2]+=de4[x2]
                            l4r[x2]+=de4[x2]
                            Ximt2[x2]+=de1[x2]
                            Ximt3[x2]+=de2[x2]
                            Xkmt1[x2]+=de3[x2]
                            Xkmt4[x2]+=de4[x2]
                        for ssx in range(2):
                            for xn in range(MTnumber):
                                for ton1 in range(Nma[ssx][xn][0]):   
                                    if kinam[ssx][xn][0][ton1]==1:
                                        numa[ssx][xn][0][ton1][0]+=de1[0]
                                    if kinbm[ssx][xn][0][ton1]==1:
                                        numa[ssx][xn][0][ton1][1]+=de1[1]
                                for ton1 in range(Nma[ssx][xn][1]):   
                                    if kinam[ssx][xn][1][ton1]==1:
                                        numa[ssx][xn][1][ton1][0]+=de2[0]
                                    if kinbm[ssx][xn][1][ton1]==1:
                                        numa[ssx][xn][1][ton1][1]+=de2[1]
                                for sik in range(2):
                                    for ton1 in range(Nma1[sik][ssx][xn][0]):   
                                        if kinam1[sik][ssx][xn][0][ton1]==1:
                                            numa1[sik][ssx][xn][0][ton1][0]+=de3[sik]
                                        if kinbm1[sik][ssx][xn][0][ton1]==1:
                                            numa1[sik][ssx][xn][0][ton1][1]+=de1[sik]
                                    for ton1 in range(Nma1[sik][ssx][xn][1]):   
                                        if kinam1[sik][ssx][xn][1][ton1]==1:
                                            numa1[sik][ssx][xn][1][ton1][0]+=de4[sik]
                                        if kinbm1[sik][ssx][xn][1][ton1]==1:
                                            numa1[sik][ssx][xn][1][ton1][1]+=de2[sik]
                        Xpole+=de0
                        Xpo+=de7
                        Xkin+=de5
                        Xkin1+=de6
                        ypsl0=energy0()
                        ypsl0p=ypsl0
                        ypsl0px=ypsl0
                        
                if pan1==1:
                    if abs(na)+abs(nb)==0:
                        pan[x1][i]=0


    for x1 in range(pair):
        for i in range(nu1[x1]):
            if kinap[x1][i]+kinbp[x1][i]<2:
                if pan1==1:
                    panp[x1][i]=0
                if kinap[x1][i]==1 and kinbp[x1][i]==0:
                    na=stepnum(0,0,0)
                    if na==1:
                        motorp[x1][i][0]+=d
                    if na==-1:
                        motorp[x1][i][0]-=d
                if kinap[x1][i]==0 and kinbp[x1][i]==1:
                    nb=stepnum(0,0,0)
                    if nb==1:
                        motorp[x1][i][1]-=d
                    if nb==-1:
                        motorp[x1][i][1]+=d
            if kinap[x1][i]==1 and kinbp[x1][i]==1:
                if pan1!=0:
                    dx1=(motorp[x1][i][0]-motorp[x1][i][1])
                    for x2 in range(pair):
                        F3[x2]=Kp2*(Xpo-l3r[x2])
                        F1[x2]=Kp1*(l1l[x2]-Xpole)+Kp3*(l1r[x2]-Xkin)
                        F2[x2]=Kp2*(l2l[x2]-Xpole)
                        F4[x2]=Kp1*(Xpo-l4r[x2])+Kp3*(Xkin1-l4l[x2])
                        for ton1 in range(nu[x2]):
                            if kina[x2][ton1]==1 and kinb[x2][ton1]==1:
                                dxc[x2][ton1]=motor[x2][ton1][0]-motor[x2][ton1][1]

                                if dxc[x2][ton1]>xdmotor:
                                    F3[x2]+=(dxc[x2][ton1]-xdmotor)*Km
                                    F2[x2]+=(dxc[x2][ton1]-xdmotor)*Km
                                if dxc[x2][ton1]<-xdmotor:
                                    F3[x2]+=(dxc[x2][ton1]+xdmotor)*Km
                                    F2[x2]+=(dxc[x2][ton1]+xdmotor)*Km
                            if kina[x2][ton1]==0 or kinb[x2][ton1]==0:
                                dxc[x2][ton1]=0
                        for ton1 in range(nu1[x2]):
                            if kinap[x2][ton1]==1 and kinbp[x2][ton1]==1:
                                dxcp[x2][ton1]=motorp[x2][ton1][0]-motorp[x2][ton1][1]
                                if x1==x2 and i==ton1:
                                    dxcp[x2][ton1]+=d
                                if dxcp[x2][ton1]>xdmotor:
                                    F3[x2]+=(dxcp[x2][ton1]-xdmotor)*Km
                                    F1[x2]+=(dxcp[x2][ton1]-xdmotor)*Km
                                if dxcp[x2][ton1]<-xdmotor:
                                    F3[x2]+=(dxcp[x2][ton1]+xdmotor)*Km
                                    F1[x2]+=(dxcp[x2][ton1]+xdmotor)*Km
                            if kinap[x2][ton1]==0 or kinbp[x2][ton1]==0:
                                dxcp[x2][ton1]=0
                        for ton1 in range(nu1x[x2]):
                            if kinapx[x2][ton1]==1 and kinbpx[x2][ton1]==1:
                                dxcpx[x2][ton1]=motorpx[x2][ton1][0]-motorpx[x2][ton1][1]
                                if dxcpx[x2][ton1]>xdmotor:
                                    F4[x2]-=(dxcpx[x2][ton1]-xdmotor)*Km
                                    F2[x2]-=(dxcpx[x2][ton1]-xdmotor)*Km
                                if dxcpx[x2][ton1]<-xdmotor:
                                    F4[x2]-=(dxcpx[x2][ton1]+xdmotor)*Km
                                    F2[x2]-=(dxcpx[x2][ton1]+xdmotor)*Km
                            if kinapx[x2][ton1]==0 or kinbpx[x2][ton1]==0:
                                dxcpx[x2][ton1]=0
                    for ssx in range(2):
                        for xn in range(MTnumber):
                            for ton1 in range(Nma[ssx][xn][0]):
                                if kinam[ssx][xn][0][ton1]==1 and kinbm[ssx][xn][0][ton1]==1:
                                    dxnuma=numa[ssx][xn][0][ton1][0]-numa[ssx][xn][0][ton1][1]
                                    for to2 in range(xn,MTnumber-1):
                                        dxnuma+=overlap[0][ssx][1][to2]-overlap[1][ssx][1][to2]
                                    F2[0]+=Kpn5*dxnuma
                                    F2[1]-=Kpn5*dxnuma
                            for ton1 in range(Nma[ssx][xn][1]):
                                if kinam[ssx][xn][1][ton1]==1 and kinbm[ssx][xn][1][ton1]==1:
                                    dxnuma=numa[ssx][xn][1][ton1][0]-numa[ssx][xn][1][ton1][1]
                                    for to2 in range(xn,MTnumber-1):
                                        dxnuma+=-overlap[0][ssx][2][to2]+overlap[1][ssx][2][to2]
                                    F3[0]-=Kpn5*dxnuma
                                    F3[1]+=Kpn5*dxnuma
                            for sik in range(2):
                                for ton1 in range(Nma1[sik][ssx][xn][0]):
                                    if kinam1[sik][ssx][xn][0][ton1]==1 and kinbm1[sik][ssx][xn][0][ton1]==1:
                                        dxnuma1=numa1[sik][ssx][xn][0][ton1][0]-numa1[sik][ssx][xn][0][ton1][1]
                                        for to2 in range(xn,MTnumber-1):
                                            dxnuma1+=overlap[sik][ssx][0][to2]-overlap[sik][ssx][1][to2]
                                        F1[sik]+=Kpn5*dxnuma1
                                        F2[sik]-=Kpn5*dxnuma1
                                for ton1 in range(Nma1[sik][ssx][xn][1]):
                                    if kinam1[sik][ssx][xn][1][ton1]==1 and kinbm1[sik][ssx][xn][1][ton1]==1:
                                        dxnuma1=numa1[sik][ssx][xn][1][ton1][0]-numa1[sik][ssx][xn][1][ton1][1]
                                        for to2 in range(xn,MTnumber-1):
                                            dxnuma1+=-overlap[sik][ssx][3][to2]+overlap[sik][ssx][2][to2]
                                        F4[sik]-=Kpn5*dxnuma1
                                        F3[sik]+=Kpn5*dxnuma1
                    zj0p[x1][i],zj1p[x1][i],zj2p[x1][i],zj3p[x1][i],zj4p[x1][i],zj5p[x1][i],zj6p[x1][i],zj7p[x1][i]=jiao(dxc,dxcp,dxcpx,F1,F2,F3,F4,monum,monump,monumpx)
                    dxcp[x1][i]=dx1-d
                    if dx1+d>xdmotor:
                        F3[x1]-=(dx1+d-xdmotor)*Km
                        F1[x1]-=(dx1+d-xdmotor)*Km
                    if dx1+d<-xdmotor:
                        F3[x1]-=(dx1+d+xdmotor)*Km
                        F1[x1]-=(dx1+d+xdmotor)*Km
                    if dx1-d>xdmotor:
                        F3[x1]+=(dx1-d-xdmotor)*Km
                        F1[x1]+=(dx1-d-xdmotor)*Km
                    if dx1-d<-xdmotor:
                        F3[x1]+=(dx1-d+xdmotor)*Km
                        F1[x1]+=(dx1-d+xdmotor)*Km
                    
                    js0p[x1][i],js1p[x1][i],js2p[x1][i],js3p[x1][i],js4p[x1][i],js5p[x1][i],js6p[x1][i],js7p[x1][i]=jiao(dxc,dxcp,dxcpx,F1,F2,F3,F4,monum,monump,monumpx)
                    ypsl1p[x1][i],ypsl2p[x1][i]=energyp(x1,i)

                na=stepnum(ypsl0p,ypsl1p[x1][i],ypsl2p[x1][i])
                nb=stepnum(ypsl0p,ypsl1p[x1][i],ypsl2p[x1][i])

                if motorp[x1][i][0]+d>l1r[x1] and na==1:
                    na=0
                if motorp[x1][i][1]-d<l3l[x1] and nb==1:
                    nb=0
                if abs(na)>0.9 and abs(nb)>0.9:
                    if na+nb>=-1:
                        na=min(1,round(na+nb))
                    if na+nb<-1:
                        na=-1
                    nb=0
                if na>0.9:
                    zq=0
                    for xn in range(nu1[x1]):
                        if motorp[x1][i][0]+d>=motorp[x1][xn][0] and  motorp[x1][i][0]<motorp[x1][xn][0] and kinap[x1][xn]==1:
                            zq=3
                    if zq==0:
                        motorp[x1][i][0]+=d
                        pan1=1
                        panp[x1][i]=1
                if na<-0.9:
                    zq=0
                    for xn in range(nu1[x1]):
                        if motorp[x1][i][0]-d<=motorp[x1][xn][0] and motorp[x1][i][0]>motorp[x1][xn][0] and kinap[x1][xn]==1:
                            zq=3
                    if zq==0:
                        motorp[x1][i][0]-=d
                        pan1=1
                        panp[x1][i]=1
                if nb>0.9 and na==0:
                    zq=0
                    for xn in range(nu1[x1]):
                        if motorp[x1][i][1]-d<=motorp[x1][xn][1] and  motorp[x1][i][1]>motorp[x1][xn][1] and kinbp[x1][xn]==1:
                            zq=3
                    if zq==0:
                        motorp[x1][i][1]-=d
                        pan1=1
                        panp[x1][i]=1
                if nb<-0.9 and na==0:
                    zq=0
                    for xn in range(nu1[x1]):
                        if motorp[x1][i][1]+d>=motorp[x1][xn][1] and  motorp[x1][i][1]<motorp[x1][xn][1] and kinbp[x1][xn]==1:
                            zq=3
                    if zq==0:
                        motorp[x1][i][1]+=d
                        pan1=1
                        panp[x1][i]=1
                if pan1==1:
                    if abs(na)+abs(nb)==0:
                        panp[x1][i]=0
                if panp[x1][i]==1 and zq==0:
                    #print('mpz',ypsl0p,ypsl1p[i],ypsl2p[i],na,nb,motorp[i][0]-motorp[i][1])
                    if na>0.1 or nb>0.1:
                        for x2 in range(pair):
                            for xn in range(nu[x2]):
                                if kina[x2][xn]==1:
                                    motor[x2][xn][0]+=zj1p[x1][i][x2]
                                if kinb[x2][xn]==1:
                                    motor[x2][xn][1]+=zj2p[x1][i][x2]
                            for xn in range(nu1[x2]):
                                if kinap[x2][xn]==1:
                                    motorp[x2][xn][0]+=zj3p[x1][i][x2]
                                if kinbp[x2][xn]==1:
                                    motorp[x2][xn][1]+=zj2p[x1][i][x2]
                            for xn in range(nu1x[x2]):
                                if kinapx[x2][xn]==1:
                                    motorpx[x2][xn][0]+=zj4p[x1][i][x2]
                                if kinbpx[x2][xn]==1:
                                    motorpx[x2][xn][1]+=zj1p[x1][i][x2]
                            
                            for ssx in range(2):
                                for xn in range(numc1[x2][ssx]):
                                    motormc1[x2][ssx][xn]+=zj3p[x1][i][x2]
                                for xn in range(numc2[x2][ssx]):
                                    motormc2[x2][ssx][xn]+=zj1p[x1][i][x2]
                                for xn in range(numc3[x2][ssx]):
                                    motormc3[x2][ssx][xn]+=zj2p[x1][i][x2]
                                for xn in range(numc4[x2][ssx]):
                                    motormc4[x2][ssx][xn]+=zj4p[x1][i][x2]
                                for xn in range(MTnumber+1):
                                    node1[x2][ssx][0][xn]+=zj3p[x1][i][x2]
                                    node1[x2][ssx][1][xn]+=zj1p[x1][i][x2]
                                    node1[x2][ssx][2][xn]+=zj2p[x1][i][x2]
                                    node1[x2][ssx][3][xn]+=zj4p[x1][i][x2]
                            
                            l2l[x2]+=zj1p[x1][i][x2]
                            l2r[x2]+=zj1p[x1][i][x2]
                            l3l[x2]+=zj2p[x1][i][x2]
                            l3r[x2]+=zj2p[x1][i][x2]
                            l1l[x2]+=zj3p[x1][i][x2]
                            l1r[x2]+=zj3p[x1][i][x2]
                            l4l[x2]+=zj4p[x1][i][x2]
                            l4r[x2]+=zj4p[x1][i][x2]
                            Ximt2[x2]+=zj1p[x1][i][x2]
                            Ximt3[x2]+=zj2p[x1][i][x2]
                            Xkmt1[x2]+=zj3p[x1][i][x2]
                            Xkmt4[x2]+=zj4p[x1][i][x2]
                        Xpole+=zj0p[x1][i]
                        Xpo+=zj7p[x1][i]
                        Xkin+=zj5p[x1][i]
                        Xkin1+=zj6p[x1][i]
                        for ssx in range(2):
                            for xn in range(MTnumber):
                                for ton1 in range(Nma[ssx][xn][0]):   
                                    if kinam[ssx][xn][0][ton1]==1:
                                        numa[ssx][xn][0][ton1][0]+=zj1p[x1][i][0]
                                    if kinbm[ssx][xn][0][ton1]==1:
                                        numa[ssx][xn][0][ton1][1]+=zj1p[x1][i][1]
                                for ton1 in range(Nma[ssx][xn][1]):   
                                    if kinam[ssx][xn][1][ton1]==1:
                                        numa[ssx][xn][1][ton1][0]+=zj2p[x1][i][0]
                                    if kinbm[ssx][xn][1][ton1]==1:
                                        numa[ssx][xn][1][ton1][1]+=zj2p[x1][i][1]
                                for sik in range(2):
                                    for ton1 in range(Nma1[sik][ssx][xn][0]):   
                                        if kinam1[sik][ssx][xn][0][ton1]==1:
                                            numa1[sik][ssx][xn][0][ton1][0]+=zj3p[x1][i][sik]
                                        if kinbm1[sik][ssx][xn][0][ton1]==1:
                                            numa1[sik][ssx][xn][0][ton1][1]+=zj1p[x1][i][sik]
                                    for ton1 in range(Nma1[sik][ssx][xn][1]):   
                                        if kinam1[sik][ssx][xn][1][ton1]==1:
                                            numa1[sik][ssx][xn][1][ton1][0]+=zj4p[x1][i][sik]
                                        if kinbm1[sik][ssx][xn][1][ton1]==1:
                                            numa1[sik][ssx][xn][1][ton1][1]+=zj2p[x1][i][sik]
                    if na<-0.1 or nb<-0.1:
                        for x2 in range(pair):
                            for xn in range(nu[x2]):
                                if kina[x2][xn]==1:
                                    motor[x2][xn][0]+=js1p[x1][i][x2]
                                if kinb[x2][xn]==1:
                                    motor[x2][xn][1]+=js2p[x1][i][x2]
                            for xn in range(nu1[x2]):
                                if kinap[x2][xn]==1:
                                    motorp[x2][xn][0]+=js3p[x1][i][x2]
                                if kinbp[x2][xn]==1:
                                    motorp[x2][xn][1]+=js2p[x1][i][x2]
                            for xn in range(nu1x[x2]):
                                if kinapx[x2][xn]==1:
                                    motorpx[x2][xn][0]+=js4p[x1][i][x2]
                                if kinbpx[x2][xn]==1:
                                    motorpx[x2][xn][1]+=js1p[x1][i][x2]
                            
                                
                            for ssx in range(2):
                                for xn in range(numc1[x2][ssx]):
                                    motormc1[x2][ssx][xn]+=js3p[x1][i][x2]
                                for xn in range(numc2[x2][ssx]):
                                    motormc2[x2][ssx][xn]+=js1p[x1][i][x2]
                                for xn in range(numc3[x2][ssx]):
                                    motormc3[x2][ssx][xn]+=js2p[x1][i][x2]
                                for xn in range(numc4[x2][ssx]):
                                    motormc4[x2][ssx][xn]+=js4p[x1][i][x2]
                                for xn in range(MTnumber+1):
                                    node1[x2][ssx][0][xn]+=js3p[x1][i][x2]
                                    node1[x2][ssx][1][xn]+=js1p[x1][i][x2]
                                    node1[x2][ssx][2][xn]+=js2p[x1][i][x2]
                                    node1[x2][ssx][3][xn]+=js4p[x1][i][x2]
                            
                            l2l[x2]+=js1p[x1][i][x2]
                            l2r[x2]+=js1p[x1][i][x2]
                            l3l[x2]+=js2p[x1][i][x2]
                            l3r[x2]+=js2p[x1][i][x2]
                            l1l[x2]+=js3p[x1][i][x2]
                            l1r[x2]+=js3p[x1][i][x2]
                            l4l[x2]+=js4p[x1][i][x2]
                            l4r[x2]+=js4p[x1][i][x2]
                            Ximt2[x2]+=js1p[x1][i][x2]
                            Ximt3[x2]+=js2p[x1][i][x2]
                            Xkmt1[x2]+=js3p[x1][i][x2]
                            Xkmt4[x2]+=js4p[x1][i][x2]
                        Xpole+=js0p[x1][i]
                        Xpo+=js7p[x1][i]
                        Xkin+=js5p[x1][i]
                        Xkin1+=js6p[x1][i]
                        for ssx in range(2):
                            for xn in range(MTnumber):
                                for ton1 in range(Nma[ssx][xn][0]):   
                                    if kinam[ssx][xn][0][ton1]==1:
                                        numa[ssx][xn][0][ton1][0]+=js1p[x1][i][0]
                                    if kinbm[ssx][xn][0][ton1]==1:
                                        numa[ssx][xn][0][ton1][1]+=js1p[x1][i][1]
                                for ton1 in range(Nma[ssx][xn][1]):   
                                    if kinam[ssx][xn][1][ton1]==1:
                                        numa[ssx][xn][1][ton1][0]+=js2p[x1][i][0]
                                    if kinbm[ssx][xn][1][ton1]==1:
                                        numa[ssx][xn][1][ton1][1]+=js2p[x1][i][1]
                                for sik in range(2):
                                    for ton1 in range(Nma1[sik][ssx][xn][0]):   
                                        if kinam1[sik][ssx][xn][0][ton1]==1:
                                            numa1[sik][ssx][xn][0][ton1][0]+=js3p[x1][i][sik]
                                        if kinbm1[sik][ssx][xn][0][ton1]==1:
                                            numa1[sik][ssx][xn][0][ton1][1]+=js1p[x1][i][sik]
                                    for ton1 in range(Nma1[sik][ssx][xn][1]):   
                                        if kinam1[sik][ssx][xn][1][ton1]==1:
                                            numa1[sik][ssx][xn][1][ton1][0]+=js4p[x1][i][sik]
                                        if kinbm1[sik][ssx][xn][1][ton1]==1:
                                            numa1[sik][ssx][xn][1][ton1][1]+=js2p[x1][i][sik]
                                
                    ypsl0=energy0()
                    ypsl0p=ypsl0
                    ypsl0px=ypsl0
                    

    for x1 in range(pair):
        for i in range(nu1x[x1]):
            if kinapx[x1][i]+kinbpx[x1][i]<2:
                panpx[x1][i]=0
                if kinapx[x1][i]==1 and kinbpx[x1][i]==0:
                    na=stepnum(0,0,0)
                    if na==1:
                        motorpx[x1][i][0]-=d
                    if na==-1:
                        motorpx[x1][i][0]+=d
                if kinapx[x1][i]==0 and kinbpx[x1][i]==1:
                    nb=stepnum(0,0,0)
                    if nb==1:
                        motorpx[x1][i][1]+=d
                    if nb==-1:
                        motorpx[x1][i][1]-=d
            if kinapx[x1][i]==1 and kinbpx[x1][i]==1:
                if pan1!=0:
                    dx1=(motorpx[x1][i][0]-motorpx[x1][i][1])
                    for x2 in range(pair):
                        F3[x2]=Kp2*(Xpo-l3r[x2])
                        F1[x2]=Kp1*(l1l[x2]-Xpole)+Kp3*(l1r[x2]-Xkin)
                        F2[x2]=Kp2*(l2l[x2]-Xpole)
                        F4[x2]=Kp1*(Xpo-l4r[x2])+Kp3*(Xkin1-l4l[x2])
                        for ton1 in range(nu[x2]):
                            if kina[x2][ton1]==1 and kinb[x2][ton1]==1:
                                dxc[x2][ton1]=motor[x2][ton1][0]-motor[x2][ton1][1]
                                if dxc[x2][ton1]>xdmotor:
                                    F3[x2]+=(dxc[x2][ton1]-xdmotor)*Km
                                    F2[x2]+=(dxc[x2][ton1]-xdmotor)*Km
                                if dxc[x2][ton1]<-xdmotor:
                                    F3[x2]+=(dxc[x2][ton1]+xdmotor)*Km
                                    F2[x2]+=(dxc[x2][ton1]+xdmotor)*Km
                            if kina[x2][ton1]==0 or kinb[x2][ton1]==0:
                                dxc[x2][ton1]=0
                        for ton1 in range(nu1[x2]):
                            if kinap[x2][ton1]==1 and kinbp[x2][ton1]==1:
                                dxcp[x2][ton1]=motorp[x2][ton1][0]-motorp[x2][ton1][1]

                                if dxcp[x2][ton1]>xdmotor:
                                    F3[x2]+=(dxcp[x2][ton1]-xdmotor)*Km
                                    F1[x2]+=(dxcp[x2][ton1]-xdmotor)*Km
                                if dxcp[x2][ton1]<-xdmotor:
                                    F3[x2]+=(dxcp[x2][ton1]+xdmotor)*Km
                                    F1[x2]+=(dxcp[x2][ton1]+xdmotor)*Km
                            if kinap[x2][ton1]==0 or kinbp[x2][ton1]==0:
                                dxcp[x2][ton1]=0
                        for ton1 in range(nu1x[x2]):
                            if kinapx[x2][ton1]==1 and kinbpx[x2][ton1]==1:
                                dxcpx[x2][ton1]=motorpx[x2][ton1][0]-motorpx[x2][ton1][1]
                                if x1==x2 and i==ton1:
                                    dxcpx[x2][ton1]+=d
                                if dxcpx[x2][ton1]>xdmotor:
                                    F4[x2]-=(dxcpx[x2][ton1]-xdmotor)*Km
                                    F2[x2]-=(dxcpx[x2][ton1]-xdmotor)*Km
                                if dxcpx[x2][ton1]<-xdmotor:
                                    F4[x2]-=(dxcpx[x2][ton1]+xdmotor)*Km
                                    F2[x2]-=(dxcpx[x2][ton1]+xdmotor)*Km
                            if kinapx[x2][ton1]==0 or kinbpx[x2][ton1]==0:
                                dxcpx[x2][ton1]=0
                    for ssx in range(2):
                        for xn in range(MTnumber):
                            for ton1 in range(Nma[ssx][xn][0]):
                                if kinam[ssx][xn][0][ton1]==1 and kinbm[ssx][xn][0][ton1]==1:
                                    dxnuma=numa[ssx][xn][0][ton1][0]-numa[ssx][xn][0][ton1][1]
                                    for to2 in range(xn,MTnumber-1):
                                        dxnuma+=overlap[0][ssx][1][to2]-overlap[1][ssx][1][to2]
                                    F2[0]+=Kpn5*dxnuma
                                    F2[1]-=Kpn5*dxnuma
                            for ton1 in range(Nma[ssx][xn][1]):
                                if kinam[ssx][xn][1][ton1]==1 and kinbm[ssx][xn][1][ton1]==1:
                                    dxnuma=numa[ssx][xn][1][ton1][0]-numa[ssx][xn][1][ton1][1]
                                    for to2 in range(xn,MTnumber-1):
                                        dxnuma+=-overlap[0][ssx][2][to2]+overlap[1][ssx][2][to2]
                                    F3[0]-=Kpn5*dxnuma
                                    F3[1]+=Kpn5*dxnuma
                            for sik in range(2):
                                for ton1 in range(Nma1[sik][ssx][xn][0]):
                                    if kinam1[sik][ssx][xn][0][ton1]==1 and kinbm1[sik][ssx][xn][0][ton1]==1:
                                        dxnuma1=numa1[sik][ssx][xn][0][ton1][0]-numa1[sik][ssx][xn][0][ton1][1]
                                        for to2 in range(xn,MTnumber-1):
                                            dxnuma1+=overlap[sik][ssx][0][to2]-overlap[sik][ssx][1][to2]
                                        F1[sik]+=Kpn5*dxnuma1
                                        F2[sik]-=Kpn5*dxnuma1
                                for ton1 in range(Nma1[sik][ssx][xn][1]):
                                    if kinam1[sik][ssx][xn][1][ton1]==1 and kinbm1[sik][ssx][xn][1][ton1]==1:
                                        dxnuma1=numa1[sik][ssx][xn][1][ton1][0]-numa1[sik][ssx][xn][1][ton1][1]
                                        for to2 in range(xn,MTnumber-1):
                                            dxnuma1+=-overlap[sik][ssx][3][to2]+overlap[sik][ssx][2][to2]
                                        F4[sik]-=Kpn5*dxnuma1
                                        F3[sik]+=Kpn5*dxnuma1
                    zj0px[x1][i],zj1px[x1][i],zj2px[x1][i],zj3px[x1][i],zj4px[x1][i],zj5px[x1][i],zj6px[x1][i],zj7px[x1][i]=jiao(dxc,dxcp,dxcpx,F1,F2,F3,F4,monum,monump,monumpx)
                    dxcpx[x1][i]=dx1-d
                    if dx1+d>xdmotor:
                        F4[x1]+=(dx1+d-xdmotor)*Km
                        F2[x1]+=(dx1+d-xdmotor)*Km
                    if dx1+d<-xdmotor:
                        F4[x1]+=(dx1+d+xdmotor)*Km
                        F2[x1]+=(dx1+d+xdmotor)*Km
                    if dx1-d>xdmotor:
                        F4[x1]-=(dx1-d-xdmotor)*Km
                        F2[x1]-=(dx1-d-xdmotor)*Km
                    if dx1-d<-xdmotor:
                        F4[x1]-=(dx1-d+xdmotor)*Km
                        F2[x1]-=(dx1-d+xdmotor)*Km
                    js0px[x1][i],js1px[x1][i],js2px[x1][i],js3px[x1][i],js4px[x1][i],js5px[x1][i],js6px[x1][i],js7px[x1][i]=jiao(dxc,dxcp,dxcpx,F1,F2,F3,F4,monum,monump,monumpx)
                    ypsl1px[x1][i],ypsl2px[x1][i]=energypx(x1,i)

                na=stepnum(ypsl0px,ypsl2px[x1][i],ypsl1px[x1][i])
                nb=stepnum(ypsl0px,ypsl2px[x1][i],ypsl1px[x1][i])
                if motorpx[x1][i][0]-d<l4l[x1] and na==1:
                    na=0
                if motorpx[x1][i][1]+d>l2r[x1] and nb==1:
                    nb=0
                if abs(na)>0.9 and abs(nb)>0.9:
                    if na+nb>=-1:
                        na=min(1,round(na+nb))
                    if na+nb<-1:
                        na=-1
                    nb=0
                if na<-0.9:
                    zq=0
                    for xn in range(nu1x[x1]):
                        if motorpx[x1][i][0]+d>=motorpx[x1][xn][0] and  motorpx[x1][i][0]<motorpx[x1][xn][0] and kinapx[x1][xn]==1:
                            zq=3
                    if zq==0:
                        motorpx[x1][i][0]+=d
                        pan1=1
                        panpx[x1][i]=1

                if na>0.9:
                    zq=0
                    for xn in range(nu1x[x1]):
                        if motorpx[x1][i][0]-d<=motorpx[x1][xn][0] and motorpx[x1][i][0]>motorpx[x1][xn][0] and kinapx[x1][xn]==1:
                            zq=3
                    if zq==0:
                        motorpx[x1][i][0]-=d
                        pan1=1
                        panpx[x1][i]=1
                if nb<-0.9 and na==0:
                    zq=0
                    for xn in range(nu1x[x1]):
                        if motorpx[x1][i][1]-d<=motorpx[x1][xn][1] and  motorpx[x1][i][1]>motorpx[x1][xn][1] and kinbpx[x1][xn]==1:
                            zq=3
                    if zq==0:
                        motorpx[x1][i][1]-=d
                        pan1=1
                        panpx[x1][i]=1
                if nb>0.9 and na==0:
                    zq=0
                    for xn in range(nu1x[x1]):
                        if motorpx[x1][i][1]+d>=motorpx[x1][xn][1] and  motorpx[x1][i][1]<motorpx[x1][xn][1] and kinbpx[x1][xn]==1:
                            zq=3
                    if zq==0:
                        motorpx[x1][i][1]+=d
                        pan1=1
                        panpx[x1][i]=1
                if panpx[x1][i]==1 and zq==0:
                    #print('mpxz',ypsl0px,ypsl2px[i],ypsl1px[i],dxcpx[i])
                    if na<-0.1 or nb<-0.1:
                        for x2 in range(pair):
                            for xn in range(nu[x2]):
                                if kina[x2][xn]==1:
                                    motor[x2][xn][0]+=zj1px[x1][i][x2]
                                if kinb[x2][xn]==1:
                                    motor[x2][xn][1]+=zj2px[x1][i][x2]
                            for xn in range(nu1[x2]):
                                if kinap[x2][xn]==1:
                                    motorp[x2][xn][0]+=zj3px[x1][i][x2]
                                if kinbp[x2][xn]==1:
                                    motorp[x2][xn][1]+=zj2px[x1][i][x2]
                            for xn in range(nu1x[x2]):
                                if kinapx[x2][xn]==1:
                                    motorpx[x2][xn][0]+=zj4px[x1][i][x2]
                                if kinbpx[x2][xn]==1:
                                    motorpx[x2][xn][1]+=zj1px[x1][i][x2]
                            for ssx in range(2):
                                for xn in range(numc1[x2][ssx]):
                                    motormc1[x2][ssx][xn]+=zj3px[x1][i][x2]
                                for xn in range(numc2[x2][ssx]):
                                    motormc2[x2][ssx][xn]+=zj1px[x1][i][x2]
                                for xn in range(numc3[x2][ssx]):
                                    motormc3[x2][ssx][xn]+=zj2px[x1][i][x2]
                                for xn in range(numc4[x2][ssx]):
                                    motormc4[x2][ssx][xn]+=zj4px[x1][i][x2]
                                for xn in range(MTnumber+1):
                                    node1[x2][ssx][0][xn]+=zj3px[x1][i][x2]
                                    node1[x2][ssx][1][xn]+=zj1px[x1][i][x2]
                                    node1[x2][ssx][2][xn]+=zj2px[x1][i][x2]
                                    node1[x2][ssx][3][xn]+=zj4px[x1][i][x2]
                            
                            l2l[x2]+=zj1px[x1][i][x2]
                            l2r[x2]+=zj1px[x1][i][x2]
                            l3l[x2]+=zj2px[x1][i][x2]
                            l3r[x2]+=zj2px[x1][i][x2]
                            l1l[x2]+=zj3px[x1][i][x2]
                            l1r[x2]+=zj3px[x1][i][x2]
                            l4l[x2]+=zj4px[x1][i][x2]
                            l4r[x2]+=zj4px[x1][i][x2]
                            Ximt2[x2]+=zj1px[x1][i][x2]
                            Ximt3[x2]+=zj2px[x1][i][x2]
                            Xkmt1[x2]+=zj3px[x1][i][x2]
                            Xkmt4[x2]+=zj4px[x1][i][x2]
                        Xpole+=zj0px[x1][i]
                        Xpo+=zj7px[x1][i]
                        Xkin+=zj5px[x1][i]
                        Xkin1+=zj6px[x1][i]
                        for ssx in range(2):

                            for xn in range(MTnumber):
                                for ton1 in range(Nma[ssx][xn][0]):   
                                    if kinam[ssx][xn][0][ton1]==1:
                                        numa[ssx][xn][0][ton1][0]+=zj1px[x1][i][0]
                                    if kinbm[ssx][xn][0][ton1]==1:
                                        numa[ssx][xn][0][ton1][1]+=zj1px[x1][i][1]
                                for ton1 in range(Nma[ssx][xn][1]):   
                                    if kinam[ssx][xn][1][ton1]==1:
                                        numa[ssx][xn][1][ton1][0]+=zj2px[x1][i][0]
                                    if kinbm[ssx][xn][1][ton1]==1:
                                        numa[ssx][xn][1][ton1][1]+=zj2px[x1][i][1]
                                for sik in range(2):
                                    for ton1 in range(Nma1[sik][ssx][xn][0]):   
                                        if kinam1[sik][ssx][xn][0][ton1]==1:
                                            numa1[sik][ssx][xn][0][ton1][0]+=zj3px[x1][i][sik]
                                        if kinbm1[sik][ssx][xn][0][ton1]==1:
                                            numa1[sik][ssx][xn][0][ton1][1]+=zj1px[x1][i][sik]
                                    for ton1 in range(Nma1[sik][ssx][xn][1]):   
                                        if kinam1[sik][ssx][xn][1][ton1]==1:
                                            numa1[sik][ssx][xn][1][ton1][0]+=zj4px[x1][i][sik]
                                        if kinbm1[sik][ssx][xn][1][ton1]==1:
                                            numa1[sik][ssx][xn][1][ton1][1]+=zj2px[x1][i][sik]
                                
                    if na>0.1 or nb>0.1:
                        for x2 in range(pair):
                            for xn in range(nu[x2]):
                                if kina[x2][xn]==1:
                                    motor[x2][xn][0]+=js1px[x1][i][x2]
                                if kinb[x2][xn]==1:
                                    motor[x2][xn][1]+=js2px[x1][i][x2]
                            for xn in range(nu1[x2]):
                                if kinap[x2][xn]==1:
                                    motorp[x2][xn][0]+=js3px[x1][i][x2]
                                if kinbp[x2][xn]==1:
                                    motorp[x2][xn][1]+=js2px[x1][i][x2]
                            for xn in range(nu1x[x2]):
                                if kinapx[x2][xn]==1:
                                    motorpx[x2][xn][0]+=js4px[x1][i][x2]
                                if kinbpx[x2][xn]==1:
                                    motorpx[x2][xn][1]+=js1px[x1][i][x2]
                            for ssx in range(2):
                                for xn in range(numc1[x2][ssx]):
                                    motormc1[x2][ssx][xn]+=js3px[x1][i][x2]
                                for xn in range(numc2[x2][ssx]):
                                    motormc2[x2][ssx][xn]+=js1px[x1][i][x2]
                                for xn in range(numc3[x2][ssx]):
                                    motormc3[x2][ssx][xn]+=js2px[x1][i][x2]
                                for xn in range(numc4[x2][ssx]):
                                    motormc4[x2][ssx][xn]+=js4px[x1][i][x2]
                                for xn in range(MTnumber+1):
                                    node1[x2][ssx][0][xn]+=js3px[x1][i][x2]
                                    node1[x2][ssx][1][xn]+=js1px[x1][i][x2]
                                    node1[x2][ssx][2][xn]+=js2px[x1][i][x2]
                                    node1[x2][ssx][3][xn]+=js4px[x1][i][x2]
                            
                            l2l[x2]+=js1px[x1][i][x2]
                            l2r[x2]+=js1px[x1][i][x2]
                            l3l[x2]+=js2px[x1][i][x2]
                            l3r[x2]+=js2px[x1][i][x2]
                            l1l[x2]+=js3px[x1][i][x2]
                            l1r[x2]+=js3px[x1][i][x2]
                            l4l[x2]+=js4px[x1][i][x2]
                            l4r[x2]+=js4px[x1][i][x2]
                            Ximt2[x2]+=js1px[x1][i][x2]
                            Ximt3[x2]+=js2px[x1][i][x2]
                            Xkmt1[x2]+=js3px[x1][i][x2]
                            Xkmt4[x2]+=js4px[x1][i][x2]
                        Xpole+=js0px[x1][i]
                        Xpo+=js7px[x1][i]
                        Xkin+=js5px[x1][i]
                        Xkin1+=js6px[x1][i]
                        for ssx in range(2):
                            for xn in range(MTnumber):
                                for ton1 in range(Nma[ssx][xn][0]):   
                                    if kinam[ssx][xn][0][ton1]==1:
                                        numa[ssx][xn][0][ton1][0]+=js1px[x1][i][0]
                                    if kinbm[ssx][xn][0][ton1]==1:
                                        numa[ssx][xn][0][ton1][1]+=js1px[x1][i][1]
                                for ton1 in range(Nma[ssx][xn][1]):   
                                    if kinam[ssx][xn][1][ton1]==1:
                                        numa[ssx][xn][1][ton1][0]+=js2px[x1][i][0]
                                    if kinbm[ssx][xn][1][ton1]==1:
                                        numa[ssx][xn][1][ton1][1]+=js2px[x1][i][1]
                                for sik in range(2):
                                    for ton1 in range(Nma1[sik][ssx][xn][0]):   
                                        if kinam1[sik][ssx][xn][0][ton1]==1:
                                            numa1[sik][ssx][xn][0][ton1][0]+=js3px[x1][i][sik]
                                        if kinbm1[sik][ssx][xn][0][ton1]==1:
                                            numa1[sik][ssx][xn][0][ton1][1]+=js1px[x1][i][sik]
                                    for ton1 in range(Nma1[sik][ssx][xn][1]):   
                                        if kinam1[sik][ssx][xn][1][ton1]==1:
                                            numa1[sik][ssx][xn][1][ton1][0]+=js4px[x1][i][sik]
                                        if kinbm1[sik][ssx][xn][1][ton1]==1:
                                            numa1[sik][ssx][xn][1][ton1][1]+=js2px[x1][i][sik]
                                
                    ypsl0=energy0()
                    ypsl0p=ypsl0
                    ypsl0px=ypsl0
                    ckF,de0,de1,de2,de3,de4,de5,de6,de7=checkF()
                    if ckF==1:
                        #print(kk)
                        for x2 in range(pair):
                            for xn in range(nu[x2]):
                                if kina[x2][xn]==1:
                                    motor[x2][xn][0]+=de1[x2]
                                if kinb[x2][xn]==1:
                                    motor[x2][xn][1]+=de2[x2]
                            for xn in range(nu1[x2]):
                                if kinap[x2][xn]==1:
                                    motorp[x2][xn][0]+=de3[x2]
                                if kinbp[x2][xn]==1:
                                    motorp[x2][xn][1]+=de2[x2]
                            for xn in range(nu1x[x2]):
                                if kinapx[x2][xn]==1:
                                    motorpx[x2][xn][0]+=de4[x2]
                                if kinbpx[x2][xn]==1:
                                    motorpx[x2][xn][1]+=de1[x2]


                            for ssx in range(2):
                                for xn in range(numc1[x2][ssx]):
                                    motormc1[x2][ssx][xn]+=de3[x2]
                                for xn in range(numc2[x2][ssx]):
                                    motormc2[x2][ssx][xn]+=de1[x2]
                                for xn in range(numc3[x2][ssx]):
                                    motormc3[x2][ssx][xn]+=de2[x2]
                                for xn in range(numc4[x2][ssx]):
                                    motormc4[x2][ssx][xn]+=de4[x2]
                                for xn in range(MTnumber+1):
                                    node1[x2][ssx][0][xn]+=de3[x2]
                                    node1[x2][ssx][1][xn]+=de1[x2]
                                    node1[x2][ssx][2][xn]+=de2[x2]
                                    node1[x2][ssx][3][xn]+=de4[x2]
                            
                            l2l[x2]+=de1[x2]
                            l2r[x2]+=de1[x2]
                            l3l[x2]+=de2[x2]
                            l3r[x2]+=de2[x2]
                            l1l[x2]+=de3[x2]
                            l1r[x2]+=de3[x2]
                            l4l[x2]+=de4[x2]
                            l4r[x2]+=de4[x2]
                            Ximt2[x2]+=de1[x2]
                            Ximt3[x2]+=de2[x2]
                            Xkmt1[x2]+=de3[x2]
                            Xkmt4[x2]+=de4[x2]
                        for ssx in range(2):
                            for xn in range(MTnumber):
                                for ton1 in range(Nma[ssx][xn][0]):   
                                    if kinam[ssx][xn][0][ton1]==1:
                                        numa[ssx][xn][0][ton1][0]+=de1[0]
                                    if kinbm[ssx][xn][0][ton1]==1:
                                        numa[ssx][xn][0][ton1][1]+=de1[1]
                                for ton1 in range(Nma[ssx][xn][1]):   
                                    if kinam[ssx][xn][1][ton1]==1:
                                        numa[ssx][xn][1][ton1][0]+=de2[0]
                                    if kinbm[ssx][xn][1][ton1]==1:
                                        numa[ssx][xn][1][ton1][1]+=de2[1]
                                for sik in range(2):
                                    for ton1 in range(Nma1[sik][ssx][xn][0]):   
                                        if kinam1[sik][ssx][xn][0][ton1]==1:
                                            numa1[sik][ssx][xn][0][ton1][0]+=de3[sik]
                                        if kinbm1[sik][ssx][xn][0][ton1]==1:
                                            numa1[sik][ssx][xn][0][ton1][1]+=de1[sik]
                                    for ton1 in range(Nma1[sik][ssx][xn][1]):   
                                        if kinam1[sik][ssx][xn][1][ton1]==1:
                                            numa1[sik][ssx][xn][1][ton1][0]+=de4[sik]
                                        if kinbm1[sik][ssx][xn][1][ton1]==1:
                                            numa1[sik][ssx][xn][1][ton1][1]+=de2[sik]
                        Xpole+=de0
                        Xpo+=de7
                        Xkin+=de5
                        Xkin1+=de6
                        ypsl0=energy0()
                        ypsl0p=ypsl0
                        ypsl0px=ypsl0
                if pan1==1:
                    if abs(na)+abs(nb)==0:
                        panpx[x1][i]=0  

    if pan1==1:
        for x1 in range(pair):
            if sum(pan[x1])+sum(panp[x1])+sum(panpx[x1])!=0:
                pan1=1
                break
            pan1=0
###############################################################Eg5 detach  

    for x1 in range(pair):
        tuogeng=0
        for xbb in range(nu[x1]):
            xpa=0
            if kina[x1][xbb]==0 and kinb[x1][xbb]==1:
                xpa=1
                kinb[x1][xbb]=dissociation(0,0,0,0)
                if motor[x1][xbb][1]>=l2l[x1] and motor[x1][xbb][1]<=l2r[x1]:
                    kina[x1][xbb]=rebind()
                if kinb[x1][xbb]==1 and kina[x1][xbb]==1:
                    lian1=0
                    for xn in range(nu[x1]):
                        if kina[x1][xn]==1 and xn!=xbb and abs(l2r[x1]-round((l2r[x1]-motor[x1][xbb][1])/d)*d-motor[x1][xn][0])<1:
                            lian1=1
                            break
                    if lian1==1:
                        if l2r[x1]+round((motor[x1][xbb][1]-l2r[x1])/d)*d>=motor[x1][xbb][1]:
                            la=(round((motor[x1][xbb][1]-l2r[x1])/d)-1)*d
                        if l2r[x1]+round((motor[x1][xbb][1]-l2r[x1])/d)*d<motor[x1][xbb][1]:
                            la=(round((motor[x1][xbb][1]-l2r[x1])/d)+1)*d
                        for xn in range(nu[x1]):
                            if kina[x1][xn]==1 and xn!=xbb and abs(l2r[x1]+la-motor[x1][xn][0])<1:
                                lian1=2
                                break
                    if lian1==0:
                        motor[x1][xbb][0]=l2r[x1]+round((motor[x1][xbb][1]-l2r[x1])/d)*d
                    if lian1==1:
                        motor[x1][xbb][0]=l2r[x1]+la
                    if lian1==2:
                        kina[x1][xbb]=0
                    pan1=1
                    monum[x1]+=1
            if xpa==0 and kina[x1][xbb]==1 and kinb[x1][xbb]==0:
                xpa=1
                kina[x1][xbb]=dissociation(0,0,0,0)
                if motor[x1][xbb][0]>=l3l[x1] and motor[x1][xbb][0]<=l3r[x1]:
                    kinb[x1][xbb]=rebind()
                if kinb[x1][xbb]==1 and kina[x1][xbb]==1:
                    lian1=0
                    for xn in range(nu[x1]):
                        if kinb[x1][xn]==1 and xn!=xbb and abs(l3l[x1]+round((motor[x1][xbb][0]-l3l[x1])/d)*d-motor[x1][xn][1])<1:
                            lian1=1
                            break
                    if lian1==1:
                        if l3l[x1]+round((motor[x1][xbb][0]-l3l[x1])/d)*d>=motor[x1][xbb][0]:
                            la=(round((motor[x1][xbb][0]-l3l[x1])/d)-1)*d
                        if l3l[x1]+round((motor[x1][xbb][0]-l3l[x1])/d)*d<motor[x1][xbb][0]:
                            la=(round((motor[x1][xbb][0]-l3l[x1])/d)+1)*d
                        for xn in range(nu[x1]):
                            if kinb[x1][xn]==1 and xn!=xbb and abs(l3l[x1]+la-motor[x1][xn][1])<1:
                                lian1=2
                                break
                    if lian1==0:
                        motor[x1][xbb][1]=l3l[x1]+round((motor[x1][xbb][0]-l3l[x1])/d)*d
                    if lian1==1:
                        motor[x1][xbb][1]=l3l[x1]+la
                    if lian1==2:
                        kinb[x1][xbb]=0
                    pan1=1
                    monum[x1]+=1
            if xpa==0 and kina[x1][xbb]==1 and kinb[x1][xbb]==1:
                F=0
                if motor[x1][xbb][0]-motor[x1][xbb][1]>xdmotor:
                    F=Km*(motor[x1][xbb][0]-motor[x1][xbb][1]-xdmotor)
                if motor[x1][xbb][0]-motor[x1][xbb][1]<-xdmotor:
                    F=Km*(motor[x1][xbb][0]-motor[x1][xbb][1]+xdmotor)
                kina[x1][xbb]=dissociation(F,ypsl0px,ypsl1[x1][xbb],ypsl2[x1][xbb])
                kinb[x1][xbb]=dissociation(F,ypsl0px,ypsl1[x1][xbb],ypsl2[x1][xbb])
                if motor[x1][xbb][0]>l2r[x1] or motor[x1][xbb][0]<l2l[x1]:
                    kina[x1][xbb]=0
                if motor[x1][xbb][1]<l3l[x1] or motor[x1][xbb][1]>l3r[x1]:
                    kinb[x1][xbb]=0
                if kina[x1][xbb]==0 or kinb[x1][xbb]==0:
                    monum[x1]-=1
                    pan1=1
                    ckF,de0,de1,de2,de3,de4,de5,de6,de7=checkF()
                    if ckF==1:
                        for x2 in range(pair):
                            for xn in range(nu[x2]):
                                if kina[x2][xn]==1:
                                    motor[x2][xn][0]+=de1[x2]
                                if kinb[x2][xn]==1:
                                    motor[x2][xn][1]+=de2[x2]
                            for xn in range(nu1[x2]):
                                if kinap[x2][xn]==1:
                                    motorp[x2][xn][0]+=de3[x2]
                                if kinbp[x2][xn]==1:
                                    motorp[x2][xn][1]+=de2[x2]
                            for xn in range(nu1x[x2]):
                                if kinapx[x2][xn]==1:
                                    motorpx[x2][xn][0]+=de4[x2]
                                if kinbpx[x2][xn]==1:
                                    motorpx[x2][xn][1]+=de1[x2]
                            for ssx in range(2):
                                for xn in range(numc1[x2][ssx]):
                                    motormc1[x2][ssx][xn]+=de3[x2]
                                for xn in range(numc2[x2][ssx]):
                                    motormc2[x2][ssx][xn]+=de1[x2]
                                for xn in range(numc3[x2][ssx]):
                                    motormc3[x2][ssx][xn]+=de2[x2]
                                for xn in range(numc4[x2][ssx]):
                                    motormc4[x2][ssx][xn]+=de4[x2]
                                for xn in range(MTnumber+1):
                                    node1[x2][ssx][0][xn]+=de3[x2]
                                    node1[x2][ssx][1][xn]+=de1[x2]
                                    node1[x2][ssx][2][xn]+=de2[x2]
                                    node1[x2][ssx][3][xn]+=de4[x2]
                            
                            
                            l2l[x2]+=de1[x2]
                            l2r[x2]+=de1[x2]
                            l3l[x2]+=de2[x2]
                            l3r[x2]+=de2[x2]
                            l1l[x2]+=de3[x2]
                            l1r[x2]+=de3[x2]
                            l4l[x2]+=de4[x2]
                            l4r[x2]+=de4[x2]
                            Ximt2[x2]+=de1[x2]
                            Ximt3[x2]+=de2[x2]
                            Xkmt1[x2]+=de3[x2]
                            Xkmt4[x2]+=de4[x2]
                        Xpole+=de0
                        Xpo+=de7
                        Xkin+=de5
                        Xkin1+=de6
                        for ssx in range(2):
                            for xn in range(MTnumber):
                                for ton1 in range(Nma[ssx][xn][0]):   
                                    if kinam[ssx][xn][0][ton1]==1:
                                        numa[ssx][xn][0][ton1][0]+=de1[0]
                                    if kinbm[ssx][xn][0][ton1]==1:
                                        numa[ssx][xn][0][ton1][1]+=de1[1]
                                for ton1 in range(Nma[ssx][xn][1]):   
                                    if kinam[ssx][xn][1][ton1]==1:
                                        numa[ssx][xn][1][ton1][0]+=de2[0]
                                    if kinbm[ssx][xn][1][ton1]==1:
                                        numa[ssx][xn][1][ton1][1]+=de2[1]
                                for sik in range(2):
                                    for ton1 in range(Nma1[sik][ssx][xn][0]):   
                                        if kinam1[sik][ssx][xn][0][ton1]==1:
                                            numa1[sik][ssx][xn][0][ton1][0]+=de3[sik]
                                        if kinbm1[sik][ssx][xn][0][ton1]==1:
                                            numa1[sik][ssx][xn][0][ton1][1]+=de1[sik]
                                    for ton1 in range(Nma1[sik][ssx][xn][1]):   
                                        if kinam1[sik][ssx][xn][1][ton1]==1:
                                            numa1[sik][ssx][xn][1][ton1][0]+=de4[sik]
                                        if kinbm1[sik][ssx][xn][1][ton1]==1:
                                            numa1[sik][ssx][xn][1][ton1][1]+=de2[sik]
                        ypsl0=energy0()
                        ypsl0p=ypsl0
                        ypsl0px=ypsl0
                   
            if kina[x1][xbb]==0 and kinb[x1][xbb]==0:
                tuogeng=1
########################################################删去没用的
        if tuogeng==1:
            for xn in range(nu[x1]):
                if kina[x1][xn]==0 and kinb[x1][xn]==0:
                    tuogeng=0
                    del motor[x1][xn]
                    del kina[x1][xn]
                    del kinb[x1][xn]
                    del dxc[x1][xn]
                    del ypsl1[x1][xn]
                    del ypsl2[x1][xn]
                    del zj7[x1][xn]
                    del js7[x1][xn]
                    del zj6[x1][xn]
                    del js6[x1][xn]
                    del zj5[x1][xn]
                    del js5[x1][xn]
                    del zj4[x1][xn]
                    del js4[x1][xn]
                    del zj3[x1][xn]
                    del js3[x1][xn]
                    del zj2[x1][xn]
                    del js2[x1][xn]
                    del zj1[x1][xn]
                    del js1[x1][xn]
                    del zj0[x1][xn]
                    del js0[x1][xn]
                    del pan[x1][xn]
                    nu[x1]-=1
                    break 
##################################################################Eg5 dissociation
        tuogeng=0
        nu[x1]=len(kina[x1])
        for xbb in range(nu1[x1]):
            xpa=0
            if kinap[x1][xbb]==0 and kinbp[x1][xbb]==1:
                xpa=1
                kinbp[x1][xbb]=dissociation(0,0,0,0)
                if motorp[x1][xbb][1]>=l3l[x1] and motorp[x1][xbb][1]<=l1r[x1]:
                    kinap[x1][xbb]=rebind()
                if kinbp[x1][xbb]==1 and kinap[x1][xbb]==1:
                    lian1=0
                    for xn in range(nu1[x1]):
                        if kinap[x1][xn]==1 and xn!=xbb and abs(l1l[x1]-round((l1l[x1]-motorp[x1][xbb][1])/d)*d-motorp[x1][xn][0])<1:
                            lian1=1
                            break
                    if lian1==1:
                        if l1l[x1]+round((motorp[x1][xbb][1]-l1l[x1])/d)*d>=motorp[x1][xbb][1]:
                            la=(round((motorp[x1][xbb][1]-l1l[x1])/d)-1)*d
                        if l1l[x1]+round((motorp[x1][xbb][1]-l1l[x1])/d)*d<motorp[x1][xbb][1]:
                            la=(round((motorp[x1][xbb][1]-l1l[x1])/d)+1)*d
                        for xn in range(nu1[x1]):
                            if kinap[x1][xn]==1 and xn!=xbb and abs(l1l[x1]+la-motorp[x1][xn][0])<1:
                                lian1=2
                                break
                    if lian1==0:
                        motorp[x1][xbb][0]=l1l[x1]+round((motorp[x1][xbb][1]-l1l[x1])/d)*d
                    if lian1==1:
                        motorp[x1][xbb][0]=l1l[x1]+la
                    if lian1==2:
                        kinap[x1][xbb]=0
                    pan1=1
                    monump[x1]+=1
            if xpa==0 and kinap[x1][xbb]==1 and kinbp[x1][xbb]==0:
                xpa=1
                kinap[x1][xbb]=dissociation(0,0,0,0)
                if motorp[x1][xbb][0]>=l3l[x1] and motorp[x1][xbb][0]<=l1r[x1]:
                    kinbp[x1][xbb]=rebind()
                if kinbp[x1][xbb]==1 and kinap[x1][xbb]==1:
                    lian1=0
                    for xn in range(nu1[x1]):
                        if kinbp[x1][xn]==1 and xn!=xbb and abs(l3l[x1]+round((motorp[x1][xbb][0]-l3l[x1])/d)*d-motorp[x1][xn][1])<1:
                            lian1=1
                            break
                    if lian1==1:
                        if l3l[x1]+round((motorp[x1][xbb][0]-l3l[x1])/d)*d>=motorp[x1][xbb][0]:
                            la=(round((motorp[x1][xbb][0]-l3l[x1])/d)-1)*d
                        if l3l[x1]+round((motorp[x1][xbb][0]-l3l[x1])/d)*d<motorp[x1][xbb][0]:
                            la=(round((motorp[x1][xbb][0]-l3l[x1])/d)+1)*d
                        for xn in range(nu1[x1]):
                            if kinbp[x1][xn]==1 and xn!=xbb and abs(l3l[x1]+la-motorp[x1][xn][1])<1:
                                lian1=2
                                break
                    if lian1==0:
                        motorp[x1][xbb][1]=l3l[x1]+round((motorp[x1][xbb][0]-l3l[x1])/d)*d
                    if lian1==1:
                        motorp[x1][xbb][1]=l3l[x1]+la
                    if lian1==2:
                        kinbp[x1][xbb]=0
                    pan1=1
                    monump[x1]+=1
            if xpa==0 and kinap[x1][xbb]==1 and kinbp[x1][xbb]==1:
                F=0
                if motorp[x1][xbb][0]-motorp[x1][xbb][1]>xdmotor:
                    F=Km*(motorp[x1][xbb][0]-motorp[x1][xbb][1]-xdmotor)
                if motorp[x1][xbb][0]-motorp[x1][xbb][1]<-xdmotor:
                    F=Km*(motorp[x1][xbb][0]-motorp[x1][xbb][1]+xdmotor)
                kinap[x1][xbb]=dissociation(F,ypsl0px,ypsl1p[x1][xbb],ypsl2p[x1][xbb])
                kinbp[x1][xbb]=dissociation(F,ypsl0px,ypsl1p[x1][xbb],ypsl2p[x1][xbb])
                if motorp[x1][xbb][0]>l1r[x1] or motorp[x1][xbb][0]<l1l[x1]:
                    kinap[x1][xbb]=0
                if motorp[x1][xbb][1]<l3l[x1] or motorp[x1][xbb][1]>l3r[x1]:
                    kinbp[x1][xbb]=0
                if kinap[x1][xbb]==0 or kinbp[x1][xbb]==0:
                    monump[x1]-=1
                    pan1=1
                    ckF,de0,de1,de2,de3,de4,de5,de6,de7=checkF()
                    if ckF==1:
                        for x2 in range(pair):
                            for xn in range(nu[x2]):
                                if kina[x2][xn]==1:
                                    motor[x2][xn][0]+=de1[x2]
                                if kinb[x2][xn]==1:
                                    motor[x2][xn][1]+=de2[x2]
                            for xn in range(nu1[x2]):
                                if kinap[x2][xn]==1:
                                    motorp[x2][xn][0]+=de3[x2]
                                if kinbp[x2][xn]==1:
                                    motorp[x2][xn][1]+=de2[x2]
                            for xn in range(nu1x[x2]):
                                if kinapx[x2][xn]==1:
                                    motorpx[x2][xn][0]+=de4[x2]
                                if kinbpx[x2][xn]==1:
                                    motorpx[x2][xn][1]+=de1[x2]
                            for ssx in range(2):
                                for xn in range(numc1[x2][ssx]):
                                    motormc1[x2][ssx][xn]+=de3[x2]
                                for xn in range(numc2[x2][ssx]):
                                    motormc2[x2][ssx][xn]+=de1[x2]
                                for xn in range(numc3[x2][ssx]):
                                    motormc3[x2][ssx][xn]+=de2[x2]
                                for xn in range(numc4[x2][ssx]):
                                    motormc4[x2][ssx][xn]+=de4[x2]
                                for xn in range(MTnumber+1):
                                    node1[x2][ssx][0][xn]+=de3[x2]
                                    node1[x2][ssx][1][xn]+=de1[x2]
                                    node1[x2][ssx][2][xn]+=de2[x2]
                                    node1[x2][ssx][3][xn]+=de4[x2]
                            
                            
                            l2l[x2]+=de1[x2]
                            l2r[x2]+=de1[x2]
                            l3l[x2]+=de2[x2]
                            l3r[x2]+=de2[x2]
                            l1l[x2]+=de3[x2]
                            l1r[x2]+=de3[x2]
                            l4l[x2]+=de4[x2]
                            l4r[x2]+=de4[x2]
                            Ximt2[x2]+=de1[x2]
                            Ximt3[x2]+=de2[x2]
                            Xkmt1[x2]+=de3[x2]
                            Xkmt4[x2]+=de4[x2]
                        Xpole+=de0
                        Xpo+=de7
                        Xkin+=de5
                        Xkin1+=de6
                        for ssx in range(2):
                            for xn in range(MTnumber):
                                for ton1 in range(Nma[ssx][xn][0]):   
                                    if kinam[ssx][xn][0][ton1]==1:
                                        numa[ssx][xn][0][ton1][0]+=de1[0]
                                    if kinbm[ssx][xn][0][ton1]==1:
                                        numa[ssx][xn][0][ton1][1]+=de1[1]
                                for ton1 in range(Nma[ssx][xn][1]):   
                                    if kinam[ssx][xn][1][ton1]==1:
                                        numa[ssx][xn][1][ton1][0]+=de2[0]
                                    if kinbm[ssx][xn][1][ton1]==1:
                                        numa[ssx][xn][1][ton1][1]+=de2[1]
                                for sik in range(2):
                                    for ton1 in range(Nma1[sik][ssx][xn][0]):   
                                        if kinam1[sik][ssx][xn][0][ton1]==1:
                                            numa1[sik][ssx][xn][0][ton1][0]+=de3[sik]
                                        if kinbm1[sik][ssx][xn][0][ton1]==1:
                                            numa1[sik][ssx][xn][0][ton1][1]+=de1[sik]
                                    for ton1 in range(Nma1[sik][ssx][xn][1]):   
                                        if kinam1[sik][ssx][xn][1][ton1]==1:
                                            numa1[sik][ssx][xn][1][ton1][0]+=de4[sik]
                                        if kinbm1[sik][ssx][xn][1][ton1]==1:
                                            numa1[sik][ssx][xn][1][ton1][1]+=de2[sik]
                        ypsl0=energy0()
                        ypsl0p=ypsl0
                        ypsl0px=ypsl0
                    
            if kinap[x1][xbb]==0 and kinbp[x1][xbb]==0:
                tuogeng=1
        if tuogeng==1:
            for xn in range(nu1[x1]):
                if kinap[x1][xn]==0 and kinbp[x1][xn]==0:
                    tuogeng=0
                    del motorp[x1][xn]
                    del kinap[x1][xn]
                    del kinbp[x1][xn]
                    del dxcp[x1][xn]
                    del ypsl1p[x1][xn]
                    del ypsl2p[x1][xn]
                    del zj7p[x1][xn]
                    del js7p[x1][xn]
                    del zj6p[x1][xn]
                    del js6p[x1][xn]
                    del zj5p[x1][xn]
                    del js5p[x1][xn]
                    del zj4p[x1][xn]
                    del js4p[x1][xn]
                    del zj3p[x1][xn]
                    del js3p[x1][xn]
                    del zj2p[x1][xn]
                    del js2p[x1][xn]
                    del zj1p[x1][xn]
                    del js1p[x1][xn]
                    del zj0p[x1][xn]
                    del js0p[x1][xn]
                    del panp[x1][xn]
                    nu1[x1]-=1
                    break
        tuogeng=0
        for xbb in range(nu1x[x1]):
            xpa=0
            if kinapx[x1][xbb]==0 and kinbpx[x1][xbb]==1:
                xpa=1
                kinbpx[x1][xbb]=dissociation(0,0,0,0)
                if motorpx[x1][xbb][1]>=l4l[x1] and motorpx[x1][xbb][1]<=l2r[x1]:
                    kinapx[x1][xbb]=rebind()

                if kinbpx[x1][xbb]==1 and kinapx[x1][xbb]==1:
                    lian1=0
                    #print('111')
                    for xn in range(nu1x[x1]):
                        if kinapx[x1][xn]==1 and xn!=xbb and abs(l4l[x1]-round((l4l[x1]-motorpx[x1][xbb][1])/d)*d-motorpx[x1][xn][0])<1:
                            lian1=1
                            break
                    if lian1==1:
                        if l4l[x1]+round((motorpx[x1][xbb][1]-l4l[x1])/d)*d>=motorpx[x1][xbb][1]:
                            la=(round((motorpx[x1][xbb][1]-l4l[x1])/d)-1)*d
                        if l4l[x1]+round((motorpx[x1][xbb][1]-l4l[x1])/d)*d<motorpx[x1][xbb][1]:
                            la=(round((motorpx[x1][xbb][1]-l4l[x1])/d)+1)*d
                        for xn in range(nu1x[x1]):
                            if kinapx[x1][xn]==1 and xn!=xbb and abs(l4l[x1]+la-motorpx[x1][xn][0])<1:
                                lian1=2
                                break
                    if lian1==0:
                        motorpx[x1][xbb][0]=l4l[x1]+round((motorpx[x1][xbb][1]-l4l[x1])/d)*d
                    if lian1==1:
                        motorpx[x1][xbb][0]=l4l[x1]+la
                    if lian1==2:
                        kinapx[x1][xbb]=0
                        #print('222')
                    pan1=1
                    monumpx[x1]+=1
            if xpa==0 and kinapx[x1][xbb]==1 and kinbpx[x1][xbb]==0:
                xpa=1
                kinapx[x1][xbb]=dissociation(0,0,0,0)
                if motorpx[x1][xbb][0]>=l4l[x1] and motorpx[x1][xbb][0]<=l2r[x1]:
                    kinbpx[x1][xbb]=rebind()
                if kinbpx[x1][xbb]==1 and kinapx[x1][xbb]==1:
                    lian1=0
                    for xn in range(nu1x[x1]):
                        if kinbpx[x1][xn]==1 and xn!=xbb and abs(l2l[x1]+round((motorpx[x1][xbb][0]-l2l[x1])/d)*d-motorpx[x1][xn][1])<1:
                            lian1=1
                            break
                    if lian1==1:
                        if l2l[x1]+round((motorpx[x1][xbb][0]-l2l[x1])/d)*d>=motorpx[x1][xbb][0]:
                            la=(round((motorpx[x1][xbb][0]-l2l[x1])/d)-1)*d
                        if l2l[x1]+round((motorpx[x1][xbb][0]-l2l[x1])/d)*d<motorpx[x1][xbb][0]:
                            la=(round((motorpx[x1][xbb][0]-l2l[x1])/d)+1)*d
                        for xn in range(nu1x[x1]):
                            if kinbpx[x1][xn]==1 and xn!=xbb and abs(l2l[x1]+la-motorpx[x1][xn][1])<1:
                                lian1=2
                                break
                    if lian1==0:
                        motorpx[x1][xbb][1]=l2l[x1]+round((motorpx[x1][xbb][0]-l2l[x1])/d)*d
                    if lian1==1:
                        motorpx[x1][xbb][1]=l2l[x1]+la
                    if lian1==2:
                        kinbpx[x1][xbb]=0
                    pan1=1
                    monumpx[x1]+=1
            if xpa==0 and kinapx[x1][xbb]==1 and kinbpx[x1][xbb]==1:
                F=0
                if motorpx[x1][xbb][0]-motorpx[x1][xbb][1]>xdmotor:
                    F=-Km*(motorpx[x1][xbb][0]-motorpx[x1][xbb][1]-xdmotor)
                if motorpx[x1][xbb][0]-motorpx[x1][xbb][1]<-xdmotor:
                    F=-Km*(motorpx[x1][xbb][0]-motorpx[x1][xbb][1]+xdmotor)
                kinapx[x1][xbb]=dissociation(F,ypsl0px,ypsl2px[x1][xbb],ypsl1px[x1][xbb])
                kinbpx[x1][xbb]=dissociation(F,ypsl0px,ypsl2px[x1][xbb],ypsl1px[x1][xbb])
                if motorpx[x1][xbb][0]>l4r[x1] or motorpx[x1][xbb][0]<l4l[x1]:
                    kinapx[x1][xbb]=0
                if motorpx[x1][xbb][1]<l2l[x1] or motorpx[x1][xbb][1]>l2r[x1]:
                    kinbpx[x1][xbb]=0
                if kinapx[x1][xbb]==0 or kinbpx[x1][xbb]==0:
                    monumpx[x1]-=1
                    pan1=1
                    ckF,de0,de1,de2,de3,de4,de5,de6,de7=checkF()
                    if ckF==1:
                        for x2 in range(pair):
                            for xn in range(nu[x2]):
                                if kina[x2][xn]==1:
                                    motor[x2][xn][0]+=de1[x2]
                                if kinb[x2][xn]==1:
                                    motor[x2][xn][1]+=de2[x2]
                            for xn in range(nu1[x2]):
                                if kinap[x2][xn]==1:
                                    motorp[x2][xn][0]+=de3[x2]
                                if kinbp[x2][xn]==1:
                                    motorp[x2][xn][1]+=de2[x2]
                            for xn in range(nu1x[x2]):
                                if kinapx[x2][xn]==1:
                                    motorpx[x2][xn][0]+=de4[x2]
                                if kinbpx[x2][xn]==1:
                                    motorpx[x2][xn][1]+=de1[x2]
                            for ssx in range(2):
                                for xn in range(numc1[x2][ssx]):
                                    motormc1[x2][ssx][xn]+=de3[x2]
                                for xn in range(numc2[x2][ssx]):
                                    motormc2[x2][ssx][xn]+=de1[x2]
                                for xn in range(numc3[x2][ssx]):
                                    motormc3[x2][ssx][xn]+=de2[x2]
                                for xn in range(numc4[x2][ssx]):
                                    motormc4[x2][ssx][xn]+=de4[x2]
                                for xn in range(MTnumber+1):
                                    node1[x2][ssx][0][xn]+=de3[x2]
                                    node1[x2][ssx][1][xn]+=de1[x2]
                                    node1[x2][ssx][2][xn]+=de2[x2]
                                    node1[x2][ssx][3][xn]+=de4[x2]
                            
                            
                            l2l[x2]+=de1[x2]
                            l2r[x2]+=de1[x2]
                            l3l[x2]+=de2[x2]
                            l3r[x2]+=de2[x2]
                            l1l[x2]+=de3[x2]
                            l1r[x2]+=de3[x2]
                            l4l[x2]+=de4[x2]
                            l4r[x2]+=de4[x2]
                            Ximt2[x2]+=de1[x2]
                            Ximt3[x2]+=de2[x2]
                            Xkmt1[x2]+=de3[x2]
                            Xkmt4[x2]+=de4[x2]
                        Xpole+=de0
                        Xpo+=de7
                        Xkin+=de5
                        Xkin1+=de6
                        for ssx in range(2):
                            for xn in range(MTnumber):
                                for ton1 in range(Nma[ssx][xn][0]):   
                                    if kinam[ssx][xn][0][ton1]==1:
                                        numa[ssx][xn][0][ton1][0]+=de1[0]
                                    if kinbm[ssx][xn][0][ton1]==1:
                                        numa[ssx][xn][0][ton1][1]+=de1[1]
                                for ton1 in range(Nma[ssx][xn][1]):   
                                    if kinam[ssx][xn][1][ton1]==1:
                                        numa[ssx][xn][1][ton1][0]+=de2[0]
                                    if kinbm[ssx][xn][1][ton1]==1:
                                        numa[ssx][xn][1][ton1][1]+=de2[1]

                                for sik in range(2):
                                    for ton1 in range(Nma1[sik][ssx][xn][0]):   
                                        if kinam1[sik][ssx][xn][0][ton1]==1:
                                            numa1[sik][ssx][xn][0][ton1][0]+=de3[sik]
                                        if kinbm1[sik][ssx][xn][0][ton1]==1:
                                            numa1[sik][ssx][xn][0][ton1][1]+=de1[sik]
                                    for ton1 in range(Nma1[sik][ssx][xn][1]):   
                                        if kinam1[sik][ssx][xn][1][ton1]==1:
                                            numa1[sik][ssx][xn][1][ton1][0]+=de4[sik]
                                        if kinbm1[sik][ssx][xn][1][ton1]==1:
                                            numa1[sik][ssx][xn][1][ton1][1]+=de2[sik]
                        ypsl0=energy0()
                        ypsl0p=ypsl0
                        ypsl0px=ypsl0
                        ckF,de0,de1,de2,de3,de4,de5,de6,de7=checkF()
                        if ckF==1:
                            for x2 in range(pair):
                                for xn in range(nu[x2]):
                                    if kina[x2][xn]==1:
                                        motor[x2][xn][0]+=de1[x2]
                                    if kinb[x2][xn]==1:
                                        motor[x2][xn][1]+=de2[x2]
                                for xn in range(nu1[x2]):
                                    if kinap[x2][xn]==1:
                                        motorp[x2][xn][0]+=de3[x2]
                                    if kinbp[x2][xn]==1:
                                        motorp[x2][xn][1]+=de2[x2]
                                for xn in range(nu1x[x2]):
                                    if kinapx[x2][xn]==1:
                                        motorpx[x2][xn][0]+=de4[x2]
                                    if kinbpx[x2][xn]==1:
                                        motorpx[x2][xn][1]+=de1[x2]
                                for ssx in range(2):
                                    for xn in range(numc1[x2][ssx]):
                                        motormc1[x2][ssx][xn]+=de3[x2]
                                    for xn in range(numc2[x2][ssx]):
                                        motormc2[x2][ssx][xn]+=de1[x2]
                                    for xn in range(numc3[x2][ssx]):
                                        motormc3[x2][ssx][xn]+=de2[x2]
                                    for xn in range(numc4[x2][ssx]):
                                        motormc4[x2][ssx][xn]+=de4[x2]
                                    for xn in range(MTnumber+1):
                                        node1[x2][ssx][0][xn]+=de3[x2]
                                        node1[x2][ssx][1][xn]+=de1[x2]
                                        node1[x2][ssx][2][xn]+=de2[x2]
                                        node1[x2][ssx][3][xn]+=de4[x2]
                                

                                l2l[x2]+=de1[x2]
                                l2r[x2]+=de1[x2]
                                l3l[x2]+=de2[x2]
                                l3r[x2]+=de2[x2]
                                l1l[x2]+=de3[x2]
                                l1r[x2]+=de3[x2]
                                l4l[x2]+=de4[x2]
                                l4r[x2]+=de4[x2]
                                Ximt2[x2]+=de1[x2]
                                Ximt3[x2]+=de2[x2]
                                Xkmt1[x2]+=de3[x2]
                                Xkmt4[x2]+=de4[x2]
                            Xpole+=de0
                            Xpo+=de7
                            Xkin+=de5
                            Xkin1+=de6
                            for ssx in range(2):
                                for xn in range(MTnumber):
                                    for ton1 in range(Nma[ssx][xn][0]):   
                                        if kinam[ssx][xn][0][ton1]==1:
                                            numa[ssx][xn][0][ton1][0]+=de1[0]
                                        if kinbm[ssx][xn][0][ton1]==1:
                                            numa[ssx][xn][0][ton1][1]+=de1[1]
                                    for ton1 in range(Nma[ssx][xn][1]):   
                                        if kinam[ssx][xn][1][ton1]==1:
                                            numa[ssx][xn][1][ton1][0]+=de2[0]
                                        if kinbm[ssx][xn][1][ton1]==1:
                                            numa[ssx][xn][1][ton1][1]+=de2[1]
                                    for sik in range(2):
                                        for ton1 in range(Nma1[sik][ssx][xn][0]):   
                                            if kinam1[sik][ssx][xn][0][ton1]==1:
                                                numa1[sik][ssx][xn][0][ton1][0]+=de3[sik]
                                            if kinbm1[sik][ssx][xn][0][ton1]==1:
                                                numa1[sik][ssx][xn][0][ton1][1]+=de1[sik]
                                        for ton1 in range(Nma1[sik][ssx][xn][1]):   
                                            if kinam1[sik][ssx][xn][1][ton1]==1:
                                                numa1[sik][ssx][xn][1][ton1][0]+=de4[sik]
                                            if kinbm1[sik][ssx][xn][1][ton1]==1:
                                                numa1[sik][ssx][xn][1][ton1][1]+=de2[sik]
                            ypsl0=energy0()
                            ypsl0p=ypsl0
                            ypsl0px=ypsl0
            if kinapx[x1][xbb]==0 and kinbpx[x1][xbb]==0:
                tuogeng=1
        if tuogeng==1:
            for xn in range(nu1x[x1]):
                if kinapx[x1][xn]==0 and kinbpx[x1][xn]==0:
                    tuogeng=0
                    del motorpx[x1][xn]
                    del kinapx[x1][xn]
                    del kinbpx[x1][xn]
                    del dxcpx[x1][xn]
                    del ypsl1px[x1][xn]
                    del ypsl2px[x1][xn]
                    del zj7px[x1][xn]
                    del js7px[x1][xn]
                    del zj6px[x1][xn]
                    del js6px[x1][xn]
                    del zj5px[x1][xn]
                    del js5px[x1][xn]
                    del zj4px[x1][xn]
                    del js4px[x1][xn]
                    del zj3px[x1][xn]
                    del js3px[x1][xn]
                    del zj2px[x1][xn]
                    del js2px[x1][xn]
                    del zj1px[x1][xn]
                    del js1px[x1][xn]
                    del zj0px[x1][xn]
                    del js0px[x1][xn]
                    del panpx[x1][xn]
                    nu1x[x1]=len(kinapx[x1])
                    break

    if  Xpole>0:
        break
    if a%1000==0:
        ads+=1
        len1=[[] for x1 in range(pair)]
        for x1 in range(pair):
            for xx in range(2):
                for xn in range(MTnumber-1):
                    len1[x1].append(round(node1[x1][0][xx][xn+1]-node1[x1][0][xx][xn],2))
                    len1[x1].append(round(node1[x1][1][xx][xn+1]-node1[x1][1][xx][xn],2))
            for xx in [2,3]:
                for xn in range(MTnumber-1):
                    len1[x1].append(round(node1[x1][0][xx][xn]-node1[x1][0][xx][xn+1],2))
                    len1[x1].append(round(node1[x1][1][xx][xn]-node1[x1][1][xx][xn+1],2))

        time1.append(a*h)
        MTX1.append(round(numpy.mean(lxian[0]),1))
        MTX2.append(round(Xpo-Xpole,2))
        MTzn6.append(monum[0])
        MTzn7.append(Kp3*(l4l[1]-Xkin1))
        MTzn8.append(-Kp3*(l1r[1]-Xkin))
        MTzn18.append(monum[1])
        MTzn9.append(round(numpy.mean(lxian[1]),1))
        
        MTzn11.append(Kp3*(l4l[0]-Xkin1))
        MTzn12.append(-Kp3*(l1r[0]-Xkin))
        MTzn13.append(round(Xkin,2))
        MTzn14.append(round(Xkin1,2))
        MTzn15.append(nu[0])
        MTzn16.append(nu[1])
        MTk1.append(round((numpy.mean(desk1)-numpy.mean(deska1)),2))
        MTi1.append(pos1[0]-posa1[0])
        MTzn3.append(pos4[1]-posa4[1])
        MTzn1.append(pos4[0]-posa4[0])
        MTzn2.append(round((numpy.mean(desi2)-numpy.mean(desia2)),2))
        MTzn17.append(round((numpy.mean(Ximt2)-numpy.mean(ximta2)),2))
        MTzn20.append(pos1[1]-posa1[1])#len1[0][1])
        MTzn21.append(pos2[0]-posa2[0])#len1[1][0])
        MTzn10.append(round((numpy.mean(Xkmt1)-numpy.mean(xkmta1)),2))#len1[1][1])
        MTzn19.append(nunum[0])#round(numpy.mean(overlap))) 
        MTzn22.append(len1[0][0])
        MTzn23.append(len1[0][1]) 
        MTzn24.append(numpy.mean(overlap)) 
        for x2 in range(pair):
            desia2[x2]=desi2[x2]
            deska1[x2]=desk1[x2]
            posa1[x2]=pos1[x2]
            posa4[x2]=pos4[x2]
            posa2[x2]=pos2[x2]
            ximta2[x2]=Ximt2[x2]
            xkmta1[x2]=Xkmt1[x2]
            ximta3[x2]=Ximt3[x2]
            xkmta4[x2]=Xkmt4[x2]

    if a%5000==0:
        dataframe = pd.DataFrame({'atime':time1,'lover':MTX1,'lover1':MTzn9,'lpole':MTX2,'rmtk':MTzn3,'rpk2':MTi1,'rdk1':MTk1,'ratepk':MTzn1,'rateid':MTzn2,'rateif':MTzn17,'n11':MTzn6,'n22':MTzn18,'n1':MTzn15,'n2':MTzn16,'xkinc':MTzn13,'xkin1c':MTzn14,'xforce':MTzn11,'xforce1':MTzn12,'xforce2':MTzn7,'xforce3':MTzn8,'lens1':MTzn20,'lens2':MTzn21,'lens3':MTzn10,'np':MTzn19,'overlap':MTzn24,'lenl2':MTzn22,'lenl3':MTzn23})
        dataframe.to_csv('./2e'+str(koffn)+str(Foffn)+str(FPE)+str(pi1)+'alp'+str(alp)+str(Fxing)+str(nant)+str(MTnumber)+'B'+str(B)+str(Fp0)+str(Kp1)+str(Kp2)+str(Kp3)+str(vd)+str(kon)+str(vp1)+'ss11.csv',index=False,sep=',')

       
      


# In[ ]:


3 10-4 0.03


# In[ ]:




