import unittest
from captcha import resolveCaptcha, resolveCaptchaTwo, resolveCaptchaTwo_solB


class TestResolveCaptcha(unittest.TestCase):

    def test_resolve_function_is_working(self):
        self.assertEqual(resolveCaptcha(""), 0)

    def test_no_match(self):
        self.assertEqual(resolveCaptcha(""), 0)
        self.assertEqual(resolveCaptcha("4321"), 0)
        self.assertEqual(resolveCaptcha("1234"), 0)
        self.assertEqual(resolveCaptcha("5234"), 0)

    def test_simple_match(self):
        self.assertEqual(resolveCaptcha("1122"), 3)
        self.assertEqual(resolveCaptcha("2233"), 5)
        self.assertEqual(resolveCaptcha("5511"), 6)
        self.assertEqual(resolveCaptcha("7733"), 10)

    def test_same_numbers_match(self):
        self.assertEqual(resolveCaptcha("1111"), 4)
        self.assertEqual(resolveCaptcha("2222"), 8)
        self.assertEqual(resolveCaptcha("3333"), 12)
        self.assertEqual(resolveCaptcha("7777"), 28)
        self.assertEqual(resolveCaptcha("7777"), 28)

    def test_single_circle_match(self):
        self.assertEqual(resolveCaptcha("1451"), 1)
        self.assertEqual(resolveCaptcha("2562"), 2)
        self.assertEqual(resolveCaptcha("3453"), 3)
        self.assertEqual(resolveCaptcha("91212129"), 9)

    def test_captcha_match(self):
        self.assertEqual(resolveCaptcha("911219"), 10)
        self.assertEqual(resolveCaptcha("21311332"), 6)


class TestResolveCaptchaTwo(unittest.TestCase):

    def test_resolve_function_is_working(self):
        self.assertEqual(resolveCaptchaTwo(""), 0)

    def test_no_match(self):
        self.assertEqual(resolveCaptchaTwo(""), 0)
        self.assertEqual(resolveCaptchaTwo("1221"), 0)
        self.assertEqual(resolveCaptchaTwo("1334"), 0)
        self.assertEqual(resolveCaptchaTwo("123456"), 0)
        self.assertEqual(resolveCaptchaTwo("1122"), 0)

    def test_simple_match(self):
        self.assertEqual(resolveCaptchaTwo("1212"), 6)
        self.assertEqual(resolveCaptchaTwo("2121"), 6)
        self.assertEqual(resolveCaptchaTwo("123425"), 4)
        self.assertEqual(resolveCaptchaTwo("123123"), 12)

    def test_captcha_match(self):
        self.assertEqual(resolveCaptchaTwo("12131415"), 4)


class TestResolveCaptchaTwo(unittest.TestCase):

    def test_resolve_function_is_working(self):
        self.assertEqual(resolveCaptchaTwo_solB(""), 0)

    def test_no_match(self):
        self.assertEqual(resolveCaptchaTwo_solB(""), 0)
        self.assertEqual(resolveCaptchaTwo_solB("1221"), 0)
        self.assertEqual(resolveCaptchaTwo_solB("1334"), 0)
        self.assertEqual(resolveCaptchaTwo_solB("123456"), 0)
        self.assertEqual(resolveCaptchaTwo_solB("1122"), 0)

    def test_simple_match(self):
        self.assertEqual(resolveCaptchaTwo_solB("1212"), 6)
        self.assertEqual(resolveCaptchaTwo_solB("2121"), 6)
        self.assertEqual(resolveCaptchaTwo_solB("123425"), 4)
        self.assertEqual(resolveCaptchaTwo_solB("123123"), 12)

    def test_captcha_match(self):
        self.assertEqual(resolveCaptchaTwo_solB("12131415"), 4)

print("----- PUZZLE SUM: Part one ------")
puzzle = "878938232157342756754254716586975125394865297349321236586574662994429894259828536842781199252169182743449435231194436368218599463391544461745472922916562414854275449983442828344463893618282425242643322822916857935242141636187859919626885791572268272442711988367762865741341467274718149255173686839265874184176985561996454253165784192929453678326937728571781212155346592432874244741816166328693958529938367575669663228335566435273484331452883175981955679335327231995452231118936393192583338222595982522833468533262224874637449624644318418748617949417939228988293391941457722641936417456243894182668197174255786445994567477582715692336249243254711653529871336129825735249667425238573952339922948214218872417858525199642194588448543565474847272984232637466664695217176358283788781843171636841215675851778984619377575696447366844854289534215286959727688419731976631323833892247438149829975856161755122857643731945913335556288817112993911694972667656914238999291831997163412548977649491227219477796124134958527843213824792685117696631512141241496451845758655276186597724748432996276498527911292531185292149948139724345841584782352214921634858734671118495424143437282979243347831258285851259579133433182387444656386679831584933397915132785411686688447731696776459621924821667112751789884987883991845818513249994767543526169463766975791464756526911587399764736557959464923353896921342944821833991457125256329564489631352268722457628514564128231487382111682976886838192412996932924373337524262135399256658638418515239876732866596731888779532573243713128238419234963195589987539467221517535272384899524386267268959484881379944796392255419838743164714275463459351741296586465213689853743856518583451849661592844879264196761867481258778393623584884535246239794178981387632311238115362178576899121425428114696158652976277392224226268242332589546757477683398264294929442592131949398261884548427951472128841328376819241955153423452531538413492577262348369581399925647624623868299468436859667152463974949436359589931136236247929554899679139746162554183855278713574244211854227829969443151478986413333429144796664423754818256172862812877688675514142265239992529776262844329188218189254491238956497568"
print("result = " + str(resolveCaptcha(puzzle)))

print("----- PUZZLE SUM: Part two ------")
print("result = " + str(resolveCaptchaTwo(puzzle)))

print("----- PUZZLE SUM: Part two (with solution B) ------")
print("result = " + str(resolveCaptchaTwo_solB(puzzle)))

if __name__ == '__main__':
    unittest.main()
