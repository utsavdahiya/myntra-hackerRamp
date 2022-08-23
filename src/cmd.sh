#!/usr/bin/env bash
curl --location --request POST 'https://www.myntra.com/gateway/v2/visualsearch/image?page=1&rows=5' \
--header 'authority: www.myntra.com' \
--header 'accept: application/json' \
--header 'accept-language: en-GB,en;q=0.9' \
--header 'cookie: _ga=GA1.2.1678700689.1660729809; ajs_anonymous_id=bc38f1bc-446c-48cd-ae66-8ecd32f9d3ca; ajs_user_id=c68c2a72.0210.4e29.a315.9670da4cc8e8gP0MwYxAzB; bc=true; _d_id=d1b5def3-1a43-41b7-8851-07873644d628; mynt-eupv=1; _gcl_au=1.1.433464726.1660914224; tvc_VID=1; _fbp=fb.1.1660914224900.857102999; _gid=GA1.2.1310205691.1661142008; _cc_id=c28b639646f44757bd62a52750457111; __cab=cart.fsexp%3D; ftc=false; sc_tt=true; G_ENABLED_IDPS=google; G_AUTHUSER_H=0; ilgim=true; user_uuid=d87b99e8.09c2.483c.8270.7b1efc398e47HCJ3PEKrsp; oai=144652047; oaui=144652047:191149625; uidx=d87b99e8.09c2.483c.8270.7b1efc398e47HCJ3PEKrsp; mynt-ulc=pincode%3A110085%7CaddressId%3A144652047; mynt-ulc-api=pincode%3A110085%7CaddressId%3A144652047; panoramaId_expiry=1661323554134; vw=400; vh=984; webVitals=true; cto_bundle=xo4aBl93Y1BsNFFkJTJCbjAlMkZVYkQ0WEpjNVVIQlFQSmg5OWhLRSUyRm9MSzdldVZEbDRoeHVWOTlGQm5yQm1jQkdSUnVySFdRMGJZMVIlMkZKRGZDYzB6NWFLJTJGSkxTbEdubFZubExlOU1MRllTQmNUbUROMjkzMWNGa3dONmxNTDVwN2YyNXZFSWxrNkhJc1ZXZlNBVDRyeVJwamp3eDB3JTNEJTNE; mynt-loc-src=expiry%3A1661267768747%7Csource%3AUSER; ismd=1; _mxab_=checkout.selective%3Denabled%3Bconfig.bucket%3Dregular%3Bpdp.web.savedAddress%3Denabled%3Bcheckout.couponUpsell%3Denabled%3Bcheckout.attachedProducts%3Denabled%3Bcheckout.payment.dope%3Ducretryfirst%3Bcheckout.donation%3Denabled%3Bpdp.expiry.date%3Denabled%3Bpayments.iconrevamp%3Ddisabled%3Bpdp.autoapply.newusercoupon%3Ddisabled; _pv=default; microsessid=645; utm_track_v1=%7B%22utm_source%22%3A%22direct%22%2C%22utm_medium%22%3A%22direct%22%2C%22trackstart%22%3A1661270364%2C%22trackend%22%3A1661270424%7D; lt_timeout=1; lt_session=1; at=ZXlKaGJHY2lPaUpTVXpJMU5pSXNJbXRwWkNJNklqSWlmUS5leUpoY0hCT1lXMWxJam9pYlhsdWRISmhJaXdpYVhOeklqb2lTVVJGUVNJc0luUnZhMlZ1WDNSNWNHVWlPaUpoZENJc0luTjBiM0psU1dRaU9pSXlNamszSWl3aWJITnBaQ0k2SW1Jd05XVmxNelU0TFRWbFpEQXROR0ZpT1MxaVlUSXhMV05rTnpoaFpEZzROek5tTlMweE5qWXhNVFE1T0RNMk5URTJJaXdpY0NJNklqSXlPVGNpTENKamFXUjRJam9pYlhsdWRISmhMVEF5WkRka1pXTTFMVGhoTURBdE5HTTNOQzA1WTJZM0xUbGtOakprWW1WaE5XVTJNU0lzSW5OMVlsOTBlWEJsSWpvd0xDSnpZMjl3WlNJNklrSkJVMGxESUZCUFVsUkJUQ0lzSW1WNGNDSTZNVFkyTVRJM016azJOQ3dpYm1sa2VDSTZJalU1T0dJMk5UWTNMVEZtWW1ZdE1URmxaQzA1TVRnNExUVmhPRGxsT1RsbVpUSm1OU0lzSW1saGRDSTZNVFkyTVRJM01ETTJOQ3dpZFdsa2VDSTZJbVE0TjJJNU9XVTRMakE1WXpJdU5EZ3pZeTQ0TWpjd0xqZGlNV1ZtWXpNNU9HVTBOMGhEU2pOUVJVdHljM0FpZlEuUmNlV2hUcGJnMExGcGJPWE1Xel9kbnFWdjVNSHJDY2ZyU0ZfZVo5ZHA3eFdSaUVtbUZ5bjkxR0tNa1BHaFkyTzB2eWxSVGQ4TkFNNGkxd2FfX3k0WDY3OGRPRWxFUTVjQ1hjUkR5N1ZLNTJIbnUxRnNkeU5qd1Ywd3AzcVRfMXpxUWlsajhDWXJ0d1FwclVEeDVBOHZIWXdKclg1eDd1UHFaTUVFdUM3UWZJ; rt=ZXlKaGJHY2lPaUpTVXpJMU5pSXNJbXRwWkNJNklqSWlmUS5leUp5ZEdsM0lqb3lNek15T0RBd01Dd2lZWEJ3VG1GdFpTSTZJbTE1Ym5SeVlTSXNJbWx6Y3lJNklrbEVSVUVpTENKMGIydGxibDkwZVhCbElqb2ljblFpTENKemRHOXlaVWxrSWpvaU1qSTVOeUlzSW14emFXUWlPaUppTURWbFpUTTFPQzAxWldRd0xUUmhZamt0WW1FeU1TMWpaRGM0WVdRNE9EY3paalV0TVRZMk1URTBPVGd6TmpVeE5pSXNJbkFpT2lJeU1qazNJaXdpZEc5dUlqb3hOall4TWpjd016WTBMQ0p5ZEhRaU9qRXNJbU5wWkhnaU9pSnRlVzUwY21FdE1ESmtOMlJsWXpVdE9HRXdNQzAwWXpjMExUbGpaamN0T1dRMk1tUmlaV0UxWlRZeElpd2ljM1ZpWDNSNWNHVWlPakFzSW5OamIzQmxJam9pUWtGVFNVTWdVRTlTVkVGTUlpd2laWGh3SWpveE5qZzBOVGs0TXpZMExDSnVhV1I0SWpvaU5UazRZalkxTmpjdE1XWmlaaTB4TVdWa0xUa3hPRGd0TldFNE9XVTVPV1psTW1ZMUlpd2lhV0YwSWpveE5qWXhNamN3TXpZMExDSjFhV1I0SWpvaVpEZzNZams1WlRndU1EbGpNaTQwT0ROakxqZ3lOekF1TjJJeFpXWmpNems0WlRRM1NFTktNMUJGUzNKemNDSjkuSGN4T0gzbVRVSG5iaHg5MS1hU2lFVE5JbnRWd3B3a1FQQ2JRcy1qR1RDSnkwUjJlZE5McFRoeWxiczVxOWZfRllPaWd2WXBCTXNLMEtpX0pSb2k3QkR5RGRLUUVPMFlZdVlXRDZ6Tk9ncmFwMlJQeHJ6Q2dpQUozTXMwaU55ak1sdUExYm5qbTZxRVVDVG1fZTZsQVBCYzdaaFVRZlQ4cGdxb1VsNElzYUJj; AKA_A2=A; bm_sz=F7B4392037DC1CF4B9DD5D8D4229FA2D~YAAQ3P3UFzMITciCAQAAlxJuyxCMOXGJa3J/bq/CNDNJZeF9g1jJaI/Oz6P9qF6h3utbLKd7YrpF3w5c2rPnMBff6ZEgNTzVr5tUs+GY+09FoCVziu6LVPtlwOMVryBCx2MA6M8U/CSkVoF1sE3cUcRDBCg+V+dFFmDxKDXQIPKVwC/KbTfp0W7s/GPvnpjN4mCPGYyg7ZlAVQFpSd/eAsR90wFVnIYA2fbsG9IGrJc/O1Zl4LvbDdgKxlhsW7emWThg9KeO+cNdWo8Se9RREEIaXfH02TnmvqY5+wHvJ91DFps=~4337717~3294274; ak_RT="z=1&dm=myntra.com&si=a62de590-c921-4ffc-a255-ae47b67219aa&ss=l76dhcon&sl=0&tt=0"; bm_mi=E238F47663AB21AE168AC0090C0E5B1C~YAAQ3P3UF8IITciCAQAAchduyxCgIK24OYkST/EQ9f+HfNb9HzFWfY8ziQwt0ndOlkPDfz6nmdn9H6y4XqoduI3h+OKIs5q/nxYXv+f8elJcmAPzKiybmD7dZFOpI6tNkTYD5fmI8klKDsRveCswixI6lBCoQBmsVCmzSKtvoQkTgHcLkytUDHIsfM5g/m8bJEDNTRdoNBrTXgRXrLq43dIcZPsXFStr8ozkyhdovKHc4RBpoUKoefxt7ziXx1cDTW7CYo1YI2CqGIbJLphEw5vuDPJ+GnkkKKnpPXYzu7xm47EKovAJg7WNs5DXQtuxrBYPtrqaLodtAceBoZlJAfDN4EaIkmQOPAqLriiHQP5RqE+oj7dvzHGlceD6pmAu+A93rQZhbZ6aPTkxe03PAFS18xGyLs3J/44XjcFkwOhXrqFWn7/wKbB34uWfLQ9s6Xn8zBqPDF4QoQB63VfuCwnVhA==~1; AMP_TOKEN=%24RETRIEVING; _abck=DD57C38A5F8F116708A48B6891EF6911~0~YAAQ3P3UF9sITciCAQAAdBhuywgIqAjZX8DKiachjk2av4JLpla1b5/SR/CreeCby1uZsQndQKdZSvuo1v+dXxEig/NSVCEF3zCdccb1UsbwMKhmBtRLD/SxBdoW/T3L6Uxh3B6a+BzdN72DV6tlxj0yMHS94ziDmMgpZy1eh5T3UxKBW+6ziFeKcwF9KOP3Ska3B9kqB9FRFPXN1hi44iVlmv1g9OxZ8Q42essJr1JlbVJlYeDsx08OGL5/U0MNnDUo8Qs+9aQIJsG132AFh4PsH2VkJC61P2MR4u6LuvYPaHXDRh55iY+K4B8tROjwzW574D/HRDmwSFsuVpRwiJAn2eK/5+mDj5P8dccSEU14k7m6gmvzO/MyKDK7n8vYhlzWNKjCeN6s8rzHQqU7lMczVtxA+fJP~-1~-1~1661273943; _ma_session=%7B%22id%22%3A%22e09a03de-2efc-4e53-8089-69c2355beabb-d1b5def3-1a43-41b7-8851-07873644d628%22%2C%22referrer_url%22%3A%22%22%2C%22utm_medium%22%3A%22%22%2C%22utm_source%22%3A%22%22%2C%22utm_channel%22%3A%22direct%22%7D; dp=m; ru=PF9cVGdsJ05ZCXc3ZBNwaHIlRHEfFgVfbloGWw9AGUJVCnkfOH8iRhcOBFckHkAwIzE3ODkxNjE4NTckMg%3D%3D.ac16343a6423a3d200fe8503339c5042; utrid=uuid-16609142220069; _xsrf=4o2RGd2KxTg7hsJErvAXXLcPbbERzQUZ; user_session=3T8YuClnvhaOtp6xNzy-hQ.AL8AS7t3EphgGtE-Zuu6wwZI5rzi6mQg1tjnnRAJlFDcAk4wnxMSp7uc_Ds1V1hzWh-XNzElOZcfqN9QGnuLKBx_OVxrCvIOQexq0Btta4cXYP6yA9DJP_5AHD08uwfcbGFgzuJFpzzqfJUhlWhxxEAGe6G1MizxeVIE39SsoiC-OHxSvbXOluqBOSAzq3vczO2FGjFcFOyBKhQkd6F9RhNamp5ZXdmBY5NxEJbrgY9xoU2RTLR_RQIynwkOVtFKbDq6L3oPaXrWZzByaghIHE4KDx4DHfztLVXLHHiLHozRpPrNDnJlV0_0EesgLoFIflSAY2FtsCMJXoxjwyKwkij2v6REsvMS1ewKIhQq5he14TiaAlQqkRzvDjTEGh9gI1Hqss0nUp5LaT7z5XKKshDUkOAGYKhVJsorkB4YpW7BcurHz9uQjaG8OpwFDvtQSiQS7K7K1c_WasjHuOfrb25zeEVVY3f_CkgtOvrS5rew859_xfNC-BqZ82otFmJc.1661270364682.86400000.zvLR2FR-edusC77tHak_KK-YgrcaXCIz3axzuAaXcOM; bm_sv=268868EE94488D10D7425FA9BCF45E3F~YAAQ3P3UF4cJTciCAQAAtR5uyxA8NwhEReXctAAEU5fuauMb4Gigs31Tc3va4QaGPpKes53xhGT9vug7f188KQKY/hNhP8kGE0R0tg4kUm1kmEJDMBjWpIP38DmegrYlqwL9UgfMIzBdSGAwRFit6sXEf/IcroH33wkuqDJzFR2Ge3RHpTkUmK7J1XQ+J031/ybVPhznuxkPHb9LPoQl8GIUD+WgCXx54m/+fOTU8vacaxJDrwmCCrhs1/HVd6pD~1; ak_bmsc=BB220FA0E75DA72730129649FCEEA8F5~000000000000000000000000000000~YAAQ3P3UF6UJTciCAQAAOiBuyxCp4PFfzqXJXGytiN4Mo4IriIFvGPk4uo+ggJhJCTS4QRNOl4+NHglBdHNhLEkJBlRn2Cm3m+VsQfvKAI+qBl+Mb5Hjm3WfHuipDkZL/IGQKu1rrP879Kw++ivVRN/ZnpY1UFRoya2ijsQkyLkoAuB0YGAi17vyZNUIAgSppZdai04X7rasjRDFGgO9JVZE+IHIKbVpFzixtBUc75tyNrabYrbOMRbYBu8cwFkyDZrBQE/Xoam0mg9sPdCF4IrWQMiIkPpQggE3LFo8HXbn/Vxl+FmUQk8R/J34W+wH/kEBuh06Fy/zp/J2ojqm2BZIohn+n9sReZolPgOLquy7t+m8rkoyAUUXNPdzpKn50C4D5bX5SkvygVVwTWO2Y7v4CwzkvAMsXd/WtTHiaLsJ3I08ZsQ+ENkdjmIswssBhVW7ZnVd8Jnbgzb49adlTENA2TlmQ4pO5iaxsQ9yREyHmIYQaHlCfm5Bpa68+dXGF2HOfCc=; _abck=DD57C38A5F8F116708A48B6891EF6911~-1~YAAQl/3UF3kSdrWCAQAA/+uMywgKtvtvHs0ungfPztVQBGSTxfBSjrwwC0X/2bH7SBdaZK4ojKs+RqJOkrDc0za3VSnJh0FfM3AiTTgH6lX5mz5HV6voYlDwh6FkgZuSFgsXAy45W5btkJeW5tc8dBfYAHuGEh/GhXWVEglH+3ZhZxKM2k5dHzx/AUXy8XW4e7YqgfuTXWICXWjj0UgTdk2RwOcnCZZcCdtpMKqwPrzfxy1CJ11VPXVXuG/RgwWaycUHVxXPo2gTkxtZ147xztY6s9JeMGcd5v7JccUrSCdLfwZDO/938HTeF2GqhDjNP4fs47ATmu+WR1lMAhUvKZLeRcV1G4wp3JTe1EVmzjf7nG0WvbOuoRYNoVnnYKGOfAFMy91gusgCjUYKHmy0qKY21d56i8Mt~0~-1~1661273943; ak_bmsc=BB220FA0E75DA72730129649FCEEA8F5~000000000000000000000000000000~YAAQl/3UF3oSdrWCAQAA/+uMyxCUtAbZhEC7YtQaDjBOb1KUMjZyTxOfmP05Kt/RtEHPwKBgZwuo0++b7qRB4VbGxWVF6gJGBwvLCxsql1tqbPi0nUVn8Hmkk7EVjfh8HbhJpkg6DRBSRDzzZSpTYYP68aw0xcGC/RfVDME9LOTevtreQ/a9OHRXTZLmxtSX2s0wz/orDi6sesPiyqkfYTi8RgbYak0OBTspOc6KVTqlj3nrJip+kwehhIx06ihE7n+hxiQ9rmVc/fwYSYxLvKcRyZ+zugkb/YZddMgLvB6NM0utxRVh6v+cXXvXstAJu/Lwb1Urjqp51fmYSJtzxkGKTytmcm6DIvbdD7MzKNBVD3IBt7z94/LvwWhGaizXqZYKwDoFyTI+45hm1ck2YZPGJbOJYFhFNaWOy9D1VAih6tEXmf64uu1k6TMWnzuMd38w2o8V47NLMfXJmKAHmisKxD7nxUndBYIL1/07tg9PSjd3Qyydql+8qk5QIBYN4kgHPmUYsaECWlUFJHJC+jFl4fXJnHu/Tb2rNEjaEwb5FoE3yLJKbb/HJ4MHMv/VTiXUPYUstzik4bg2HQJsNf65ubMi98ehEQOyKgTw19IKRwV9PIifqTKd221YGAWXgYmGsmXmumQQ9oapultzz3OKW4U/aukzw4tr4J9ipsU+Fq0=; bm_sv=268868EE94488D10D7425FA9BCF45E3F~YAAQl/3UF3sSdrWCAQAA/+uMyxBDAulYwcjSWiwjjhAmWEmbvlxW4t5MmVZ6APG+rIuCP/UNYC6Lp2Zqe/37vH+9RZeZbfTgYHgln3Ow6IwMMcJ/BIkxlekn8t1JWB4QiDmw83gui5aWxQ8BwvLML9PiavWVfRpyl5nlgss6n7uhSgd9g58A5oBkcCtYDGmsH7FCyfIkop22wC7KxCO01ulPTWzykjIHKAqSfiJpK8+Ja7Zsa4hmC/jTXRfOcEg4~1' \
--form 'file=@"/Users/300074702/Projects/hack/resources/img_1.png"'