# Central Limit Theorem (CLT)

## Definition

The **Central Limit Theorem (CLT)** states that the distribution of the sample mean approaches a normal distribution as the sample size increases, regardless of the shape of the population distribution.

## Mathematical Formulation

Let $X_1, X_2, ..., X_n$ be a random sample of size $n$ from any population with:
- Mean: $\mu$
- Variance: $\sigma^2$

The sample mean is defined as:
$$\bar{X} = \frac{1}{n}\sum_{i=1}^{n} X_i$$

According to CLT, as $n \to \infty$:
$$\bar{X} \sim N\left(\mu, \frac{\sigma^2}{n}\right)$$

The standardized version is:
$$Z = \frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \sim N(0,1)$$

## Key Conditions

1. **Random Sampling**: Observations must be independent and identically distributed (i.i.d.)
2. **Sample Size**: Typically $n \geq 30$ for practical applications
3. **Finite Variance**: Population variance $\sigma^2$ must be finite

## Important Properties

- **Mean of sample means**: $\mu_{\bar{X}} = \mu$
- **Standard error**: $\sigma_{\bar{X}} = \frac{\sigma}{\sqrt{n}}$
- **Shape**: Becomes approximately normal regardless of population shape

## Applications

1. **Confidence Intervals**
   $$\bar{X} \pm z_{\alpha/2} \frac{\sigma}{\sqrt{n}}$$

2. **Hypothesis Testing**
   $$Z = \frac{\bar{X} - \mu_0}{\sigma/\sqrt{n}}$$

3. **Quality Control**
4. **Statistical Inference**

## Example

For a population with $\mu = 50$, $\sigma = 10$, and sample size $n = 36$:
- Mean of sampling distribution: $\mu_{\bar{X}} = 50$
- Standard error: $\sigma_{\bar{X}} = \frac{10}{\sqrt{36}} = 1.67$
- 95% of sample means will fall between: $50 \pm 1.96 \times 1.67$

## Limitations

1. Requires sufficiently large sample size for non-normal populations
2. Assumes independent observations
3. May not apply to populations with infinite variance