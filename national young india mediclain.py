import tkinter as tk
from tkinter import ttk, messagebox
import uuid

class InsuranceCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("National Young India Mediclaim Policy")
        self.root.geometry("800x850")  # Fixed height
        self.root.resizable(False, False)
        self.center_window()

        # Rate charts (unchanged)
        self.individual_rates = {
            "Zone I": {
                "Without TPA": {
                    (0, 5): {300000: 5164, 500000: 6183, 1000000: 8829},
                    (6, 17): {300000: 4879, 500000: 6015, 1000000: 8555},
                    (18, 25): {300000: 6786, 500000: 7784, 1000000: 10573},
                    (26, 30): {300000: 8103, 500000: 9830, 1000000: 13337},
                    (31, 35): {300000: 9301, 500000: 10522, 1000000: 14394},
                    (36, 40): {300000: 10240, 500000: 11415, 1000000: 15606},
                    (41, 45): {300000: 10936, 500000: 12462, 1000000: 16912},
                    (46, 46): {300000: 11483, 500000: 13085, 1000000: 17758},
                    (47, 47): {300000: 12057, 500000: 13739, 1000000: 18646},
                    (48, 48): {300000: 12660, 500000: 14426, 1000000: 19578},
                    (49, 49): {300000: 13293, 500000: 15147, 1000000: 20557},
                    (50, 50): {300000: 13958, 500000: 15905, 1000000: 21585},
                    (51, 51): {300000: 14656, 500000: 16700, 1000000: 22664},
                    (52, 52): {300000: 15389, 500000: 17535, 1000000: 23797},
                    (53, 53): {300000: 16158, 500000: 18412, 1000000: 24987},
                    (54, 54): {300000: 16966, 500000: 19332, 1000000: 26236},
                    (55, 55): {300000: 17814, 500000: 20299, 1000000: 27548},
                    (56, 56): {300000: 18705, 500000: 21314, 1000000: 28926},
                    (57, 57): {300000: 19640, 500000: 22380, 1000000: 30372},
                    (58, 58): {300000: 20622, 500000: 23499, 1000000: 31890},
                    (59, 59): {300000: 21653, 500000: 24674, 1000000: 33485},
                    (60, 60): {300000: 22736, 500000: 25907, 1000000: 35159}
                },
                "With TPA": {
                    (0, 5): {300000: 5436, 500000: 6509, 1000000: 9293},
                    (6, 17): {300000: 5136, 500000: 6332, 1000000: 9005},
                    (18, 25): {300000: 7143, 500000: 8194, 1000000: 11129},
                    (26, 30): {300000: 8529, 500000: 10347, 1000000: 14039},
                    (31, 35): {300000: 9790, 500000: 11076, 1000000: 15151},
                    (36, 40): {300000: 10779, 500000: 12016, 1000000: 16428},
                    (41, 45): {300000: 11512, 500000: 13118, 1000000: 17802},
                    (46, 46): {300000: 12088, 500000: 13774, 1000000: 18692},
                    (47, 47): {300000: 12692, 500000: 14462, 1000000: 19627},
                    (48, 48): {300000: 13326, 500000: 15185, 1000000: 20608},
                    (49, 49): {300000: 13993, 500000: 15945, 1000000: 21639},
                    (50, 50): {300000: 14692, 500000: 16742, 1000000: 22721},
                    (51, 51): {300000: 15427, 500000: 17579, 1000000: 23857},
                    (52, 52): {300000: 16198, 500000: 18458, 1000000: 25050},
                    (53, 53): {300000: 17008, 500000: 19381, 1000000: 26302},
                    (54, 54): {300000: 17859, 500000: 20350, 1000000: 27617},
                    (55, 55): {300000: 18752, 500000: 21367, 1000000: 28998},
                    (56, 56): {300000: 19689, 500000: 22436, 1000000: 30448},
                    (57, 57): {300000: 20674, 500000: 23558, 1000000: 31970},
                    (58, 58): {300000: 21707, 500000: 24735, 1000000: 33569},
                    (59, 59): {300000: 22793, 500000: 25972, 1000000: 35247},
                    (60, 60): {300000: 23932, 500000: 27271, 1000000: 37010}
                }
            },
            "Zone II": {
                "Without TPA": {
                    (0, 5): {300000: 4845, 500000: 5860, 1000000: 8380},
                    (6, 17): {300000: 4571, 500000: 5720, 1000000: 8145},
                    (18, 25): {300000: 6580, 500000: 7526, 1000000: 10228},
                    (26, 30): {300000: 7453, 500000: 9198, 1000000: 12485},
                    (31, 35): {300000: 7918, 500000: 9378, 1000000: 12835},
                    (36, 40): {300000: 8438, 500000: 9918, 1000000: 13579},
                    (41, 45): {300000: 8598, 500000: 10082, 1000000: 13715},
                    (46, 46): {300000: 9028, 500000: 10586, 1000000: 14401},
                    (47, 47): {300000: 9479, 500000: 11116, 1000000: 15121},
                    (48, 48): {300000: 9953, 500000: 11672, 1000000: 15877},
                    (49, 49): {300000: 10451, 500000: 12255, 1000000: 16671},
                    (50, 50): {300000: 10973, 500000: 12868, 1000000: 17505},
                    (51, 51): {300000: 11522, 500000: 13511, 1000000: 18380},
                    (52, 52): {300000: 12098, 500000: 14187, 1000000: 19299},
                    (53, 53): {300000: 12703, 500000: 14896, 1000000: 20264},
                    (54, 54): {300000: 13338, 500000: 15641, 1000000: 21277},
                    (55, 55): {300000: 14005, 500000: 16423, 1000000: 22341},
                    (56, 56): {300000: 14705, 500000: 17244, 1000000: 23458},
                    (57, 57): {300000: 15441, 500000: 18106, 1000000: 24631},
                    (58, 58): {300000: 16213, 500000: 19012, 1000000: 25862},
                    (59, 59): {300000: 17023, 500000: 19962, 1000000: 27155},
                    (60, 60): {300000: 17874, 500000: 20960, 1000000: 28513}
                },
                "With TPA": {
                    (0, 5): {300000: 5100, 500000: 6169, 1000000: 8821},
                    (6, 17): {300000: 4811, 500000: 6021, 1000000: 8574},
                    (18, 25): {300000: 6926, 500000: 7922, 1000000: 10766},
                    (26, 30): {300000: 7846, 500000: 9682, 1000000: 13142},
                    (31, 35): {300000: 8335, 500000: 9872, 1000000: 13510},
                    (36, 40): {300000: 8882, 500000: 10440, 1000000: 14294},
                    (41, 45): {300000: 9050, 500000: 10613, 1000000: 14437},
                    (46, 46): {300000: 9503, 500000: 11144, 1000000: 15159},
                    (47, 47): {300000: 9978, 500000: 11701, 1000000: 15917},
                    (48, 48): {300000: 10477, 500000: 12286, 1000000: 16713},
                    (49, 49): {300000: 11001, 500000: 12900, 1000000: 17548},
                    (50, 50): {300000: 11551, 500000: 13545, 1000000: 18426},
                    (51, 51): {300000: 12128, 500000: 14222, 1000000: 19347},
                    (52, 52): {300000: 12735, 500000: 14934, 1000000: 20315},
                    (53, 53): {300000: 13372, 500000: 15680, 1000000: 21330},
                    (54, 54): {300000: 14040, 500000: 16464, 1000000: 22397},
                    (55, 55): {300000: 14742, 500000: 17287, 1000000: 23517},
                    (56, 56): {300000: 15479, 500000: 18152, 1000000: 24692},
                    (57, 57): {300000: 16253, 500000: 19059, 1000000: 25927},
                    (58, 58): {300000: 17066, 500000: 20012, 1000000: 27223},
                    (59, 59): {300000: 17919, 500000: 21013, 1000000: 28585},
                    (60, 60): {300000: 18815, 500000: 22064, 1000000: 30014}
                }
            },
            "Zone III": {
                "Without TPA": {
                    (0, 5): {300000: 3647, 500000: 4587, 1000000: 6601},
                    (6, 17): {300000: 3514, 500000: 4381, 1000000: 6281},
                    (18, 25): {300000: 5370, 500000: 6502, 1000000: 8841},
                    (26, 30): {300000: 6154, 500000: 7891, 1000000: 10711},
                    (31, 35): {300000: 6774, 500000: 8406, 1000000: 11505},
                    (36, 40): {300000: 6903, 500000: 8839, 1000000: 12115},
                    (41, 45): {300000: 7355, 500000: 9266, 1000000: 12617},
                    (46, 46): {300000: 7723, 500000: 9729, 1000000: 13248},
                    (47, 47): {300000: 8109, 500000: 10215, 1000000: 13910},
                    (48, 48): {300000: 8515, 500000: 10726, 1000000: 14606},
                    (49, 49): {300000: 8940, 500000: 11262, 1000000: 15336},
                    (50, 50): {300000: 9387, 500000: 11826, 1000000: 16103},
                    (51, 51): {300000: 9857, 500000: 12417, 1000000: 16908},
                    (52, 52): {300000: 10350, 500000: 13038, 1000000: 17754},
                    (53, 53): {300000: 10867, 500000: 13690, 1000000: 18641},
                    (54, 54): {300000: 11410, 500000: 14374, 1000000: 19573},
                    (55, 55): {300000: 11981, 500000: 15093, 1000000: 20552},
                    (56, 56): {300000: 12580, 500000: 15847, 1000000: 21580},
                    (57, 57): {300000: 13209, 500000: 16640, 1000000: 22659},
                    (58, 58): {300000: 13869, 500000: 17472, 1000000: 23792},
                    (59, 59): {300000: 14563, 500000: 18345, 1000000: 24981},
                    (60, 60): {300000: 15291, 500000: 19263, 1000000: 26230}
                },
                "With TPA": {
                    (0, 5): {300000: 3839, 500000: 4829, 1000000: 6949},
                    (6, 17): {300000: 3699, 500000: 4611, 1000000: 6611},
                    (18, 25): {300000: 5653, 500000: 6845, 1000000: 9306},
                    (26, 30): {300000: 6478, 500000: 8306, 1000000: 11275},
                    (31, 35): {300000: 7131, 500000: 8848, 1000000: 12111},
                    (36, 40): {300000: 7266, 500000: 9304, 1000000: 12752},
                    (41, 45): {300000: 7742, 500000: 9753, 1000000: 13281},
                    (46, 46): {300000: 8130, 500000: 10241, 1000000: 13945},
                    (47, 47): {300000: 8536, 500000: 10753, 1000000: 14643},
                    (48, 48): {300000: 8963, 500000: 11291, 1000000: 15375},
                    (49, 49): {300000: 9411, 500000: 11855, 1000000: 16143},
                    (50, 50): {300000: 9881, 500000: 12448, 1000000: 16951},
                    (51, 51): {300000: 10376, 500000: 13070, 1000000: 17798},
                    (52, 52): {300000: 10894, 500000: 13724, 1000000: 18688},
                    (53, 53): {300000: 11439, 500000: 14410, 1000000: 19622},
                    (54, 54): {300000: 12011, 500000: 15131, 1000000: 20604},
                    (55, 55): {300000: 12612, 500000: 15887, 1000000: 21634},
                    (56, 56): {300000: 13242, 500000: 16681, 1000000: 22715},
                    (57, 57): {300000: 13904, 500000: 17515, 1000000: 23851},
                    (58, 58): {300000: 14599, 500000: 18391, 1000000: 25044},
                    (59, 59): {300000: 15329, 500000: 19311, 1000000: 26296},
                    (60, 60): {300000: 16096, 500000: 20276, 1000000: 27611}
                }
            }
        }

        self.floater_rates = {
            "Zone I": {
                "Without TPA": {
                    "2A": {
                        (18, 25): {300000: 8569, 500000: 9829, 1000000: 13351},
                        (26, 30): {300000: 9886, 500000: 11875, 1000000: 16115},
                        (31, 35): {300000: 11484, 500000: 13170, 1000000: 17987},
                        (36, 40): {300000: 12746, 500000: 14250, 1000000: 19484},
                        (41, 45): {300000: 14448, 500000: 16377, 1000000: 22265}
                    },
                    "1A+1C": {
                        (18, 25): {300000: 8214, 500000: 9422, 1000000: 12798},
                        (26, 30): {300000: 9531, 500000: 11468, 1000000: 15562},
                        (31, 35): {300000: 10817, 500000: 12261, 1000000: 16757},
                        (36, 40): {300000: 11756, 500000: 13154, 1000000: 17969},
                        (41, 45): {300000: 12719, 500000: 14507, 1000000: 19690}
                    },
                    "1A+2C": {
                        (18, 25): {300000: 8963, 500000: 10282, 1000000: 13966},
                        (26, 30): {300000: 10280, 500000: 12328, 1000000: 16730},
                        (31, 35): {300000: 11655, 500000: 13222, 1000000: 18062},
                        (36, 40): {300000: 12594, 500000: 14115, 1000000: 19274},
                        (41, 45): {300000: 13823, 500000: 15773, 1000000: 21410}
                    },
                    "2A+1C": {
                        (18, 25): {300000: 9997, 500000: 11467, 1000000: 15576},
                        (26, 30): {300000: 11314, 500000: 13513, 1000000: 18340},
                        (31, 35): {300000: 13000, 500000: 14910, 1000000: 20350},
                        (36, 40): {300000: 14262, 500000: 15989, 1000000: 21847},
                        (41, 45): {300000: 16231, 500000: 18422, 1000000: 25042}
                    },
                    "2A+2C": {
                        (18, 25): {300000: 10746, 500000: 12327, 1000000: 16743},
                        (26, 30): {300000: 12063, 500000: 14373, 1000000: 19507},
                        (31, 35): {300000: 13838, 500000: 15871, 1000000: 21655},
                        (36, 40): {300000: 15100, 500000: 16950, 1000000: 23152},
                        (41, 45): {300000: 17335, 500000: 19689, 1000000: 26763}
                    }
                },
                "With TPA": {
                    "2A": {
                        (18, 25): {300000: 9020, 500000: 10347, 1000000: 14053},
                        (26, 30): {300000: 10406, 500000: 12500, 1000000: 16962},
                        (31, 35): {300000: 12088, 500000: 13864, 1000000: 18933},
                        (36, 40): {300000: 13417, 500000: 15000, 1000000: 20509},
                        (41, 45): {300000: 15209, 500000: 17239, 1000000: 23437}
                    },
                    "1A+1C": {
                        (18, 25): {300000: 8647, 500000: 9919, 1000000: 13471},
                        (26, 30): {300000: 10033, 500000: 12072, 1000000: 16381},
                        (31, 35): {300000: 11386, 500000: 12907, 1000000: 17638},
                        (36, 40): {300000: 12375, 500000: 13847, 1000000: 18914},
                        (41, 45): {300000: 13389, 500000: 15270, 1000000: 20726}
                    },
                    "1A+2C": {
                        (18, 25): {300000: 9435, 500000: 10823, 1000000: 14700},
                        (26, 30): {300000: 10822, 500000: 12977, 1000000: 17610},
                        (31, 35): {300000: 12268, 500000: 13919, 1000000: 19012},
                        (36, 40): {300000: 13257, 500000: 14859, 1000000: 20289},
                        (41, 45): {300000: 14551, 500000: 16604, 1000000: 22537}
                    },
                    "2A+1C": {
                        (18, 25): {300000: 10523, 500000: 12071, 1000000: 16395},
                        (26, 30): {300000: 11909, 500000: 14225, 1000000: 19304},
                        (31, 35): {300000: 13684, 500000: 15695, 1000000: 21420},
                        (36, 40): {300000: 15013, 500000: 16831, 1000000: 22996},
                        (41, 45): {300000: 17086, 500000: 19392, 1000000: 26361}
                    },
                    "2A+2C": {
                        (18, 25): {300000: 11312, 500000: 12976, 1000000: 17624},
                        (26, 30): {300000: 12698, 500000: 15129, 1000000: 20533},
                        (31, 35): {300000: 14566, 500000: 16706, 1000000: 22794},
                        (36, 40): {300000: 15895, 500000: 17843, 1000000: 24370},
                        (41, 45): {300000: 18248, 500000: 20725, 1000000: 28171}
                    }
                }
            },
            "Zone II": {
                "Without TPA": {
                    "2A": {
                        (18, 25): {300000: 8309, 500000: 9503, 1000000: 12915},
                        (26, 30): {300000: 9182, 500000: 11175, 1000000: 15172},
                        (31, 35): {300000: 9926, 500000: 11856, 1000000: 16199},
                        (36, 40): {300000: 10571, 500000: 12445, 1000000: 17037},
                        (41, 45): {300000: 11492, 500000: 13484, 1000000: 18372}
                    },
                    "1A+1C": {
                        (18, 25): {300000: 7965, 500000: 9110, 1000000: 12380},
                        (26, 30): {300000: 8838, 500000: 10782, 1000000: 14637},
                        (31, 35): {300000: 9388, 500000: 11060, 1000000: 15121},
                        (36, 40): {300000: 9908, 500000: 11600, 1000000: 15865},
                        (41, 45): {300000: 10327, 500000: 12059, 1000000: 16402}
                    },
                    "1A+2C": {
                        (18, 25): {300000: 8691, 500000: 9941, 1000000: 13510},
                        (26, 30): {300000: 9564, 500000: 11613, 1000000: 15767},
                        (31, 35): {300000: 10201, 500000: 11989, 1000000: 16383},
                        (36, 40): {300000: 10721, 500000: 12529, 1000000: 17127},
                        (41, 45): {300000: 11397, 500000: 13284, 1000000: 18066}
                    },
                    "2A+1C": {
                        (18, 25): {300000: 9693, 500000: 11087, 1000000: 15067},
                        (26, 30): {300000: 10566, 500000: 12759, 1000000: 17324},
                        (31, 35): {300000: 11396, 500000: 13538, 1000000: 18484},
                        (36, 40): {300000: 12042, 500000: 14126, 1000000: 19322},
                        (41, 45): {300000: 13221, 500000: 15461, 1000000: 21059}
                    },
                    "2A+2C": {
                        (18, 25): {300000: 10420, 500000: 11918, 1000000: 16197},
                        (26, 30): {300000: 11293, 500000: 13590, 1000000: 18454},
                        (31, 35): {300000: 12209, 500000: 14467, 1000000: 19747},
                        (36, 40): {300000: 12854, 500000: 15055, 1000000: 20585},
                        (41, 45): {300000: 14291, 500000: 16685, 1000000: 22724}
                    }
                },
                "With TPA": {
                    "2A": {
                        (18, 25): {300000: 8746, 500000: 10004, 1000000: 13594},
                        (26, 30): {300000: 9665, 500000: 11763, 1000000: 15970},
                        (31, 35): {300000: 10448, 500000: 12480, 1000000: 17051},
                        (36, 40): {300000: 11127, 500000: 13100, 1000000: 17934},
                        (41, 45): {300000: 12097, 500000: 14194, 1000000: 19340}
                    },
                    "1A+1C": {
                        (18, 25): {300000: 8384, 500000: 9590, 1000000: 13031},
                        (26, 30): {300000: 9303, 500000: 11349, 1000000: 15407},
                        (31, 35): {300000: 9882, 500000: 11642, 1000000: 15916},
                        (36, 40): {300000: 10430, 500000: 12210, 1000000: 16699},
                        (41, 45): {300000: 10870, 500000: 12694, 1000000: 17265}
                    },
                    "1A+2C": {
                        (18, 25): {300000: 9148, 500000: 10465, 1000000: 14220},
                        (26, 30): {300000: 10068, 500000: 12224, 1000000: 16596},
                        (31, 35): {300000: 10737, 500000: 12620, 1000000: 17245},
                        (36, 40): {300000: 11285, 500000: 13189, 1000000: 18029},
                        (41, 45): {300000: 11997, 500000: 13983, 1000000: 19017}
                    },
                    "2A+1C": {
                        (18, 25): {300000: 10203, 500000: 11671, 1000000: 15860},
                        (26, 30): {300000: 11123, 500000: 13431, 1000000: 18236},
                        (31, 35): {300000: 11996, 500000: 14251, 1000000: 19457},
                        (36, 40): {300000: 12675, 500000: 14870, 1000000: 20339},
                        (41, 45): {300000: 13916, 500000: 16275, 1000000: 22168}
                    },
                    "2A+2C": {
                        (18, 25): {300000: 10968, 500000: 12546, 1000000: 17049},
                        (26, 30): {300000: 11888, 500000: 14305, 1000000: 19425},
                        (31, 35): {300000: 12851, 500000: 15229, 1000000: 20786},
                        (36, 40): {300000: 13530, 500000: 15848, 1000000: 21669},
                        (41, 45): {300000: 15043, 500000: 17564, 1000000: 23920}
                    }
                }
            },
            "Zone III": {
                "Without TPA": {
                    "2A": {
                        (18, 25): {300000: 6781, 500000: 8210, 1000000: 11164},
                        (26, 30): {300000: 7565, 500000: 9599, 1000000: 13034},
                        (31, 35): {300000: 8432, 500000: 10532, 1000000: 14391},
                        (36, 40): {300000: 8728, 500000: 11104, 1000000: 15215},
                        (41, 45): {300000: 9723, 500000: 12298, 1000000: 16772}
                    },
                    "1A+1C": {
                        (18, 25): {300000: 6500, 500000: 7870, 1000000: 10701},
                        (26, 30): {300000: 7284, 500000: 9259, 1000000: 12571},
                        (31, 35): {300000: 7974, 500000: 9859, 1000000: 13481},
                        (36, 40): {300000: 8103, 500000: 10292, 1000000: 14091},
                        (41, 45): {300000: 8766, 500000: 10974, 1000000: 14940}
                    },
                    "1A+2C": {
                        (18, 25): {300000: 7093, 500000: 8588, 1000000: 11678},
                        (26, 30): {300000: 7877, 500000: 9977, 1000000: 13548},
                        (31, 35): {300000: 8637, 500000: 10662, 1000000: 14572},
                        (36, 40): {300000: 8766, 500000: 11095, 1000000: 15182},
                        (41, 45): {300000: 9640, 500000: 12032, 1000000: 16378}
                    },
                    "2A+1C": {
                        (18, 25): {300000: 7911, 500000: 9578, 1000000: 13024},
                        (26, 30): {300000: 8695, 500000: 10967, 1000000: 14894},
                        (31, 35): {300000: 9632, 500000: 11985, 1000000: 16366},
                        (36, 40): {300000: 9928, 500000: 12557, 1000000: 17190},
                        (41, 45): {300000: 11133, 500000: 14006, 1000000: 19095}
                    },
                    "2A+2C": {
                        (18, 25): {300000: 8504, 500000: 10296, 1000000: 14000},
                        (26, 30): {300000: 9288, 500000: 11685, 1000000: 15870},
                        (31, 35): {300000: 10295, 500000: 12788, 1000000: 17458},
                        (36, 40): {300000: 10591, 500000: 13359, 1000000: 18282},
                        (41, 45): {300000: 12007, 500000: 15064, 1000000: 20533}
                    }
                },
                "With TPA": {
                    "2A": {
                        (18, 25): {300000: 7138, 500000: 8643, 1000000: 11751},
                        (26, 30): {300000: 7963, 500000: 10104, 1000000: 13720},
                        (31, 35): {300000: 8876, 500000: 11086, 1000000: 15149},
                        (36, 40): {300000: 9187, 500000: 11688, 1000000: 16015},
                        (41, 45): {300000: 10235, 500000: 12945, 1000000: 17655}
                    },
                    "1A+1C": {
                        (18, 25): {300000: 6842, 500000: 8285, 1000000: 11265},
                        (26, 30): {300000: 7668, 500000: 9747, 1000000: 13234},
                        (31, 35): {300000: 8394, 500000: 10378, 1000000: 14191},
                        (36, 40): {300000: 8529, 500000: 10834, 1000000: 14832},
                        (41, 45): {300000: 9227, 500000: 11551, 1000000: 15726}
                    },
                    "1A+2C": {
                        (18, 25): {300000: 7467, 500000: 9041, 1000000: 12293},
                        (26, 30): {300000: 8292, 500000: 10502, 1000000: 14261},
                        (31, 35): {300000: 9092, 500000: 11223, 1000000: 15339},
                        (36, 40): {300000: 9227, 500000: 11679, 1000000: 15981},
                        (41, 45): {300000: 10147, 500000: 12665, 1000000: 17240}
                    },
                    "2A+1C": {
                        (18, 25): {300000: 8327, 500000: 10083, 1000000: 13710},
                        (26, 30): {300000: 9153, 500000: 11545, 1000000: 15679},
                        (31, 35): {300000: 10139, 500000: 12616, 1000000: 17228},
                        (36, 40): {300000: 10450, 500000: 13218, 1000000: 18095},
                        (41, 45): {300000: 11720, 500000: 14743, 1000000: 20100}
                    },
                    "2A+2C": {
                        (18, 25): {300000: 8952, 500000: 10839, 1000000: 14737},
                        (26, 30): {300000: 9777, 500000: 12301, 1000000: 16706},
                        (31, 35): {300000: 10837, 500000: 13461, 1000000: 18377},
                        (36, 40): {300000: 11148, 500000: 14063, 1000000: 19244},
                        (41, 45): {300000: 12639, 500000: 15856, 1000000: 21614}
                    }
                }
            }
        }

        # GUI setup
        self.setup_gui()

    def center_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - 800) // 2
        y = (screen_height - 700) // 2
        self.root.geometry(f"800x700+{x}+{y}")

    def setup_gui(self):
        # Fonts
        title_font = ("Arial", 16, "bold")
        label_font = ("Arial", 10)
        button_font = ("Arial", 10, "bold")

        # Main frame
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=2)  # Reduced pady

        # Title
        ttk.Label(self.main_frame, text="National Young India Mediclaim Policy", font=title_font).pack(pady=2)

        # Input frame
        self.input_frame = ttk.Frame(self.main_frame)
        self.input_frame.pack(fill="x", pady=2)  # Reduced pady

        # Policy Type
        ttk.Label(self.input_frame, text="Policy Type:", font=label_font).grid(row=0, column=0, padx=5, pady=2, sticky="e")
        self.policy_type = ttk.Combobox(self.input_frame, values=["Individual", "Floater"], state="readonly", width=20)
        self.policy_type.grid(row=0, column=1, padx=5, pady=2)
        self.policy_type.current(0)
        self.policy_type.bind("<<ComboboxSelected>>", self.toggle_policy_type)

        # Zone
        ttk.Label(self.input_frame, text="Zone:", font=label_font).grid(row=1, column=0, padx=5, pady=2, sticky="e")
        self.zone = ttk.Combobox(self.input_frame, values=["Zone I", "Zone II", "Zone III"], state="readonly", width=20)
        self.zone.grid(row=1, column=1, padx=5, pady=2)
        self.zone.current(0)

        # TPA
        ttk.Label(self.input_frame, text="TPA Charges:", font=label_font).grid(row=2, column=0, padx=5, pady=2, sticky="e")
        self.tpa = ttk.Combobox(self.input_frame, values=["With TPA", "Without TPA"], state="readonly", width=20)
        self.tpa.grid(row=2, column=1, padx=5, pady=2)
        self.tpa.current(1)

        # Double SI
        self.double_si_var = tk.BooleanVar()
        ttk.Checkbutton(self.input_frame, text="Double SI for 11 Critical Illness", variable=self.double_si_var).grid(row=3, column=0, columnspan=2, padx=5, pady=2, sticky="w")

        # Individual input frame
        self.individual_frame = ttk.Frame(self.main_frame)
        self.individual_frame.pack(fill="x", expand=False, pady=2)  # No expansion, reduced pady

        # Family members table
        self.table_frame = ttk.Frame(self.individual_frame)
        self.table_frame.pack(fill="both", expand=False)

        columns = ("Name", "Age", "Gender", "Relationship", "Sum Insured", "Premium")
        self.tree = ttk.Treeview(self.table_frame, columns=columns, show="headings", height=6)  # Unchanged, satisfactory
        self.tree.heading("Name", text="Name")
        self.tree.heading("Age", text="Age")
        self.tree.heading("Gender", text="Gender")
        self.tree.heading("Relationship", text="Relationship")
        self.tree.heading("Sum Insured", text="Sum Insured")
        self.tree.heading("Premium", text="Premium")
        self.tree.column("Name", width=150)
        self.tree.column("Age", width=50)
        self.tree.column("Gender", width=80)
        self.tree.column("Relationship", width=100)
        self.tree.column("Sum Insured", width=100)
        self.tree.column("Premium", width=100)
        self.tree.pack(fill="both", expand=False)

        # Input row for adding members
        self.entry_frame = ttk.Frame(self.individual_frame)
        self.entry_frame.pack(fill="x", pady=2)  # Reduced pady

        self.name_entry = ttk.Entry(self.entry_frame, width=20)
        self.name_entry.grid(row=0, column=0, padx=2)
        self.age_entry = ttk.Entry(self.entry_frame, width=8)
        self.age_entry.grid(row=0, column=1, padx=2)
        self.gender_combo = ttk.Combobox(self.entry_frame, values=["Male", "Female"], state="readonly", width=10)
        self.gender_combo.grid(row=0, column=2, padx=2)
        self.relationship_combo = ttk.Combobox(self.entry_frame, values=["Self", "Spouse", "Son", "Daughter", "Father", "Mother"], state="readonly", width=12)
        self.relationship_combo.grid(row=0, column=3, padx=2)
        self.si_combo = ttk.Combobox(self.entry_frame, values=["300000", "500000", "1000000"], state="readonly", width=12)
        self.si_combo.grid(row=0, column=4, padx=2)
        self.diabetic_var = tk.BooleanVar()
        ttk.Checkbutton(self.entry_frame, text="Diabetic", variable=self.diabetic_var).grid(row=0, column=5, padx=2)
        self.hypertension_var = tk.BooleanVar()
        ttk.Checkbutton(self.entry_frame, text="Hypertension", variable=self.hypertension_var).grid(row=0, column=6, padx=2)

        # Buttons
        self.button_frame = ttk.Frame(self.individual_frame)
        self.button_frame.pack(fill="x", pady=2)  # Reduced pady
        ttk.Button(self.button_frame, text="Add Row", command=self.add_row, style="TButton").pack(side="left", padx=5)
        ttk.Button(self.button_frame, text="Calculate Premium", command=self.calculate_premium, style="TButton").pack(side="left", padx=5)
        ttk.Button(self.button_frame, text="Reset", command=self.reset, style="TButton").pack(side="left", padx=5)

        # Floater input frame
        self.floater_frame = ttk.Frame(self.main_frame)

        ttk.Label(self.floater_frame, text="Family Category:", font=label_font).grid(row=0, column=0, padx=5, pady=2, sticky="e")
        self.family_category = ttk.Combobox(self.floater_frame, values=["2A", "1A+1C", "1A+2C", "2A+1C", "2A+2C"], state="readonly", width=20)
        self.family_category.grid(row=0, column=1, padx=5, pady=2)
        self.family_category.current(0)

        ttk.Label(self.floater_frame, text="Age of Senior Most Member:", font=label_font).grid(row=1, column=0, padx=5, pady=2, sticky="e")
        self.senior_age_entry = ttk.Entry(self.floater_frame, width=23)
        self.senior_age_entry.grid(row=1, column=1, padx=5, pady=2)

        ttk.Label(self.floater_frame, text="Sum Insured:", font=label_font).grid(row=2, column=0, padx=5, pady=2, sticky="e")
        self.floater_si = ttk.Combobox(self.floater_frame, values=["300000", "500000", "1000000"], state="readonly", width=20)
        self.floater_si.grid(row=2, column=1, padx=5, pady=2)
        self.floater_si.current(0)

        self.floater_diabetic_var = tk.BooleanVar()
        ttk.Checkbutton(self.floater_frame, text="Diabetic", variable=self.floater_diabetic_var).grid(row=3, column=0, columnspan=2, padx=5, pady=2, sticky="w")
        self.floater_hypertension_var = tk.BooleanVar()
        ttk.Checkbutton(self.floater_frame, text="Hypertension", variable=self.floater_hypertension_var).grid(row=4, column=0, columnspan=2, padx=5, pady=2, sticky="w")

        # Floater buttons
        self.floater_button_frame = ttk.Frame(self.floater_frame)
        self.floater_button_frame.grid(row=5, column=0, columnspan=2, pady=2)
        ttk.Button(self.floater_button_frame, text="Calculate Premium", command=self.calculate_premium, style="TButton").pack(side="left", padx=5)
        ttk.Button(self.floater_button_frame, text="Reset", command=self.reset, style="TButton").pack(side="left", padx=5)

        # Fix geometry manager issue
        self.floater_frame.pack(fill="x", pady=2)

        # Output Treeview (compact, no cutoff)
        self.output_frame = ttk.Frame(self.main_frame)
        self.output_frame.pack(fill="x", expand=False, pady=2)  # No expansion, reduced pady
        self.output_tree = ttk.Treeview(self.output_frame, columns=("Description", "Amount"), show="headings", height=8)  # Unchanged height
        self.output_tree.heading("Description", text="Description")
        self.output_tree.heading("Amount", text="Amount (₹)")
        self.output_tree.column("Description", width=400)
        self.output_tree.column("Amount", width=150)
        self.output_tree.pack(fill="x", expand=False)  # No expansion

        # Style
        style = ttk.Style()
        style.configure("TButton", font=button_font)
        style.configure("Treeview", font=label_font, rowheight=20)  # Compact rows
        style.configure("Treeview.Heading", font=label_font)

        # Initialize with two rows
        self.rows = []
        self.add_row()
        self.add_row()

        # Show individual frame by default
        self.toggle_policy_type()

    def toggle_policy_type(self, event=None):
        policy_type = self.policy_type.get()
        if policy_type == "Individual":
            self.floater_frame.pack_forget()
            self.individual_frame.pack(fill="x", expand=False, pady=2)
        else:
            self.individual_frame.pack_forget()
            self.floater_frame.pack(fill="x", pady=2)

    def add_row(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        gender = self.gender_combo.get()
        relationship = self.relationship_combo.get()
        sum_insured = self.si_combo.get()
        diabetic = self.diabetic_var.get()
        hypertension = self.hypertension_var.get()

        if not all([name, age, gender, relationship, sum_insured]):
            return

        try:
            age = int(age)
            sum_insured = int(sum_insured)
            if age < 0 or age > 60:
                messagebox.showerror("Error", f"Age must be between 0 and 60 for {name}")
                return
            if age > 43:
                messagebox.showwarning("Age Warning", "Entry age exceeds 43 Years")
        except ValueError:
            messagebox.showerror("Error", "Age and Sum Insured must be valid numbers")
            return

        item_id = str(uuid.uuid4())
        self.tree.insert("", "end", iid=item_id, values=(
            name, age, gender, relationship, sum_insured, ""
        ))
        self.rows.append({
            "iid": item_id,
            "name": name,
            "age": age,
            "gender": gender,
            "relationship": relationship,
            "sum_insured": sum_insured,
            "diabetic": diabetic,
            "hypertension": hypertension
        })

        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.gender_combo.set("")
        self.relationship_combo.set("")
        self.si_combo.set("")
        self.diabetic_var.set(False)
        self.hypertension_var.set(False)

    def calculate_premium(self):
        self.output_tree.delete(*self.output_tree.get_children())
        policy_type = self.policy_type.get()
        zone = self.zone.get()
        tpa = self.tpa.get()
        double_si = self.double_si_var.get()

        total_premium = 0
        breakdown = []

        if policy_type == "Individual":
            if not self.rows:
                messagebox.showerror("Error", "Please add at least one family member")
                return

            for row in self.rows:
                age = row["age"]
                sum_insured = row["sum_insured"]
                diabetic = row["diabetic"]
                hypertension = row["hypertension"]
                name = row["name"]

                # Find age band
                for (start, end), rates in self.individual_rates[zone][tpa].items():
                    if start <= age <= end:
                        base_premium = rates[sum_insured]
                        break
                else:
                    messagebox.showerror("Error", f"Invalid age {age} for {name}")
                    return

                # Apply diabetic/hypertension loadings
                loading = 0
                if diabetic and hypertension:
                    loading = base_premium * 0.15
                    breakdown.append((f"Diabetic+Hypertension Loading (15%) for {name}", f"+{loading:.2f}"))
                elif diabetic or hypertension:
                    loading = base_premium * 0.10
                    breakdown.append((f"{'Diabetic' if diabetic else 'Hypertension'} Loading (10%) for {name}", f"+{loading:.2f}"))

                member_premium = base_premium + loading
                breakdown.append((f"Premium for {name}", f"{base_premium:.2f}"))
                total_premium += member_premium

                # Update tree
                self.tree.set(row["iid"], "Premium", f"{member_premium:.2f}")

        else:  # Floater
            category = self.family_category.get()
            age_str = self.senior_age_entry.get()
            sum_insured = int(self.floater_si.get())
            diabetic = self.floater_diabetic_var.get()
            hypertension = self.floater_hypertension_var.get()

            if not all([category, age_str, sum_insured]):
                messagebox.showerror("Error", "Please fill all floater fields")
                return

            try:
                age = int(age_str)
                if age < 18 or age > 45:
                    messagebox.showerror("Error", "Age must be between 18 and 45 for floater policy")
                    return
                if age > 43:
                    messagebox.showwarning("Age Warning", "Entry age exceeds 43 Years")
            except ValueError:
                messagebox.showerror("Error", "Age must be a valid number")
                return

            # Find age band
            base_premium = None
            for (start, end), rates in self.floater_rates[zone][tpa][category].items():
                if start <= age <= end:
                    base_premium = rates[sum_insured]
                    break
            if base_premium is None:
                messagebox.showerror("Error", f"Invalid age {age} for floater policy")
                return

            # Apply diabetic/hypertension loadings
            loading = 0
            if diabetic and hypertension:
                loading = base_premium * 0.15
                breakdown.append(("Diabetic+Hypertension Loading (15%)", f"+{loading:.2f}"))
            elif diabetic or hypertension:
                loading = base_premium * 0.10
                breakdown.append((f"{'Diabetic' if diabetic else 'Hypertension'} Loading (10%)", f"+{loading:.2f}"))

            total_premium = base_premium + loading
            breakdown.append(("Base Premium", f"{base_premium:.2f}"))

        # Apply Double SI loading
        if double_si:
            double_si_loading = total_premium * 0.18
            total_premium += double_si_loading
            breakdown.append(("Double SI Loading (18%)", f"+{double_si_loading:.2f}"))

        # Apply GST
        gst = total_premium * 0.18
        total_premium += gst
        breakdown.append(("GST (18%)", f"+{gst:.2f}"))
        breakdown.append(("Final Premium", f"{total_premium:.2f}"))

        # Update output tree
        for desc, amount in breakdown:
            self.output_tree.insert("", "end", values=(desc, amount))

    def reset(self):
        self.policy_type.current(0)
        self.zone.current(0)
        self.tpa.current(1)
        self.double_si_var.set(False)
        self.tree.delete(*self.tree.get_children())
        self.output_tree.delete(*self.output_tree.get_children())
        self.rows = []
        self.add_row()
        self.add_row()
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.gender_combo.set("")
        self.relationship_combo.set("")
        self.si_combo.set("")
        self.diabetic_var.set(False)
        self.hypertension_var.set(False)
        self.family_category.current(0)
        self.senior_age_entry.delete(0, tk.END)
        self.floater_si.current(0)
        self.floater_diabetic_var.set(False)
        self.floater_hypertension_var.set(False)
        self.toggle_policy_type()

if __name__ == "__main__":
    root = tk.Tk()
    app = InsuranceCalculator(root)
    root.mainloop()