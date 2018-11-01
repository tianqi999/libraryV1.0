function checkForm() {
    if (confirm("确定保存吗?")) {
        widow.close()
    }
}
var isture;
function checkbarcode() {
    //1.获取文本框内容
    var barcode = $('input[name="barcode"]').val();
    //2.非空校验
    if (barcode.length == 0) {
        $('#' + 'barcodeSpan').html('*借书卡号不能为空');
        $('#' + 'barcodeSpan').css("color", "red");
    } else {
        //3.判断唯一性
        $.ajax({
            url: '/reader/isExist/',
            type: 'get',
            data: {'barcode': barcode},
            async: false,
            success: function (result) {
                r = result.flag;
                //4.根据服务器端的响应信息进行页面更新
                if (r) {
                    $('#' + 'barcodeSpan').html('*该借书卡号已被注册！');
                    $('#' + 'barcodeSpan').css('color', 'red');
                    isture = false
                } else {
                    $('#' + 'barcodeSpan').html('OK');
                    $('#' + 'barcodeSpan').css('color', 'green');
                    isture = true
                }
            }
        })
        return isture
    }
}
var isbture;
function checkbook() {
    //1.获取文本框内容
    var bookcode = $('input[name="bookcode"]').val();
    //2.非空校验
    if (bookcode.length == 0) {
        $('#' + 'bookSpan').html('*条形码不能为空');
        $('#' + 'bookSpan').css("color", "red");
    } else {
        //3.判断唯一性
        $.ajax({
            url: '/book/isbExist/',
            type: 'get',
            data: {'bookcode': bookcode},
            async: false,
            success: function (result) {
                r = result.flag;
                //4.根据服务器端的响应信息进行页面更新
                if (r) {
                    $('#' + 'bookSpan').html('*该条形码已被注册！');
                    $('#' + 'bookSpan').css('color', 'red');
                    isbture = false;
                } else {
                    $('#' + 'bookSpan').html('OK');
                    $('#' + 'bookSpan').css('color', 'green');
                    isbture = true;
                }
            }
        })
        return isbture
    }
}
var booktp;
function checkbooktype() {
    //1.获取文本框内容
    var typename = $('input[name="typename"]').val();
    //2.非空校验
    if (typename.length == 0) {
        $('#' + 'typeSpan').html('*类型名不能为空');
        $('#' + 'typeSpan').css("color", "red");
    } else {
        //3.判断唯一性
        $.ajax({
            url: '/book/istype/',
            type: 'get',
            data: {'typename': typename},
            async: false,
            success: function (result) {
                r = result.flag;
                //4.根据服务器端的响应信息进行页面更新
                if (r) {
                    $('#' + 'typeSpan').html('*该图书种类已存在！');
                    $('#' + 'typeSpan').css('color', 'red');
                    booktp= false;
                } else {
                    $('#' + 'typeSpan').html('OK');
                    $('#' + 'typeSpan').css('color', 'green');
                    booktp = true;
                }
            }
        })
        return booktp
    }
}
function checkField(reg, obj) {
    var val = document.getElementById(obj).value;
    var spanObj = document.getElementById(obj + "Span");
    var dataName = document.getElementById(obj).alt;
    if (dataName == undefined) {
        dataName = "图书馆简介";
    }
    if (val == "") {
        spanObj.innerHTML = dataName + "*不能为空";
        spanObj.style.color = "red";
        return false;
    } else if (reg.test(val)) {
        spanObj.innerHTML = "OK";
        spanObj.style.color = "green";
        return true;
    } else {
        spanObj.innerHTML = dataName + "*格式不符合要求";
        spanObj.style.color = "red";
        return false;
    }
}

function checkRname() {
    var val = document.getElementById("readname").value;

    var spanObj = document.getElementById("rnameSpan");
    if (val == "") {
        spanObj.innerHTML = "*姓名不能为空";
        spanObj.style.color = "red";
        return false;
    }else {
        spanObj.innerHTML = "OK"
        spanObj.style.color = "green";
        return true;
    }
}

function checkUname2() {
    var val = document.getElementById("uname").value;

    var spanObj = document.getElementById("unameSpan");
    if (val == "") {
        spanObj.innerHTML = "书架名不能为空";
        spanObj.style.color = "red";
        return false;
    }else {
        spanObj.innerHTML = "书架名可用"
        spanObj.style.color = "green";
        return true;
    }
}

function checkAll3() {
    var flag=checkUname2();
    return flag==1?true:false;
}
function checkPwd() {
    var reg = /^\w{6,8}$/;
    return checkField(reg,"pwd");
}
function checktime() {
    var reg = /^.*/;
    return checkField(reg,"btime")
}

function checkAll2() {
    var flag = checkUname() & checkPwd();
    return flag == 1 ? true : false;
}

function checkLibraryname() {
    var reg = /^[\u4e00-\u9fa5]{2,15}$/;
    return checkField(reg,"libraryname")
}

function checkCurator() {
    var reg = /^[\u4e00-\u9fa5]{2,15}$/;
    return checkField(reg,"curator")
}

function checkTel() {
    var reg = /^1[3456789]\d{9}$/;
    return checkField(reg, "tel");
}

function checkAddress() {
    var reg = /^[\u4e00-\u9fa5]{2,20}$/;
    return checkField(reg,"address")
}

function checkEmail() {
    var reg=/^[A-Za-z\d]+([-_.][A-Za-z\d]+)*@([A-Za-z\d]+[-.])+[A-Za-z\d]{2,4}$/;
    return checkField(reg,"email")
}
function checkpaperno() {
    var reg=/(^[1-9]\d{5}(18|19|([23]\d))\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx])|([1−9]\d5\d2((0[1−9])|(10|11|12))(([0−2][1−9])|10|20|30|31)\d2[0−9Xx])/;
    return checkField(reg,'paperno')
}
// function checkbarcode() {
//     var reg=/^[1-9][0-9]{5,9}$/;
//     return checkField(reg,'barcode')
// }

function checkurl() {
    var reg=/(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?/;
    return checkField(reg,"url")
}

function checkCreatedate() {
    var val = document.getElementById("createdate").value;
    var spanObj = document.getElementById("createdateSpan");
    if(val==""){
        spanObj.innerHTML="时间不能为空";
        spanObj.style.color="red";
        return false;
    }else{
        spanObj.innerHTML="OK";
        spanObj.style.color="green";
        return true;
    }
}

function checkIntroduce() {
    var reg=/^.{2,200}$/;
    return checkField(reg,"introduce")
}
function checkbookcode() {
    var reg=/^[1-9][0-9]{5,9}$/;
    return checkField(reg,'bookcode')
}
function checkisbn() {
    var reg=/^[0-9]{10,13}$/;
    return checkField(reg,'isbn')
}

function checkAll1() {
    var flag=checkpaperno()&checkRname()&checkTel()&checkEmail()&checkbarcode();
    return flag==1?true:false;
}
function checkAll4() {
    var flag=checkRname()&checkTel()&checkEmail();
    return flag==1?true:false;
}
function checkAll5() {
    var flag=checkisbn()&checkbook()&func1()&func2()&func3();
    return flag==1?true:false;
}
function checkAll6() {
    var flag=checkisbn()&func1()&func2()&func3();
    return flag==1?true:false;

}

function parModify() {
    var count=$('#addr>option:selected').val();

    location.href="/sys_settings/parameter_modify/?key="+count
}

function func(arg) {
        var val=document.getElementById(arg).value;
        var spanobj=document.getElementById(arg+"Span");
        if(val==""){
            spanobj.innerHTML="*不能为空";
            spanobj.style.color="red";
            return false;
        }else{
            spanobj.innerHTML="OK";
            spanobj.style.color="green";
            return true
        }
}
function func1() {
    return func('bname')
}
function func2() {
    return func('author')
}
function func3() {
    return func('pubilshing')
}

function funcnum() {
    return func("cost")
}

function funcprice() {
    return func("price")
}

function funcval() {
    return func("validity")
}

function funcall() {
    var flag=funcprice()&funcnum()&funcval();
    return flag==1?true:false;
}
function functxt() {
    return func('bname')
}
function checkForm0(){
			    if(checkAll1() == true)
                {alert('添加成功！')}
			}
function checkForm1(){
			    if(checkAll4() == true)
                alert('修改成功！')
            }
function checkForm2(){
                if(checkAll5()==true)
                    alert('添加成功！')
            }
function checkForm3(){
                if(checkAll6()==true)
                    alert('修改成功！')
            }
function checkFormadd() {
			    if(checkbooktype()==true)
                alert('添加成功！')
            }
function checkFormch() {
                if(checkbooktype()==true)
                alert('修改成功！')
            }
