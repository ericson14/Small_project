;(function(){
	$(function(){
		var oUser = $('#user_name')
		var oPwd = $('#pwd')
		var oCpwd = $('#cpwd')
		var oMail = $('#email')
		var oCheck = $('#allow')
		
		var reUser = /^\w{6,20}$/
		var rePass = /^[\w!@#$%^&*]{6,20}$/;
		var reMail = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/i;
		
		var cUser = false
		var cPwd = false
		var cCpwd = false
		var cMail = false
		var cCheck = true
		
		oUser.blur(function(){
			var oSpan = $(this).siblings('span')
			var tVal = $(this).val()
			if(tVal==''){
				oSpan.hide()
				cUser = false
				return
			}
			if(reUser.test( tVal )){
				oSpan.hide()
				cUser = true
			}else{
				oSpan.show().html('请输入6到20位数字字母或下划线作为用户名')
				cUser = false
			}			
		})
		
		oPwd.blur(function(){
			var oSpan = $(this).siblings('span')
			var tVal = $(this).val()
			if(tVal==''){
				oSpan.hide()
				cPwd = false
				return
			}
			if(oCpwd.val() != ''){
				if(oCpwd.val()==tVal){
					oCpwd.siblings('span').hide()
					cCpwd = true
				}else{
					oCpwd.siblings('span').show().html('两次输入的密码不相同')
					cCpwd = false
				}
			}
			if(rePass.test( tVal )){
				oSpan.hide()
				cPwd = true
			}else{
				oSpan.show().html('请输入6到20位密码支持字母数字和!@#$%^&*')
				cPwd = false
			}			
		})
		
		oCpwd.blur(function(){
			var oSpan = $(this).siblings('span')
			var tVal = $(this).val()
			if(tVal==''){
				oSpan.hide()
				cCpwd = false
				return
			}			
			if(oCpwd.val()==oPwd.val()){
				oSpan.hide()
				cCpwd = true
			}else{
				oSpan.show().html('两次输入的密码不相同')
				cCpwd = false
			}			
		})
		
		oMail.blur(function(){
			var oSpan = $(this).siblings('span')
			var tVal = $(this).val()
			if(tVal==''){
				oSpan.hide()
				cMail = false
				return
			}
			if(reMail.test( tVal )){
				oSpan.hide()
				cMail = true
			}else{
				oSpan.show().html('请输入以数字字母开头的合法的邮箱')
				cMail = false
			}			
		})
		
		oCheck.click(function(){
			var oSpan = $(this).siblings('span')
			if($(this).is(':checked')){
				oSpan.hide()
				cCheck = true
			}else{
				oSpan.show().html('请勾选上同意协议')
				cCheck = false
			}			
		})
		
		$('form').submit(function(){
			if(cUser && cCheck && cPwd && cCpwd && cMail){
				return true
			}else{
				return false
			}
		})
	})
})()
