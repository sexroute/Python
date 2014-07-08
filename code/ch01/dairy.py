import PAM30 as cPAMIE
ie= cPAMIE.PAMIE()
ie.navigate ('http://timesheetv2.paic.com.cn/timesheet/login.jsp;jsessionid=gGTXR1mpWHTp12kQy5qsWQvGmVynfyvQhGM10kpDTG98XbLSMwdC!1809703156') 
ie.setTextBox('j_username','CHENGSIQIN754') 
ie.setTextBox('j_password','Qin2012Luxe')
print(ie.getTextBoxValue('j_username', 'value'))
ie.clickButton('Submit')


