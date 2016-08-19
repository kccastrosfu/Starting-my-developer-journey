#CMPT 120 
######################################################
#Define the function cookies(n) to solve the following problem:
#A company packages and sells boxes with cookies. The boxes come in two sizes: huge and small. The “huge” box contains 48 cookies and the “small” box contains 8 cookies. The company makes the most gain by selling huge boxes: CDN$26 each. Small boxes produce less gain but still some: a small box provides the company CDN$4 gain. On the other hand, the company loses CDN$ 2 per cookie not used. Thus, the company will attempt to package as many huge boxes as possible, and then as many small boxes as possible.
#This function receives as input in the parameter variable a number of cookies available and it should return a string with the following information: first, the number of huge boxes to package, followed by two dots ("..") followed by the number of small boxes to package, followed again by two dots, followed by the number of unused cookies, followed by two dots and finally the money the company makes, considering the gains (because of the boxes packaged) minus the losses (because of the unused cookies).
#For example, calling this function as cookies(503) should return '10..2..7..254 ', because with 503 cookies the company can package 10 huge boxes, 2 small boxes and there are 7 unused cookies. The company makes CDN$ 254, that is, CDN$26 * 10 = CDN$ 260 because of the 10 huge boxes plus CDN$ 4 *2= CDN$ 8 minus CDN$ 2 * 7 = CDN$6 (the seven unused cookies).
#Notice that the company may have a net loss, when there are not enough cookies to create any package.
#
#For example:
#cookies(7) should return '0..0..7..-14'
#
#As an example, the following code fragment:
#print (cookies(503))
#should produce the output:
#10..2..7..254
#######################################################
num=100

def cookies(num):
    if num < 0: num = 0
    huge_box = num // 48
    left_ov_hugebox = num%48
    small_box = left_ov_hugebox//8
    left_ov_smallbox = left_ov_hugebox%8
    huge_proft = huge_box*26
    small_proft = small_box*4
    net_loss = left_ov_smallbox*2
    net_profit = huge_proft + small_proft - net_loss
    dots = ".."
    return (str( huge_box ) + dots + str( small_box ) + dots + str( left_ov_smallbox )+ dots + str( net_profit ))

cookies(num)
