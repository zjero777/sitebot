$(document).ready(function () {
    const input = document.querySelector('input');
    var setCaretPos = function (node, pos) {
        var node = (typeof node == "string" || node instanceof String) ? document.getElementById(node) : node;
        if (!node) {
            return false;
        } else if (node.createTextRange) {
            var textRange = node.createTextRange();
            textRange.collapse(true);
            textRange.moveEnd(pos);
            textRange.moveStart(pos);
            textRange.select();
            return true;
        } else if (node.setSelectionRange) {
            node.setSelectionRange(0, pos);
            return true;
        }
        return false;
    };

    input.focus();
    setCaretPos(input, input.value.length)
    
});
