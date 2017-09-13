# Box Blur

Last night you had to study, but decided to party instead. Now there is a black and white photo of you that is about to go viral. You cannot let this ruin your reputation, so you want to apply box blur algorithm to the photo to hide its content.

The algorithm works as follows: each pixel `x` in the resulting image has a value equal to the average value of the input image pixels' values from the `3 × 3` square with the center at `x`. All pixels at the edges are cropped.

As pixel's value is an integer, all fractions should be rounded down.

```
image = [[1, 1, 1], 
         [1, 7, 1], 
         [1, 1, 1]]
```

`boxBlur(image) = [[1]]`

`(1 + 1 + 1 + 1 + 7 + 1 + 1 + 1 + 1) / 9 = 15 / 9 = ~rounded down~ = 1`