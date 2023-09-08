#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 14:51:23 2023

@author: basakesin
"""

from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd
import lxml
import os

woman_links = {"Açık mavi kot gömlek": "https://www.trendyol.com/sr?q=A%C3%A7%C4%B1k+mavi+kot+g%C3%B6mlek",
"Koyu mavi yırtmaçlı skinny jean": "https://www.trendyol.com/sr?q=Koyu+mavi+y%C4%B1rtma%C3%A7l%C4%B1+skinny+jean",
"Siyah tek omuz midi elbise": "https://www.trendyol.com/sr?q=Siyah+tek+omuz+midi+elbise",
"Zeytin yeşili şort": "https://www.trendyol.com/sr?q=Zeytin+ye%C5%9Fili+%C5%9Fort",
"Siyah beyaz çizgili tişört": "https://www.trendyol.com/sr?q=Siyah+beyaz+%C3%A7izgili+ti%C5%9F%C3%B6rt",
"Kahverengi deri bel çantası": "https://www.trendyol.com/sr?q=Kahverengi+deri+bel+%C3%A7antas%C4%B1",
"Siyah dantelli balık etek": "https://www.trendyol.com/sr?q=Siyah+dantelli+bal%C4%B1k+etek",
"Beyaz basic tişört": "https://www.trendyol.com/sr?q=Beyaz+basic+ti%C5%9F%C3%B6rt",
"Turuncu pileli etek": "https://www.trendyol.com/sr?q=Turuncu+pileli+etek",
"Kırmızı triko hırka": "https://www.trendyol.com/sr?q=K%C4%B1rm%C4%B1z%C4%B1+triko+h%C4%B1rka",
"Mor volanlı bluz": "https://www.trendyol.com/sr?q=Mor+volanl%C4%B1+bluz",
"Açık renk mom jean": "https://www.trendyol.com/sr?q=A%C3%A7%C4%B1k+renk+mom+jean",
"Gri kapüşonlu sweatshirt": "https://www.trendyol.com/sr?q=Gri+kap%C3%BC%C5%9Fonlu+sweatshirt",
"Metalik sırt çantası": "https://www.trendyol.com/sr?q=Metalik+s%C4%B1rt+%C3%A7antas%C4%B1",
"Haki chino pantolon": "https://www.trendyol.com/sr?q=Haki+chino+pantolon",
"Kırmızı dantelli uzun elbise": "https://www.trendyol.com/sr?q=K%C4%B1rm%C4%B1z%C4%B1+dantelli+uzun+elbise",
"Yeşil sıfır yaka bluz": "https://www.trendyol.com/sr?q=Ye%C5%9Fil+s%C4%B1f%C4%B1r+yaka+bluz",
"Siyah düğmeli etek": "https://www.trendyol.com/sr?q=Siyah+d%C3%BC%C4%9Fmeli+etek",
"Mavi kot yelek": "https://www.trendyol.com/sr?q=Mavi+kot+yelek",
"Pastel pembe sırt çantası": "https://www.trendyol.com/sr?q=Pastel+pembe+s%C4%B1rt+%C3%A7antas%C4%B1",
"Bordo yüksek bel jean": "https://www.trendyol.com/sr?q=Bordo+y%C3%BCksek+bel+jean",
"Yeşil kruvaze bluz": "https://www.trendyol.com/sr?q=Ye%C5%9Fil+kruvaze+bluz",
"Siyah asimetrik etek": "https://www.trendyol.com/sr?q=Siyah+asimetrik+etek",
"Mavi denim ceket": "https://www.trendyol.com/sr?q=Mavi+denim+ceket",
"Kırmızı v yaka bluz": "https://www.trendyol.com/sr?q=K%C4%B1rm%C4%B1z%C4%B1+v+yaka+bluz",
"Bej kaşmir hırka": "https://www.trendyol.com/sr?q=Bej+ka%C5%9Fmir+h%C4%B1rka",
"Turuncu yüksek bel pantolon": "https://www.trendyol.com/sr?q=Turuncu+y%C3%BCksek+bel+pantolon",
"Beyaz dantelli mini elbise": "https://www.trendyol.com/sr?q=Beyaz+dantelli+mini+elbise",
"Siyah deri ceket": "https://www.trendyol.com/sr?q=Siyah+deri+ceket",
"Kırmızı deri çanta": "https://www.trendyol.com/sr?q=K%C4%B1rm%C4%B1z%C4%B1+deri+%C3%A7anta",
"Siyah şifon bluz": "https://www.trendyol.com/sr?q=Siyah+%C5%9Fifon+bluz",
"Gri oversized sweatshirt": "https://www.trendyol.com/sr?q=Gri+oversized+sweatshirt",
"Mavi ekose gömlek": "https://www.trendyol.com/sr?q=Mavi+ekose+g%C3%B6mlek",
"Sarı maxi elbise": "https://www.trendyol.com/sr?q=Sar%C4%B1+maxi+elbise",
"Haki yüksek bel pantolon": "https://www.trendyol.com/sr?q=Haki+y%C3%BCksek+bel+pantolon",
"Gri örgü hırka": "https://www.trendyol.com/sr?q=Gri+%C3%B6rg%C3%BC+h%C4%B1rka",
"Siyah deri mini etek": "https://www.trendyol.com/sr?q=Siyah+deri+mini+etek",
"Sarı yüksek bel jean": "https://www.trendyol.com/sr?q=Sar%C4%B1+y%C3%BCksek+bel+jean",
"Siyah şifon elbise": "https://www.trendyol.com/sr?q=Siyah+%C5%9Fifon+elbise",
"Beyaz pamuklu tişört": "https://www.trendyol.com/sr?q=Beyaz+pamuklu+ti%C5%9F%C3%B6rt",
"Beyaz dantel bluz": "https://www.trendyol.com/sr?q=Beyaz+dantel+bluz",
"Siyah deri pantolon": "https://www.trendyol.com/sr?q=Siyah+deri+pantolon",
"Yeşil midi etek": "https://www.trendyol.com/sr?q=Ye%C5%9Fil+midi+etek",
"Gri triko kazak": "https://www.trendyol.com/sr?q=Gri+triko+kazak",
"Beyaz uzun kollu tişört": "https://www.trendyol.com/sr?q=Beyaz+uzun+kollu+ti%C5%9F%C3%B6rt",
"Mavi mini denim etek": "https://www.trendyol.com/sr?q=Mavi+mini+denim+etek",
"Beyaz yüksek bel jean": "https://www.trendyol.com/sr?q=Beyaz+y%C3%BCksek+bel+jean",
"Siyah sırt çantası": "https://www.trendyol.com/sr?q=Siyah+s%C4%B1rt+%C3%A7antas%C4%B1",
"Beyaz v yaka bluz": "https://www.trendyol.com/sr?q=Beyaz+v+yaka+bluz",
"Siyah yüksek bel jean": "https://www.trendyol.com/sr?q=Siyah+y%C3%BCksek+bel+jean","Siyah kısa boy omuz açık elbise": "https://www.trendyol.com/sr?q=Siyah+k%C4%B1sa+boy+omuz+a%C3%A7%C4%B1k+elbise",
"Beyaz maxi boy standart kol elbise": "https://www.trendyol.com/sr?q=Beyaz+maxi+boy+standart+kol+elbise",
"Kırmızı midi boy straplez elbise": "https://www.trendyol.com/sr?q=K%C4%B1rm%C4%B1z%C4%B1+midi+boy+straplez+elbise",
"Mavi mini boy tek kol elbise": "https://www.trendyol.com/sr?q=Mavi+mini+boy+tek+kol+elbise",
"Yeşil regular boy tek omuz elbise": "https://www.trendyol.com/sr?q=Ye%C5%9Fil+regular+boy+tek+omuz+elbise",
"Siyah standart boy truvakar kol elbise": "https://www.trendyol.com/sr?q=Siyah+standart+boy+truvakar+kol+elbise",
"Beyaz uzun boy uzun kol elbise": "https://www.trendyol.com/sr?q=Beyaz+uzun+boy+uzun+kol+elbise",
"Kırmızı kısa boy volanlı elbise": "https://www.trendyol.com/sr?q=K%C4%B1rm%C4%B1z%C4%B1+k%C4%B1sa+boy+volanl%C4%B1+elbise",
"Mavi maxi boy yarasa kol elbise": "https://www.trendyol.com/sr?q=Mavi+maxi+boy+yarasa+kol+elbise",
"Yeşil midi boy omuz açık elbise": "https://www.trendyol.com/sr?q=Ye%C5%9Fil+midi+boy+omuz+a%C3%A7%C4%B1k+elbise",
"Siyah mini boy standart kol elbise": "https://www.trendyol.com/sr?q=Siyah+mini+boy+standart+kol+elbise",
"Beyaz regular boy straplez elbise": "https://www.trendyol.com/sr?q=Beyaz+regular+boy+straplez+elbise",
"Kırmızı standart boy tek kol elbise": "https://www.trendyol.com/sr?q=K%C4%B1rm%C4%B1z%C4%B1+standart+boy+tek+kol+elbise",
"Mavi uzun boy tek omuz elbise": "https://www.trendyol.com/sr?q=Mavi+uzun+boy+tek+omuz+elbise",
"Yeşil kısa boy truvakar kol elbise": "https://www.trendyol.com/sr?q=Ye%C5%9Fil+k%C4%B1sa+boy+truvakar+kol+elbise",
"Siyah maxi boy uzun kol elbise": "https://www.trendyol.com/sr?q=Siyah+maxi+boy+uzun+kol+elbise",
"Beyaz midi boy volanlı elbise": "https://www.trendyol.com/sr?q=Beyaz+midi+boy+volanl%C4%B1+elbise",
"Kırmızı mini boy yarasa kol elbise": "https://www.trendyol.com/sr?q=K%C4%B1rm%C4%B1z%C4%B1+mini+boy+yarasa+kol+elbise",
"Mavi regular boy omuz açık elbise": "https://www.trendyol.com/sr?q=Mavi+regular+boy+omuz+a%C3%A7%C4%B1k+elbise",
"Yeşil standart boy standart kol elbise": "https://www.trendyol.com/sr?q=Ye%C5%9Fil+standart+boy+standart+kol+elbise",
"Siyah uzun boy straplez elbise": "https://www.trendyol.com/sr?q=Siyah+uzun+boy+straplez+elbise",
"Beyaz kısa boy tek kol elbise": "https://www.trendyol.com/sr?q=Beyaz+k%C4%B1sa+boy+tek+kol+elbise",
"Kırmızı maxi boy tek omuz elbise": "https://www.trendyol.com/sr?q=K%C4%B1rm%C4%B1z%C4%B1+maxi+boy+tek+omuz+elbise",
"Mavi midi boy truvakar kol elbise": "https://www.trendyol.com/sr?q=Mavi+midi+boy+truvakar+kol+elbise",
"Yeşil mini boy uzun kol elbise": "https://www.trendyol.com/sr?q=Ye%C5%9Fil+mini+boy+uzun+kol+elbise",
"Siyah regular boy volanlı elbise": "https://www.trendyol.com/sr?q=Siyah+regular+boy+volanl%C4%B1+elbise",
"Beyaz standart boy yarasa kol elbise": "https://www.trendyol.com/sr?q=Beyaz+standart+boy+yarasa+kol+elbise",
"Kırmızı uzun boy omuz açık elbise": "https://www.trendyol.com/sr?q=K%C4%B1rm%C4%B1z%C4%B1+uzun+boy+omuz+a%C3%A7%C4%B1k+elbise",
"Mavi kısa boy standart kol elbise": "https://www.trendyol.com/sr?q=Mavi+k%C4%B1sa+boy+standart+kol+elbise",
"Yeşil maxi boy straplez elbise": "https://www.trendyol.com/sr?q=Ye%C5%9Fil+maxi+boy+straplez+elbise",
"Siyah midi boy tek kol elbise": "https://www.trendyol.com/sr?q=Siyah+midi+boy+tek+kol+elbise",
"Beyaz mini boy tek omuz elbise": "https://www.trendyol.com/sr?q=Beyaz+mini+boy+tek+omuz+elbise",
"Kırmızı regular boy truvakar kol elbise": "https://www.trendyol.com/sr?q=K%C4%B1rm%C4%B1z%C4%B1+regular+boy+truvakar+kol+elbise",
"Mavi standart boy uzun kol elbise": "https://www.trendyol.com/sr?q=Mavi+standart+boy+uzun+kol+elbise",
"Yeşil uzun boy volanlı elbise": "https://www.trendyol.com/sr?q=Ye%C5%9Fil+uzun+boy+volanl%C4%B1+elbise",
"Siyah kısa boy yarasa kol elbise": "https://www.trendyol.com/sr?q=Siyah+k%C4%B1sa+boy+yarasa+kol+elbise",
"Beyaz maxi boy omuz açık elbise": "https://www.trendyol.com/sr?q=Beyaz+maxi+boy+omuz+a%C3%A7%C4%B1k+elbise",
"Kırmızı midi boy standart kol elbise": "https://www.trendyol.com/sr?q=K%C4%B1rm%C4%B1z%C4%B1+midi+boy+standart+kol+elbise",
"Mavi mini boy straplez elbise": "https://www.trendyol.com/sr?q=Mavi+mini+boy+straplez+elbise",
"Yeşil regular boy tek kol elbise": "https://www.trendyol.com/sr?q=Ye%C5%9Fil+regular+boy+tek+kol+elbise",
"Kırmızı düz renk kısa kollu V yaka tişört": "https://www.trendyol.com/sr?q=K%C4%B1rm%C4%B1z%C4%B1+d%C3%BCz+renk+k%C4%B1sa+kollu+V+yaka+ti%C5%9F%C3%B6rt",
"Mavi çizgili kolsuz yuvarlak yaka tişört": "https://www.trendyol.com/sr?q=Mavi+%C3%A7izgili+kolsuz+yuvarlak+yaka+ti%C5%9F%C3%B6rt",
"Yeşil baskılı kısa kollu U yaka tişört": "https://www.trendyol.com/sr?q=Ye%C5%9Fil+bask%C4%B1l%C4%B1+k%C4%B1sa+kollu+U+yaka+ti%C5%9F%C3%B6rt",
"Siyah desenli straplez V yaka tişört": "https://www.trendyol.com/sr?q=Siyah+desenli+straplez+V+yaka+ti%C5%9F%C3%B6rt",
"Beyaz dijital baskı kolsuz yuvarlak yaka tişört": "https://www.trendyol.com/sr?q=Beyaz+dijital+bask%C4%B1+kolsuz+yuvarlak+yaka+ti%C5%9F%C3%B6rt",
"Kırmızı düz kısa kollu U yaka tişört": "https://www.trendyol.com/sr?q=K%C4%B1rm%C4%B1z%C4%B1+d%C3%BCz+k%C4%B1sa+kollu+U+yaka+ti%C5%9F%C3%B6rt",
"Mavi empirme baskılı straplez V yaka tişört": "https://www.trendyol.com/sr?q=Mavi+empirme+bask%C4%B1l%C4%B1+straplez+V+yaka+ti%C5%9F%C3%B6rt",
"Yeşil nakışlı işlemeli kolsuz yuvarlak yaka tişört": "https://www.trendyol.com/sr?q=Ye%C5%9Fil+nak%C4%B1%C5%9Fl%C4%B1+i%C5%9Flemeli+kolsuz+yuvarlak+yaka+ti%C5%9F%C3%B6rt",
"Siyah renkli kısa kollu U yaka tişört": "https://www.trendyol.com/sr?q=Siyah+renkli+k%C4%B1sa+kollu+U+yaka+ti%C5%9F%C3%B6rt",
"Beyaz desensiz straplez V yaka tişört": "https://www.trendyol.com/sr?q=Beyaz+desensiz+straplez+V+yaka+ti%C5%9F%C3%B6rt",
"Mor baskılı kısa kollu V yaka tişört": "https://www.trendyol.com/sr?q=Mor+bask%C4%B1l%C4%B1+k%C4%B1sa+kollu+V+yaka+ti%C5%9F%C3%B6rt",
"Turuncu düz renk kolsuz yuvarlak yaka tişört": "https://www.trendyol.com/sr?q=Turuncu+d%C3%BCz+renk+kolsuz+yuvarlak+yaka+ti%C5%9F%C3%B6rt",
"Gri çizgili straplez U yaka tişört": "https://www.trendyol.com/sr?q=Gri+%C3%A7izgili+straplez+U+yaka+ti%C5%9F%C3%B6rt",
"Sarı desenli kısa kollu V yaka tişört": "https://www.trendyol.com/sr?q=Sar%C4%B1+desenli+k%C4%B1sa+kollu+V+yaka+ti%C5%9F%C3%B6rt",
"Pembe dijital baskı kolsuz yuvarlak yaka tişört": "https://www.trendyol.com/sr?q=Pembe+dijital+bask%C4%B1+kolsuz+yuvarlak+yaka+ti%C5%9F%C3%B6rt",
"Kahverengi düz straplez V yaka tişört": "https://www.trendyol.com/sr?q=Kahverengi+d%C3%BCz+straplez+V+yaka+ti%C5%9F%C3%B6rt",
"Lacivert empirme baskılı kısa kollu U yaka tişört": "https://www.trendyol.com/sr?q=Lacivert+empirme+bask%C4%B1l%C4%B1+k%C4%B1sa+kollu+U+yaka+ti%C5%9F%C3%B6rt",
"Bej nakışlı işlemeli straplez V yaka tişört": "https://www.trendyol.com/sr?q=Bej+nak%C4%B1%C5%9Fl%C4%B1+i%C5%9Flemeli+straplez+V+yaka+ti%C5%9F%C3%B6rt",
"Yeşil renkli kolsuz yuvarlak yaka tişört": "https://www.trendyol.com/sr?q=Ye%C5%9Fil+renkli+kolsuz+yuvarlak+yaka+ti%C5%9F%C3%B6rt",
"Siyah desensiz kısa kollu U yaka tişört": "https://www.trendyol.com/sr?q=Siyah+desensiz+k%C4%B1sa+kollu+U+yaka+ti%C5%9F%C3%B6rt",
"Kırmızı baskılı straplez V yaka tişört": "https://www.trendyol.com/sr?q=K%C4%B1rm%C4%B1z%C4%B1+bask%C4%B1l%C4%B1+straplez+V+yaka+ti%C5%9F%C3%B6rt",
"Mavi düz renk kısa kollu U yaka tişört": "https://www.trendyol.com/sr?q=Mavi+d%C3%BCz+renk+k%C4%B1sa+kollu+U+yaka+ti%C5%9F%C3%B6rt",
"Siyah çizgili kolsuz V yaka tişört": "https://www.trendyol.com/sr?q=Siyah+%C3%A7izgili+kolsuz+V+yaka+ti%C5%9F%C3%B6rt",
"Yeşil desenli straplez U yaka tişört": "https://www.trendyol.com/sr?q=Ye%C5%9Fil+desenli+straplez+U+yaka+ti%C5%9F%C3%B6rt",
"Sarı dijital baskı kısa kollu V yaka tişört": "https://www.trendyol.com/sr?q=Sar%C4%B1+dijital+bask%C4%B1+k%C4%B1sa+kollu+V+yaka+ti%C5%9F%C3%B6rt",
"Turuncu düz renk straplez yuvarlak yaka tişört": "https://www.trendyol.com/sr?q=Turuncu+d%C3%BCz+renk+straplez+yuvarlak+yaka+ti%C5%9F%C3%B6rt",
"Mor empirme baskılı kolsuz U yaka tişört": "https://www.trendyol.com/sr?q=Mor+empirme+bask%C4%B1l%C4%B1+kolsuz+U+yaka+ti%C5%9F%C3%B6rt",
"Lacivert nakışlı işlemeli kısa kollu V yaka tişört": "https://www.trendyol.com/sr?q=Lacivert+nak%C4%B1%C5%9Fl%C4%B1+i%C5%9Flemeli+k%C4%B1sa+kollu+V+yaka+ti%C5%9F%C3%B6rt",
"Bej renkli straplez yuvarlak yaka tişört": "https://www.trendyol.com/sr?q=Bej+renkli+straplez+yuvarlak+yaka+ti%C5%9F%C3%B6rt",
"Yeşil desensiz kolsuz U yaka tişört": "https://www.trendyol.com/sr?q=Ye%C5%9Fil+desensiz+kolsuz+U+yaka+ti%C5%9F%C3%B6rt",
"Pembe baskılı kısa kollu V yaka tişört": "https://www.trendyol.com/sr?q=Pembe+bask%C4%B1l%C4%B1+k%C4%B1sa+kollu+V+yaka+ti%C5%9F%C3%B6rt",
"Kahverengi düz renk kolsuz U yaka tişört": "https://www.trendyol.com/sr?q=Kahverengi+d%C3%BCz+renk+kolsuz+U+yaka+ti%C5%9F%C3%B6rt",
"Gri çizgili straplez V yaka tişört": "https://www.trendyol.com/sr?q=Gri+%C3%A7izgili+straplez+V+yaka+ti%C5%9F%C3%B6rt",
"Sarı desenli kısa kollu U yaka tişört": "https://www.trendyol.com/sr?q=Sar%C4%B1+desenli+k%C4%B1sa+kollu+U+yaka+ti%C5%9F%C3%B6rt",
"Turuncu dijital baskı straplez yuvarlak yaka tişört": "https://www.trendyol.com/sr?q=Turuncu+dijital+bask%C4%B1+straplez+yuvarlak+yaka+ti%C5%9F%C3%B6rt",
"Mor düz renk kolsuz V yaka tişört": "https://www.trendyol.com/sr?q=Mor+d%C3%BCz+renk+kolsuz+V+yaka+ti%C5%9F%C3%B6rt",
"Lacivert empirme baskılı straplez U yaka tişört": "https://www.trendyol.com/sr?q=Lacivert+empirme+bask%C4%B1l%C4%B1+straplez+U+yaka+ti%C5%9F%C3%B6rt",
"Bej nakışlı işlemeli kolsuz V yaka tişört": "https://www.trendyol.com/sr?q=Bej+nak%C4%B1%C5%9Fl%C4%B1+i%C5%9Flemeli+kolsuz+V+yaka+ti%C5%9F%C3%B6rt",
"Yeşil renkli straplez U yaka tişört": "https://www.trendyol.com/sr?q=Ye%C5%9Fil+renkli+straplez+U+yaka+ti%C5%9F%C3%B6rt",
"Siyah desensiz kısa kollu V yaka tişört": "https://www.trendyol.com/sr?q=Siyah+desensiz+k%C4%B1sa+kollu+V+yaka+ti%C5%9F%C3%B6rt",
"Siyah biker desensiz mont": "https://www.trendyol.com/sr?q=Siyah+biker+desensiz+mont",
"Mavi bomber çizgili mont": "https://www.trendyol.com/sr?q=Mavi+bomber+%C3%A7izgili+mont",
"Yeşil çene korumalı dokulu mont": "https://www.trendyol.com/sr?q=Ye%C5%9Fil+%C3%A7ene+korumal%C4%B1+dokulu+mont",
"Bej fonksiyonel düz renk mont": "https://www.trendyol.com/sr?q=Bej+fonksiyonel+d%C3%BCz+renk+mont",
"Kırmızı kapüşonlu ekose mont": "https://www.trendyol.com/sr?q=K%C4%B1rm%C4%B1z%C4%B1+kap%C3%BC%C5%9Fonlu+ekose+mont",
"Mor katlanabilir baskılı mont": "https://www.trendyol.com/sr?q=Mor+katlanabilir+bask%C4%B1l%C4%B1+mont",
"Turuncu kolej düz mont": "https://www.trendyol.com/sr?q=Turuncu+kolej+d%C3%BCz+mont",
"Gri oversize desenli mont": "https://www.trendyol.com/sr?q=Gri+oversize+desenli+mont",
"Sarı şişme çizgili mont": "https://www.trendyol.com/sr?q=Sar%C4%B1+%C5%9Fi%C5%9Fme+%C3%A7izgili+mont",
"Lacivert yarım fermuarlı dokulu mont": "https://www.trendyol.com/sr?q=Lacivert+yar%C4%B1m+fermuar%C4%B1l%C4%B1+dokulu+mont",
"Kahverengi biker düz renk mont": "https://www.trendyol.com/sr?q=Kahverengi+biker+d%C3%BCz+renk+mont",
"Beyaz bomber dokulu mont": "https://www.trendyol.com/sr?q=Beyaz+bomber+dokulu+mont",
"Pembe çene korumalı ekose mont": "https://www.trendyol.com/sr?q=Pembe+%C3%A7ene+korumal%C4%B1+ekose+mont",
"Füme fonksiyonel desensiz mont": "https://www.trendyol.com/sr?q=F%C3%BCme+fonksiyonel+desensiz+mont",
"Siyah kapüşonlu desenli mont": "https://www.trendyol.com/sr?q=Siyah+kap%C3%BC%C5%9Fonlu+desenli+mont",
"Lila katlanabilir baskılı mont": "https://www.trendyol.com/sr?q=Lila+katlanabilir+bask%C4%B1l%C4%B1+mont",
"Turkuaz kolej çizgili mont": "https://www.trendyol.com/sr?q=Turkuaz+kolej+%C3%A7izgili+mont",
"Mavi oversize düz mont": "https://www.trendyol.com/sr?q=Mavi+oversize+d%C3%BCz+mont",
"Zeytin yeşili şişme desenli mont": "https://www.trendyol.com/sr?q=Zeytin+ye%C5%9Fili+%C5%9Fi%C5%9Fme+desenli+mont",
"Kırmızı yarım fermuarlı dokulu mont": "https://www.trendyol.com/sr?q=K%C4%B1rm%C4%B1z%C4%B1+yar%C4%B1m+fermuar%C4%B1l%C4%B1+dokulu+mont",
"Turuncu biker ekose mont": "https://www.trendyol.com/sr?q=Turuncu+biker+ekose+mont",
"Yeşil bomber desensiz mont": "https://www.trendyol.com/sr?q=Ye%C5%9Fil+bomber+desensiz+mont",
"Bej çene korumalı baskılı mont": "https://www.trendyol.com/sr?q=Bej+%C3%A7ene+korumal%C4%B1+bask%C4%B1l%C4%B1+mont",
"Mor fonksiyonel çizgili mont": "https://www.trendyol.com/sr?q=Mor+fonksiyonel+%C3%A7izgili+mont",
"Gri kapüşonlu düz renk mont": "https://www.trendyol.com/sr?q=Gri+kap%C3%BC%C5%9Fonlu+d%C3%BCz+renk+mont",
"Lacivert katlanabilir dokulu mont": "https://www.trendyol.com/sr?q=Lacivert+katlanabilir+dokulu+mont",
"Beyaz kolej desenli mont": "https://www.trendyol.com/sr?q=Beyaz+kolej+desenli+mont",
"Kahverengi oversize ekose mont": "https://www.trendyol.com/sr?q=Kahverengi+oversize+ekose+mont",
"Sarı şişme desensiz mont": "https://www.trendyol.com/sr?q=Sar%C4%B1+%C5%9Fi%C5%9Fme+desensiz+mont",
"Füme yarım fermuarlı baskılı mont": "https://www.trendyol.com/sr?q=F%C3%BCme+yar%C4%B1m+fermuar%C4%B1l%C4%B1+bask%C4%B1l%C4%B1+mont",
"Kırmızı asimetrik yaka mini abiye elbise": "https://www.trendyol.com/sr?q=K%C4%B1rm%C4%B1z%C4%B1+asimetrik+yaka+mini+abiye+elbise",
"Mavi balıkçı yaka midi abiye elbise": "https://www.trendyol.com/sr?q=Mavi+bal%C4%B1k%C3%A7%C4%B1+yaka+midi+abiye+elbise",
"Yeşil bebe yaka uzun abiye elbise": "https://www.trendyol.com/sr?q=Ye%C5%9Fil+bebe+yaka+uzun+abiye+elbise",
"Mor bisiklet yaka kısa abiye elbise": "https://www.trendyol.com/sr?q=Mor+bisiklet+yaka+k%C4%B1sa+abiye+elbise",
"Beyaz boyundan bağlamalı regular abiye elbise": "https://www.trendyol.com/sr?q=Beyaz+boyundan+ba%C4%9Flamal%C4%B1+regular+abiye+elbise",
"Pembe carmen yaka standart abiye elbise": "https://www.trendyol.com/sr?q=Pembe+carmen+yaka+standart+abiye+elbise",
"Gri degaje yaka maxi abiye elbise": "https://www.trendyol.com/sr?q=Gri+degaje+yaka+maxi+abiye+elbise",
"Sarı dik yaka kısa abiye elbise": "https://www.trendyol.com/sr?q=Sar%C4%B1+dik+yaka+k%C4%B1sa+abiye+elbise",
"Turuncu gömlek yaka midi abiye elbise": "https://www.trendyol.com/sr?q=Turuncu+g%C3%B6mlek+yaka+midi+abiye+elbise",
"Lacivert hakim yaka uzun abiye elbise": "https://www.trendyol.com/sr?q=Lacivert+hakim+yaka+uzun+abiye+elbise",
"Yüksek topuklu siyah deri stiletto": "https://www.trendyol.com/sr?q=Y%C3%BCksek+topuklu+siyah+deri+stiletto",
"Orta topuklu mavi süet bağcıklı ayakkabı": "https://www.trendyol.com/sr?q=Orta+topuklu+mavi+s%C3%BCet+ba%C4%9Fc%C4%B1kl%C4%B1+ayakkab%C4%B1",
"Düz tabanlı beyaz kumaş spor ayakkabı": "https://www.trendyol.com/sr?q=D%C3%BCz+tabanl%C4%B1+beyaz+kuma%C5%9F+spor+ayakkab%C4%B1",
"Yüksek topuklu kırmızı deri platform ayakkabı": "https://www.trendyol.com/sr?q=Y%C3%BCksek+topuklu+k%C4%B1rm%C4%B1z%C4%B1+deri+platform+ayakkab%C4%B1",
"Düz tabanlı kahverengi süet mokasen": "https://www.trendyol.com/sr?q=D%C3%BCz+tabanl%C4%B1+kahverengi+s%C3%BCet+mokasen",
"Orta topuklu gri kumaş babet": "https://www.trendyol.com/sr?q=Orta+topuklu+gri+kuma%C5%9F+babet",
"Yüksek topuklu siyah tek şeritli abiye ayakkabı": "https://www.trendyol.com/sr?q=Y%C3%BCksek+topuklu+siyah+tek+%C5%9Feritli+abiye+ayakkab%C4%B1",
"Orta topuklu lacivert süet bağcıklı bot": "https://www.trendyol.com/sr?q=Orta+topuklu+lacivert+s%C3%BCet+ba%C4%9Fc%C4%B1kl%C4%B1+bot",
"Düz tabanlı yeşil kumaş slip-on ayakkabı": "https://www.trendyol.com/sr?q=D%C3%BCz+tabanl%C4%B1+ye%C5%9Fil+kuma%C5%9F+slip-on+ayakkab%C4%B1",
"Yüksek topuklu pembe deri çizme": "https://www.trendyol.com/sr?q=Y%C3%BCksek+topuklu+pembe+deri+%C3%A7izme",
"Orta topuklu siyah süet ankle boot": "https://www.trendyol.com/sr?q=Orta+topuklu+siyah+s%C3%BCet+ankle+boot",
"Yüksek topuklu altın rengi abiye sandalet": "https://www.trendyol.com/sr?q=Y%C3%BCksek+topuklu+alt%C4%B1n+rengi+abiye+sandalet",
"Düz tabanlı beyaz deri spor ayakkabı": "https://www.trendyol.com/sr?q=D%C3%BCz+tabanl%C4%B1+beyaz+deri+spor+ayakkab%C4%B1",
"Orta topuklu kahverengi deri çizme": "https://www.trendyol.com/sr?q=Orta+topuklu+kahverengi+deri+%C3%A7izme",
"Düz tabanlı siyah kumaş espadril": "https://www.trendyol.com/sr?q=D%C3%BCz+tabanl%C4%B1+siyah+kuma%C5%9F+espadril",
"Yüksek topuklu gümüş rengi gladyatör sandalet": "https://www.trendyol.com/sr?q=Y%C3%BCksek+topuklu+g%C3%BCm%C3%BC%C5%9F+rengi+gladyat%C3%B6r+sandalet",
"Orta topuklu bordo süet babet": "https://www.trendyol.com/sr?q=Orta+topuklu+bordo+s%C3%BCet+babet",
"Düz tabanlı mavi kumaş loafer": "https://www.trendyol.com/sr?q=D%C3%BCz+tabanl%C4%B1+mavi+kuma%C5%9F+loafer",
"Yüksek topuklu yeşil deri stiletto": "https://www.trendyol.com/sr?q=Y%C3%BCksek+topuklu+ye%C5%9Fil+deri+stiletto",
"Orta topuklu siyah süet Chelsea bot": "https://www.trendyol.com/sr?q=Orta+topuklu+siyah+s%C3%BCet+Chelsea+bot",
"Adidas beyaz logolu deri spor ayakkabı": "https://www.trendyol.com/sr?q=Adidas+beyaz+logolu+deri+spor+ayakkab%C4%B1",
"Nike siyah logolu kumaş spor ayakkabı": "https://www.trendyol.com/sr?q=Nike+siyah+logolu+kuma%C5%9F+spor+ayakkab%C4%B1",
"Adidas kırmızı logolu deri spor ayakkabı": "https://www.trendyol.com/sr?q=Adidas+k%C4%B1rm%C4%B1z%C4%B1+logolu+deri+spor+ayakkab%C4%B1",
"Nike mavi logolu kumaş spor ayakkabı": "https://www.trendyol.com/sr?q=Nike+mavi+logolu+kuma%C5%9F+spor+ayakkab%C4%B1",
"Adidas yeşil logolu deri spor ayakkabı": "https://www.trendyol.com/sr?q=Adidas+ye%C5%9Fil+logolu+deri+spor+ayakkab%C4%B1",
"Nike turuncu logolu kumaş spor ayakkabı": "https://www.trendyol.com/sr?q=Nike+turuncu+logolu+kuma%C5%9F+spor+ayakkab%C4%B1",
"Adidas sarı logolu deri spor ayakkabı": "https://www.trendyol.com/sr?q=Adidas+sar%C4%B1+logolu+deri+spor+ayakkab%C4%B1",
"Nike mor logolu kumaş spor ayakkabı": "https://www.trendyol.com/sr?q=Nike+mor+logolu+kuma%C5%9F+spor+ayakkab%C4%B1",
"Adidas pembe logolu deri spor ayakkabı": "https://www.trendyol.com/sr?q=Adidas+pembe+logolu+deri+spor+ayakkab%C4%B1",
"Nike gri logolu kumaş spor ayakkabı": "https://www.trendyol.com/sr?q=Nike+gri+logolu+kuma%C5%9F+spor+ayakkab%C4%B1"}
man_links = {
             "Erkek Şort": "https://www.trendyol.com/erkek-sort-x-g2-c119",
}


   
downloaded_folders_name = 'Trendyol Resimler'
source_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), downloaded_folders_name)

df = pd.DataFrame(columns=range(9))
df.columns = ["Resim Ismi", "Başlık", "Urun Link", "Fotoğraf Link", "Kategori", "Özellikler", "Özellik Açıklaması", "Fiyat", "Etiket"]

def scrap(links):
    benzerlik = 0
    ind = 1
    for i in links.items():
        print(i)
        name = i[0]
        base_link = i[1]
        liste = []
        a = 1
        benzerlik = benzerlik + 1
        while a <= 1:
            r = requests.get(base_link)
            soup = BeautifulSoup(r.content, 'lxml')
            urunler = soup.find_all("div", attrs={"class": "p-card-chldrn-cntnr"})

            for urun in urunler:
                link_basi = "https://www.trendyol.com"
                link_sonu = urun.a.get("href")
                link = link_basi + link_sonu

                r1 = requests.get(link)
                soup1 = BeautifulSoup(r1.content, 'lxml')

                # Fotoğraf Linki
                foto = soup1.find("img", attrs={"class": "detail-section-img"})
                if foto == None:
                    foto = soup1.find("img", attrs={"class": "ph-gl-img"})
                try:
                    foto_link = foto.get("src")
                except:
                    foto_link = np.nan

                # Başlık
                try:
                    baslik = soup1.find("h1", attrs={"class": "pr-new-br"})
                    baslik = baslik.find("span").text.strip()
                except:
                    baslik = np.nan

                # Fiyat
                fiyat = soup1.find("span", attrs={"class": "prc-dsc"})
                if fiyat != None:
                    fiyat = fiyat.text.strip()
                else:
                    fiyat = np.nan

                # Kategori
                try:
                    kategori = soup1.find_all("a", attrs={"class": "breadcrumb-item"})
                    kategori = kategori[3].text.strip()
                except:
                    kategori = np.nan

                # Özellikler
                try:
                    ozellikler = soup1.find_all("li", attrs={"class": "detail-attr-item"})
                    attr_titles = []
                    attr = []

                    for j in ozellikler:
                        attr_titles.append(j.find("span").text.strip())
                        attr.append(j.find("b").text.strip())
                except:
                    attr = np.nan
                    attr_titles = np.nan

                print(kategori)
                img_id = 'img_' + str(ind) + 'jpg'
                liste.append([img_id, baslik, link, foto_link, kategori, attr_titles, attr, fiyat, benzerlik])
                ind = ind + 1

            a = a + 1

        df = pd.DataFrame(liste)
        df.to_excel(os.path.join(source_folder, str(name) + ".xlsx"))

scrap(man_links)
scrap(woman_links)