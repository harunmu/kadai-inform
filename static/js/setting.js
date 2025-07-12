// 各項目の「変更」ボタンで編集モードに切り替え
function setupEdit(section) {
    document.getElementById(section+'-edit').addEventListener('click', function() {
        document.getElementById(section+'-view').classList.add('d-none');
        document.getElementById(section+'-input').classList.remove('d-none');
        document.getElementById(section+'-edit').classList.add('d-none');
        document.getElementById(section+'-save').classList.remove('d-none');
    });
}

// 各項目の「確定」ボタンでフォームを送信
function setupSave(section) {
    document.getElementById(section+'-save').addEventListener('click', function() {
        document.getElementById('setting-form').submit();
    });
}

['email','loginid','loginpw','notif'].forEach(setupEdit);
['email','loginid','loginpw','notif'].forEach(setupSave); 