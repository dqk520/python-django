#coding=UTF-8
import sys  
reload(sys)  
sys.setdefaultencoding('utf8') 
from django.db import models
from django.db.models.query import QuerySet

class Publisher(models.Model):
    name = models.CharField(db_column='name',max_length=40)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()	
    def __unicode__(self):
       return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
    def __unicode__(self):
        return self.title
		
class Mima(models.Model):
    mimabh = models.CharField(db_column='员工编号', max_length=255, blank=True, null=True)
    mimagh = models.CharField(db_column='工号', max_length=255, blank=True, null=True)
    mimaxm = models.CharField(db_column='姓名', max_length=255, blank=True, null=True)
    mimasf = models.CharField(db_column='身份证号', max_length=255, blank=True, null=True) 
    mimayh = models.CharField(db_column='银行卡号', max_length=255, blank=True, null=True)
    mimamm = models.CharField(db_column='密码', max_length=255, blank=True, null=True)
	
    class Meta:
        managed = False
        db_table = 'mima'
		
    def toJSON(self):
        import json
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))
		
	
class Gzzb3(models.Model):
    gz1 = models.FloatField(db_column='时间', blank=True, null=True)  
    gz2 = models.FloatField(db_column='代扣税', blank=True, null=True)  
    gz3 = models.FloatField(db_column='实际扣税', blank=True, null=True)  
    gz4 = models.FloatField(db_column='实发工资', blank=True, null=True)  
    gz5 = models.FloatField(db_column='实发工资2', blank=True, null=True)  
    gz6 = models.FloatField(db_column='应发工资总', blank=True, null=True)  
    gz7 = models.FloatField(db_column='实发工资总', blank=True, null=True)  
    gz8 = models.CharField(db_column='身份证号码', max_length=255, blank=True, null=True)  
    gz9 = models.FloatField(db_column='员工编号', blank=True, null=True)  
    gz10 = models.CharField(db_column='银行号', max_length=255, blank=True, null=True)  
    gz11 = models.CharField(db_column='上海缴纳个税', max_length=255, blank=True, null=True)  
    gz12 = models.FloatField(db_column='表2绩效', blank=True, null=True)  
    gz13 = models.FloatField(db_column='表1绩效', blank=True, null=True)  
    gz14 = models.FloatField(db_column='普通加班费', blank=True, null=True)  
    gz15 = models.FloatField(db_column='2倍加班费', blank=True, null=True)  
    gz16 = models.FloatField(db_column='法定加班费', blank=True, null=True)  
    gz17 = models.FloatField(db_column='社保', blank=True, null=True)  
    gz18 = models.FloatField(db_column='表1病假扣', blank=True, null=True)  
    gz19 = models.FloatField(db_column='表2病假扣', blank=True, null=True)  
    gz20 = models.FloatField(db_column='表1事假扣', blank=True, null=True)  
    gz21 = models.FloatField(db_column='表2事假扣', blank=True, null=True)  
    gz22 = models.FloatField(db_column='表1轮休扣', blank=True, null=True)  
    gz23 = models.FloatField(db_column='表2轮休扣', blank=True, null=True)  
    gz24 = models.FloatField(db_column='其他扣', blank=True, null=True)  
    gz25 = models.FloatField(db_column='表2扣', blank=True, null=True)  
    gz26 = models.FloatField(db_column='绩效增减', blank=True, null=True)  
    gz27 = models.FloatField(db_column='起征点', blank=True, null=True)  
    gz28 = models.FloatField(db_column='法定和2倍加班费', blank=True, null=True)  
    gz29 = models.FloatField(db_column='轮休和其他扣', blank=True, null=True)  
    gz30 = models.FloatField(db_column='病事假扣', blank=True, null=True)  
    gz31 = models.FloatField(db_column='应发工资', blank=True, null=True)  
    gz32 = models.FloatField(db_column='纳税工资', blank=True, null=True)  
    gz33 = models.CharField(db_column='基地', max_length=255, blank=True, null=True)  
    gz34 = models.CharField(db_column='单位号', max_length=255, blank=True, null=True)  
    gz35 = models.FloatField(db_column='加班基数', blank=True, null=True)  
    gz36 = models.CharField(db_column='单位', max_length=255, blank=True, null=True)  
    gz37 = models.CharField(db_column='工号', max_length=255, blank=True, null=True)  
    gz38 = models.CharField(db_column='姓名', max_length=255, blank=True, null=True)  
    gz39 = models.FloatField(db_column='缺勤', blank=True, null=True)  
    gz40 = models.FloatField(db_column='加班日', blank=True, null=True)  
    gz41 = models.FloatField(db_column='二倍日', blank=True, null=True)  
    gz42 = models.FloatField(db_column='出勤', blank=True, null=True)  
    gz43 = models.FloatField(db_column='法定日', blank=True, null=True)  
    gz44 = models.FloatField(db_column='病假日', blank=True, null=True)  
    gz45 = models.CharField(db_column='病假3月', max_length=255, blank=True, null=True)  
    gz46 = models.FloatField(db_column='其他日', blank=True, null=True)  
    gz47 = models.FloatField(db_column='轮休日', blank=True, null=True)  
    gz48 = models.FloatField(db_column='工资标准', blank=True, null=True)  
    gz49 = models.FloatField(db_column='岗位工资', blank=True, null=True)  
    gz50 = models.FloatField(db_column='绩效工资', blank=True, null=True)  
    gz51 = models.FloatField(db_column='绩效增减1', blank=True, null=True)  
    gz52 = models.FloatField(db_column='绩效增减2', blank=True, null=True)  
    gz53 = models.FloatField(db_column='职务', blank=True, null=True)  
    gz54 = models.FloatField(db_column='驻岛', blank=True, null=True)  
    gz55 = models.FloatField(db_column='工龄', blank=True, null=True)  
    gz56 = models.FloatField(db_column='伙食补贴', blank=True, null=True)  
    gz57 = models.FloatField(db_column='中夜班津贴', blank=True, null=True)  
    gz58 = models.FloatField(db_column='节日费', blank=True, null=True)  
    gz59 = models.FloatField(db_column='综合栏1', blank=True, null=True)  
    gz60 = models.FloatField(db_column='综合栏2', blank=True, null=True)  
    gz61 = models.FloatField(db_column='水电费', blank=True, null=True)  
    gz62 = models.FloatField(db_column='养老费', blank=True, null=True)  
    gz63 = models.FloatField(db_column='医疗', blank=True, null=True)  
    gz64 = models.FloatField(db_column='失保', blank=True, null=True)  
    gz65 = models.FloatField(db_column='公积金', blank=True, null=True)  
    gz66 = models.FloatField(db_column='扣发', blank=True, null=True)  
    gz67 = models.FloatField(db_column='饭贴基数', blank=True, null=True)  
    gz68 = models.CharField(db_column='分类', max_length=255, blank=True, null=True)  
    gz69 = models.FloatField(db_column='通讯费', blank=True, null=True)  
    gz70 = models.CharField(db_column='岗位', max_length=255, blank=True, null=True)  
    gz71 = models.CharField(db_column='学历', max_length=255, blank=True, null=True)  
    gz72 = models.CharField(db_column='入司时间', max_length=255, blank=True, null=True)  
    gz73 = models.CharField(db_column='家庭住址', max_length=255, blank=True, null=True)  
    gz74 = models.CharField(db_column='转正日期', max_length=255, blank=True, null=True)  
    gz75 = models.FloatField(db_column='性别', blank=True, null=True)  
    gz76 = models.CharField(db_column='序列号', max_length=255, blank=True, null=True)  
    gz77 = models.CharField(db_column='社保编号', max_length=255, blank=True, null=True)  
    gz78 = models.CharField(db_column='公积金编号', max_length=255, blank=True, null=True)  
    gz79 = models.FloatField(db_column='学历补贴', blank=True, null=True)  
    gz80 = models.FloatField(db_column='职称补贴', blank=True, null=True)  
    gz81 = models.FloatField(db_column='特技补贴', blank=True, null=True)  
    gz82 = models.FloatField(db_column='岗位补贴', blank=True, null=True)  
    gz83 = models.FloatField(db_column='津贴合计', blank=True, null=True)  
    gz84 = models.CharField(db_column='工资制', max_length=255, blank=True, null=True)  
	
    class Meta:
        managed = False
        db_table = 'gzzb3'
		