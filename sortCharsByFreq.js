/**
 * @param {string} s
 * @return {string}
 */
var frequencySort = function(s) {
    var sorted = objToArr(countChars(s)).sort(function(a, b){return b.num-a.num});
    var finalString = "", i;
    for (obj in sorted) {
        for(i = 0; i < sorted[obj].num; i++) {
            finalString += sorted[obj].char;
        }
    }
    return finalString;
};

function objToArr(obj) {
    var arr = [];
    for (k in obj) {
        arr.push({
            "char": k,
            "num": obj[k]
        })
    }
    return arr;
}

function countChars(s) {
    var counter = {};
    for(var i in s) {
        counter[s[i]] ? counter[s[i]]++ : (counter[s[i]] = 1)
    }
    return counter;
}
console.log(frequencySort("tree"))