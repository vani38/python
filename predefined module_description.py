Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import math as m
m.sqrt(25)
5.0
from math import sqrt,pow
sqrt(625)
25.0
pow(4,2)
16.0
help('math')
Help on built-in module math:

NAME
    math

DESCRIPTION
    This module provides access to the mathematical functions
    defined by the C standard.

FUNCTIONS
    acos(x, /)
        Return the arc cosine (measured in radians) of x.

        The result is between 0 and pi.

    acosh(x, /)
        Return the inverse hyperbolic cosine of x.

    asin(x, /)
        Return the arc sine (measured in radians) of x.

        The result is between -pi/2 and pi/2.

    asinh(x, /)
        Return the inverse hyperbolic sine of x.

    atan(x, /)
        Return the arc tangent (measured in radians) of x.

        The result is between -pi/2 and pi/2.

    atan2(y, x, /)
        Return the arc tangent (measured in radians) of y/x.

        Unlike atan(y/x), the signs of both x and y are considered.

    atanh(x, /)
        Return the inverse hyperbolic tangent of x.

    cbrt(x, /)
        Return the cube root of x.

    ceil(x, /)
        Return the ceiling of x as an Integral.

        This is the smallest integer >= x.

    comb(n, k, /)
        Number of ways to choose k items from n items without repetition and without order.

        Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
        to zero when k > n.

        Also called the binomial coefficient because it is equivalent
        to the coefficient of k-th term in polynomial expansion of the
        expression (1 + x)**n.

        Raises TypeError if either of the arguments are not integers.
        Raises ValueError if either of the arguments are negative.

    copysign(x, y, /)
        Return a float with the magnitude (absolute value) of x but the sign of y.

        On platforms that support signed zeros, copysign(1.0, -0.0)
        returns -1.0.

    cos(x, /)
        Return the cosine of x (measured in radians).

    cosh(x, /)
        Return the hyperbolic cosine of x.

    degrees(x, /)
        Convert angle x from radians to degrees.

    dist(p, q, /)
        Return the Euclidean distance between two points p and q.

        The points should be specified as sequences (or iterables) of
        coordinates.  Both inputs must have the same dimension.

        Roughly equivalent to:
            sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))

    erf(x, /)
        Error function at x.

    erfc(x, /)
        Complementary error function at x.

    exp(x, /)
        Return e raised to the power of x.

    exp2(x, /)
        Return 2 raised to the power of x.

    expm1(x, /)
        Return exp(x)-1.

        This function avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small x.

    fabs(x, /)
        Return the absolute value of the float x.

    factorial(n, /)
        Find n!.

        Raise a ValueError if x is negative or non-integral.

    floor(x, /)
        Return the floor of x as an Integral.

        This is the largest integer <= x.

    fmod(x, y, /)
        Return fmod(x, y), according to platform C.

        x % y may differ.

    frexp(x, /)
        Return the mantissa and exponent of x, as pair (m, e).

        m is a float and e is an int, such that x = m * 2.**e.
        If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0.

    fsum(seq, /)
        Return an accurate floating point sum of values in the iterable seq.

        Assumes IEEE-754 floating point arithmetic.

    gamma(x, /)
        Gamma function at x.

    gcd(*integers)
        Greatest Common Divisor.

    hypot(...)
        hypot(*coordinates) -> value

        Multidimensional Euclidean distance from the origin to a point.

        Roughly equivalent to:
            sqrt(sum(x**2 for x in coordinates))

        For a two dimensional point (x, y), gives the hypotenuse
        using the Pythagorean theorem:  sqrt(x*x + y*y).

        For example, the hypotenuse of a 3/4/5 right triangle is:

            >>> hypot(3.0, 4.0)
            5.0

    isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
        Determine whether two floating point numbers are close in value.

          rel_tol
            maximum difference for being considered "close", relative to the
            magnitude of the input values
          abs_tol
            maximum difference for being considered "close", regardless of the
            magnitude of the input values

        Return True if a is close in value to b, and False otherwise.

        For the values to be considered close, the difference between them
        must be smaller than at least one of the tolerances.

        -inf, inf and NaN behave similarly to the IEEE 754 Standard.  That
        is, NaN is not close to anything, even itself.  inf and -inf are
        only close to themselves.

    isfinite(x, /)
        Return True if x is neither an infinity nor a NaN, and False otherwise.

    isinf(x, /)
        Return True if x is a positive or negative infinity, and False otherwise.

    isnan(x, /)
        Return True if x is a NaN (not a number), and False otherwise.

    isqrt(n, /)
        Return the integer part of the square root of the input.

    lcm(*integers)
        Least Common Multiple.

    ldexp(x, i, /)
        Return x * (2**i).

        This is essentially the inverse of frexp().

    lgamma(x, /)
        Natural logarithm of absolute value of Gamma function at x.

    log(...)
        log(x, [base=math.e])
        Return the logarithm of x to the given base.

        If the base is not specified, returns the natural logarithm (base e) of x.

    log10(x, /)
        Return the base 10 logarithm of x.

    log1p(x, /)
        Return the natural logarithm of 1+x (base e).

        The result is computed in a way which is accurate for x near zero.

    log2(x, /)
        Return the base 2 logarithm of x.

    modf(x, /)
        Return the fractional and integer parts of x.

        Both results carry the sign of x and are floats.

    nextafter(x, y, /, *, steps=None)
        Return the floating-point value the given number of steps after x towards y.

        If steps is not specified or is None, it defaults to 1.

        Raises a TypeError, if x or y is not a double, or if steps is not an integer.
        Raises ValueError if steps is negative.

    perm(n, k=None, /)
        Number of ways to choose k items from n items without repetition and with order.

        Evaluates to n! / (n - k)! when k <= n and evaluates
        to zero when k > n.

        If k is not specified or is None, then k defaults to n
        and the function returns n!.

        Raises TypeError if either of the arguments are not integers.
        Raises ValueError if either of the arguments are negative.

    pow(x, y, /)
        Return x**y (x to the power of y).

    prod(iterable, /, *, start=1)
        Calculate the product of all the elements in the input iterable.

        The default start value for the product is 1.

        When the iterable is empty, return the start value.  This function is
        intended specifically for use with numeric values and may reject
        non-numeric types.

    radians(x, /)
        Convert angle x from degrees to radians.

    remainder(x, y, /)
        Difference between x and the closest integer multiple of y.

        Return x - n*y where n*y is the closest integer multiple of y.
        In the case where x is exactly halfway between two multiples of
        y, the nearest even value of n is used. The result is always exact.

    sin(x, /)
        Return the sine of x (measured in radians).

    sinh(x, /)
        Return the hyperbolic sine of x.

    sqrt(x, /)
        Return the square root of x.

    sumprod(p, q, /)
        Return the sum of products of values from two iterables p and q.

        Roughly equivalent to:

            sum(itertools.starmap(operator.mul, zip(p, q, strict=True)))

        For float and mixed int/float inputs, the intermediate products
        and sums are computed with extended precision.

    tan(x, /)
        Return the tangent of x (measured in radians).

    tanh(x, /)
        Return the hyperbolic tangent of x.

    trunc(x, /)
        Truncates the Real x to the nearest Integral toward 0.

        Uses the __trunc__ magic method.

    ulp(x, /)
        Return the value of the least significant bit of the float x.

DATA
    e = 2.718281828459045
    inf = inf
    nan = nan
    pi = 3.141592653589793
    tau = 6.283185307179586

FILE
    (built-in)






help('random')
Help on module random:

NAME
    random - Random variable generators.

MODULE REFERENCE
    https://docs.python.org/3.12/library/random.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
        bytes
        -----
               uniform bytes (values between 0 and 255)

        integers
        --------
               uniform within range

        sequences
        ---------
               pick random element
               pick random sample
               pick weighted random sample
               generate random permutation

        distributions on the real line:
        ------------------------------
               uniform
               triangular
               normal (Gaussian)
               lognormal
               negative exponential
               gamma
               beta
               pareto
               Weibull

        distributions on the circle (angles 0 to 2pi)
        ---------------------------------------------
               circular uniform
               von Mises

        discrete distributions
        ----------------------
               binomial


    General notes on the underlying Mersenne Twister core generator:

    * The period is 2**19937-1.
    * It is one of the most extensively tested generators in existence.
    * The random() method is implemented in C, executes in a single Python step,
      and is, therefore, threadsafe.

CLASSES
    _random.Random(builtins.object)
        Random
            SystemRandom

    class Random(_random.Random)
     |  Random(x=None)
     |
     |  Random number generator base class used by bound module functions.
     |
     |  Used to instantiate instances of Random to get generators that don't
     |  share state.
     |
     |  Class Random can also be subclassed if you want to use a different basic
     |  generator of your own devising: in that case, override the following
     |  methods:  random(), seed(), getstate(), and setstate().
     |  Optionally, implement a getrandbits() method so that randrange()
     |  can cover arbitrarily large ranges.
     |
     |  Method resolution order:
     |      Random
     |      _random.Random
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __getstate__(self)
     |      Helper for pickle.
     |
     |  __init__(self, x=None)
     |      Initialize an instance.
     |
     |      Optional argument x controls seeding, as for Random.seed().
     |
     |  __reduce__(self)
     |      Helper for pickle.
     |
     |  __setstate__(self, state)
     |
     |  betavariate(self, alpha, beta)
     |      Beta distribution.
     |
     |      Conditions on the parameters are alpha > 0 and beta > 0.
     |      Returned values range between 0 and 1.
     |
     |      The mean (expected value) and variance of the random variable are:
     |
     |          E[X] = alpha / (alpha + beta)
     |          Var[X] = alpha * beta / ((alpha + beta)**2 * (alpha + beta + 1))
     |
     |  binomialvariate(self, n=1, p=0.5)
     |      Binomial random variable.
     |
     |      Gives the number of successes for *n* independent trials
     |      with the probability of success in each trial being *p*:
     |
     |          sum(random() < p for i in range(n))
     |
     |      Returns an integer in the range:   0 <= X <= n
     |
     |      The mean (expected value) and variance of the random variable are:
     |
     |          E[X] = n * p
     |          Var[x] = n * p * (1 - p)
     |
     |  choice(self, seq)
     |      Choose a random element from a non-empty sequence.
     |
     |  choices(self, population, weights=None, *, cum_weights=None, k=1)
     |      Return a k sized list of population elements chosen with replacement.
     |
     |      If the relative weights or cumulative weights are not specified,
     |      the selections are made with equal probability.
     |
     |  expovariate(self, lambd=1.0)
     |      Exponential distribution.
     |
     |      lambd is 1.0 divided by the desired mean.  It should be
     |      nonzero.  (The parameter would be called "lambda", but that is
     |      a reserved word in Python.)  Returned values range from 0 to
     |      positive infinity if lambd is positive, and from negative
     |      infinity to 0 if lambd is negative.
     |
     |      The mean (expected value) and variance of the random variable are:
     |
     |          E[X] = 1 / lambd
     |          Var[X] = 1 / lambd ** 2
     |
     |  gammavariate(self, alpha, beta)
     |      Gamma distribution.  Not the gamma function!
     |
     |      Conditions on the parameters are alpha > 0 and beta > 0.
     |
     |      The probability distribution function is:
     |
     |                  x ** (alpha - 1) * math.exp(-x / beta)
     |        pdf(x) =  --------------------------------------
     |                    math.gamma(alpha) * beta ** alpha
     |
     |      The mean (expected value) and variance of the random variable are:
     |
     |          E[X] = alpha * beta
     |          Var[X] = alpha * beta ** 2
     |
     |  gauss(self, mu=0.0, sigma=1.0)
     |      Gaussian distribution.
     |
     |      mu is the mean, and sigma is the standard deviation.  This is
     |      slightly faster than the normalvariate() function.
     |
     |      Not thread-safe without a lock around calls.
     |
     |  getstate(self)
     |      Return internal state; can be passed to setstate() later.
     |
     |  lognormvariate(self, mu, sigma)
     |      Log normal distribution.
     |
     |      If you take the natural logarithm of this distribution, you'll get a
     |      normal distribution with mean mu and standard deviation sigma.
     |      mu can have any value, and sigma must be greater than zero.
     |
     |  normalvariate(self, mu=0.0, sigma=1.0)
     |      Normal distribution.
     |
     |      mu is the mean, and sigma is the standard deviation.
     |
     |  paretovariate(self, alpha)
     |      Pareto distribution.  alpha is the shape parameter.
     |
     |  randbytes(self, n)
     |      Generate n random bytes.
     |
     |  randint(self, a, b)
     |      Return random integer in range [a, b], including both end points.
     |
     |  randrange(self, start, stop=None, step=1)
     |      Choose a random item from range(stop) or range(start, stop[, step]).
     |
     |      Roughly equivalent to ``choice(range(start, stop, step))`` but
     |      supports arbitrarily large ranges and is optimized for common cases.
     |
     |  sample(self, population, k, *, counts=None)
     |      Chooses k unique random elements from a population sequence.
     |
     |      Returns a new list containing elements from the population while
     |      leaving the original population unchanged.  The resulting list is
     |      in selection order so that all sub-slices will also be valid random
     |      samples.  This allows raffle winners (the sample) to be partitioned
     |      into grand prize and second place winners (the subslices).
     |
     |      Members of the population need not be hashable or unique.  If the
     |      population contains repeats, then each occurrence is a possible
     |      selection in the sample.
     |
     |      Repeated elements can be specified one at a time or with the optional
     |      counts parameter.  For example:
     |
     |          sample(['red', 'blue'], counts=[4, 2], k=5)
     |
     |      is equivalent to:
     |
     |          sample(['red', 'red', 'red', 'red', 'blue', 'blue'], k=5)
     |
     |      To choose a sample from a range of integers, use range() for the
     |      population argument.  This is especially fast and space efficient
     |      for sampling from a large population:
     |
     |          sample(range(10000000), 60)
     |
     |  seed(self, a=None, version=2)
     |      Initialize internal state from a seed.
     |
     |      The only supported seed types are None, int, float,
     |      str, bytes, and bytearray.
     |
     |      None or no argument seeds from current time or from an operating
     |      system specific randomness source if available.
     |
     |      If *a* is an int, all bits are used.
     |
     |      For version 2 (the default), all of the bits are used if *a* is a str,
     |      bytes, or bytearray.  For version 1 (provided for reproducing random
     |      sequences from older versions of Python), the algorithm for str and
     |      bytes generates a narrower range of seeds.
     |
     |  setstate(self, state)
     |      Restore internal state from object returned by getstate().
     |
     |  shuffle(self, x)
     |      Shuffle list x in place, and return None.
     |
     |  triangular(self, low=0.0, high=1.0, mode=None)
     |      Triangular distribution.
     |
     |      Continuous distribution bounded by given lower and upper limits,
     |      and having a given mode value in-between.
     |
     |      http://en.wikipedia.org/wiki/Triangular_distribution
     |
     |      The mean (expected value) and variance of the random variable are:
     |
     |          E[X] = (low + high + mode) / 3
     |          Var[X] = (low**2 + high**2 + mode**2 - low*high - low*mode - high*mode) / 18
     |
     |  uniform(self, a, b)
     |      Get a random number in the range [a, b) or [a, b] depending on rounding.
     |
     |      The mean (expected value) and variance of the random variable are:
     |
     |          E[X] = (a + b) / 2
     |          Var[X] = (b - a) ** 2 / 12
     |
     |  vonmisesvariate(self, mu, kappa)
     |      Circular data distribution.
     |
     |      mu is the mean angle, expressed in radians between 0 and 2*pi, and
     |      kappa is the concentration parameter, which must be greater than or
     |      equal to zero.  If kappa is equal to zero, this distribution reduces
     |      to a uniform random angle over the range 0 to 2*pi.
     |
     |  weibullvariate(self, alpha, beta)
     |      Weibull distribution.
     |
     |      alpha is the scale parameter and beta is the shape parameter.
     |
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |
     |  __init_subclass__(**kwargs)
     |      Control how subclasses generate random integers.
     |
     |      The algorithm a subclass can use depends on the random() and/or
     |      getrandbits() implementation available to it and determines
     |      whether it can generate random integers from arbitrarily large
     |      ranges.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables
     |
     |  __weakref__
     |      list of weak references to the object
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  VERSION = 3
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from _random.Random:
     |
     |  getrandbits(self, k, /)
     |      getrandbits(k) -> x.  Generates an int with k random bits.
     |
     |  random(self, /)
     |      random() -> x in the interval [0, 1).
     |
     |  ----------------------------------------------------------------------
     |  Static methods inherited from _random.Random:
     |
     |  __new__(*args, **kwargs) class method of _random.Random
     |      Create and return a new object.  See help(type) for accurate signature.

    class SystemRandom(Random)
     |  SystemRandom(x=None)
     |
     |  Alternate random number generator using sources provided
     |  by the operating system (such as /dev/urandom on Unix or
     |  CryptGenRandom on Windows).
     |
     |   Not available on all systems (see os.urandom() for details).
     |
     |  Method resolution order:
     |      SystemRandom
     |      Random
     |      _random.Random
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  getrandbits(self, k)
     |      getrandbits(k) -> x.  Generates an int with k random bits.
     |
     |  getstate = _notimplemented(self, *args, **kwds)
     |
     |  randbytes(self, n)
     |      Generate n random bytes.
     |
     |  random(self)
     |      Get the next random number in the range 0.0 <= X < 1.0.
     |
     |  seed(self, *args, **kwds)
     |      Stub method.  Not used for a system random number generator.
     |
     |  setstate = _notimplemented(self, *args, **kwds)
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from Random:
     |
     |  __getstate__(self)
     |      Helper for pickle.
     |
     |  __init__(self, x=None)
     |      Initialize an instance.
     |
     |      Optional argument x controls seeding, as for Random.seed().
     |
     |  __reduce__(self)
     |      Helper for pickle.
     |
     |  __setstate__(self, state)
     |
     |  betavariate(self, alpha, beta)
     |      Beta distribution.
     |
     |      Conditions on the parameters are alpha > 0 and beta > 0.
     |      Returned values range between 0 and 1.
     |
     |      The mean (expected value) and variance of the random variable are:
     |
     |          E[X] = alpha / (alpha + beta)
     |          Var[X] = alpha * beta / ((alpha + beta)**2 * (alpha + beta + 1))
     |
     |  binomialvariate(self, n=1, p=0.5)
     |      Binomial random variable.
     |
     |      Gives the number of successes for *n* independent trials
     |      with the probability of success in each trial being *p*:
     |
     |          sum(random() < p for i in range(n))
     |
     |      Returns an integer in the range:   0 <= X <= n
     |
     |      The mean (expected value) and variance of the random variable are:
     |
     |          E[X] = n * p
     |          Var[x] = n * p * (1 - p)
     |
     |  choice(self, seq)
     |      Choose a random element from a non-empty sequence.
     |
     |  choices(self, population, weights=None, *, cum_weights=None, k=1)
     |      Return a k sized list of population elements chosen with replacement.
     |
     |      If the relative weights or cumulative weights are not specified,
     |      the selections are made with equal probability.
     |
     |  expovariate(self, lambd=1.0)
     |      Exponential distribution.
     |
     |      lambd is 1.0 divided by the desired mean.  It should be
     |      nonzero.  (The parameter would be called "lambda", but that is
     |      a reserved word in Python.)  Returned values range from 0 to
     |      positive infinity if lambd is positive, and from negative
     |      infinity to 0 if lambd is negative.
     |
     |      The mean (expected value) and variance of the random variable are:
     |
     |          E[X] = 1 / lambd
     |          Var[X] = 1 / lambd ** 2
     |
     |  gammavariate(self, alpha, beta)
     |      Gamma distribution.  Not the gamma function!
     |
     |      Conditions on the parameters are alpha > 0 and beta > 0.
     |
     |      The probability distribution function is:
     |
     |                  x ** (alpha - 1) * math.exp(-x / beta)
     |        pdf(x) =  --------------------------------------
     |                    math.gamma(alpha) * beta ** alpha
     |
     |      The mean (expected value) and variance of the random variable are:
     |
     |          E[X] = alpha * beta
     |          Var[X] = alpha * beta ** 2
     |
     |  gauss(self, mu=0.0, sigma=1.0)
     |      Gaussian distribution.
     |
     |      mu is the mean, and sigma is the standard deviation.  This is
     |      slightly faster than the normalvariate() function.
     |
     |      Not thread-safe without a lock around calls.
     |
     |  lognormvariate(self, mu, sigma)
     |      Log normal distribution.
     |
     |      If you take the natural logarithm of this distribution, you'll get a
     |      normal distribution with mean mu and standard deviation sigma.
     |      mu can have any value, and sigma must be greater than zero.
     |
     |  normalvariate(self, mu=0.0, sigma=1.0)
     |      Normal distribution.
     |
     |      mu is the mean, and sigma is the standard deviation.
     |
     |  paretovariate(self, alpha)
     |      Pareto distribution.  alpha is the shape parameter.
     |
     |  randint(self, a, b)
     |      Return random integer in range [a, b], including both end points.
     |
     |  randrange(self, start, stop=None, step=1)
     |      Choose a random item from range(stop) or range(start, stop[, step]).
     |
     |      Roughly equivalent to ``choice(range(start, stop, step))`` but
     |      supports arbitrarily large ranges and is optimized for common cases.
     |
     |  sample(self, population, k, *, counts=None)
     |      Chooses k unique random elements from a population sequence.
     |
     |      Returns a new list containing elements from the population while
     |      leaving the original population unchanged.  The resulting list is
     |      in selection order so that all sub-slices will also be valid random
     |      samples.  This allows raffle winners (the sample) to be partitioned
     |      into grand prize and second place winners (the subslices).
     |
     |      Members of the population need not be hashable or unique.  If the
     |      population contains repeats, then each occurrence is a possible
     |      selection in the sample.
     |
     |      Repeated elements can be specified one at a time or with the optional
     |      counts parameter.  For example:
     |
     |          sample(['red', 'blue'], counts=[4, 2], k=5)
     |
     |      is equivalent to:
     |
     |          sample(['red', 'red', 'red', 'red', 'blue', 'blue'], k=5)
     |
     |      To choose a sample from a range of integers, use range() for the
     |      population argument.  This is especially fast and space efficient
     |      for sampling from a large population:
     |
     |          sample(range(10000000), 60)
     |
     |  shuffle(self, x)
     |      Shuffle list x in place, and return None.
     |
     |  triangular(self, low=0.0, high=1.0, mode=None)
     |      Triangular distribution.
     |
     |      Continuous distribution bounded by given lower and upper limits,
     |      and having a given mode value in-between.
     |
     |      http://en.wikipedia.org/wiki/Triangular_distribution
     |
     |      The mean (expected value) and variance of the random variable are:
     |
     |          E[X] = (low + high + mode) / 3
     |          Var[X] = (low**2 + high**2 + mode**2 - low*high - low*mode - high*mode) / 18
     |
     |  uniform(self, a, b)
     |      Get a random number in the range [a, b) or [a, b] depending on rounding.
     |
     |      The mean (expected value) and variance of the random variable are:
     |
     |          E[X] = (a + b) / 2
     |          Var[X] = (b - a) ** 2 / 12
     |
     |  vonmisesvariate(self, mu, kappa)
     |      Circular data distribution.
     |
     |      mu is the mean angle, expressed in radians between 0 and 2*pi, and
     |      kappa is the concentration parameter, which must be greater than or
     |      equal to zero.  If kappa is equal to zero, this distribution reduces
     |      to a uniform random angle over the range 0 to 2*pi.
     |
     |  weibullvariate(self, alpha, beta)
     |      Weibull distribution.
     |
     |      alpha is the scale parameter and beta is the shape parameter.
     |
     |  ----------------------------------------------------------------------
     |  Class methods inherited from Random:
     |
     |  __init_subclass__(**kwargs)
     |      Control how subclasses generate random integers.
     |
     |      The algorithm a subclass can use depends on the random() and/or
     |      getrandbits() implementation available to it and determines
     |      whether it can generate random integers from arbitrarily large
     |      ranges.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from Random:
     |
     |  __dict__
     |      dictionary for instance variables
     |
     |  __weakref__
     |      list of weak references to the object
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from Random:
     |
     |  VERSION = 3
     |
     |  ----------------------------------------------------------------------
     |  Static methods inherited from _random.Random:
     |
     |  __new__(*args, **kwargs) class method of _random.Random
     |      Create and return a new object.  See help(type) for accurate signature.

FUNCTIONS
    betavariate(alpha, beta) method of Random instance
        Beta distribution.

        Conditions on the parameters are alpha > 0 and beta > 0.
        Returned values range between 0 and 1.

        The mean (expected value) and variance of the random variable are:

            E[X] = alpha / (alpha + beta)
            Var[X] = alpha * beta / ((alpha + beta)**2 * (alpha + beta + 1))

    binomialvariate(n=1, p=0.5) method of Random instance
        Binomial random variable.

        Gives the number of successes for *n* independent trials
        with the probability of success in each trial being *p*:

            sum(random() < p for i in range(n))

        Returns an integer in the range:   0 <= X <= n

        The mean (expected value) and variance of the random variable are:

            E[X] = n * p
            Var[x] = n * p * (1 - p)

    choice(seq) method of Random instance
        Choose a random element from a non-empty sequence.

    choices(population, weights=None, *, cum_weights=None, k=1) method of Random instance
        Return a k sized list of population elements chosen with replacement.

        If the relative weights or cumulative weights are not specified,
        the selections are made with equal probability.

    expovariate(lambd=1.0) method of Random instance
        Exponential distribution.

        lambd is 1.0 divided by the desired mean.  It should be
        nonzero.  (The parameter would be called "lambda", but that is
        a reserved word in Python.)  Returned values range from 0 to
        positive infinity if lambd is positive, and from negative
        infinity to 0 if lambd is negative.

        The mean (expected value) and variance of the random variable are:

            E[X] = 1 / lambd
            Var[X] = 1 / lambd ** 2

    gammavariate(alpha, beta) method of Random instance
        Gamma distribution.  Not the gamma function!

        Conditions on the parameters are alpha > 0 and beta > 0.

        The probability distribution function is:

                    x ** (alpha - 1) * math.exp(-x / beta)
          pdf(x) =  --------------------------------------
                      math.gamma(alpha) * beta ** alpha

        The mean (expected value) and variance of the random variable are:

            E[X] = alpha * beta
            Var[X] = alpha * beta ** 2

    gauss(mu=0.0, sigma=1.0) method of Random instance
        Gaussian distribution.

        mu is the mean, and sigma is the standard deviation.  This is
        slightly faster than the normalvariate() function.

        Not thread-safe without a lock around calls.

    getrandbits(k, /) method of Random instance
        getrandbits(k) -> x.  Generates an int with k random bits.

    getstate() method of Random instance
        Return internal state; can be passed to setstate() later.

    lognormvariate(mu, sigma) method of Random instance
        Log normal distribution.

        If you take the natural logarithm of this distribution, you'll get a
        normal distribution with mean mu and standard deviation sigma.
        mu can have any value, and sigma must be greater than zero.

    normalvariate(mu=0.0, sigma=1.0) method of Random instance
        Normal distribution.

        mu is the mean, and sigma is the standard deviation.

    paretovariate(alpha) method of Random instance
        Pareto distribution.  alpha is the shape parameter.

    randbytes(n) method of Random instance
        Generate n random bytes.

    randint(a, b) method of Random instance
        Return random integer in range [a, b], including both end points.

    random() method of Random instance
        random() -> x in the interval [0, 1).

    randrange(start, stop=None, step=1) method of Random instance
        Choose a random item from range(stop) or range(start, stop[, step]).

        Roughly equivalent to ``choice(range(start, stop, step))`` but
        supports arbitrarily large ranges and is optimized for common cases.

    sample(population, k, *, counts=None) method of Random instance
        Chooses k unique random elements from a population sequence.

        Returns a new list containing elements from the population while
        leaving the original population unchanged.  The resulting list is
        in selection order so that all sub-slices will also be valid random
        samples.  This allows raffle winners (the sample) to be partitioned
        into grand prize and second place winners (the subslices).

        Members of the population need not be hashable or unique.  If the
        population contains repeats, then each occurrence is a possible
        selection in the sample.

        Repeated elements can be specified one at a time or with the optional
        counts parameter.  For example:

            sample(['red', 'blue'], counts=[4, 2], k=5)

        is equivalent to:

            sample(['red', 'red', 'red', 'red', 'blue', 'blue'], k=5)

        To choose a sample from a range of integers, use range() for the
        population argument.  This is especially fast and space efficient
        for sampling from a large population:

            sample(range(10000000), 60)

    seed(a=None, version=2) method of Random instance
        Initialize internal state from a seed.

        The only supported seed types are None, int, float,
        str, bytes, and bytearray.

        None or no argument seeds from current time or from an operating
        system specific randomness source if available.

        If *a* is an int, all bits are used.

        For version 2 (the default), all of the bits are used if *a* is a str,
        bytes, or bytearray.  For version 1 (provided for reproducing random
        sequences from older versions of Python), the algorithm for str and
        bytes generates a narrower range of seeds.

    setstate(state) method of Random instance
        Restore internal state from object returned by getstate().

    shuffle(x) method of Random instance
        Shuffle list x in place, and return None.

    triangular(low=0.0, high=1.0, mode=None) method of Random instance
        Triangular distribution.

        Continuous distribution bounded by given lower and upper limits,
        and having a given mode value in-between.

        http://en.wikipedia.org/wiki/Triangular_distribution

        The mean (expected value) and variance of the random variable are:

            E[X] = (low + high + mode) / 3
            Var[X] = (low**2 + high**2 + mode**2 - low*high - low*mode - high*mode) / 18

    uniform(a, b) method of Random instance
        Get a random number in the range [a, b) or [a, b] depending on rounding.

        The mean (expected value) and variance of the random variable are:

            E[X] = (a + b) / 2
            Var[X] = (b - a) ** 2 / 12

    vonmisesvariate(mu, kappa) method of Random instance
        Circular data distribution.

        mu is the mean angle, expressed in radians between 0 and 2*pi, and
        kappa is the concentration parameter, which must be greater than or
        equal to zero.  If kappa is equal to zero, this distribution reduces
        to a uniform random angle over the range 0 to 2*pi.

    weibullvariate(alpha, beta) method of Random instance
        Weibull distribution.

        alpha is the scale parameter and beta is the shape parameter.

DATA
    __all__ = ['Random', 'SystemRandom', 'betavariate', 'binomialvariate',...

FILE
    c:\users\administrator\appdata\local\programs\python\python312\lib\random.py


>>> 
>>> 
