/**
 * Definition for an interval.
 * function Interval(start, end) {
 *     this.start = start;
 *     this.end = end;
 * }
 */
function Interval(start, end) {
        this.start = start;
         this.end = end;
    }

/**
 * @param {Interval[]} intervals
 * @return {Interval[]}
 */
var merge = function(intervals) {
    sorted = intervals.sort(function(a, b) {
        return b.start - a.start;
    })
};