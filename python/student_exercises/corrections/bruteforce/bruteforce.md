This is a hashed password that is generated using the SHA-256 algorithm.
You task is to find the password that was used to generate this hash.
For that you need to know some information about the password:
- It is an alphabetical string
- It is a lower case string
- It is a 5 letter string

The password to be found is hashed using the SHA-256 algorithm.
The SHA-256 algorithm is a hashing algorithm that takes a string as input and generates a 256 bit (32 byte) hash as output.
The hash is a hexadecimal string that is 64 characters long.

*You can use the hashlib library to generate the hash of a string.*

example:

```python    
password = hashlib.sha256("MyCurrentPassword".encode()).hexdigest()
```

here, `MyCurrentPassword` is the password string you want to find the hash for.

the `hexdigest()` method returns the hash as a hexadecimal **string**.

Knowing that information, 
you can write a program that will generate all possible combinations of 5 letter strings. and try to break the password.

You can also try to answer to the question regarding password security.

| population/length | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
  |-------------------|---|---|---|---|---|----|----|----|----|----|
  | lower_case (26)   | 0.002970344 | 0.077228944 | 2.007952544 | 52.206766144 | 1357.375919744 | 35291.773913344 | 917586.121746944 | 23857239.165420543 | 620288218.3009342 | 16127493675.824287 |
  | upper_case (26)   | 0.002970344 | 0.077228944 | 2.007952544 | 52.206766144 | 1357.375919744 | 35291.773913344 | 917586.121746944 | 23857239.165420543 | 620288218.3009342 | 16127493675.824287 |
  | digits (10)       | 2.5e-05 | 0.00025 | 0.0025 | 0.025 | 0.25 | 2.5 | 25.0 | 250.0 | 2500.0 | 25000.0 |
  | special (32)      | 0.008388608 | 0.268435456 | 8.589934592 | 274.877906944 | 8796.093022208 | 281474.976710656 | 9007199.254740993 | 288230376.15171176 | 9223372036.854776 | 295147905179.35284 |
  | alpha_lower_upper (52) | 0.095051008 | 4.942652416 | 257.017925632 | 13364.932132864 | 694976.470908928 | 36138776.48726425 | 1879216377.3377414 | 97719251621.56255 | 5081401084321.253 | 264232856384705.12 |
  | alphanumeric (62) | 0.229033208 | 14.200058896 | 880.403651552 | 54585.026396224 | 3384271.636565888 | 209824841.46708506 | 13009140170.959274 | 806566690599.475 | 50007134817167.445 | 3100442358664381.5 |
  | all_characters (95) | 1.93445234375 | 183.77297265625 | 17458.43240234375 | 1658551.0782226562 | 157562352.43115234 | 14968423480.959473 | 1422000230691.15 | 135090021915659.23 | 1.2833552081987628e+16 | 1.2191874477888246e+18 |