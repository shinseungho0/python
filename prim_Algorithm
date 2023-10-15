{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM8C5msDTiINtKnfwPoncqr",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/shinseungho0/python/blob/main/python.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def prim(start):\n",
        "  global mat # global은 전역변수를 만들어준다.\n",
        "  visited = set() # set()함수는 집합\n",
        "  visited.add(start) # 집합에 원소 추가\n",
        "  for _ in range(5):\n",
        "    min = 100\n",
        "    for node in visited:\n",
        "            for j in range(0, 6):\n",
        "                if j not in visited and 0 < mat[node][j] <= min:\n",
        "                    min = mat[node][j]\n",
        "                    edges.append((node, j, min))\n",
        "                    nodes.append(j)\n",
        "    for i in nodes:\n",
        "      visited.add(i)\n",
        "mat = [[0] * 7 for _ in range(7)]\n",
        "edges = []\n",
        "nodes = []\n",
        "for _ in range(10):\n",
        "    a, b, cost = map(int, input().split())\n",
        "    mat[a][b] = cost\n",
        "    mat[b][a] = cost\n",
        "prim(2) # c = 2번부터 시작\n",
        "print(edges)"
      ],
      "metadata": {
        "id": "VRxcyg9LyGM6",
        "outputId": "32bd7dce-5faf-423a-834c-7aab4a362b2a",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0 1 3\n",
            "0 3 2\n",
            "0 4 4\n",
            "1 2 1\n",
            "1 3 4\n",
            "1 5 2\n",
            "2 5 1\n",
            "3 4 5\n",
            "3 5 7\n",
            "4 5 9\n",
            "[(2, 1, 1), (2, 5, 1), (1, 0, 3), (0, 3, 2), (0, 4, 4)]\n"
          ]
        }
      ]
    }
  ]
}
