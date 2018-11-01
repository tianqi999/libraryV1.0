function checkForm() {
    if (confirm("确定保存吗?")) {
        widow.close()
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
        spanObj.innerHTML = dataName + "不能为空";
        spanObj.style.color = "red";
        return false;
    } else if (reg.test(val)) {
        spanObj.innerHTML = "OK";
        spanObj.style.color = "green";
        return true;
    } else {
        spanObj.innerHTML = dataName + "格式不符合要求";
        spanObj.style.color = "red";
        return false;
    }
}
var i;
function checkUname() {
    var info=$('input[name=uname]').val();
    var obj=document.getElementById("unameSpan")
    if(info==""){
            obj.innerHTML="用户名不可为空";
            obj.style.color="red";
        }else{
         $.ajax({
            url:'/sys_settings/getManagerName/',
            type:'get',
            data:{'ManagerName':info},
            async:false,
            success:function (result) {
                if(result.flag){
                    obj.innerHTML="用户名可用";
                    obj.style.color="green";
                    i=true;
                }else{
                    obj.innerHTML="用户名已存在";
                    obj.style.color="red";
                    i=false
                }
            }
        })
        return i;
    }

}

var q;
function checkUname2() {
    var info=$('input[name=uname]').val();
    var obj=document.getElementById("unameSpan")
    if(info==""){
            obj.innerHTML="书架名不可为空";
            obj.style.color="red";
        }else{
         $.ajax({
            url:'/sys_settings/getBookcase/',
            type:'get',
            data:{'Bookcase':info},
            async:false,
            success:function (result) {
                if(result.flag){
                    obj.innerHTML="书架名可用";
                    obj.style.color="green";
                    q=true;
                }else{
                    obj.innerHTML="书架名已存在";
                    obj.style.color="red";
                    q=false
                }
            }
        })
        return q;
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
    var reg=/^[1-9A-Za-z]\w{5,10}@\w{2,8}\.(com){1}(\.cn){0,1}$/;
    return checkField(reg,"email")
}

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

function checkAll1() {
    var flag=checkLibraryname()&checkCurator()&checkTel()&checkAddress()&checkEmail()&checkurl()&checkCreatedate()&checkIntroduce();
    return flag==1?true:false;
}

function main_func() {
    alert("对不起,您没有权限")
}

function parModify() {
    var count=$('#addr>option:selected').val();

    location.href="/sys_settings/parameter_modify/?key="+count
}

function func(arg) {
        var val=document.getElementById(arg).value;
        var spanobj=document.getElementById(arg+"Span");
        if(val==""){
            spanobj.innerHTML="不能为空";
            spanobj.style.color="red";
            return false;
        }else{
            spanobj.innerHTML="OK";
            spanobj.style.color="green";
            return true
        }
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

function funcborrow() {
    var count=$('input[name=barcode]').val();
    // var info=$('input[name=inputkey]').val();
    // location.href="/book_operation/bookBorrow/?key="+count+"&value="+info;

    $.get('/book_operation/getReaderInfo/',{'readerid':count},function (result) {
        // console.log(result.reader);

        var reader = JSON.parse(result.reader);

        $('#readername').val(reader.rname);
        $('#sex').val(reader.gender);
        $('#paperType').val(reader.papertype);
        $('#readerType').val(result.typename);
        $('#paperNo').val(reader.paperno);
        $('#number').val(result.num);


    });

}

function bookInfo() {
    var s=$('#inputkey').val();
    var f=$('input[name=f]:checked').val();
    $.get('/book_operation/getBookInfo/',{'f':f,'s':s},function (result) {
        console.log(result.bookInfo)

        var bookInfo = JSON.parse(result.bookInfo);

        $('#bookname').val(bookInfo.bname);
        $('#publish').val(bookInfo.pubilshing);
        $('#operrate').val(result.bookcase);
        $('#price').val(bookInfo.price);
    })

}

function borrow() {
    var barcode =$('#barcode').val();
    var key = $('#inputkey').val();
    var borrowtime = $('#olddate').val();
    var backtime = $('#newdate').val();
    if (barcode.length == 0||key.length == 0||borrowtime.length == 0||backtime.length == 0){
        alert('信息不完整，请重新检查');
        return false;
    }else{
        alert('借阅成功')
    }
}