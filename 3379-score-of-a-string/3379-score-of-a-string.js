/**
 * @param {string} s
 * @return {number}
 */
var scoreOfString = function(s) {
    res = 0
    for(i=0 ; i<s.length -1 ; i++){
        res += Math.abs(s.charCodeAt(i) -   s.charCodeAt(i+1))
    }
    return res
};