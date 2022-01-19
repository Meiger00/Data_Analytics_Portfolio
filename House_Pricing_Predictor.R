# Import the necessary packages
library(dplyr)
library(plyr)
library(lmtest)
library(car)
library(olsrr)
library(MVN)
library(MASS)
library(forecast)

# Read in the training data set
setwd("C:/Users/darkn/Google Drive/URI/Multivariate Statistical Analysis/data")
df = read.csv('House_train.csv', header=T)
df = df[,c("YearBuilt", "YearRemodAdd", "TotalBsmtSF", 
           "X1stFlrSF", "X2ndFlrSF", "GarageArea", "GrLivArea",
           "GarageCars", "FullBath", "SalePrice")]

# Drop any rows with at least one missing value in any given column
df = na.omit(df)

# Drop any duplicate rows
df = distinct(df)

##### LINEAR REGRESSION ASSUMPTION TESTING #####

# 1) RANDOM SAMPLE: Simple random sampling was used to construct the training data from the set of 
# all observations in the data set. The assumption of Random Sampling is thus satisfied.

# 2) LINEARITY: 
pairs(df[,c(1:7,10)]) 
# Based on visual inspection of the generated scatterplot matrix, linear relationships with strengths 
# ranging from weak to moderate appear to be exhibited between the response variable (SalePrice) and
# each of the respective predictor variables (sans discrete, quantitative predictors). Of note, the
# linearity exhibited between SalePrice and YearBuilt and YearRemodAdd is not relevant given that these
# predictor variables are both categorical. When building the regression model, both variables would
# have their values binned and coded as respective dummy variables. Regardless, the assumption of
# linearity is satisfied.

# 3) ZERO MEAN: 
lin = lm(SalePrice ~ YearBuilt + YearRemodAdd + TotalBsmtSF + X1stFlrSF + X2ndFlrSF
         + GarageArea + GrLivArea, data = df)
mean(residuals(lin)) 
# The mean of all of the model's error terms is very close to 0 (-0.0000000000008309177). While not
# exactly 0, this result indicates that the error distribution is approximately centered at 0 and thus
# the assumption of zero mean is (approximately) satisfied.

# 4) CONSTANT VARIANCE:
bptest(lin) 
# The Breusch-Pagan test (conducted below) produces a BP value (364.5) with a p-value of <0.001. The
# BP test result forces us to reject the null hypothesis that the variance among error terms from the
# model are all equal/constant at a 99.9% confidence level. The results therefore communicate that
# heteroscedasticity (i.e., non-constant variance among error terms) in the regression model is present
# with a 99.9% confidence level. This finding indicates that non-constant variance among error terms is
# present in the model, and thus the model does NOT satisfy the assumption of constant variance.

# COERCING CONSTANT VARIANCE AMONG ERROR TERMS
BoxCox.lambda(df$SalePrice)
SalePrice.transformed = BoxCox(df$SalePrice, lambda = -0.3307673)
df.modified = cbind(df[,c(1:9)], SalePrice.transformed)
modified.lin = lm(SalePrice.transformed ~ YearBuilt + YearRemodAdd + TotalBsmtSF + X1stFlrSF + X2ndFlrSF
                  + GarageArea + GrLivArea, data = df.modified)
bptest(modified.lin)

SalePrice.transformed = log(df[,10]) # Applying a concave function transformation to the response variable
df.modified = cbind(df[,c(1:9)], SalePrice.transformed)
modified.lin = lm(SalePrice.transformed ~ YearBuilt + YearRemodAdd + TotalBsmtSF + X1stFlrSF + X2ndFlrSF
                  + GarageArea + GrLivArea, data = df.modified)
df.modified = cbind(df.modified, resid(modified.lin))
colnames(df.modified)[11] = "Resid"
df.modified = subset(df.modified, df.modified$Resid < 0.2 & df.modified$Resid > -0.2)
modified.lin = lm(SalePrice.transformed ~ YearBuilt + YearRemodAdd + TotalBsmtSF + X1stFlrSF + X2ndFlrSF
                  + GarageArea + GrLivArea, data = df.modified)
plot(modified.lin)
bptest(modified.lin)

# Removing observations that appear to result in increased heteroscedasticity.


# Binning categorical variables
for (i in 1:nrow(df.modified)){
  if (df.modified[i,1] < 1900){
    df.modified[i,1] = 1
  }
  if (df.modified[i,1] >= 1900 & df.modified[i,1] < 1925){
    df.modified[i,1] = 2
  }
  if (df.modified[i,1] >= 1925 & df.modified[i,1] < 1950){
    df.modified[i,1] = 3
  }
  if (df.modified[i,1] >= 1950 & df.modified[i,1] < 1975){
    df.modified[i,1] = 4
  }
  if (df.modified[i,1] >= 1975 & df.modified[i,1] < 2000){
    df.modified[i,1] = 5
  }
  if (df.modified[i,1] >= 2000){
    df.modified[i,1] = 6
  }
}

for (i in 1:nrow(df.modified)){
  if (df.modified[i,2] < 1900){
    df.modified[i,2] = 1
  }
  if (df.modified[i,2] >= 1900 & df.modified[i,2] < 1925){
    df.modified[i,2] = 2
  }
  if (df.modified[i,2] >= 1925 & df.modified[i,2] < 1950){
    df.modified[i,2] = 3
  }
  if (df.modified[i,2] >= 1950 & df.modified[i,2] < 1975){
    df.modified[i,2] = 4
  }
  if (df.modified[i,2] >= 1975 & df.modified[i,2] < 2000){
    df.modified[i,2] = 5
  }
  if (df.modified[i,2] >= 2000){
    df.modified[i,2] = 6
  }
}

# Converting categorical variables to factors
df.modified$YearBuilt = as.factor(df.modified$YearBuilt)
df.modified$YearRemodAdd = as.factor(df.modified$YearRemodAdd)

# 5) INDEPENDENCE OF ERRORS: 
dwtest(lin) 
# The Durbin-Watson test returns a value of 1.977 with a p-value >0.1. Given this result, we can accept
# the null hypothesis that the true autocorrelation of error term's from the model is equal to 0 at a 95%
# confidence level. The true autocorrelation of the error terms from the model is thus NOT greater than
# 0 and thus the assumption that error terms from the model are independent of each other is satisfied.

# 6) NORMALITY OF ERRORS:
qqPlot(lin, main = 'Q-Q Plot w/ 95% Confidence Interval') 
# The Q-Q Plot suggests approximate normality among the standardized residuals for all theoretical
# quantiles between -3 and 2 with a 95% confidence level, although a deviation of values from the 
# reference line between quantiles 2 and 3 suggests some degree of a non-normal distribution for 
# residuals within that range at the same confidence level. The assumption that all random errors 
# from the model follow a normal distribution thus is NOT satisfied.

# OUTLIERS:
ols_plot_resid_stud(lin) 
# Many studentized residuals fall outside the threshold of -3 to 3, suggesting that there are 
# outlying observations in the data set that need to be dropped.

ols_plot_resid_stud(modified.lin)
modified.lin = lm(SalePrice.transformed ~ YearBuilt + YearRemodAdd + TotalBsmtSF + X1stFlrSF + X2ndFlrSF
                  + GarageArea + GrLivArea, data = df.modified)
df.modified = df.modified[c(1:622, 624:654, 656:663, 665:695, 697:713, 715:796,
                            798:1041, 1044:1202, 1204:1301, 1303:1367, 1369:1427,
                            1429:1460),]
df.modified = df.modified[c(1:136, 138:459, 461:470, 
                            472:567, 569:625, 627:647, 649:655, 657:667,
                            669:686, 688:704, 706:805, 807:962, 964:1047, 
                            1049:1053, 1055:1180, 1182:1307, 1309:1382,
                            1384:1395, 1397:1425, 1427:1460),]
modified.lin = lm(SalePrice.transformed ~ YearBuilt + YearRemodAdd + TotalBsmtSF + X1stFlrSF + X2ndFlrSF
                  + GarageArea + GrLivArea, data = df.modified)
ols_plot_resid_stud(modified.lin)

# HIGH LEVERAGE POINTS:
ols_plot_resid_lev(modified.lin)
# Many observations were found to have high leverage (see plot points in red and pink) and thus are
# determined to have a high impact on how the model's estimated regression line was fit. Analyzing
# the context of each observation found to have high leverage may be of value if aiming to optimize
# the fit/predictive power of the multiple linear regression model. Of note, the generated plot uses
# residuals (not studentized residuals) to determine outliers, which accounts for the discrepancy in
# outlying observations found between this plot and the studentized residuals plot from a previous line. 

# COLLINERAITY: 
vif(lin) # vif() was called to calculate the presence of collinearity among predictor variables in the
# regression model. Several predictor variables returned a variance inflation factor (VIF) of greater
# than 5 (X1stFlrSF, X2nsFlySF, GrLivArea), indicating the presence of collinearity among the implicated
# predictors. Dropping at least one of the collinear predictors or combining them into a single 
# predictor may be effective at mitigating collinearity in order to optimize the fit/predictive power 
# of the multiple linear regression model.

modified.lin = lm(SalePrice.transformed ~ YearBuilt + YearRemodAdd + TotalBsmtSF + X1stFlrSF
                  + GarageArea + GrLivArea, data = df.modified) # Dropping X2ndFlrSF from the regression model
vif(modified.lin) 
# No VIF > 5, thus indicating that multicollinearity is no longer being exhibited among the predictors

# OVERALL LIST OF ISSUES RELATED TO THE MODEL:
# - Assumption of Constant Variance NOT satisfied (heteroscedasticity is present in the regression model
# with a 99.9% confidence level)
# - Assumption of Normality NOT satisfied (based on the results of the Q-Q Plot, which suggested some
# degree of a non-normal distribution for residuals within the 2nd to 3rd quantile range at the 95% 
# confidence level)
# - Many outliers and high-leverage points found (based on the respective residual and studentized 
# residual plots)
# - Collinearity noted relative to several of the predictor variables included in the regression model
# based on their variance inflation factor


##### TESTING FOR MULTIVARIATE NORMAL #####

mvn(subset(df[,1:9], df$SalePrice >= median(df$SalePrice)), mvnTest = "hz", multivariatePlot = "qq")$multivariateNormality 
# Outputs the result of the Henze-Zirkler test of Multivariate normality. Considering the p-value, the 
# results indicate that values contained within the rows where SalePrice is greater than or equal to 
# the median of values in the column DO NOT follow a multivariate normal distribution with a 
# significance level of 0.05 Also output a Chi-Square Q-Q Plot, which exhibits that the Mahalanobis 
# Distance^2 metric for values begins to skew away from the reference line beginning roughly at the 
# 15th Chi-Square quantile, further validating the conclusion of the Henze-Zirkler test regarding the 
# absence of multivariate normal.

mvn(subset(df[,1:9], df$SalePrice < median(df$SalePrice)), mvnTest = "hz", multivariatePlot= "qq")$multivariateNormality 
# Outputs the result of the Henze-Zirkler test of Multivariate normality. Considering the p-value, the 
# results indicate that values contained within the rows where SalePrice is less than the median of 
# values in the column DO NOT follow a multivariate normal distribution with a significance level of 
# 0.05. Also outputs a Chi-Square Q-Q Plot, which exhibits that the Mahalanobis Distance^2 metric for 
# values begins to skew away from the reference line beginning roughly at the 18th Chi-Square quantile,
# further validating the conclusion of the Henze-Zirkler test regarding the absence of multivariate 
# normal.
