function boxBlur(image) {
  var answer = [];
  for (var x = 1; x < image.length - 1; x++) {
    var line = [];
    for (var y = 1; y < image[0].length - 1; y++) {
      var sum = 0;
      for (var dx = -1; dx <= 1; dx++) {
        for (var dy = -1; dy <= 1; dy++) {
          sum += image[x + dx][y + dy];
        }
      }
      line.push(Math.floor(sum / 9));
    }
    answer.push(line);
  }
  return answer;
};


var image = [[1,1,1], [1,7,1], [1,1,1]];
boxBlur(image);
var image = [[0,18,9], [27,9,0], [81,63,45]];
boxBlur(image);
var image = [[36,0,18,9], [27,54,9,0], [81,63,72,45]];
boxBlur(image);
var image = [[7,4,0,1], [5,6,2,2], [6,10,7,8], [1,4,2,0]];
boxBlur(image);
var image = [[36,0,18,9,9,45,27], [27,0,54,9,0,63,90], [81,63,72,45,18,27,0], [0,0,9,81,27,18,45], [45,45,27,27,90,81,72], [45,18,9,0,9,18,45], [27,81,36,63,63,72,81]];
boxBlur(image);
