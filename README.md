# Caesar_cipher

## We’re keeping it really basic here so the only pieces are queens and each queen is represented by a blue or red square.
## Chess board is an 8 by 8 grid of alternating black and white squares. The queens are red and blue squares.

- [x] Create an encrypt function that takes in a plain text phrase and a numeric shift.
### the phrase will then be shifted that many letters.
- E.g. encrypt(‘abc’,1) would return ‘bcd’ =
- E.g. encrypt(‘abc’, 10) would return ‘klm’

- [x] shifts that exceed 26 should wrap around
- E.g. encrypt(‘abc’,27) would return ‘bcd’
- [x] should have add_red method that accepts a row and column as input which colors corresponding cell.

- [x] shifts that push a letter out or range should wrap around
- E.g. encrypt(‘zzz’,1) would return ‘aaa’

- [x] Create a decrypt function that takes in encrypted text and numeric shift which will restore the encrypted text back to its original form when correct key is supplied.

- [x] create a crack function that will decode the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key.
- [x] Devise a method for the computer to determine if code was broken with minimal human guidance.


### I take a 3hrs to done all work

## The pull requst : https://github.com/shahd1995913/-caesar_cipher/pull/2
