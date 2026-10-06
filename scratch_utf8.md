<center>
<img src="../images/fscampus_small2.png" width="1200"/>
</center>

<center>

# Investments

***Finance 2 - BFIN***

**Dr. Omer Cayirli**

Lecturer in Empirical Finance

omer_cayirli@uncbusiness.net
</center>

---

## Lecture 06

---


### Outline

*   Index Models and The Capital Asset Pricing Model
    
    *   The Single-Index Model
    
    *   The Capital Asset Pricing Model

Interactive examples require a live Python kernel and access to Yahoo Finance and Fama/French data.

---



### A Single-Factor Market

*   Advantages
    *   Reduces the number of inputs for diversification
        *   Without an index model, analyzing 50 stocks requires:
            
            $$[n = 50 \, \text{estimates of expected returns}] + [n = 50 \, \text{estimates of variances}]$$

            $$(n^2 – n)/2 = 1,225 \, \text{estimates of covariances} \quad \Rightarrow \quad 1,325 \, \text{total estimates}$$

        *   The single-index model uses 50 alphas, 50 betas, 50 firm-specific variances, and 2 market estimates (expected excess return and variance): 152 inputs, taking $r_f$ as given.
    

*   Model

    $r_i = E(r_i) + \text{unanticipated surprise}$

    $r_i = E(r_i) + \beta_i m + e_i$

    Here $m=R_M-E(R_M)$ is the unexpected market excess return, and $E(e_i)=0$.

---



### A Single-Factor Market

*   Let $R_i=r_i-r_f$ and $R_M=r_M-r_f$ be excess returns, with a fixed risk-free rate $r_f$.

*   Regression equation:
    $$R_i(t) = \alpha_i + \beta_i R_M(t) + e_i(t)$$
*   Expected return-beta relationship:
    $$E(R_i) = \alpha_i + \beta_i E(R_M)$$
*   Variance = Systematic risk + Firm-specific risk:
    $$\sigma_i^2 = \beta_i^2 \sigma_M^2 + \sigma^2(e_i)$$
*   Covariance = Product of betas $\times$ Market risk:
    $$\text{Cov}(R_i, R_j) = \beta_i \beta_j \sigma_M^2$$
*   Correlation =
    $$\text{Corr}(R_i, R_j) = \frac{\beta_i \beta_j \sigma_M^2}{\sigma_i \sigma_j} = \left(\frac{\beta_i\sigma_M}{\sigma_i}\right)\left(\frac{\beta_j\sigma_M}{\sigma_j}\right)$$
    $$= \text{Corr}(R_i, R_M) \times \text{Corr}(R_j, R_M)$$

---



### A Single-Factor Market

*   Some securities will be more sensitive than others to macroeconomic shocks.

*   The variance of returns attributable to the marketwide factor is called the systematic risk of the security.

*   The index model assumes $E(e_i\mid R_M)=0$ and $\text{Cov}(e_i,e_j)=0$ for $i\ne j$:
    
    *   The only source of covariance between any pair of securities is their common dependence on the market return.
    
    $$\text{Cov}(R_i, R_j) = \beta_i \beta_j \sigma_M^2$$
    
    $$\text{Corr}(R_i, R_j) = \text{Corr}(R_i, R_M) \times \text{Corr}(R_j, R_M)$$


---



### A Single-Factor Market

$$R_i(t) = \alpha_i + \beta_i R_M(t) + e_i(t)$$

$$E(R_i) = \alpha_i + \beta_i E(R_M)$$

*   $\alpha$ is the security's expected excess return when the market excess return is zero. It is the vertical intercept.

*   The slope of the line in the figure is the security's beta coefficient, $\beta_i$.

---



def show_comparative_analysis():
    # Keep this demonstration independent of other notebook cells.
    import yfinance as yf
    import pandas as pd
    import numpy as np
    import statsmodels.api as sm
    import pandas_datareader.data as web
    import matplotlib.pyplot as plt
    import ipywidgets as widgets
    from IPython.display import display, HTML, clear_output
    import datetime
    import warnings

    # --- 1. UI Widgets ---
    style = {'description_width': 'initial'}
    stock_widget = widgets.Text(value='AMZN', description='Stock Ticker:', style=style)
    market_widget = widgets.Text(value='^SP500TR', description='Market Index:', style=style)
    start_date_widget = widgets.DatePicker(description='Start Date:', value=datetime.date(2010, 1, 1))
    split_date_widget = widgets.DatePicker(description='Split Date:', value=datetime.date(2018, 1, 1))
    end_date_widget = widgets.DatePicker(description='End Date:', value=datetime.date(2024, 12, 31))
    run_button = widgets.Button(description="Run Comparative Analysis", button_style='success', icon='cogs')
    output_plots = widgets.Output()
    output_stats = widgets.Output()

    # --- 2. Core Analysis and Display Function ---
    def run_comparative_analysis(b=None):
        with output_plots: clear_output(wait=True)
        with output_stats: clear_output(wait=True)

        stock_ticker = stock_widget.value.upper()
        market_ticker = market_widget.value.upper()
        start, split, end = start_date_widget.value, split_date_widget.value, end_date_widget.value
    
        if not (stock_ticker and market_ticker and start and split and end and start < split < end):
            with output_plots: display(HTML("<p style='color:red;'>Error: Provide valid tickers and ensure Start < Split < End.</p>")); return

        if split.day != 1:
            with output_plots:
                display(HTML("<p style='color:red;'>Choose the first day of a month for the split; that month belongs to the second subsample.</p>"))
            return

        with output_plots: print(f"Downloading data for {stock_ticker} and {market_ticker} from {start} to {end}...")
        try:
            tickers = [stock_ticker, market_ticker]
            data = yf.download(tickers, start=start, end=end + datetime.timedelta(days=1), interval='1mo', auto_adjust=True, progress=False)['Close']
            data = data.rename(columns={col: col.upper() for col in data.columns})
            if stock_ticker not in data.columns or market_ticker not in data.columns or data[stock_ticker].isnull().all() or data[market_ticker].isnull().all():
                raise ValueError(f"Could not retrieve valid data for one or both tickers.")
            # Preserve missing calendar months before calculating monthly returns.
            data = data.sort_index()
            data.index = pd.DatetimeIndex(data.index).to_period('M')
            data = data[~data.index.duplicated(keep='last')]
            data = data.reindex(pd.period_range(data.index.min(), data.index.max(), freq='M'))
            data.index = data.index.to_timestamp()
            returns = data.pct_change(fill_method=None)
        
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", FutureWarning)
                ff = web.DataReader('F-F_Research_Data_Factors', 'famafrench', start=start, end=end)[0]
            rf = ff['RF'] / 100
        
            returns.index = returns.index.to_period('M').to_timestamp()
            if isinstance(rf.index, pd.PeriodIndex):
                 rf.index = rf.index.to_timestamp(how='start')

            merged_data = returns.join(rf.rename('RF'), how='inner')
            merged_data = merged_data[[stock_ticker, market_ticker, 'RF']].dropna()
            if merged_data.empty: raise ValueError("No overlapping data found between returns and risk-free rate after alignment.")
            excess_returns = merged_data[[stock_ticker, market_ticker]].subtract(merged_data['RF'], axis=0)
        except Exception as e:
            with output_plots: clear_output(wait=True); display(HTML(f"<p style='color:red;'>Data Error: {e}</p>")); return

        sub1_end = split - datetime.timedelta(days=1)
        sample_months = excess_returns.index.to_period('M')
        split_month = pd.Period(split, freq='M')
        sub1_returns = excess_returns.loc[sample_months < split_month]
        sub2_returns = excess_returns.loc[sample_months >= split_month]
    
        models = {}
        for i, ret_df in enumerate([sub1_returns, sub2_returns]):
            # --- FIX: Ensure data is perfectly aligned before regression ---
            ret_df = ret_df[[stock_ticker, market_ticker]].dropna()
            # --- End of FIX ---

            if len(ret_df) < 10: models[f'sub{i+1}'] = None; continue
            y = ret_df[stock_ticker]; X = sm.add_constant(ret_df[market_ticker])
            models[f'sub{i+1}'] = sm.OLS(y, X).fit()

        with output_stats:
            html_stats = ""
            for i, model in enumerate([models['sub1'], models['sub2']]):
                period = f"({start.year}-{sub1_end.year})" if i == 0 else f"({split.year}-{end.year})"
                title = f"<h4>Sub-sample {i+1} {period}</h4>"
                if model is None:
                    html_stats += f"<div style='flex:1; padding:0 10px;'>{title}<p style='color:orange;'>Insufficient data.</p></div>"; continue
                stats_df = pd.DataFrame({'Coefficient': model.params, 'Std. Error': model.bse, 't-stat': model.tvalues, 'p-value': model.pvalues}).rename(index={'const': 'Alpha', market_ticker: 'Beta'})
                summary_text = f"<b>R²:</b> {model.rsquared:.4f}, <b>Adj. R²:</b> {model.rsquared_adj:.4f}, <b>Obs:</b> {model.nobs:.0f}"
                html_stats += f"<div style='flex:1; padding:0 10px;'>{title}{stats_df.style.format('{:.4f}').to_html()}{summary_text}</div>"
            display(HTML(f"<div style='display:flex;'>{html_stats}</div>"))

        with output_plots:
            clear_output(wait=True)
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
        
            if not excess_returns.empty:
                x_min, x_max = excess_returns[market_ticker].min(), excess_returns[market_ticker].max()
                y_min, y_max = excess_returns[stock_ticker].min(), excess_returns[stock_ticker].max()
                x_pad = (x_max - x_min) * 0.1; y_pad = (y_max - y_min) * 0.1
                global_xlim = (x_min - x_pad, x_max + x_pad); global_ylim = (y_min - y_pad, y_max + y_pad)
            else:
                global_xlim, global_ylim = (-0.2, 0.2), (-0.4, 0.4)

            for i, (ax, model, ret_df) in enumerate(zip([ax1, ax2], [models['sub1'], models['sub2']], [sub1_returns, sub2_returns])):
                period = f"({start.year}-{sub1_end.year})" if i == 0 else f"({split.year}-{end.year})"
                ax.set_title(f'SCL for {stock_ticker} - Sub-sample {i+1} {period}', fontsize=12)
            
                # Use the cleaned dataframe for plotting as well
                ret_df = ret_df[[stock_ticker, market_ticker]].dropna()

                if model is None:
                    ax.text(0.5, 0.5, 'Insufficient Data', ha='center'); continue
                ax.scatter(ret_df[market_ticker], ret_df[stock_ticker], color='deepskyblue', s=15)
                x_values = ret_df[market_ticker].to_numpy()
                order = np.argsort(x_values)
                ax.plot(x_values[order], np.asarray(model.fittedvalues)[order], color='black', linewidth=1.5)
                ax.set_xlabel(f'{market_ticker} Excess Return'); ax.set_ylabel(f'{stock_ticker} Excess Return')
                ax.axhline(0, color='black', linewidth=0.75); ax.axvline(0, color='black', linewidth=0.75)
                ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x*100:.0f}%'))
                ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{y*100:.0f}%'))
                ax.grid(True, linestyle=':', alpha=0.6)
                ax.set_xlim(global_xlim); ax.set_ylim(global_ylim)
            
            plt.tight_layout(); plt.show()

    # --- 3. Assemble UI ---
    run_button.on_click(run_comparative_analysis)
    controls = widgets.VBox([widgets.HBox([stock_widget, market_widget]), widgets.HBox([start_date_widget, split_date_widget, end_date_widget]), widgets.HTML('Split on the first day of a month; that month starts the second subsample.'), run_button], layout=widgets.Layout(align_items='center'))
    display(widgets.VBox([controls, output_plots, output_stats]))
    run_comparative_analysis(None)

show_comparative_analysis()


---

### Single-Index Model: Portfolio Beta and Risk

The three stocks below are part of a broader market that satisfies the single-index model. Form a portfolio $P$ using their capitalizations as weights. The portfolio's beta relative to the market index is 1.

| Stock | Capitalization | Beta | Mean Excess Return | Standard Deviation |
| :----: | -------------: | ---: | -----------------: | -----------------: |
| Alpha | 3,000 | 1.1 | 9.0% | 35.0% |
| Beta | 1,800 | ??? | 4.0% | 25.0% |
| Gamma | 1,200 | 1.35 | 15.0% | 45.0% |

The standard deviation of the market index is 20%.

  a. What is the beta of Stock Beta? What is the mean excess return of portfolio $P$?

  b. What is the covariance between stocks Alpha and Beta?

  c. What is the covariance between Stock Beta and the market index?

  d. Break down the variance of Stock Beta into its systematic and firm-specific components.

$$
\text{Cov}(R_i, R_j) = \beta_i \beta_j \sigma_M^2
$$

$$
\sigma_i^2 = \beta_i^2 \sigma_M^2 + \sigma^2(e_i)
$$

---


### Single-Index Model: Portfolio Beta and Risk

$$
\text{Total Capitalization} = 3{,}000 + 1{,}800 + 1{,}200 = 6{,}000
$$

$$
w_A = \frac{3{,}000}{6{,}000}=0.50,\quad
w_B = \frac{1{,}800}{6{,}000}=0.30,\quad
w_C = \frac{1{,}200}{6{,}000}=0.20.
$$

Since portfolio $P$ has beta 1, its beta is the weighted average of its stocks' betas:

$$
1 = w_A\beta_A+w_B\beta_B+w_C\beta_C
  =0.50(1.1)+0.30\beta_B+0.20(1.35).
$$

$$
\beta_B=\frac{1-0.55-0.27}{0.30}=0.60.
$$

$$
E(R_P)=w_AE(R_A)+w_BE(R_B)+w_CE(R_C)
=0.50(9\%)+0.30(4\%)+0.20(15\%)=8.70\%.
$$

$$
\text{Cov}(R_A,R_B)=\beta_A\beta_B\sigma_M^2
=1.1(0.60)(0.20)^2=0.02640.
$$

$$
\text{Cov}(R_B,R_M)=\beta_B\sigma_M^2
=0.60(0.20)^2=0.02400.
$$

$$
\sigma_B^2=(0.25)^2=0.06250.
$$

$$
\text{Systematic variance}=\beta_B^2\sigma_M^2
=(0.60)^2(0.20)^2=0.01440.
$$

$$
\text{Firm-specific variance}=\sigma^2(e_B)
=\sigma_B^2-\beta_B^2\sigma_M^2
=0.06250-0.01440=0.04810.
$$

---


import numpy as np

# Data
cap_A, beta_A, ER_A, sigma_A = 3000, 1.1, 0.09, 0.35
cap_B, ER_B, sigma_B = 1800, 0.04, 0.25
cap_C, beta_C, ER_C, sigma_C = 1200, 1.35, 0.15, 0.45
sigma_M = 0.20

# Part (a): Weights, Beta B, and portfolio P's mean excess return
total_cap = cap_A + cap_B + cap_C
w_A = cap_A / total_cap
w_B = cap_B / total_cap
w_C = cap_C / total_cap
beta_B = (1 - w_A * beta_A - w_C * beta_C) / w_B
ER_P = w_A * ER_A + w_B * ER_B + w_C * ER_C
print(f"w_A: {w_A:.4f}, w_B: {w_B:.4f}, w_C: {w_C:.4f}")
print(f"Beta_B: {beta_B:.4f}")
print(f"ER_P: {ER_P * 100:.2f}%")

# Part (b): Cov(A,B)
cov_AB = beta_A * beta_B * sigma_M**2
print(f"Cov(A,B): {cov_AB:.5f}")

# Part (c): Cov(B,M)
cov_BM = beta_B * sigma_M**2
print(f"Cov(B,M): {cov_BM:.5f}")

# Part (d): Variance Breakdown B
var_B = sigma_B**2
systematic_B = beta_B**2 * sigma_M**2
firm_specific_B = var_B - systematic_B
print(f"Var_B: {var_B:.5f}")
print(f"Systematic_B: {systematic_B:.5f}")
print(f"Firm-Specific_B: {firm_specific_B:.5f}")

---

### Index Model Regression Equation

$$
R_i(t) = \alpha_i + \beta_i R_M(t) + e_i(t)
$$

Here $R_i(t)=r_i(t)-r_f(t)$ and $R_M(t)=r_M(t)-r_f(t)$; the S&P 500 total-return index can serve as the market index.

| Description | Symbol |
| :--- | :---: |
| The stock's expected excess return when the market excess return is zero (regression intercept) | $\alpha_i$ |
| The market component of the stock's excess return;<br>$\beta_i$ measures responsiveness to the market | $\beta_i R_M(t)$ |
| The unexpected component of return in any period due to unexpected events<br>that are relevant only to this security (firm specific) | $e_i$ |
| The variance attributable to the uncertainty of the common<br>macro-economic factor | $\beta_i^2 \sigma_M^2$ |
| The variance attributable to firm-specific uncertainty | $\sigma^2(e_i)$ |

---

def show_single_index_model():
    # Keep this demonstration independent of other notebook cells.
    # If needed, uncomment and run once:
    # %pip install -U yfinance curl_cffi pandas pandas-datareader numpy statsmodels matplotlib ipywidgets

    import yfinance as yf
    import pandas as pd
    import numpy as np
    import statsmodels.api as sm
    import pandas_datareader.data as web
    import ipywidgets as widgets
    from IPython.display import display, HTML, clear_output, Markdown
    import datetime
    import warnings

    # --- 1. UI Widgets ---
    style = {'description_width': 'initial'}
    stock_widget = widgets.Text(value='AMZN', description='Stock Ticker:', style=style)
    market_widget = widgets.Text(value='^SP500TR', description='Market Index:', style=style)
    start_date_widget = widgets.DatePicker(description='Start Date:', value=datetime.date(2010, 1, 1))
    end_date_widget = widgets.DatePicker(description='End Date:', value=datetime.date(2025, 12, 31))
    run_button = widgets.Button(description="Run Single-Index Model", button_style='success', icon='cogs')
    output_area = widgets.Output()

    # --- 2. Main Analysis and Display Function ---
    def run_single_index_model(b=None):
        with output_area:
            clear_output(wait=True)

            stock_ticker = stock_widget.value.upper()
            market_ticker = market_widget.value.upper()
            start, end = start_date_widget.value, end_date_widget.value
        
            if not (stock_ticker and market_ticker and start and end and start < end):
                display(HTML("<p style='color:red;'>Error: Provide valid tickers and a valid date range.</p>")); return

            print(f"Downloading data and running regression for {stock_ticker} vs. {market_ticker}...")
            try:
                tickers = [stock_ticker, market_ticker]
                end_date = end + datetime.timedelta(days=1)  # Yahoo's end date is exclusive.
                downloaded = yf.download(
                    tickers, start=start, end=end_date, interval='1mo',
                    group_by='ticker', auto_adjust=True, actions=False, progress=False
                )
                if downloaded.empty:
                    raise ValueError("yf.download returned an empty DataFrame.")

                # With auto_adjust=True, Close is the adjusted-close series.
                series = []
                for ticker in tickers:
                    if ticker in downloaded.columns.get_level_values(0):
                        ticker_data = downloaded[ticker]
                        if 'Close' in ticker_data.columns and ticker_data['Close'].notna().any():
                            series.append(ticker_data['Close'].rename(ticker))
                if len(series) != 2:
                    raise ValueError("Adjusted-close data are required for both tickers.")

                adjusted_close = pd.concat(series, axis=1).sort_index()[tickers]
                # Preserve missing calendar months before calculating monthly returns.
                adjusted_close = adjusted_close.sort_index()
                adjusted_close.index = pd.DatetimeIndex(adjusted_close.index).to_period('M')
                adjusted_close = adjusted_close[~adjusted_close.index.duplicated(keep='last')]
                adjusted_close = adjusted_close.reindex(pd.period_range(adjusted_close.index.min(), adjusted_close.index.max(), freq='M'))
                adjusted_close.index = adjusted_close.index.to_timestamp()
                returns = adjusted_close.pct_change(fill_method=None).dropna()
                if len(returns) < 12:
                    raise ValueError("At least 12 complete monthly returns are required.")
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore", FutureWarning)
                    ff = web.DataReader('F-F_Research_Data_Factors', 'famafrench', start=start, end=end)[0]
                rf = (ff['RF'].astype(float) / 100).rename('RF')
                returns.index = pd.DatetimeIndex(returns.index).to_period('M').to_timestamp()
                if isinstance(rf.index, pd.PeriodIndex):
                    rf.index = rf.index.to_timestamp(how='start')
                merged_data = returns.join(rf, how='inner').dropna()
                if len(merged_data) < 12:
                    raise ValueError("Fewer than 12 complete months remain after aligning assets and RF.")
                excess_returns = merged_data[tickers].subtract(merged_data['RF'], axis=0)
            
                y = excess_returns[stock_ticker]
                X = sm.add_constant(excess_returns[market_ticker])
                model = sm.OLS(y, X).fit()

                clear_output(wait=True)
            
                stats_summary = {'Multiple R': np.sqrt(model.rsquared), 'R-Square': model.rsquared, 'Adjusted R-Square': model.rsquared_adj, 'Standard Error': np.sqrt(model.mse_resid), 'Observations': int(model.nobs)}
                stats_df1 = pd.DataFrame(pd.Series(stats_summary, name=''))
            
                stats_df2 = pd.DataFrame({'Coefficients': model.params, 'Standard Error': model.bse, 't-statistic': model.tvalues, 'p-value': model.pvalues}).rename(index={'const': 'Intercept', market_ticker: 'Market index'})

                explanation_md = """
*   Adjusted R-square accounts for sample size and the number of predictors.
*   The regression standard error estimates the standard deviation of the residual, $e_i$. A higher value indicates more firm-specific return variation.
"""

                display(HTML(f"<h4>Regression statistics for {stock_ticker}</h4>"))
                display(stats_df1.style.format('{:.4f}', subset=pd.IndexSlice[:'Standard Error']))
                display(stats_df2.style.format('{:.4f}'))
                display(Markdown(explanation_md))

            except Exception as e:
                clear_output(wait=True)
                display(HTML(f"<p style='color:red;'>An error occurred: {e}</p>"))

    # --- 3. Assemble UI ---
    run_button.on_click(run_single_index_model)
    controls = widgets.VBox([widgets.HBox([stock_widget, market_widget]), widgets.HBox([start_date_widget, end_date_widget]), run_button], layout=widgets.Layout(align_items='center'))

    display(widgets.VBox([controls, output_area]))


show_single_index_model()


---

### Fifteen-stock index-model comparison

This comparison covers 15 Yahoo Finance tickers across 11 sectors. The following cell estimates the same regression measures from monthly adjusted prices and monthly risk-free rates. 

| Ticker | Company | Sector |
| :---: | :--- | :--- |
| MSFT | Microsoft | Technology |
| JPM | JPMorgan Chase | Financials |
| JNJ | Johnson & Johnson | Health care |
| XOM | ExxonMobil | Energy |
| KO | Coca-Cola | Consumer staples |
| UNP | Union Pacific | Industrials |
| AAPL | Apple | Technology |
| BAC | Bank of America | Financials |
| PFE | Pfizer | Health care |
| CVX | Chevron | Energy |
| MCD | McDonald's | Consumer discretionary |
| VZ | Verizon | Communication services |
| NEE | NextEra Energy | Utilities |
| PLD | Prologis | Real estate |
| SHW | Sherwin-Williams | Materials |

* The market series is the S&P 500 total-return index (`^SP500TR`). 
* Regression alpha, residual standard deviation, and the standard error of alpha are monthly figures. 
* Adjusted beta uses the simple shrinkage rule $\frac{2}{3}\hat\beta+\frac{1}{3}(1)$; it is not another regression estimate.

---


# If needed, uncomment and run once:
# %pip install -U yfinance curl_cffi pandas pandas-datareader numpy statsmodels ipywidgets

import datetime
import warnings
import numpy as np
import pandas as pd
import yfinance as yf
import statsmodels.api as sm
import pandas_datareader.data as web
import ipywidgets as widgets
from IPython.display import display, HTML, clear_output


def show_fifteen_stock_index_model():
    stocks = {
        'MSFT': ('Microsoft', 'Technology'),
        'JPM': ('JPMorgan Chase', 'Financials'),
        'JNJ': ('Johnson & Johnson', 'Health care'),
        'XOM': ('ExxonMobil', 'Energy'),
        'KO': ('Coca-Cola', 'Consumer staples'),
        'UNP': ('Union Pacific', 'Industrials'),
        'AAPL': ('Apple', 'Technology'),
        'BAC': ('Bank of America', 'Financials'),
        'PFE': ('Pfizer', 'Health care'),
        'CVX': ('Chevron', 'Energy'),
        'MCD': ("McDonald's", 'Consumer discretionary'),
        'VZ': ('Verizon', 'Communication services'),
        'NEE': ('NextEra Energy', 'Utilities'),
        'PLD': ('Prologis', 'Real estate'),
        'SHW': ('Sherwin-Williams', 'Materials'),
    }
    market_ticker = '^SP500TR'
    start_box = widgets.DatePicker(description='Start Date:', value=datetime.date(2010, 1, 1))
    end_box = widgets.DatePicker(description='End Date:', value=datetime.date(2025, 12, 31))
    run = widgets.Button(description='Run Fifteen-Stock Comparison', button_style='success')
    result = widgets.Output()

    def calculate(_=None):
        with result:
            clear_output(wait=True)
            start, end = start_box.value, end_box.value
            if not (start and end and start < end):
                display(HTML('<p style="color:red;">Enter a valid start and end date.</p>'))
                return
            try:
                tickers = list(stocks) + [market_ticker]
                # Yahoo excludes the end date; auto_adjust=True makes Close adjusted.
                downloaded = yf.download(
                    tickers, start=start, end=end + datetime.timedelta(days=1),
                    interval='1mo', group_by='ticker', auto_adjust=True,
                    actions=False, progress=False
                )
                if downloaded.empty:
                    raise ValueError('Yahoo returned no monthly prices.')
                prices = {}
                for ticker in tickers:
                    if ticker in downloaded.columns.get_level_values(0):
                        item = downloaded[ticker]
                        if 'Close' in item.columns and item['Close'].notna().any():
                            prices[ticker] = item['Close']
                missing = [ticker for ticker in tickers if ticker not in prices]
                if missing:
                    raise ValueError('Missing adjusted closes: ' + ', '.join(missing))

                prices = pd.DataFrame(prices).sort_index()
                prices.index = pd.DatetimeIndex(prices.index).to_period('M')
                prices = prices[~prices.index.duplicated(keep='last')]
                # Preserve missing calendar months before calculating monthly returns.
                prices = prices.reindex(pd.period_range(
                    prices.index.min(), prices.index.max(), freq='M'))
                returns = prices.pct_change(fill_method=None)
                with warnings.catch_warnings():
                    warnings.simplefilter('ignore', FutureWarning)
                    factors = web.DataReader(
                        'F-F_Research_Data_Factors', 'famafrench', start=start, end=end
                    )[0]
                rf = (factors['RF'].astype(float) / 100).rename('RF')
                rf.index = pd.PeriodIndex(rf.index, freq='M')
                aligned = returns.join(rf, how='inner').dropna()
                if len(aligned) < 24:
                    raise ValueError('At least 24 complete monthly observations are required.')
                market_excess = (aligned[market_ticker] - aligned['RF']).rename('Market')
                X = sm.add_constant(market_excess)
                rows = []
                for ticker, (company, sector) in stocks.items():
                    stock_excess = aligned[ticker] - aligned['RF']
                    fit = sm.OLS(stock_excess, X).fit()
                    beta = fit.params['Market']
                    rows.append({
                        'Ticker': ticker, 'Company': company, 'Sector': sector,
                        'Beta': beta, 'Alpha (monthly)': fit.params['const'],
                        'R-square': fit.rsquared, 'Residual SD (monthly)': np.sqrt(fit.mse_resid),
                        'SE beta': fit.bse['Market'], 'SE alpha': fit.bse['const'],
                        'Adjusted beta': (2 * beta + 1) / 3,
                    })
                table = pd.DataFrame(rows).set_index(['Ticker', 'Company', 'Sector'])
                display(HTML(
                    f'<p>{len(aligned)} monthly observations, '
                    f'{aligned.index.min()} to {aligned.index.max()}; '
                    f'market: {market_ticker}.</p>'
                ))
                display(table.style.format({
                    'Beta': '{:.3f}', 'Alpha (monthly)': '{:.2%}', 'R-square': '{:.3f}',
                    'Residual SD (monthly)': '{:.2%}', 'SE beta': '{:.3f}',
                    'SE alpha': '{:.2%}', 'Adjusted beta': '{:.3f}',
                }))
            except Exception as exc:
                display(HTML(f'<p style="color:red;">Data error: {exc}</p>'))

    run.on_click(calculate)
    display(widgets.VBox([widgets.HBox([start_box, end_box]), run, result]))


show_fifteen_stock_index_model()


### Covariance estimation and portfolio choice

* Mean-variance optimization requires a covariance matrix. 

    *   For $n$ stocks, estimating every variance and covariance directly requires $n(n+1)/2$ distinct entries. 
    
    *   Sampling error in these estimates can make optimal portfolio weights unstable.

*   The single-index model approximates cross-stock covariance as $\beta_i\beta_j\sigma_M^2$ and adds firm-specific variance to each stock's own variance. 
    *   This reduces the number of risk estimates, but assumes firm-specific shocks are uncorrelated.

*   The tradeoff is fewer noisy estimates against a more restrictive picture of how stocks move together.

---


def show_model_comparison():
    # Keep this demonstration independent of other notebook cells.
    import yfinance as yf
    import pandas as pd
    import numpy as np
    import statsmodels.api as sm
    import pandas_datareader.data as web
    from scipy.optimize import minimize
    from IPython.display import display, HTML, clear_output, Markdown
    import ipywidgets as widgets
    import matplotlib.pyplot as plt
    import datetime
    import warnings
    import io, base64

    ALL_TICKERS = ['AMD', 'AMZN', 'F', 'JPM', 'NVDA', 'PFE', 'TGT', 'XOM', 'WMT', 'VZ']
    start_date_widget = widgets.DatePicker(description='Start Date:', value=datetime.date(2010, 1, 1))
    end_date_widget = widgets.DatePicker(description='End Date:', value=datetime.date(2025, 12, 31))
    checkbox_widgets = {t: widgets.Checkbox(value=True, description=t, indent=False, layout=widgets.Layout(width='auto')) for t in ALL_TICKERS}
    allow_short_widget = widgets.Checkbox(value=False, description='Allow Short Selling')
    run_button = widgets.Button(description="Run Model Comparison", button_style='success', icon='cogs')
    output_area = widgets.Output()

    def optimize_frontier(mean_returns, cov_matrix, rf_rate, allow_short):
        if len(mean_returns) < 2: return None
        num_assets = len(mean_returns)
        initial_guess = np.array(num_assets * [1./num_assets])
        def portfolio_variance(w, cov): return w.T @ cov @ w
        def neg_sharpe(w, mean_ret, cov, rf):
            er = w.T @ mean_ret; std = np.sqrt(w.T @ cov @ w)
            return -(er - rf) / std if std > 1e-9 else 1e9
        constraints = ({'type': 'eq', 'fun': lambda w: np.sum(w) - 1})
        bounds = None if allow_short else tuple((0, 1) for _ in range(num_assets))
        opt_result = minimize(neg_sharpe, initial_guess, args=(mean_returns, cov_matrix, rf_rate), method='SLSQP', bounds=bounds, constraints=constraints)
        if not opt_result.success: return None
        opt_weights = opt_result.x
        opt_er = opt_weights @ mean_returns
        opt_std = np.sqrt(opt_weights.T @ cov_matrix @ opt_weights)
        opt_sharpe = (opt_er - rf_rate) / opt_std
        # Each covariance specification has its own global minimum-variance portfolio.
        solver_options = {'ftol': 1e-12, 'maxiter': 1000}
        gmvp = minimize(portfolio_variance, initial_guess, args=(cov_matrix,),
                        method='SLSQP', bounds=bounds, constraints=constraints,
                        options=solver_options)
        if not gmvp.success: return None
        gmvp_er = float(gmvp.x @ mean_returns)
        gmvp_std = np.sqrt(max(float(gmvp.fun), 0))
        lo, hi = float(mean_returns.min()), float(mean_returns.max())
        if np.isclose(lo, hi):
            # Equal means leave only the GMVP efficient.
            target_returns = np.array([gmvp_er])
        else:
            upper_return = max(hi, gmvp_er + (hi - lo)) if allow_short else hi
            target_returns = np.linspace(gmvp_er, upper_return, 50)
        frontier_std = [gmvp_std]
        for tr in target_returns[1:]:
            constraints_fr = [{'type': 'eq', 'fun': lambda w: np.sum(w)-1},
                              {'type': 'eq', 'fun': lambda w: w.T @ mean_returns - tr}]
            res = minimize(portfolio_variance, gmvp.x, args=(cov_matrix,),
                           method='SLSQP', bounds=bounds, constraints=constraints_fr,
                           options=solver_options)
            frontier_std.append(np.sqrt(max(float(res.fun), 0)) if res.success else np.nan)
        return {'weights': opt_weights, 'er': opt_er, 'std': opt_std, 'sharpe': opt_sharpe,
                'gmvp_return': gmvp_er, 'frontier_stds': np.array(frontier_std),
                'frontier_returns': target_returns}

    def run_comparison(b=None):
        with output_area:
            clear_output(wait=True)
            selected_tickers = [t for t, cb in checkbox_widgets.items() if cb.value]
            allow_short = allow_short_widget.value
            market_ticker = '^SP500TR'
            start, end = start_date_widget.value, end_date_widget.value
            if len(selected_tickers) < 2 or start is None or end is None or start >= end:
                display(HTML("<p style='color:red;'>Error: Select at least 2 assets and a valid date range.</p>")); return
            print("Downloading data...")
            try:
                all_tickers_dl = list(set(selected_tickers + [market_ticker]))
                data = yf.download(all_tickers_dl, start=start, end=end + datetime.timedelta(days=1), interval='1mo', auto_adjust=True, progress=False)['Close']
                # Preserve missing calendar months before calculating monthly returns.
                data = data.sort_index()
                data.index = pd.DatetimeIndex(data.index).to_period('M')
                data = data[~data.index.duplicated(keep='last')]
                data = data.reindex(pd.period_range(data.index.min(), data.index.max(), freq='M'))
                data.index = data.index.to_timestamp()
                returns = data.pct_change(fill_method=None)
                if market_ticker not in returns.columns:
                    raise ValueError(f"Market proxy {market_ticker} not found.")
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore", FutureWarning)
                    ff = web.DataReader('F-F_Research_Data_Factors', 'famafrench', start=start, end=end)[0]
                returns.index = returns.index.to_period('M').to_timestamp()
                ff.index = ff.index.to_timestamp(how='start')
                rf_series = (ff['RF'] / 100)
                aligned_returns = returns.join(rf_series).dropna()
                if aligned_returns.empty: raise ValueError("No valid overlapping data after aligning returns and risk-free rate.")
                market_excess = aligned_returns[market_ticker] - aligned_returns['RF']
                stock_excess = aligned_returns[selected_tickers].subtract(aligned_returns['RF'], axis=0)
            except Exception as e:
                display(HTML(f"<p style='color:red;'>Data Error: {e}</p>")); return
        
            print("Running optimizations...")
            full_cov_matrix = stock_excess.cov()
            mean_excess_returns = stock_excess.mean()
            full_cov_results = optimize_frontier(mean_excess_returns, full_cov_matrix, 0, allow_short)

            betas, alphas, resid_vars = {}, {}, {}
            X = sm.add_constant(market_excess)
            X.columns = ['const', 'MKT']
            for stock in stock_excess.columns:
                temp_df = pd.concat([stock_excess[stock], X['MKT']], axis=1).dropna()
                if len(temp_df) < 10: continue
                y_reg = temp_df[stock]
                X_reg = sm.add_constant(temp_df['MKT'])
                model = sm.OLS(y_reg, X_reg).fit()
                alphas[stock] = model.params['const']; betas[stock] = model.params['MKT']; resid_vars[stock] = model.mse_resid
        
            betas, alphas, resid_vars = pd.Series(betas), pd.Series(alphas), pd.Series(resid_vars)
            if betas.empty:
                display(HTML("<p style='color:orange;'>Could not estimate betas for any selected stock.</p>")); return
            
            index_model_cov = pd.DataFrame(np.outer(betas, betas) * market_excess.var() + np.diag(resid_vars), index=betas.index, columns=betas.index)
            mean_excess_returns_im = alphas + betas * market_excess.mean()
            index_model_results = optimize_frontier(mean_excess_returns_im, index_model_cov, 0, allow_short)
        
            clear_output(wait=True)
            if index_model_results is None or full_cov_results is None:
                display(HTML("<p style='color:orange;'>Optimization failed. Try different assets or a longer period.</p>")); return
        
            weights_index = pd.Series(index_model_results['weights'], index=betas.index)
            weights_full = pd.Series(full_cov_results['weights'], index=stock_excess.columns).reindex(betas.index)
            weights_df = pd.DataFrame({'Index Model': weights_index, 'Full-Covariance Model': weights_full})
        
            stats_data = {'Index Model': [index_model_results['er'], index_model_results['std'], index_model_results['sharpe']], 'Full-Covariance Model': [full_cov_results['er'], full_cov_results['std'], full_cov_results['sharpe']]}
            stats_df = pd.DataFrame(stats_data, index=['Risk premium', 'Standard deviation', 'Sharpe ratio'])
            table_html = "<h4>A. Weights in Optimal Risky Portfolio</h4>" + weights_df.style.format('{:.2%}').to_html()
            table_html += "<h4>B. Portfolio Characteristics</h4>" + stats_df.style.format('{:.4f}').to_html()
        
            fig, ax = plt.subplots(figsize=(7, 6))
            m1 = np.isfinite(index_model_results['frontier_stds']); m2 = np.isfinite(full_cov_results['frontier_stds'])
            ax.plot(index_model_results['frontier_stds'][m1], index_model_results['frontier_returns'][m1], color='black', marker='d', markersize=4, label='Index Model')
            ax.plot(full_cov_results['frontier_stds'][m2], full_cov_results['frontier_returns'][m2], color='deepskyblue', marker='s', markersize=4, label='Full Covariance Model')
            ax.set_xlabel('Standard Deviation'); ax.set_ylabel('Risk Premium'); ax.set_title('Efficient Frontier Comparison')
            ax.legend(); ax.grid(True, linestyle=':', alpha=0.7)
            buf = io.BytesIO(); plt.savefig(buf, format='png'); buf.seek(0)
            img_str = base64.b64encode(buf.read()).decode('utf-8'); plt.close(fig); buf.close()
            plot_html = f'<img src="data:image/png;base64,{img_str}"/>'
        
            explanation_md = """
*   Is the index model inferior to the full-blown Markowitz model?
    *   It imposes additional assumptions that may not be fully accurate.
    *   The Markowitz model allows far more flexibility in modeling asset covariance structure.
    *   Estimating the covariances with a sufficient degree of accuracy is an issue.
"""
        
            display(HTML(f"<div style='display:flex; align-items: flex-start;'><div style='flex:1; padding-right:20px;'>{table_html}</div><div style='flex:1;'>{plot_html}</div></div>"))
            display(Markdown(explanation_md))

    run_button.on_click(run_comparison)
    date_controls = widgets.HBox([start_date_widget, end_date_widget])
    all_checkboxes = list(checkbox_widgets.values()); midpoint = len(all_checkboxes) // 2
    checkbox_grid = widgets.VBox([widgets.HBox(all_checkboxes[:midpoint]), widgets.HBox(all_checkboxes[midpoint:])])
    asset_controls = widgets.VBox([widgets.Label("Select Assets:"), checkbox_grid, allow_short_widget])
    ui = widgets.VBox([date_controls, asset_controls, run_button], layout=widgets.Layout(align_items='center'))

    display(widgets.VBox([ui, output_area]))
    run_comparison(None)

show_model_comparison()


---

### The Capital Asset Pricing Model (CAPM)

* Portfolio theory identifies preferred portfolios given expected returns, variances, and covariances. 

* CAPM asks which expected returns are consistent with investors choosing portfolios and markets clearing.

* Under CAPM's common expectations and common risk-free rate, every investor combines the risk-free asset with the same tangency portfolio; risk aversion determines the mix. 
    *   Since aggregate risky holdings must equal market supply, this tangency portfolio is the value-weighted market portfolio of all traded risky assets. 
    
    * Under these assumptions, the market portfolio is mean-variance efficient.

---


### The Capital Asset Pricing Model (CAPM)

**Assumptions**

* Investors share a planning horizon and expectations about returns, variances, and covariances, and choose mean-variance optimal portfolios.
* They can borrow or lend without limit at the risk-free rate $r_f$.
* Assets are tradable and divisible; markets are competitive, with no taxes, transaction costs, or short-sale restrictions.

**Main result**

For total returns $r_i$ and $r_M$:

$$E(r_i)=r_f+\beta_i[E(r_M)-r_f].$$

The expected risk premium of security $i$ is $\beta_i$ times the expected market risk premium. Using the earlier excess-return notation $R_i=r_i-r_f$ and $R_M=r_M-r_f$, this is $E(R_i)=\beta_i E(R_M)$.

**Beta**

$$\beta_i=\frac{\operatorname{Cov}(r_i,r_M)}{\operatorname{Var}(r_M)}=\frac{\sigma_i\rho_{i,M}}{\sigma_M}.$$

---


### The Capital Asset Pricing Model: Security Market Line (SML)

*   Plots the expected return of assets against their beta.

*   In CAPM equilibrium, correctly priced assets lie on the SML; points above or below it have nonzero alpha.


<img src = "../figures/lecture_06_security_market_line.png" width="540">

*   SML vs CML
    *   SML
        *   Shows systematic risk only
        *   Correctly priced securities and portfolios lie on the SML
    *   CML
        *   Relates expected return to total volatility
        *   Efficient portfolios combining the risk-free asset and the market portfolio lie on the CML

---



### From the Tangency Portfolio to the Market Portfolio

<img src="../figures/lecture_06_cal_to_cml.png" width="1000">

* $P$ is the optimal risky portfolio where the CAL is tangent to the efficient frontier. 

* Under CAPM assumptions, market clearing identifies this common tangency portfolio as $M$: $P=M$, and CAL($P$) becomes the CML.

---


### Total Risk and Systematic Risk

<img src="../figures/lecture_06_cml_vs_sml.png" width="1100">

*   The same hypothetical stocks have unchanged expected returns in both panels. 

*   Total volatility includes diversifiable risk; CAPM rewards exposure to market risk, measured by beta. 

---


### CAPM: covariance and the risk premium

* The market risk premium depends on market variance and the effective aggregate risk-aversion coefficient $\bar A$:
  $$E(R_M)=\bar A\sigma_M^2.$$

* Security $i$ contributes $w_i\operatorname{Cov}(R_i,R_M)$ to market variance, where $w_i$ is its market weight:
  $$\operatorname{Cov}(R_i,R_M)=\sum_j w_j\operatorname{Cov}(R_i,R_j).$$

* In CAPM equilibrium, the expected premium compensates this covariance risk at the market's rate:
  $$E(R_i)=\frac{E(R_M)}{\sigma_M^2}\operatorname{Cov}(R_i,R_M)=\beta_i E(R_M).$$

Since $R_i=r_i-r_f$, the expected total return is:
$$E(r_i)=r_f+\beta_i[E(r_M)-r_f].$$

---


### CAPM: a numerical example

For Gamma from the preceding figure, use the following inputs for the same period:

| $r_f$ | $E(r_M)$ | $\sigma_M$ | $\sigma_\Gamma$ | $\rho_{\Gamma,M}$ |
| :---: | :---: | :---: | :---: | :---: |
| 2% | 9% | 16% | 20% | 0.52 |

What expected return does CAPM imply for Gamma?

$$E(R_M)=9\%-2\%=7\%,\qquad \sigma_M^2=(0.16)^2=0.0256.$$

$$\operatorname{Cov}(R_\Gamma,R_M)=0.52(0.20)(0.16)=0.01664
\quad\Rightarrow\quad \beta_\Gamma=\frac{0.01664}{0.0256}=0.65.$$

$$E(R_\Gamma)=\frac{0.07}{0.0256}(0.01664)=0.65(7\%)=4.55\%.$$

$$E(r_\Gamma)=2\%+4.55\%=6.55\%.$$

Gamma has higher total volatility than the market, but a lower expected return because its beta is only 0.65.

---


### CAPM for portfolios

For a fully invested portfolio, $\sum_i w_i=1$. Expected returns and betas are weighted averages:

$$E(r_P)=\sum_i w_i E(r_i),\qquad \beta_P=\sum_i w_i\beta_i.$$

If the component assets satisfy CAPM, so does the portfolio:

$$E(r_P)=\sum_i w_i\left[r_f+\beta_i(E(r_M)-r_f)\right]
=r_f+\beta_P[E(r_M)-r_f].$$

The market portfolio has beta one:

$$\beta_M=\frac{\operatorname{Cov}(r_M,r_M)}{\operatorname{Var}(r_M)}
=\frac{\sigma_M^2}{\sigma_M^2}=1.$$

---


### The SML and alpha

<img src="../figures/lecture_06_sml_slope_alpha.png" width="1100">

* Alpha is the difference between a security's expected return and the return required by CAPM:
  $$E(r_i)-r_f=\alpha_i+\beta_i[E(r_M)-r_f].$$
* A security above the SML has positive alpha; one below it has negative alpha. CAPM equilibrium implies $\alpha_i=0$.

In the figure:
$$E(r_{\text{stock}})_{\text{CAPM}}=6\%+1.2(14\%-6\%)=15.6\%,
\qquad \alpha=17\%-15.6\%=1.4\text{ percentage points}.$$

---


### Cost of Capital

* The Equity Cost of Capital
    * Best expected return available in the market on investments with similar risk.
    * Under the CAPM?
        * Investments have similar risk if they have the same sensitivity to market risk, as measured by their beta with the market portfolio.

* The Market Portfolio
    * Value-weighted vs. equal-weighted
    * S&P 500, DJIA, Nasdaq Composite, S&P 1500 Composite, Russell 2000, Wilshire 5000.

* The Market Risk Premium
    * Risk-Free Rate: Maturity vs. investment horizon
    * The Risk Premium
        * Historical
        * Expected
<style>
  .returns-table {
    border-collapse: collapse;
    width: auto;
    margin: 1em 0;
    font-family: Arial, sans-serif;
    color: white;
    background-color: #003366;
    border: 1px solid #FFFFFF;
  }
  .returns-table th, .returns-table td {
    border: 1px solid #FFFFFF;
    padding: 8px 10px;
    text-align: left;
  }
  .returns-table th {
    background-color: #D3D3D3;

    color: #4A4A4A;
    font-weight: bold;
    text-align: center;
  }
  .returns-table td.metric {
    font-weight: normal;
  }
  .returns-table td.value {
    text-align: right;
    font-weight: bold;
  }
  .returns-table tr.premium td.metric {
    font-weight: bold;
  }
  .returns-table caption {
    caption-side: bottom;
    font-size: 0.9em;
    color: #A9A9A9;
    padding-top: 8px;
    text-align: center;
  }
</style>

<table class="returns-table">
  <thead>
    <tr>
      <th>Metric</th>
      <th>Arithmetic Average Annual Return (1928–2025)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="metric">S&P 500 Total Return (incl. dividends)</td>
      <td class="value">11.86%</td>
    </tr>
    <tr>
      <td class="metric">3-Month Treasury Bill Return</td>
      <td class="value">3.42%</td>
    </tr>
    <tr class="premium">
      <td class="metric">Equity Risk Premium vs. T-Bill</td>
      <td class="value">8.44%</td>
    </tr>
    <tr>
      <td class="metric">10-Year Treasury Bond Return</td>
      <td class="value">4.82%</td>
    </tr>
    <tr class="premium">
      <td class="metric">Equity Risk Premium vs. 10-Yr Bond</td>
      <td class="value">7.03%</td>
    </tr>
  </tbody>
</table>

Risk premiums are calculated before rounding the averages, so displayed values may differ by 0.01 percentage point.

[Source: NYU Stern, Historical Returns (Damodaran)](https://pages.stern.nyu.edu/adamodar/New_Home_Page/datafile/histretSP.html)

---



### The Capital Asset Pricing Model

*   Beta Estimation
    
    *   Using Historical Returns
    
        *   What is the assumption?
    
    *   Best-fitting line
    
        *   Beta corresponds to the slope of the best-fitting line in the plot of the security's excess returns vs. the market excess return.
    
    *   Linear Regression
    $$ R_i(t) = \alpha_i + \beta_i R_M(t) + e_i(t) $$

---



# If needed, uncomment and run once, then restart the kernel:
# %pip install -U yfinance curl_cffi numpy pandas pandas-datareader matplotlib statsmodels ipywidgets

import datetime
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import yfinance as yf
import pandas_datareader.data as web
import statsmodels.api as sm
import ipywidgets as widgets
from IPython.display import display, clear_output, HTML


def show_beta_estimation_tool():
    # Keep this cell's controls independent of widgets in other cells.
    style = {'description_width': '80px'}
    date_layout = widgets.Layout(width='220px')
    start_box = widgets.DatePicker(
        description='Start Date:', value=datetime.date(2015, 1, 1),
        style=style, layout=date_layout)
    end_box = widgets.DatePicker(
        description='End Date:', value=datetime.date(2025, 12, 31),
        style=style, layout=date_layout)
    run_button = widgets.Button(
        description='Fetch Data & Plot Betas', button_style='success', icon='cogs',
        layout=widgets.Layout(width='auto', min_width='200px', margin='10px 0 0 0'))
    output_plots = widgets.Output()
    output_stats = widgets.Output()
    stock_symbols = ['AMZN', 'CSCO', 'XOM', 'TSLA']
    market_ticker = '^SP500TR'
    min_obs = 12

    summary_css = """
    <style>
    .beta-regression-summary table {
        width: auto; margin: 0 0 15px 0; border-collapse: collapse;
        font-family: Arial, sans-serif; font-size: 0.85em; text-align: right;
    }
    .beta-regression-summary th, .beta-regression-summary td {
        border: 1px solid #D3D3D3; padding: 4px 6px;
    }
    .beta-regression-summary th { background-color: #f0f0f0; text-align: center; }
    .beta-regression-summary caption {
        margin-bottom: 0.5em; font-weight: bold; font-size: 1.1em;
    }
    </style>
    """

    def fetch_calculate_and_plot(_=None):
        with output_stats:
            clear_output(wait=True)
        with output_plots:
            clear_output(wait=True)
            start, end = start_box.value, end_box.value
            if start is None or end is None or start >= end:
                display(HTML("<p style='color:red;'>Enter a start date before the end date.</p>"))
                return

            run_button.disabled = True
            try:
                print(f"Downloading monthly adjusted prices: {start} to {end}...")
                tickers = stock_symbols + [market_ticker]
                downloaded = yf.download(
                    tickers, start=start, end=end + datetime.timedelta(days=1),
                    interval='1mo', auto_adjust=True, group_by='ticker',
                    progress=False, actions=False)
                if downloaded is None or downloaded.empty:
                    raise ValueError('Yahoo returned no adjusted-close data.')
                series = {}
                for ticker in tickers:
                    if ticker in downloaded.columns.get_level_values(0):
                        item = downloaded[ticker]
                        if 'Close' in item and item['Close'].notna().any():
                            series[ticker] = item['Close']
                if market_ticker not in series:
                    raise ValueError(f'Market data unavailable for {market_ticker}.')

                prices = pd.DataFrame(series).sort_index()
                prices.index = pd.DatetimeIndex(prices.index).to_period('M')
                prices = prices[~prices.index.duplicated(keep='last')]
                # Preserve missing calendar months and never fill missing prices.
                prices = prices.reindex(pd.period_range(
                    prices.index.min(), prices.index.max(), freq='M'))
                returns = prices.pct_change(fill_method=None).replace([np.inf, -np.inf], np.nan)

                print('Downloading monthly Fama/French risk-free returns...')
                with warnings.catch_warnings():
                    warnings.simplefilter('ignore', FutureWarning)
                    factors = web.DataReader(
                        'F-F_Research_Data_Factors', 'famafrench',
                        start=start, end=end)[0]
                if factors.empty or 'RF' not in factors:
                    raise ValueError('Monthly risk-free data are unavailable.')
                rf = (pd.to_numeric(factors['RF'], errors='coerce') / 100).rename('RF')
                rf.index = pd.PeriodIndex(rf.index, freq='M')

                # Each stock uses its own overlap with the market and monthly RF.
                regressions, skipped = {}, []
                for ticker in stock_symbols:
                    if ticker not in returns:
                        skipped.append(f'{ticker}: no adjusted prices')
                        continue
                    paired = returns[[ticker, market_ticker]].join(rf, how='inner').dropna()
                    if len(paired) < min_obs:
                        skipped.append(f'{ticker}: fewer than {min_obs} aligned monthly returns')
                        continue
                    x = (paired[market_ticker] - paired['RF']).rename('Market excess return')
                    y = (paired[ticker] - paired['RF']).rename('Stock excess return')
                    if np.ptp(x.to_numpy()) < 1e-12:
                        skipped.append(f'{ticker}: market excess return has no variation')
                        continue
                    model = sm.OLS(y, sm.add_constant(x, has_constant='add')).fit()
                    regressions[ticker] = (x, y, model)
                if not regressions:
                    raise ValueError('No stocks can be estimated. ' + '; '.join(skipped))

                clear_output(wait=True)
                if skipped:
                    print('Skipped: ' + '; '.join(skipped))
                all_x = np.concatenate([item[0].to_numpy() for item in regressions.values()])
                x_lo, x_hi = min(all_x.min(), 0), max(all_x.max(), 0)
                x_pad = max((x_hi-x_lo)*0.08, 0.005)
                common_x_limits = (x_lo-x_pad, x_hi+x_pad)
                ncols, nrows = 2, (len(regressions)+1)//2
                summaries = []

                with plt.rc_context({
                    'axes.grid': True, 'grid.linestyle': ':', 'grid.alpha': 0.3,
                    'axes.edgecolor': '#DDDDDD', 'axes.linewidth': 0.6,
                    'font.family': 'DejaVu Sans',
                }):
                    fig, axes = plt.subplots(
                        nrows, ncols, figsize=(7.5*ncols, 6*nrows), squeeze=False)
                    for ax, (ticker, (x, y, model)) in zip(axes.flat, regressions.items()):
                        alpha_est = model.params['const']
                        beta_est = model.params['Market excess return']
                        ax.scatter(x, y, color='#1f77b4', s=35, alpha=0.5,
                                   label='Monthly observations')
                        x_line = np.linspace(x.min(), x.max(), 100)
                        ax.plot(x_line, alpha_est + beta_est*x_line, color='#8B0000',
                                lw=1.5, label='Fitted line (SCL)')
                        ax.set_xlabel('Market excess return', fontsize=10)
                        ax.set_ylabel('Stock excess return', fontsize=10)
                        ax.set_title(
                            f'{ticker} | {x.index.min()} to {x.index.max()} | n={len(x)}',
                            fontsize=11)
                        ax.set_xlim(common_x_limits)
                        all_y = np.r_[y.to_numpy(), model.fittedvalues.to_numpy(), 0.0]
                        y_lo, y_hi = all_y.min(), all_y.max()
                        y_pad = max((y_hi-y_lo)*0.1, 0.005)
                        ax.set_ylim(y_lo-y_pad, y_hi+y_pad)
                        ax.xaxis.set_major_formatter(PercentFormatter(1))
                        ax.yaxis.set_major_formatter(PercentFormatter(1))
                        ax.tick_params(labelsize=9)
                        ax.legend(loc='lower right', fontsize=9, framealpha=0.8)
                        annotation = (
                            f'Monthly alpha = {alpha_est:.2%}\n'
                            f'Beta = {beta_est:.2f}\n'
                            f'$R^2$ = {model.rsquared:.2f}')
                        ax.text(.04, .96, annotation, transform=ax.transAxes,
                                fontsize=9, va='top',
                                bbox={'boxstyle':'round,pad=0.4', 'fc':'#F0E68C',
                                      'alpha':.85, 'edgecolor':'#BDB76B'})
                        summary = model.summary(
                            title=f'{ticker} vs {market_ticker}: {x.index.min()} to {x.index.max()}')
                        summaries.append(
                            "<div class='beta-regression-summary'>" + summary.as_html() + '</div>')
                    for ax in axes.flat[len(regressions):]:
                        fig.delaxes(ax)
                    fig.suptitle(
                        f'Cost of Capital: Beta Estimation\nMonthly excess returns | '
                        f'{start.isoformat()} to {end.isoformat()}', fontsize=16)
                    fig.tight_layout(rect=[0, 0.02, 1, 0.94])
                    display(fig)
                    plt.close(fig)
                with output_stats:
                    display(HTML(summary_css + ''.join(summaries)))
            except Exception as exc:
                clear_output(wait=True)
                display(HTML(f"<p style='color:red;'>Analysis could not be completed: {exc}</p>"))
            finally:
                run_button.disabled = False

    run_button.on_click(fetch_calculate_and_plot)
    date_inputs = widgets.HBox(
        [start_box, end_box],
        layout=widgets.Layout(justify_content='center', margin='0 0 10px 0'))
    controls = widgets.VBox(
        [date_inputs, run_button], layout=widgets.Layout(align_items='center'))
    return widgets.VBox([
        widgets.HTML("<h2 style='text-align:center;'>Cost of Capital: Beta Estimation Tool</h2>"),
        controls, output_plots, widgets.HTML("<hr style='margin:20px 0;'>"), output_stats])


display(show_beta_estimation_tool())


---

### The Capital Asset Pricing Model

*   Historical Betas
    $$r_{i,t}^e = \alpha_i + \beta_i r_{M,t}^e + \epsilon_{i,t}$$
    $$\text{S.E.}(\hat{\beta}_i) = \frac{\sqrt{1-R^2}}{\sqrt{T-2}} \frac{\hat{\sigma}_i}{\hat{\sigma}_M}$$

    Here $T$ is the number of observations; the formula uses sample standard deviations and conventional OLS standard errors with an intercept.

*   The precision of an OLS beta estimate can be increased by

    *   Increasing the number of observations (T),

    *   By using portfolios instead of individual securities,

    *   By increasing the frequency of return observations

---



### The Capital Asset Pricing Model

*   Should idiosyncratic risk matter for pricing?

*   Would you ever buy a stock with negative expected returns?

*   How do the betas add up?

*   Can you arbitrage stocks that are on the SML? Not on the SML?

*   A stock's beta stays the same, but its firm-specific volatility rises. 

    *   Does its CAPM expected return change? 
    
    *   Could its effect on a concentrated portfolio's risk change?

---



### Question 1

Markowitz portfolio construction uses the full covariance matrix, including each stock's total variance. Yet CAPM links a stock's expected return to its beta, not its total volatility.

Why can firm-specific risk affect portfolio choice without earning a risk premium in CAPM equilibrium? Explain the role of diversification and the market portfolio.

---


### Question 2

An analyst regresses the monthly excess returns of Gamma and Delta on the market's monthly excess returns. The regressions have $R_\Gamma^2=0.80$ and $R_\Delta^2=0.20$.

* What do these $R^2$ values tell us about each stock's historical relationship with the market? 

* Can we infer which stock has a higher CAPM expected return, is easier to forecast, or would diversify an existing portfolio more? 

* What additional information would we need?

---


### Question 3

An analyst regresses Lambda's monthly excess returns on the market's monthly excess returns. For the same sample, the regression reports:

*   Beta ($\beta_\Lambda$) = 1.4
*   Alpha ($\alpha_\Lambda$) = 2.0%
*   R-squared ($R^2$) = 0.49
*   Standard deviation of the market's excess returns ($\sigma_M$) = 20%

a. What is the standard deviation of Lambda's excess returns?

b. What is the covariance between Lambda's and the market's excess returns?

c. What is their correlation? Explain its sign.

---


### Question 4

An analyst estimates single-index regressions of Theta's and Sigma's excess returns on the market's excess return $R_M$. All figures use the same return period, and the two stocks' residuals are uncorrelated.

| Stock | Alpha ($\alpha$) | Beta ($\beta$) | Residual standard deviation ($\sigma_e$) |
| :--- | ---: | ---: | ---: |
| Theta | 1.5% | 1.2 | 8% |
| Sigma | -0.5% | 0.8 | 6% |

The market's expected excess return is 8%, and its standard deviation is 20%. Portfolio $P$ holds 50% in each stock.

a. What is each stock's expected excess return?

b. What is the covariance between the two stocks' excess returns?

c. What are portfolio $P$'s alpha, beta, and residual standard deviation?

---


### Question 5

You are evaluating Stock Kappa using CAPM and considering a risky portfolio that combines Kappa with the market. All inputs refer to the same period. Assume Kappa's firm-specific return is uncorrelated with the market.

* Kappa's beta: 1.5
* Kappa's residual standard deviation: 15%
* Your forecast for Kappa's total return: 16%
* Your forecast for the market's total return: 10%
* The market's standard deviation: 20%
* The risk-free rate: 2%

a. What return does CAPM require for Kappa?

b. What is Kappa's alpha based on your forecast?

c. What weights in Kappa and the market maximize the risky portfolio's Sharpe ratio? The weights must sum to one.

d. What is the beta of this portfolio?

e. An analyst claims that a portfolio with a beta above 1 must have a lower Sharpe ratio than the market. Calculate both Sharpe ratios and assess the claim.

---


### What is next?

*   Multifactor Models
*   Arbitrage Pricing Theory
*   Reading(s): BKM Ch. 10
*   Suggested Problems
    *   Ch.8: 6, 9-12
    *   Ch.9: 2, 4, 8, 17-19, 21.
    *   Ch.9-CFA Problems: 1-2, 8-9,12.

---
