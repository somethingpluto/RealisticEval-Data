//Regexes generated by ChatGPT, to match real numbers between a range (such as -90 to 90), and reject any character in the string

//I could tell you what these mean, but I won't. Too bad !
const LatitudeInputMatcherRegex = "^-?(?:90(?:\\.0+)?|[1-8]?\\d(?:\\.\\d+)?|0(?:\\.\\d+)?)$"
const LongitudeInputMatcherRegex = "^-?(?:180(?:\\.0+)?|[1-8]?\\d(?:\\.\\d+)?|0(?:\\.\\d+)?)$"