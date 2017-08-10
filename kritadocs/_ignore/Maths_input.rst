Also known as Numerical Input boxes. You can make Krita do simple maths
for you in the places where we have number input. Just select the number
in a spinbox, or rightclick a slider to activate number input. It
doesn't do unit conversion yet, but this is planned.

Possible Functions
------------------

Addition (Operator<nowiki>:</nowiki> + )
    Just adds the numbers. Usage: <code>50+100</code> Output:
    <code>150</code>
Subtraction (Operator<nowiki>:</nowiki> - )
    Just subtracts the last number from the first. Usage:
    <code>50-100</code> Output: <code>50</code>
Multiplication (Operator<nowiki>:</nowiki> \* )
    Just multiplies the numbers. Usage: <code>50\*100</code> Output:
    <code>5000</code>
Division (Operator<nowiki>:</nowiki> / )
    Just multiplies the numbers. Usage: <code>50/100</code> Output:
    <code>0.5</code>
Exponent (Operator<nowiki>:</nowiki> ^ )
    Makes the last number the exponent of the first and calculates the
    result. Usage: <code>2^8</code> Output: <code>256</code>
Sine (Operator<nowiki>:</nowiki> sin() )
    Gives you the sine of the given angle. Usage: <code>sin(50)</code>
    Output: <code>0.76</code>
Cosine (Operator<nowiki>:</nowiki> cos() )
    Gives you the cosine of the given angle. Usage: <code>cos(50)</code>
    Output: <code>0.64</code>
Tangent (Operator<nowiki>:</nowiki> tan() )
    Gives you the tangent of the given angle. Usage:
    <code>tan(50)</code> Output: <code>1.19</code>
Arc Sine (Operator<nowiki>:</nowiki> asin() )
    Inverse function of the sinus, gives you the angle which the sinus
    equals the argument. Usage: <code>asin(0.76)</code> Output:
    <code>50</code>
Arc Cosine (Operator<nowiki>:</nowiki> acos() )
    Inverse function of the cosinus, gives you the angle which the
    cosinus equals the argument. Usage: <code>acos(0.64)</code> Output:
    <code>50</code>
Arc Tangent (Operator<nowiki>:</nowiki> atan() )
    Inverse function of the tangent, gives you the angle which the
    tangent equals the argument. Usage: <code>atan(1.19)</code> Output:
    <code>50</code>
Absolute (Operator<nowiki>:</nowiki> abs() )
    Gives you the value without negatives. Usage:
    <code>abs(75-100)</code> Output: <code>25</code>
Exponent (Operator<nowiki>:</nowiki> exp() )
    Gives you given values using e as the exponent. Usage:
    <code>exp(1)</code> Output: <code>2.7183</code>
Natural Logarithm (Operator<nowiki>:</nowiki> ln() )
    Gives you the natural logarithm, which means it has the inverse
    functionality to exp(). Usage: <code>ln(2)</code> Output:
    <code>0.6931</code>

The following are technically supported but bugged:

Common Logarithm (Operator<nowiki>:</nowiki> log10() )
    Gives you logarithms of the given value. Usage:
    <code>log10(50)</code> Output: <code>0.64</code>

Order of Operations.
--------------------

The order of operations is a globally agreed upon reading order for
interpreting mathematical expressions. It solves how to read an
expression like:

<code>2+3\*4</code>

You could read it as 2+3 = 5, and then 5\*4 =20. Or you could say 3\*4 =
12 and then 2+12 = 14.

The order of operations itself is Exponents, Multiplication, Addition,
Subtraction. So we first multiply, and then add, making the answer to
the above 14, and this is how Krita will interpret the above.

We can use brackets to specify certain operations go first, so to get 20
from the above expression, we do the following:

<code>( 2+3 )\*4</code>

Krita can interpret the brackets accordingly and will give 20 from this.

Errors
------

Sometimes, you see the result becoming red. This means you made a
mistake and Krita cannot parse your maths expression. Simply click the
input box and try again.

`Category:Reference Manual <Category:Reference_Manual>`__
