// معالجة تسجيل الدخول
document.getElementById("loginForm").onsubmit = function(event) {
    event.preventDefault(); // منع إرسال النموذج بالطريقة الافتراضية
    var username = event.target.username.value; // الحصول على اسم المستخدم
    var password = event.target.password.value; // الحصول على كلمة المرور

    // إرسال طلب تسجيل الدخول إلى الخادم
    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `username=${username}&password=${password}`
    }).then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json(); // تحويل الاستجابة إلى JSON
    }).then(data => {
        // عرض البيانات أو الرسالة
        if (data.error) {
            document.getElementById("result").innerText = data.error; // عرض خطأ إذا حدث
        } else {
            document.getElementById("result").innerText = "تم تسجيل الدخول بنجاح!"; // رسالة نجاح
            // يمكنك إعادة توجيه المستخدم هنا إلى صفحة أخرى أو تحديث المحتوى
            // window.location.href = '/dashboard'; // على سبيل المثال
        }
    }).catch(error => {
        document.getElementById("result").innerText = "حدث خطأ: " + error.message; // عرض أي أخطاء
    });
};

// معالجة التسجيل
document.getElementById("signupForm").onsubmit = function(event) {
    event.preventDefault(); // منع إرسال النموذج بالطريقة الافتراضية
    var new_username = event.target.new_username.value; // الحصول على اسم المستخدم الجديد
    var new_password = event.target.new_password.value; // الحصول على كلمة المرور الجديدة
    var confirm_password = event.target.confirm_password.value; // الحصول على تأكيد كلمة المرور

    // تحقق من تطابق كلمة المرور
    if (new_password !== confirm_password) {
        document.getElementById("result").innerText = "كلمة المرور وتأكيد كلمة المرور لا تتطابق!";
        return;
    }

    // إرسال طلب التسجيل إلى الخادم
    fetch('/signup', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `username=${new_username}&password=${new_password}`
    }).then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json(); // تحويل الاستجابة إلى JSON
    }).then(data => {
        // عرض البيانات أو الرسالة
        if (data.error) {
            document.getElementById("result").innerText = data.error; // عرض خطأ إذا حدث
        } else {
            document.getElementById("result").innerText = "تم التسجيل بنجاح!"; // رسالة نجاح
        }
    }).catch(error => {
        document.getElementById("result").innerText = "حدث خطأ: " + error.message; // عرض أي أخطاء
    });
};
```
