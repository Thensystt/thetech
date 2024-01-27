# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

html_content = """
<div class="section__common_wrap">
        <div class="section__title">
            <h3></h3>
            <div class="desc__medium"></div>
        </div>
                <div class="section__common_inner section__wide_inner">
            <div class="section__title">
                <h3>Смешанное (накопительное) страхование</h3>
            </div>
            <div class="dropdown__tablet_block">
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 01 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 01 ? accordion = 01 : accordion = null">
                                    В чем разница между накоплением денег на депозите в банке и покупкой полиса?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer01" :style="accordion == 01 ? 'max-height: ' + $refs.accordioncontainer01.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Если Вы хотите получить максимальный процент накопления в относительно короткие сроки, то Вам необходимо обратиться в Банк. Если в Ваши планы входит накопление денег на учебу детей, свадьбу, обеспечение пенсией старости и т.д., то предпочтительнее обратиться в компанию по страхованию жизни.</p>

<p>В отличии от банковских депозитов, срок которых может быть до 5 лет, страхование жизни может быть долгосрочным, т.е. и на 5, 10 и 20 лет.</p>

<p>Депозит только дает возможность накопить определенную сумму и получить гарантированный инвестиционный доход.</p>

<p>Полис же накопительного страхования жизни дает возможность Страхователю не только накопить определенную сумму денег, но и застраховать свою жизнь на сумму, которую он хочет накопить.</p>

<p>Если Страхователь благополучно дожил до окончания срока страхования, он получает все свои накопленные деньги. В случае же его смерти вне зависимости от того, когда она произошла (в начале срока страхования или в конце) и сколько он накопил денег, выгодоприобретателям будет выплачена сумма, которая была бы накоплена, если бы застрахованный был жив, т.е. страховая сумма на которую он был застрахован.</p>

<p>Выгодоприобретателя, т.е. получателя выплаты определяет сам Страхователь и указывает его в страховом полисе. В случае же смерти вкладчика депозита выплату – накопленную сумму на депозите получают наследники, определенные гражданским кодексом РК.</p>

<p>Кроме страхования жизни на случай смерти, дополнительно можно застраховаться от других рисков, например, на случай инвалидности. Если во время действия страховой защиты застрахованному была присвоена инвалидность, то дальнейшую оплату взносов по полису в этот период производить не надо. По окончании срока страхования компания выплачивает всю страховую сумму с инвестиционным доходом, которая была бы накоплена, если бы застрахованный был здоров и продолжал работать.</p>

<p>Накопить определенную сумму денег можно и в пользу ребенка к наступлению заранее оговоренного срока - события в жизни, например к совершеннолетию, бракосочетанию, поступление в ВУЗ и т.д.</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 02 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 02 ? accordion = 02 : accordion = null">
                                    В чём заключаются главные принципы накопительного страхования жизни?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer02" :style="accordion == 02 ? 'max-height: ' + $refs.accordioncontainer02.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Из всех видов страхования важнейшим для каждого человека является страхование жизни. Понятно, что от несчастных случаев и ударов судьбы застраховаться невозможно, но смягчить их последствия и оказать помощь родным и близким — вполне по силам каждому. В основе страхования жизни лежит долгосрочность отношений между клиентом и страховой компанией. При заключении договора человек должен четко понимать, что предусматривает та или иная форма договора.</p>

<p>Страхование жизни представляет собой совокупность видов страхования, предусматривающих осуществление страховой выплаты в случаях смерти застрахованного или дожития им до окончания срока страхования либо определенного договором страхования возраста.</p>

<p>Страхование жизни на случай смерти или потери трудоспособности окажется просто незаменимым при кредитовании. Ведь если с заемщиком случится непредвиденное - инвалидность или смерть, бремя долгов неминуемо ляжет на плечи родных. Для того, чтобы этого избежать, достаточно заключить договор страхования на страховую сумму, равную размеру кредита. В некоторых странах, например, развивается ипотека, и зачастую страхование жизни заемщика является одним из главных условий выдачи ипотечного кредита.</p>

<p>Страхование жизни с участием страхователя в инвестиционном доходе страховщика представляет собой совокупность видов накопительного страхования, предусматривающих осуществление страховой выплаты в случаях смерти застрахованного или дожития им до окончания срока страхования либо определенного договором страхования возраста с условием участия страхователя (застрахованного, выгодоприобретателя) в прибыли, получаемой страховой организацией в результате инвестиционной деятельности посредством осуществления дополнительных страховых выплат либо увеличения страховой суммы.</p>

<p>Накопительное страхование жизни с дополнительной программой страхования от несчастных случаев представляет собой непросто страхование жизни. В рамках единственного договора клиент может застраховаться от несчастного случая, повлекшего госпитализацию, телесные повреждения, временную утрату трудоспособности. Неприятные последствия болезни или травмы, таким образом, не будут так сильно ощутимы со стороны как самого клиента, так и его родных и близких.</p>

<p>В настоящее время накопительное страхование жизни становится все более популярным, поскольку страховые компании предлагают своим клиентам все новые и все более выгодные программы. Накопительное страхование можно с успехом использовать для накопления денег практически на любые цели: обучение детей, дополнительную (негосударственную) пенсию, покупку жилья, путешествия и т.д. Можно заботиться о своей семье, можно думать о своем будущем. Реализация всех этих благородных и дальновидных планов становится возможной благодаря заключению договора страхования жизни. Тем более, что к стандартным условиям срочного страхования жизни добавляется возможность накопления средств и получения гарантированных сумм при дожитии до конца срока страхования.</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 03 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 03 ? accordion = 03 : accordion = null">
                                    Как изменить периодичность оплаты, или увеличить/уменьшить размер страховой премии по договору?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer03" :style="accordion == 03 ? 'max-height: ' + $refs.accordioncontainer03.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Изменение периодичности оплаты страхового взноса, размер страхового взноса, включение/исключение дополнительных покрытий осуществляется только на годовщину договора, т.е. в месяц заключения договора.
	<br>При этом по договору страхования не должно быть задолженности по оплате страховых взносов.
	<br> Для внесения изменений Страхователь (клиент) обращается в филиал страховой компании, где ему необходимо написать заявление на изменение пунктов договора и обязательно предоставить оригинал текущего договора.</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 04 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 04 ? accordion = 04 : accordion = null">
                                    Как изменить выгодоприобретателя в договоре страхования? 
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer04" :style="accordion == 04 ? 'max-height: ' + $refs.accordioncontainer04.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Для изменения выгодоприобретателя Страхователю (клиенту) необходимо обратиться в филиал страховой компании, написать заявление на изменение выгодопреобретателя и обязательно предоставить оригинал текущего договора.</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 05 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 05 ? accordion = 05 : accordion = null">
                                    Если Страхователь умер, что делать?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer05" :style="accordion == 05 ? 'max-height: ' + $refs.accordioncontainer05.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Застрахованному лицу по договору необходимо обратиться в филиал страховой компании и напитсать заявление на изменение Страхователя. Приложить свидетельство о смерти Страхователя и оригинал договора страхования для заключения обновленного договора.
	<br>
	<br>
</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 06 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 06 ? accordion = 06 : accordion = null">
                                    Как расторгнуть договор страхования?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer06" :style="accordion == 06 ? 'max-height: ' + $refs.accordioncontainer06.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Страхователю (клиенту) необходимо обратиться в филиал страховой компании и написать заявление на расторжение, обязательно необходимо предоставить оригинал договора страхования и реквизиты Страхователя.</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 07 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 07 ? accordion = 07 : accordion = null">
                                    Когда осуществлется возврат средств после расторжения договора?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer07" :style="accordion == 07 ? 'max-height: ' + $refs.accordioncontainer07.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Возврат денежных средств осуществляется течении 30-40 календарных дней, с даты подачи заявления на расторжение.</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 08 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 08 ? accordion = 08 : accordion = null">
                                    Что нужно сделать, чтобы восстановить действие договора страхования, который был приостановлен в связи с неоплатой страховых взносов?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer08" :style="accordion == 08 ? 'max-height: ' + $refs.accordioncontainer08.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Страхователю (клиенту) необходимо обратиться в филиал страховой компании, оплатить задолженность по страховым взносам и написать заявление на восстановление действия договора, приложив документы подтверждающие причину не уплаты (в зависимости от количества просроченных дней).</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 09 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 09 ? accordion = 09 : accordion = null">
                                    Если не отражаются платежи в графике платежей, но оплата страховых взносов производилась, что нужно сделать Страхователю?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer09" :style="accordion == 09 ? 'max-height: ' + $refs.accordioncontainer09.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Страхователю (клиенту) необходимо обратиться в филиал страховой компании и предоставить все квитанции об оплате либо платежные поручения с места работы.</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 010 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 010 ? accordion = 010 : accordion = null">
                                    Как можно получить займ под залог выкупной суммы по договору страхования?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer010" :style="accordion == 010 ? 'max-height: ' + $refs.accordioncontainer010.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Страхователю (клиенту) необходимо обратиться в филиал страховой компании и написать заявление на предоставления займа, а также предоставить оригинал договора страхования и реквизиты Страхователя.</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 011 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 011 ? accordion = 011 : accordion = null">
                                    Как досрочно закрыть займ, полученный под залог выкупной суммы?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer011" :style="accordion == 011 ? 'max-height: ' + $refs.accordioncontainer011.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Страхователю (клиенту) необходимо обратиться в страховую Компанию для расчета и оплаты остатка задолженности по займу и написать заявление на досрочное погашение займа.</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                            </div>
        </div>
                <div class="section__common_inner section__wide_inner">
            <div class="section__title">
                <h3>Смешанное страхование в пользу ребенка</h3>
            </div>
            <div class="dropdown__tablet_block">
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 11 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 11 ? accordion = 11 : accordion = null">
                                    В чем выгоды программы смешанного страхования жизни в пользу ребенка?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer11" :style="accordion == 11 ? 'max-height: ' + $refs.accordioncontainer11.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Во-первых, накопление денежных средств для ребенка к определенному событию (совершеннолетие, обучение в ВУЗе, бракосочетание), а во-вторых, предоставление ему финансовой поддержки в том случае, если родитель пострадает в результате болезни или несчастного случая и соответственно потеряет доход.</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 12 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 12 ? accordion = 12 : accordion = null">
                                    Какие документы необходимы для приобретения полиса?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer12" :style="accordion == 12 ? 'max-height: ' + $refs.accordioncontainer12.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Для приобретения полиса необходимы следующие документы:</p>

<ul>
	<li>заявление на страхование</li>
	<li>удостоверение личности</li>
	<li>РНН</li>
</ul>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 13 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 13 ? accordion = 13 : accordion = null">
                                    Есть ли ограничения по возрасту для детей, в чью пользу составляется договор?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer13" :style="accordion == 13 ? 'max-height: ' + $refs.accordioncontainer13.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Да, на страхование принимаются дети до 15 лет. Так как срок страхования должен быть не менее 3 лет (18 лет – 3)</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 14 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 14 ? accordion = 14 : accordion = null">
                                    На какой срок заключается договор?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer14" :style="accordion == 14 ? 'max-height: ' + $refs.accordioncontainer14.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>На срок от 3 до 18 лет</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 15 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 15 ? accordion = 15 : accordion = null">
                                    Кто может приобрести полис страхования в пользу ребенка?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer15" :style="accordion == 15 ? 'max-height: ' + $refs.accordioncontainer15.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Страхователем, или владельцем полиса, в пользу ребенка может быть любой человек старше 18 лет, либо юридическое лицо. Именно страхователь берет на себя все обязательства по договору страхования, выплачивает взносы и обладает всеми правами на полис.</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 16 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 16 ? accordion = 16 : accordion = null">
                                    Если клиент утерял договор страхования, каковы его действия?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer16" :style="accordion == 16 ? 'max-height: ' + $refs.accordioncontainer16.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    Страхователь (клиент) обращается в филиал страховой компании, где ему необходимо написать заявление об утере договора страхования и выписке дубликата.

<table width="875" cellspacing="0" cellpadding="0" border="0"></table>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                            </div>
        </div>
                <div class="section__common_inner section__wide_inner">
            <div class="section__title">
                <h3>Пенсионный аннуитет</h3>
            </div>
            <div class="dropdown__tablet_block">
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 21 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 21 ? accordion = 21 : accordion = null">
                                    Кто имеет право на заключение договора пенсионного пожизненного аннуитета?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer21" :style="accordion == 21 ? 'max-height: ' + $refs.accordioncontainer21.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Заключить договор пожизненного пенсионного аннуитета могут женщины, достигшие 50 лет, и мужчины, достигшие 55 лет, и имеющие достаточность пенсионных накоплений для обеспечения выплаты не ниже размера минимальной пенсии. А также другие категории граждан, согласно Таблице №1.&nbsp;</p>

<table border="">
	<tbody>
		<tr>
			<td><strong>1) Лица, достигшие пенсионного возраста:</strong></td>
			<td><strong>3) Женщины при достаточности пенсионных накоплений для обеспечения выплаты не ниже размера минимальной пенсии по достижении:</strong></td>
		</tr>
		<tr>
			<td>мужчины: с 1 июля 2001 года – по достижении 63 лет;</td>
			<td>c 1 марта 2016 года – 50 лет;</td>
		</tr>
		<tr>
			<td>женщины:</td>
			<td>c 1 января 2018 года - 50,5 года;</td>
		</tr>
		<tr>
			<td>с 1 июля 2001 года – по достижении 58 лет;</td>
			<td>c 1 января 2019 года - 51 года;</td>
		</tr>
		<tr>
			<td>с 1 января 2018 года - по достижении 58,5 лет;</td>
			<td>c 1 января 2020 года - 51,5 года;</td>
		</tr>
		<tr>
			<td>c 1 января 2019 года - по достижении 59 лет;</td>
			<td>c 1 января 2021 года - 52 лет;</td>
		</tr>
		<tr>
			<td>c 1 января 2020 года - по достижении 59,5 лет;</td>
			<td>c 1 января 2022 года - 52,5 года;</td>
		</tr>
		<tr>
			<td>c 1 января 2021 года - по достижении 60 лет;</td>
			<td>c 1 января 2023 года - 53 лет;</td>
		</tr>
		<tr>
			<td>c 1 января 2022 года - по достижении 60,5 лет;</td>
			<td>c 1 января 2024 года - 53,5 года;</td>
		</tr>
		<tr>
			<td>с 1 января 2023 года - по достижении 61 года;</td>
			<td>c 1 января 2025 года - 54 лет;</td>
		</tr>
		<tr>
			<td>c 1 января 2024 года - по достижении 61,5 года;</td>
			<td>c 1 января 2026 года - 54,5 года;</td>
		</tr>
		<tr>
			<td>c 1 января 2025 года - по достижении 62 лет;</td>
			<td>c 1 января 2027 года - 55 лет.</td>
		</tr>
		<tr>
			<td>c 1 января 2026 года - по достижении 62,5 лет;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>c 1 января 2027 года - по достижении 63 лет.</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td><strong>2) Мужчины по достижении 55-летнего возраста при достаточности пенсионных накоплений&nbsp;</strong>для обеспечения выплаты не ниже размера минимальной пенсии</td>
			<td><strong>4) Лица, достигшие 50-летнего возраста, при наличии стажа работы не менее 5 лет на работах с вредными (особо вредными) условиями труда.</strong></td>
		</tr>
		<tr>
			<td colspan=""><strong>5) Инвалиды I и IIгрупп, если инвалидность установлена бессрочно</strong></td>
		</tr>
	</tbody>
</table>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 22 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 22 ? accordion = 22 : accordion = null">
                                    Что представляет собой достаточность пенсионных накоплений?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer22" :style="accordion == 22 ? 'max-height: ' + $refs.accordioncontainer22.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Достаточность пенсионных накоплений для заключения договора пенсионного аннуитета рассчитывается на основании минимальной пенсии, установленной Правительством РК на текущий год, индексации, связанной с увеличением минимальной пенсии, показателей дожития для расчета выплат по пенсионным аннуитетам.</p>

<p>
	<br>
</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 23 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 23 ? accordion = 23 : accordion = null">
                                    Какова достаточность пенсионный накоплений на сегодняшний день?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer23" :style="accordion == 23 ? 'max-height: ' + $refs.accordioncontainer23.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Достаточность пенсионных накоплений определяется с учетом пола, возраста клиента.</p>

<p>Так для женщин в возрасте 50 лет, сумма пенсионных накоплений должна быть не ниже 13 987 139 тенге, для мужчин в возрасте 55 лет - не ниже 10 001 551 тенге.</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 24 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 24 ? accordion = 24 : accordion = null">
                                    Если у Клиента недостаточно пенсионных накоплений, сформированных за счет обязательных пенсионных взносов для заключения Договора?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer24" :style="accordion == 24 ? 'max-height: ' + $refs.accordioncontainer24.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>В случае недостаточности пенсионных накоплений, сформированных за счет обязательных пенсионных взносов и (или) обязательных профессиональных пенсионных взносов, для заключения договора пенсионного аннуитета могут быть использованы пенсионные накопления, сформированные за счет добровольных пенсионных взносов.</p>

<p>В случае недостаточности пенсионных накоплений, сформированных за счет обязательных профессиональных пенсионных взносов, для заключения договора пенсионного аннуитета лица, достигшие 50-летнего возраста, при наличии стажа работы не менее 5 лет на работах с вредными условиями труда, имеют право использовать пенсионные накопления, сформированные за счет обязательных пенсионных взносов.</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 25 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 25 ? accordion = 25 : accordion = null">
                                    Как определяется размер ежемесячной выплаты по договору пожизненного пенсионного аннуитета?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer25" :style="accordion == 25 ? 'max-height: ' + $refs.accordioncontainer25.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Размер ежемесячной выплаты расчитывается актуарием, с учетом суммы пенсионных накоплений, возраста, пола клиента, показателей дожитиия, по методике, утвержденной НБ РК. Ежемесячная страховая выплата не может быть ниже размера минимальной пенсии, установленного законом о республиканском бюджете на соответствующий финансовый год, на дату заключения Договора пенсионного аннуитета. (Законом РК «О республиканском бюджете на 2016-2018 годы» установлена минимальная пенсия - на уровне 25 824 тенге).</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 26 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 26 ? accordion = 26 : accordion = null">
                                    Как осуществляются выплаты по договору пенсионного аннуитета? И куда они перечисляются?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer26" :style="accordion == 26 ? 'max-height: ' + $refs.accordioncontainer26.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Аннуитетные выплаты по договору пенсионного аннуитета осуществляются ежемесячно, ежеквартально, раз в пол года или один раз в год - по выбору Клиента. Аннуитетные выплаты переводятся на банковский счет Аннуитента или Выгодоприобретателя, указанный в договоре пенсионного аннуитета.</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 27 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 27 ? accordion = 27 : accordion = null">
                                    Если я уезжаю на ПМЖ в другую страну, что происходит с этими выплатами?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer27" :style="accordion == 27 ? 'max-height: ' + $refs.accordioncontainer27.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>В случае переезда на ПМЖ в другую страну, аннуитетные выплаты продолжают осуществляться на счет, указанный Аннуитентом в договоре пенсионного аннуитета (любой БВУ в РК). В случае невозможности получения Аннуитентом аннуитетных выплат за пределами РК, он может оставить доверенное лицо в РК, которое будет получать эти выплаты и перечислять Аннуитенту.</p>

<p>
	<br>
</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 28 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 28 ? accordion = 28 : accordion = null">
                                    Наследуются ли пенсионные накопления, переведенные в Компанию по страхованию жизни (КСЖ)?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer28" :style="accordion == 28 ? 'max-height: ' + $refs.accordioncontainer28.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Пенсионные накопления, переведенные в аннуитетную компанию, не наследуются, но, заключив договор пенсионного аннуитета, клиент может определить гарантированный период в течение которого КСЖ обязана осуществлять аннуитетные выплаты в случае смерти наследникам Аннуитента, определенному Страхователем при заключении настоящего договора.</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 29 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 29 ? accordion = 29 : accordion = null">
                                    Сколько составляет гарантированный период?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer29" :style="accordion == 29 ? 'max-height: ' + $refs.accordioncontainer29.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Гарантированный период устанавливает по желанию Клиента и максимально может достигать 30 лет.</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 210 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 210 ? accordion = 210 : accordion = null">
                                    В случае установления гарантированного периода как действует договор страхования?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer210" :style="accordion == 210 ? 'max-height: ' + $refs.accordioncontainer210.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Если, Клиент выбирает гарантированный период, например, 15 лет, то в случае ухода из жизни до момента окончания этого периода, его наследники вправе получать аннуитетные выплаты до того, пока действует этот период. Так, если Клиент уйдет из жизни за 3 года, до момента окончания этого периода, то оставшиеся 3 года его наследники будут получать аннуитетные выплаты.</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 211 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 211 ? accordion = 211 : accordion = null">
                                    Если Клиент ушел из жизни, но в договоре не был указан гарантированный период, получат ли наследники какую-то компенсацию?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer211" :style="accordion == 211 ? 'max-height: ' + $refs.accordioncontainer211.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Наследники имеют право на получение единовременной выплаты на погребение в размере и порядке, предусмотренном законодательством Республики Казахстан о пенсионном обеспечении, но не менее 15-ти кратного месячного расчетного показателя (МРП), установленного на соответствующий финансовый год законом о республиканском бюджете.</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 212 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 212 ? accordion = 212 : accordion = null">
                                    Предусмотрена ли индексация аннуитетных выплат в связи с изменением экономической ситуации в стране?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer212" :style="accordion == 212 ? 'max-height: ' + $refs.accordioncontainer212.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Да, в договоре аннуитета предусмотрена ежегодная индексация аннуитетных выплат на 5%.</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 213 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 213 ? accordion = 213 : accordion = null">
                                    Чем гарантированы пенсионные накопления, переведенные в АО «Дочерняя компания Народного Банка Казахстана по страхованию жизни «Халык-Life»?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer213" :style="accordion == 213 ? 'max-height: ' + $refs.accordioncontainer213.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <ol>
	<li>Лицензия, выдана НБ РК (переоформлена за №2.2.12 от 28.12.2022г.). Опыт работы на рынке - около 18 лет;</li>
	<li>Единственный Акционер - АО «Народный Банк Казахстана» (владеет 100% акций);</li>
	<li>Компания на 01.09.2019г. занимает 1 место на рынке по размеру активов и собственного капитала, 1 место по размеру страховых резервов;</li>
	<li>Компания имеет рейтинг финансовой устойчивости на уровне «B++» и кредитный рейтинг на уровне «bbb», который является наивысшим среди всех казахстанских компаний по страхованию жизни, от международного рейтингового агентства АM Best. Прогноз по рейтингам «Стабильный». Международное рейтинговое агентство S&amp;P Global Ratings присвоило АО «Халык-Life» долгосрочный рейтинг финансовой устойчивости на уровне «ВВВ-» и рейтинг по казахстанской национальной шкале «kzAАА». Прогноз изменения рейтинга - «Стабильный».</li>
</ol>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 214 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 214 ? accordion = 214 : accordion = null">
                                    Как расторгнуть договор  пенсионного аннуитета?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer214" :style="accordion == 214 ? 'max-height: ' + $refs.accordioncontainer214.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>В соответствии с законом Республики Казахстан "О пенсионном обеспечении в Республике Казахстан" расторжение договора пенсионного аннуитета возможно только по инициативе страхователя при условии заключения договора пенсионного аннуитета с другой страховой организацией, но не ранее двух лет с даты его заключения или в случае смены гражданства. Страхователь обязан при расторжении договора пенсионного аннуитета обратиться с заявлением о расторжении договора пенсионного аннуитета и предоставить оригинал договора с новой страховой организацией в течение десяти рабочих дней со дня заключения нового договора пенсионного аннуитета.
	<br>В случае выезда на постояное место жительство за пределы Республике Казахстан, необходимо предоставить помимо паспорта иностранного гражданина, дополнительно документ подтверждающий факт выезда из миграционной службы, а также счет, открытый в банке на территории Республике Казахстан.</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 215 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 215 ? accordion = 215 : accordion = null">
                                    В чем выгода получения выплат из Компании по страхованию жизни перед пенсионным фондом?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer215" :style="accordion == 215 ? 'max-height: ' + $refs.accordioncontainer215.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <ul>
	<li>Получение аннуитетных выплат ПОЖИЗНЕННО.</li>
	<li>Возможность ДОСРОЧНО воспользоваться пенсионными накоплениями (женщины с 50 лет, мужчины с 55 лет).</li>
	<li>Возможность получения пенсионных выплат из 3-х ИСТОЧНИКОВ по достижении пенсионного возраста: базовая пенсия (стаж до 1998г.); аннуитетные выплаты по договору пенсионного аннуитета; выплаты из ЕНПФ, сформированные после заключения договора пенсионного аннуитета до момента выхода на заслуженный отдых.</li>
	<li>Снижение инфляционных рисков (возможность ИНДЕКСАЦИИ АННУИТЕТНЫХ ВЫПЛАТ).</li>
	<li>Возможность установления ГАРАНТИРОВАННОГО ПЕРИОДА ВЫПЛАТ для наследников (до 30 лет).</li>
</ul>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 216 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 216 ? accordion = 216 : accordion = null">
                                    Если по договору пенсионного аннуитета страхователь умер, как получить выплату и какие документы для этого необходимы?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer216" :style="accordion == 216 ? 'max-height: ' + $refs.accordioncontainer216.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p><strong>Перечень документов, необходимых при оформлении получения единовременной выплаты на погребение:</strong></p>

<ol>
	<li>Свидетельство о смерти (копия нотариально засвидетельствованная);</li>
	<li>Свидетельство о праве на наследство (оригинал или копия нотариально засвидетельствованная) - по договорам, заключенным с 2014 года - Свидетельство о праве на наследство не требуется;</li>
	<li>Удостоверение личности/ свидетельство о рождении (ИИН, если несовершеннолетний) наследников;</li>
	<li>Уведомления по банковскому счету на наследников (на несовершеннолетних детей счет обязательно, в случае предоставления счета родителя/законного представителя необходимо согласие органов опеки и попечительства на выплату родителю/законному представителю);</li>
	<li>Если выплата по договорам, заключенным с 2014 года, необходим документ, подтверждающий родственные отношения (свидетельство о браке или свидетельство о рождении).</li>
</ol>

<p>
	<br>
</p>

<p><strong>Перечень документов, необходимых при оформлении выплаты последующих страховых выплат на выгодоприобретателей по договору/наследников по закону РК (если имеется гарантированный период):</strong></p>

<ol>
	<li>Свидетельство о смерти (копия нотариально засвидетельствованная);</li>
	<li>Свидетельство о праве на наследство - оригинал или копия нотариально засвидетельствованная (в случае, если наследник (и)); если указан выгодоприобретатель по договору - то Свидетельство о праве на наследство не требуется;</li>
	<li>Удостоверение личности/ свидетельство о рождении наследников (ИИН, если несовершеннолетний);</li>
	<li>Уведомления по банковскому счету на наследников (на несовершеннолетних детей счет обязательно, в случае предоставления счета родителя/законного представителя необходимо согласие органов опеки и попечительства на выплату родителю/законному представителю).</li>
</ol>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 217 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 217 ? accordion = 217 : accordion = null">
                                    По договору пенсионного аннуитета можно ли получить выплату раньше срока (не по графику)?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer217" :style="accordion == 217 ? 'max-height: ' + $refs.accordioncontainer217.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Согласно статье 272 Гражданского кодекса Республики Казахстан, обязательство должно исполняться надлежащим образом в соответствии с условиями Договора. Компания осуществляет выплаты в соответствии с условиями с графиком выплат.</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 218 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 218 ? accordion = 218 : accordion = null">
                                    В какой срок Компания предоставляет ответ на  запрос (на изменение периодичности выплат, на индексацию договора, на размер выкупной суммы, на дубликат договора, на расшифровку выплат и прочее)?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer218" :style="accordion == 218 ? 'max-height: ' + $refs.accordioncontainer218.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Ответ на запросы предоставляются в течение 15 календарных дней с даты подачи запроса.</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 219 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 219 ? accordion = 219 : accordion = null">
                                    Может ли вместо меня страхователя/застрахованного/выгодоприобритателя в Компанию обратиться поверенный?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer219" :style="accordion == 219 ? 'max-height: ' + $refs.accordioncontainer219.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Поверенный может обратиться в Компанию при наличии документа, удостоверяющего личность доверителя, оригинала или копии нотариально засвидетельствованной доверенности с правом полномочий. Поверенный только подписывает заявление. Но в случае выплаты или расторжения договора страхования, сумма переводится только на счет самого страхователя/застрахованного/выгодоприобретателя (поверенный не является получателем денег).</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                            </div>
        </div>
                <div class="section__common_inner section__wide_inner">
            <div class="section__title">
                <h3>Групповое страхование</h3>
            </div>
            <div class="dropdown__tablet_block">
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 31 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 31 ? accordion = 31 : accordion = null">
                                    Почему работодателям будет выгоден этот страховой полис?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer31" :style="accordion == 31 ? 'max-height: ' + $refs.accordioncontainer31.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Данный вид страхования дает возможность работодателям обезопасить свою компанию от потенциальных финансовых потерь, которые могут возникнуть в связи с неожиданной утратой ключевого лица, обладающего уникальными связями, технологиями и пр.</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 32 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 32 ? accordion = 32 : accordion = null">
                                    От каких параметров будет зависеть стоимость страховки?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer32" :style="accordion == 32 ? 'max-height: ' + $refs.accordioncontainer32.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Стоимость размера страховой премии зависит от ряда факторов, таких как возраст Застрахованных, род профессиональной деятельности, хобби, показатель состояния здоровья и др.</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 33 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 33 ? accordion = 33 : accordion = null">
                                    На какой срок приобретается полис по страхованию жизни ключевых сотрудников?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer33" :style="accordion == 33 ? 'max-height: ' + $refs.accordioncontainer33.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Срок действия полиса группового срочного страхования жизни – 1 год.</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 34 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 34 ? accordion = 34 : accordion = null">
                                    Существуют ли возрастные ограничения для сотрудников по этому страховому продукту?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer34" :style="accordion == 34 ? 'max-height: ' + $refs.accordioncontainer34.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Да, возраст Застрахованного не может быть менее 16 лет. Также данная программа ограничивает возраст Застрахованного - на момент заключения Договора страхования он не должен превышать 62 года (включительно) для мужчин и 57 лет (включительно) для женщин.</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 35 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 35 ? accordion = 35 : accordion = null">
                                    А что если с застрахованным сотрудником ничего не случилось? Страховая компания вернет деньги?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer35" :style="accordion == 35 ? 'max-height: ' + $refs.accordioncontainer35.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Нет, данная программа страхования жизни не предполагает возврат части страховой премии в случае если с Застрахованными сотрудниками не произошел страховой случай. Для этого существуют другие программы.</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                            </div>
        </div>
                <div class="section__common_inner section__wide_inner">
            <div class="section__title">
                <h3>Обязательное страхование работника от несчастных случаев при исполнении им трудовых (служебных) обязанностей</h3>
            </div>
            <div class="dropdown__tablet_block">
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 41 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 41 ? accordion = 41 : accordion = null">
                                    Могу я заключить договор обязательного страхования работника от несчастных случаев с любой страховой компанией?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer41" :style="accordion == 41 ? 'max-height: ' + $refs.accordioncontainer41.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Нет. Договор обязательного страхования работника от несчастных случаев должен быть заключен&nbsp;<strong>только со страховщиком, имеющим лицензию на право осуществления страховой деятельности по классу аннуитетное страхование и данному виду обязательного страхования.</strong></p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 42 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 42 ? accordion = 42 : accordion = null">
                                    Может ли страховая компания отказать в заключении договора страхования?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer42" :style="accordion == 42 ? 'max-height: ' + $refs.accordioncontainer42.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Нет. Страхователь свободен в выборе страховщика, а Страховщик не вправе отказать Страхователю в заключении договора обязательного страхования.</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 43 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 43 ? accordion = 43 : accordion = null">
                                    В течение какого времени необходимо заключить Договор обязательного страхования работника от несчастных случаев?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer43" :style="accordion == 43 ? 'max-height: ' + $refs.accordioncontainer43.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Согласно действующего Законодательства РК, Страхователь (работодатель) обязан заключить договор обязательного страхования работника от несчастных случаев со страховщиком в течение первой декады месяца, следующего за месяцем, в котором страхователем начато осуществление деятельности.</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 44 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 44 ? accordion = 44 : accordion = null">
                                    На какой срок можно заключить договор страхования?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer44" :style="accordion == 44 ? 'max-height: ' + $refs.accordioncontainer44.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Сроком на 12 месяцев, если деятельность Страхователя менее 12-ти месяцев, то на срок осуществления деятельности Страхователя.</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 45 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 45 ? accordion = 45 : accordion = null">
                                    Как рассчитывается размер страхового взноса по договору страхования?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer45" :style="accordion == 45 ? 'max-height: ' + $refs.accordioncontainer45.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Размер страховой премии (страхового взноса) определяется соглашением сторон на основе страхового тарифа, дифференцированного по видам экономической деятельности, в зависимости от класса профессионального риска, умноженного на страховую сумму по договору страхования.</p>

<p>
	<br>
</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 46 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 46 ? accordion = 46 : accordion = null">
                                    Как правильно рассчитать страховую сумму по договору страхования?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer46" :style="accordion == 46 ? 'max-height: ' + $refs.accordioncontainer46.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Страховая сумма по договору страхования не должна быть менее годового фонда оплаты труда (ГФОТ*) всех работников на момент заключения договора обязательного страхования работника от несчастных случаев.</p>

<p>*ГФОТ рассчитывается как:</p>

<p>сумма ежемесячного доход каждого работника, но не более десятикратного размера МЗП, установленного законом о республиканском бюджете на соответствующий финансовый год, умноженного на двенадцать.</p>

<p>Например, если в компании работают 5 человек, заработная плата каждого из которых составляет 120 000 тенге в месяц, то ГФОТ = 5 человек* (120 000 тенге * 12 месяцев) = 7 200 000 тенге</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 47 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 47 ? accordion = 47 : accordion = null">
                                    Есть ли законодательно установленный размер страховых тарифов?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer47" :style="accordion == 47 ? 'max-height: ' + $refs.accordioncontainer47.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Да, размер тарифов установлен в Законе РК «Об обязательном страховании гражданско-правовой ответственности работодателя за причинение вреда жизни и здоровью работника при исполнении им трудовых (служебных) обязанностей».</p>

<table style="margin-right: calc(53%); width: 47%;" border="">
	<tbody>
		<tr>
			<td style="width: 58.2623%; text-align: center;">

				<p>Класс профессионального риска</p>
			</td>
			<td style="width: 41.5418%; text-align: center;">

				<p>Страховой тариф&nbsp; &nbsp; &nbsp;</p>
			</td>
		</tr>
		<tr>
			<td style="width: 58.2623%; text-align: center;">

				<p>1</p>
			</td>
			<td style="width: 41.5418%; text-align: center;">

				<p>0,12%</p>
			</td>
		</tr>
		<tr>
			<td style="width: 58.2623%; text-align: center;">

				<p>2</p>
			</td>
			<td style="width: 41.5418%; text-align: center;">

				<p>0,29%</p>
			</td>
		</tr>
		<tr>
			<td style="width: 58.2623%; text-align: center;">

				<p>3</p>
			</td>
			<td style="width: 41.5418%; text-align: center;">

				<p>0,48%</p>
			</td>
		</tr>
		<tr>
			<td style="width: 58.2623%; text-align: center;">

				<p>4</p>
			</td>
			<td style="width: 41.5418%; text-align: center;">

				<p>0,49%</p>
			</td>
		</tr>
		<tr>
			<td style="width: 58.2623%; text-align: center;">

				<p>5</p>
			</td>
			<td style="width: 41.5418%; text-align: center;">

				<p>0,52%</p>
			</td>
		</tr>
		<tr>
			<td style="width: 58.2623%; text-align: center;">

				<p>6</p>
			</td>
			<td style="width: 41.5418%; text-align: center;">

				<p>0,53%</p>
			</td>
		</tr>
		<tr>
			<td style="width: 58.2623%; text-align: center;">

				<p>7</p>
			</td>
			<td style="width: 41.5418%; text-align: center;">

				<p>0,54%</p>
			</td>
		</tr>
		<tr>
			<td style="width: 58.2623%; text-align: center;">

				<p>8</p>
			</td>
			<td style="width: 41.5418%; text-align: center;">

				<p>0,65%</p>
			</td>
		</tr>
		<tr>
			<td style="width: 58.2623%; text-align: center;">

				<p>9</p>
			</td>
			<td style="width: 41.5418%; text-align: center;">

				<p>0,56%</p>
			</td>
		</tr>
		<tr>
			<td style="width: 58.2623%; text-align: center;">

				<p>10</p>
			</td>
			<td style="width: 41.5418%; text-align: center;">

				<p>0,88%</p>
			</td>
		</tr>
		<tr>
			<td style="width: 58.2623%; text-align: center;">

				<p>11</p>
			</td>
			<td style="width: 41.5418%; text-align: center;">

				<p>0,75%</p>
			</td>
		</tr>
		<tr>
			<td style="width: 58.2623%; text-align: center;">

				<p>12</p>
			</td>
			<td style="width: 41.5418%; text-align: center;">

				<p>0,76%</p>
			</td>
		</tr>
		<tr>
			<td style="width: 58.2623%; text-align: center;">

				<p>13</p>
			</td>
			<td style="width: 41.5418%; text-align: center;">

				<p>1,29%</p>
			</td>
		</tr>
		<tr>
			<td style="width: 58.2623%; text-align: center;">

				<p>14</p>
			</td>
			<td style="width: 41.5418%; text-align: center;">

				<p>1,55%</p>
			</td>
		</tr>
		<tr>
			<td style="width: 58.2623%; text-align: center;">

				<p>15</p>
			</td>
			<td style="width: 41.5418%; text-align: center;">

				<p>1,13%</p>
			</td>
		</tr>
		<tr>
			<td style="width: 58.2623%; text-align: center;">

				<p>16</p>
			</td>
			<td style="width: 41.5418%; text-align: center;">

				<p>1,17%</p>
			</td>
		</tr>
		<tr>
			<td style="width: 58.2623%; text-align: center;">

				<p>17</p>
			</td>
			<td style="width: 41.5418%; text-align: center;">

				<p>1,21%</p>
			</td>
		</tr>
		<tr>
			<td style="width: 58.2623%; text-align: center;">

				<p>18</p>
			</td>
			<td style="width: 41.5418%; text-align: center;">

				<p>2,43%</p>
			</td>
		</tr>
		<tr>
			<td style="width: 58.2623%; text-align: center;">

				<p>19</p>
			</td>
			<td style="width: 41.5418%; text-align: center;">

				<p>1,75%</p>
			</td>
		</tr>
		<tr>
			<td style="width: 58.2623%; text-align: center;">

				<p>20</p>
			</td>
			<td style="width: 41.5418%; text-align: center;">

				<p>2,05%</p>
			</td>
		</tr>
		<tr>
			<td style="width: 58.2623%; text-align: center;">

				<p>21</p>
			</td>
			<td style="width: 41.5418%; text-align: center;">

				<p>2,54%</p>
			</td>
		</tr>
		<tr>
			<td style="width: 58.2623%; text-align: center;">

				<p>22</p>
			</td>
			<td style="width: 41.5418%; text-align: center;">

				<p>2,96%</p>
			</td>
		</tr>
	</tbody>
</table>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 48 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 48 ? accordion = 48 : accordion = null">
                                    Как определить размер страхового тарифа, если страхователь осуществляет несколько видов экономической деятельности?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer48" :style="accordion == 48 ? 'max-height: ' + $refs.accordioncontainer48.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>В случае когда страхователь осуществляет несколько видов экономической деятельности, то он подлежит отнесению к классу профессионального риска, соответствующему основному виду его деятельности. В случае, когда страхователь осуществляет несколько видов экономической деятельности, равномерно распределенных в общем объеме производства, он подлежит отнесению к тому виду экономической деятельности, которому соответствует более высокий класс профессионального риска.</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 49 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 49 ? accordion = 49 : accordion = null">
                                    Как возмещается вред, причиненный работнику в результате несчастного случая на производстве?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer49" :style="accordion == 49 ? 'max-height: ' + $refs.accordioncontainer49.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <table border="0">
	<tbody>
		<tr>
			<td>

				<p>Возмещение вреда, связанного с утратой заработка (дохода) работником в связи с установлением ему степени утраты профессиональной трудоспособности<strong>&nbsp;от 5% до 29% включительно</strong></p>
			</td>
			<td>

				<p>Возмещение вреда, связанного с утратой заработка (дохода) работником в связи с установлением ему степени утраты профессиональной трудоспособности&nbsp;<strong>от 30% до 100% включительно</strong></p>
			</td>
			<td>

				<p>Возмещение вреда, связанного&nbsp;<strong>со смертью работника</strong></p>
			</td>
		</tr>
		<tr>
			<td>

				<p><strong>осуществляется Страхователем</strong> согласно трудовому законодательству Республики Казахстан</p>
			</td>
			<td>

				<p><strong>осуществляется страховой компанией</strong></p>
			</td>
		</tr>
	</tbody>
</table>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 410 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 410 ? accordion = 410 : accordion = null">
                                    Как осуществляется страховая выплата после урегулирования страхового случая?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer410" :style="accordion == 410 ? 'max-height: ' + $refs.accordioncontainer410.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <table border="">
	<tbody>
		<tr>
			<td>

				<p>Страховая выплата, связанная&nbsp;<strong>с утратой заработка (дохода) работником в связи с установлением ему степени утраты профессиональной трудоспособности на срок менее одного года</strong></p>
			</td>
			<td>

				<p>Страховая выплата, связанная&nbsp;<strong>с утратой заработка (дохода) работником в связи с установлением ему степени утраты профессиональной трудоспособности на срок один год и более</strong></p>
			</td>
			<td>

				<p>Страховая выплата по возмещению вреда, связанного&nbsp;<strong>со смертью работника</strong></p>
			</td>
		</tr>
		<tr>
			<td>

				<p>осуществляется страховщиком ежемесячно на основании договора аннуитета</p>
			</td>
			<td>

				<p>осуществляется в виде аннуитетных выплат в пользу работника в течение срока, равного сроку установления либо продления (переосвидетельствования) степени утраты профессиональной трудоспособности работника в соответствии с договором аннуитета, заключенным со страхователем в соответствии со статьей 23 Закона об обязательном страховании работника, но не более срока достижения работником пенсионного возраста, установленного законодательством Республики Казахстан о пенсионном обеспечении</p>
			</td>
			<td>

				<p>осуществляется в виде аннуитетных выплат в пользу лиц, имеющих согласно законам Республики Казахстан право на возмещение вреда, в течение срока, установленного Гражданским кодексом Республики Казахстан</p>
			</td>
		</tr>
	</tbody>
</table>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 411 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 411 ? accordion = 411 : accordion = null">
                                    Как осуществляется возмещение расходов, вызванных повреждением здоровья с установлением степени утраты профессиональной трудоспособности ?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer411" :style="accordion == 411 ? 'max-height: ' + $refs.accordioncontainer411.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Возмещение расходов, вызванных повреждением здоровья с установлением степени утраты профессиональной трудоспособности осуществляется страховщиком на основании документов, подтверждающих эти расходы, представленных работником либо лицом, понесшим эти расходы.</p>

<p>Совокупный размер страховых выплат по возмещению дополнительных расходов, вызванных повреждением здоровья, не может превышать следующие размеры (в месячных расчетных показателях, установленных на соответствующий финансовый год законом о республиканском бюджете):</p>

<ol>
	<li>при установлении степени утраты профессиональной трудоспособности от 30 до 59 процентов включительно - 500 МРП;</li>
	<li>при установлении степени утраты профессиональной трудоспособности от 60 до 89 процентов включительно – 750 МРП;</li>
	<li>при установлении степени утраты профессиональной трудоспособности от 90 до 100 процентов включительно – 1 000 МРП.</li>
</ol>

<p>При этом возмещению страховщиком не подлежат расходы, которые входят в гарантированный объем бесплатной медицинской помощи в соответствии с законодательством Республики Казахстан в области здравоохранения.</p>

<p>Совокупные страховые выплаты по возмещению дополнительных расходов, вызванных повреждением здоровья, осуществляются страховщиком по соответствующей первично установленной степени утраты профессиональной трудоспособности в пределах размеров, указанных выше.</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 412 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 412 ? accordion = 412 : accordion = null">
                                    Предусмотрено ли возмещение расходов на погребение в случае смерти работника?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer412" :style="accordion == 412 ? 'max-height: ' + $refs.accordioncontainer412.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Да, предусмотрено. Расходы на погребение с случае смерти пострадавшего работника осуществляются лицу, осуществившему его погребение. Такие расходы возмещаются в размере 100 МРП.</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 413 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 413 ? accordion = 413 : accordion = null">
                                    В каких случаях заключается договор аннуитета?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer413" :style="accordion == 413 ? 'max-height: ' + $refs.accordioncontainer413.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>В случае установления либо продления (переосвидетельствования) степени утраты профессиональной трудоспособности работника либо его смерти работодатель обязан заключить договор аннуитета в пользу работника либо лица, имеющего право на возмещение вреда в связи со смертью работника, со страховщиком, заключившим договор обязательного страхования работника от несчастных случаев, в период действия которого произошел страховой случай.</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                            </div>
        </div>
                <div class="section__common_inner section__wide_inner">
            <div class="section__title">
                <h3>Другое</h3>
            </div>
            <div class="dropdown__tablet_block">
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 51 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 51 ? accordion = 51 : accordion = null">
                                    Заключаются ли договоры страхования жизни с гражданами других стран?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer51" :style="accordion == 51 ? 'max-height: ' + $refs.accordioncontainer51.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Да, возможно заключение договора страхования, с теми иностранными гражданами, которые постоянно проживают на территории Казахстана.</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 52 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 52 ? accordion = 52 : accordion = null">
                                    Каким образом будущий Клиент может произвести платежи?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer52" :style="accordion == 52 ? 'max-height: ' + $refs.accordioncontainer52.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Клиент может произвести платежи самостоятельно через любые отделения АО «Народный Банк Казахстана» или других банков, или написав Заявление в бухгалтерию по месту своей работы об удержании страховых взносов в пользу АО «Халык-Life».</p>

<p>Для повышения удобства оплаты страховых взносов АО «Халык-Life» предоставляет Вам возможность оплачивать свои страховые взносы через Финансовый портал интернет-банкинга «Homebank»,</p>

<p>через отделения АО «Казпочта», онлайн на сайте компании:</p>

<ul>
	<li>для проведения оплаты страховых взносов через Финансовый портал Страхователям АО «Халык-Life», которые являются владельцами платёжных карточек АО «Народный Банк Казахстана», необходимо зайти на Интернет-сайт по адресу www.homebank.kz и оформить соответствующую подписку на услугу оплаты страховых взносов;</li>
	<li>для того, чтобы оплатить страховой взнос через&nbsp;отделения АО «Казпочта» клиенту необходимо указать номер договора страхования, сообщить кассиру код платежа – 4321 и название компании – АО «Халык-Life».</li>
	<li>для оплаты страховой премии Онлайн на Главной странице сайта необходимо нажать на ссылку «Оплата полиса» в правом верхнем углу; затем на новой странице заполнить необходимые поля.</li>
</ul>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 53 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 53 ? accordion = 53 : accordion = null">
                                    Существуют ли возможности досрочного расторжения договора и каковы при этом условия?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer53" :style="accordion == 53 ? 'max-height: ' + $refs.accordioncontainer53.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>По некоторым программам страхования Страхователь вправе отказаться от Договора страхования в любое время, представив Страховщику заявление на досрочное прекращение Договора страхования. Но существуют программы, например, такие как Пенсионный Аннуитет, Договор по которым может быть расторгнут только по истечении 2-х лет непрерывного действия Договора. При досрочном прекращении Договора Страхователь имеет право на получение от Страховщика выкупной суммы, размеры которой указываются в полисе по состоянию на дату окончания каждого года страхования. Выкупная сумма по истечении первого года страхования равна нулю. Выкупная сумма и начисленные Страховые дивиденды подлежат выплате Страхователю не позднее тридцати календарных дней со дня представления Страховщику заявления на досрочное прекращение Договора. К тому же Страховщик при выплате выкупной суммы и страховых дивидендов вправе удержать сумму денег в размере задолженности Страхователя по просроченным страховым взносам, причитающимся к уплате до наступления даты досрочного прекращения, а также любую другую задолженность Страхователя Страховщику.</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 54 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 54 ? accordion = 54 : accordion = null">
                                    Может ли клиент изменить (повысить или понизить) годовой взнос?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer54" :style="accordion == 54 ? 'max-height: ' + $refs.accordioncontainer54.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>При изменении взноса программа пересчитывается. Страховая сумма определяется размером последнего годового взноса. Клиент не может менять свои взносы как угодно, а только в соответствии с правилами, устанавливаемые конкретной страховой компанией. Сумма накоплений формируется из реально вкладываемых Клиентом денег, каждое изменение программы будет стоить дополнительных затрат Клиенту, а для АО «Дочерняя компания Народного Банка Казахстана по страхованию жизни «Халык-Life» - это регистрация нового пакета документов, полное изменение компьютерной программы, изготовление и выдача нового полиса, внесение корректировок в финансовые расчеты компании. Компания предпочитает стабильность, когда Клиент вносит одинаковые взносы, это выгодно как Компании, так и Клиенту.</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 55 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 55 ? accordion = 55 : accordion = null">
                                    Если вкладчик одинок (т.е. нет ни ближних, ни дальних родственников), и наступил страховой случай - что будет с его деньгами? Остаются ли они у Компании?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer55" :style="accordion == 55 ? 'max-height: ' + $refs.accordioncontainer55.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Здесь необходимо уточнить о какой программе страхования идет речь.</p>

<p>Если это пенсионный аннуитет, то в момент заключения договора клиент сам выбирает условия наследования, он может назначить наследниками конкретных людей (это могут быть и не родственники), либо страховую компанию.</p>

<p>Если клиента интересует программа накопительного страхования, то в данном случае клиент обязательно должен указать выгодоприобретателей (это могут быть и не родственники), при страховом случае по данной программе наследником клиента компания выступать не может.</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 56 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 56 ? accordion = 56 : accordion = null">
                                    Можно ли передать права на полис другому лицу? И в каких случаях?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer56" :style="accordion == 56 ? 'max-height: ' + $refs.accordioncontainer56.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>В целом передать право на страховой полис другому лицу можно, но только при условии письменного согласия застрахованного лица. В данном случае необходимо понимать, что в терминологии, используемой в страховании, существуют определения: «Страхователь», «Выгодоприобретатель» и «Застрахованный».</p>

<p>Страхователь – это лицо, заключающее с компанией по страхованию жизни договор страхования, которое оплачивает страховые взносы и несет ответственность по договору страхования. Выгодоприобретатель - это лицо, которое в соответствии с условиями договора страхования является получателем страховой выплаты. А Застрахованный – это лицо, в отношении которого осуществляется страхование, то есть тот, чья жизнь и здоровье застрахованы по договору страхования. Именно поэтому, если Страхователь и Застрахованный – разные люди, то для передачи прав на полис другому лицу требуется письменное согласие Застрахованного.</p>

<p>В каждом новом страховом году клиент имеет право изменять условия страхования, так же клиент может изменить страхователя, то есть передать обязанности по договору другому лицу, но изменить застрахованного нельзя.</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 57 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 57 ? accordion = 57 : accordion = null">
                                    Потерял полис, что делать?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer57" :style="accordion == 57 ? 'max-height: ' + $refs.accordioncontainer57.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>При утере оригинала страхового полиса, необходимо заполнить форму заявления об утере и выписке дубликата. Выписывается аналогичный утерянному полис и ставиться на верхнем правом углу штамп «Дубликат».</p>

<p>
	<br>
</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 58 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 58 ? accordion = 58 : accordion = null">
                                    Что произойдет, если очередной страховой взнос не уплачен вовремя?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer58" :style="accordion == 58 ? 'max-height: ' + $refs.accordioncontainer58.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>В случае неуплаты очередного страхового взноса, Страхователю предоставляется период отсрочки 30 календарных дней, в случае неуплаты взноса по истечении периода отсрочки действие полиса приостанавливается на год. Если, в течение года действие полиса не было восстановлено, полис расторгается в одностороннем порядке.</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 59 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 59 ? accordion = 59 : accordion = null">
                                    Каковы гарантии надежности компании?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer59" :style="accordion == 59 ? 'max-height: ' + $refs.accordioncontainer59.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>У каждого из нас свои понятия о надежности и поэтому для человека, не связанного со страхованием, бывает сложно определить, надежна компания или нет. На что же смотреть в первую очередь, определяя, надежна страховая компания или нет?</p>

<p><strong>В страховании надежность компании определяют следующие параметры:</strong></p>

<ul>
	<li>Наличие у компании лицензии для работы на территории РK.</li>
	<li>Учредители компании, их финансовая состоятельность.</li>
	<li>Перестраховывает компания свои риски и где?</li>
</ul>

<p>Если Клиент получил ответы на эти вопросы и ответы его удовлетворили, значит, компания надежна.</p>

<p>АО «Дочерняя компания Народного Банка Казахстана по страхованию жизни «Халык-Life» было основано в ноябре 2005 года как дочерняя организация одного из ведущих банков страны АО «Народный Банк Казахстана», который по сей день является системообразующим банком страны и владеет 100% акций Компании.</p>

<p>17 ноября 2006 года Компания получила Лицензию на право осуществления страховой деятельности. В июне 2009 года Компания получила Лицензию на право осуществления перестраховочной деятельности.</p>

<p>04 ноября 2016 года Компанией была получена обновленная лицензия №2.2.41 в связи с изменением фактического места положения головного офиса Компании.</p>

<p>Компания переоформила лицензию на право осуществления страховой (перестраховочной) деятельности по отрасли «страхование жизни» и получила обновленную лицензию &nbsp;№2.2.10 от 11 октября 2022 года.</p>

<p>28 декабря 2022 года Компания переоформила лицензию на право осуществления страховой (перестраховочной) деятельности по отрасли «страхование жизни» и получила обновленную лицензию &nbsp;№2.2.12.</p>

<p>&nbsp;</p>

<p>АО «Халык-Life» является членом Ассоциации Финансистов Казахстана, а также имеет сертифицированную &nbsp;Систему Менеджмента Качества соответствующую международному стандарту ISO 9001:2015 и подтвержденную международной компанией Британский Институт Стандартов (BSI), сертификат о соответствии стандарту Системы Экологического Менеджмента CT РК ISO 14001-2016 (ISO 14001-2015).</p>

<p>Международное рейтинговое агентство S&amp;P Global Ratings присвоило АО «Халык-Life» &nbsp;долгосрочный рейтинг финансовой устойчивости на уровне «ВВВ-» и рейтинг по казахстанской национальной шкале «kzAАА». Прогноз изменения рейтинга - «Стабильный».
	<br>
	<br>Компания имеет рейтинг финансовой устойчивости на уровне «B++» и кредитный рейтинг на уровне «bbb», который является наивысшим среди всех казахстанских компаний по страхованию жизни, от международного рейтингового агентства АM Best. Прогноз по рейтингам «Стабильный». </p>

<p>С развитием региональной филиальной сети подразделений в 20 городах Казахстана и, благодаря накопленному опыту, АО «Халык-Life» готово предоставлять надежные услуги по страхованию жизни как можно большему числу казахстанцев.</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 510 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 510 ? accordion = 510 : accordion = null">
                                    Что этакое – андеррайтинг страховой компании?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer510" :style="accordion == 510 ? 'max-height: ' + $refs.accordioncontainer510.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Дословно&nbsp;<strong>"underwriting"</strong> переводится с английского как&nbsp;<strong>"подписание под"</strong>чем-либо, под какими-либо условиями.</p>

<p>Андеррайтинг – это процесс, заключающийся в анализе и отборе рисков для принятия их на страхование (перестрахование); включает их идентификацию, оценку, классификацию по источникам и степеням опасности, квалификацию на стандартные или нестандартные, определение сроков, условий и размеров покрытия, расчёт размеров страховой премии.</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 511 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 511 ? accordion = 511 : accordion = null">
                                    Какие виды андеррайтинга проводятся при страховании жизни и здоровья?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer511" :style="accordion == 511 ? 'max-height: ' + $refs.accordioncontainer511.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>При страховании жизни и здоровья человека проводятся следующие виды андеррайтинга:</p>

<ol>
	<li>медицинский</li>
	<li>профессиональный</li>
	<li>финансовый</li>
	<li>риски свободного времени.</li>
</ol>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                            </div>
        </div>
                <div class="section__common_inner section__wide_inner">
            <div class="section__title">
                <h3>Добровольное ненакопительное страхование</h3>
            </div>
            <div class="dropdown__tablet_block">
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 61 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 61 ? accordion = 61 : accordion = null">
                                    По договору аннуитетного страхования (в случае потери кормильца) удерживаются ли какие-то суммы с выплаты?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer61" :style="accordion == 61 ? 'max-height: ' + $refs.accordioncontainer61.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <ol>
	<li>По договору аннуитетного страхования с выплаты НЕ удерживаются обязательные пенсионные взносы;</li>
	<li>В случае, если получатель аннуитетных выплат по договору аннуитетного страхования является резидентом Республики Казахстан, страховые выплаты не подлежат налогообложению индивидуальным подоходным налогом;</li>
	<li>По договору аннуитетного страхования &nbsp;с выплаты удерживается индивидуальный подоходный налог в размере 15% в случае, когда Застрахованным является нерезидент Республики Казахстан.</li>
</ol>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 62 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 62 ? accordion = 62 : accordion = null">
                                    По договору аннуитетного страхования (при установлении инвалидности) удерживаются ли какие-то суммы с выплаты?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer62" :style="accordion == 62 ? 'max-height: ' + $refs.accordioncontainer62.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <ol>
	<li>По договору аннуитетного страхования (по инвалидности) с выплаты удерживается обязательный пенсионный взнос 10%, в том случае, если Застрахованному установлена инвалидность 1, 2 или 3 группы со сроком переосвидетельствования.</li>
	<li>По договору аннуитетного страхования (по инвалидности) с выплаты НЕ удерживается обязательный пенсионный взнос, в том случае, если Застрахованному установлена инвалидность 1 или 2 группы бессрочно.</li>
	<li>По договору аннуитетного страхования (по инвалидности) с выплаты НЕ удерживается обязательный пенсионный взнос, в том случае,если Застрахованный является пенсионером.</li>
	<li>По договору аннуитетного страхования (по инвалидности) с выплаты удерживается индивидуальный подоходный налог 15% в том случае, если Застрахованным является нерезидент Республики Казахстан.</li>
</ol>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 63 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 63 ? accordion = 63 : accordion = null">
                                    По договору добровольного аннуитетного страхования удерживаются ли какие-то суммы с выплаты?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer63" :style="accordion == 63 ? 'max-height: ' + $refs.accordioncontainer63.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p><strong>По договорам добровольного аннуитетного страхования:</strong>
	<br>1) С выплаты не удерживается обязательный пенсионный взнос.
	<br>2) У резидентов Республики Казахстан по договорам добровольного аннуитетного страхования с выплаты не удерживается индивидуальный подоходный налог.
	<br>3) У нерезидентов Республики Казахстан с выплат удерживается индивидуальный подоходный налог в размере 15%.
	<br>
	<br> По договорам пенсионного аннуитета у нерезидентов Республики Казахстан удерживается индивидуальный подоходный налог в размере 10%.</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 64 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 64 ? accordion = 64 : accordion = null">
                                    Как расторгнуть договор страхования жизни заемщика и вернуть остаток страховой премии?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer64" :style="accordion == 64 ? 'max-height: ' + $refs.accordioncontainer64.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Страхователю (клиенту) необходимо обратиться в филиал страховой компании, при себе иметь удостоверение личности, реквизиты 20-значного банковского счета, справку подтверждающая закрытие кредита.</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 65 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 65 ? accordion = 65 : accordion = null">
                                    По договору страхования жизни заемщика можно ли заранее сделать расчет по возврату части страховой премии в случае досрочного погашения займа?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer65" :style="accordion == 65 ? 'max-height: ' + $refs.accordioncontainer65.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Да, для этого Страхователю (клиенту) необходимо обратиться в контакт-центр по номеру 7123 либо в обратиться в филиал страховой компании для предварительного расчета.</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 66 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 66 ? accordion = 66 : accordion = null">
                                    Можно ли заключить договор обязательного страхования от несчастного случая в онлайн формате? 
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer66" :style="accordion == 66 ? 'max-height: ' + $refs.accordioncontainer66.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>Да, онлайн договоры обязательное страхование от несчастных случаев заключаются на сайте <a href="https://online.halyklife.kz">https://online.halyklife.kz</a> </p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 67 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 67 ? accordion = 67 : accordion = null">
                                    Как можно расторгнуть договор страхования выезжающих за рубеж и вернуть оплаченные деньги в случае отказа от страхования?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer67" :style="accordion == 67 ? 'max-height: ' + $refs.accordioncontainer67.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>При отказе Страхователя (Застрахованного) от договора страхования до начала срока страхования, страховая премия подлежит возврату Страхователю (Застрахованному) в случае отказа Посольств в открытии визы в размере 100 % от уплаченной страховой премии.</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                <div class="smooth-accordion-alpine" x-data="{accordion:null}">
                    <div class="smooth-accordion-alpine-wrap">
                        <div class="smooth-accordion-alpine-list">
                            <div class="smooth-accordion-alpine-item" :class="{'collapsed': accordion == 68 }">
                                <a class="smooth-accordion-alpine-btn text-medium" @click="accordion !== 68 ? accordion = 68 : accordion = null">
                                    Как расторгнуть договор  пенсионного аннуитета?
                                </a>
                                <div class="smooth-accordion-alpine-content" x-ref="accordioncontainer68" :style="accordion == 68 ? 'max-height: ' + $refs.accordioncontainer68.scrollHeight + 'px' : ''" style="">
                                    <div class="smooth-accordion-alpine-content-wrap">
                                        <div class="item__accordion">
                                            <div class="item__wrap">
                                                <div class="item__content">
                                                    <p>В соответствии с законом Республики Казахстан "О пенсионном обеспечении в Республике Казахстан" расторжение договора пенсионного аннуитета возможно только по инициативе страхователя при условии заключения договора пенсионного аннуитета с другой страховой организацией, но не ранее двух лет с даты его заключения или в случае смены гражданства. Страхователь обязан при расторжении договора пенсионного аннуитета обратиться с заявлением о расторжении договора пенсионного аннуитета и предоставить оригинал договора с новой страховой организацией в течение десяти рабочих дней со дня заключения нового договора пенсионного аннуитета.
	<br>В случае выезда на постояное место жительство за пределы Республике Казахстан, необходимо предоставить помимо паспорта иностранного гражданина, дополнительно документ подтверждающий факт выезда из миграционной службы, а также счет, открытый в банке на территории Республике Казахстан.</p>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                            </div>
        </div>
            </div>
"""


soup = BeautifulSoup(html_content, 'html.parser')

sections = soup.find_all(class_="section__common_inner")

links_array = []
for section in sections:
    items = section.find_all(class_="smooth-accordion-alpine-item")
    for item in items:
        link = item.find(class_="smooth-accordion-alpine-btn").get_text(strip=True)
        links_array.append(link)

paragraphs_array = []
for section in sections:
    items = section.find_all(class_="smooth-accordion-alpine-item")
    for item in items:
        paragraph = item.find(class_="item__content").get_text(strip=True)
        paragraphs_array.append(paragraph)


def get_links_array():
    return links_array

def get_paragraphs_array():
    return paragraphs_array

