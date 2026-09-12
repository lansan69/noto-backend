import os
from openai import OpenAI
from app.core.config import settings
from app.features.notes.data.models.notes_models import NotesModel

print(settings.ALIBABA_API_KEY)
print(settings.ALIBABA_OPENAI_COMPATIBLE_ENDPOINT)

client = OpenAI(
    api_key=settings.ALIBABA_API_KEY,
    base_url=settings.ALIBABA_OPENAI_COMPATIBLE_ENDPOINT
)

transcript = """

Speaker A
00:00:00 - 00:00:14
¿Cuánto tiempo? ¿Cuántas licencias tengo que vender para sacar al menos el costo? O sea, los 3 millones rápidamente. ¿Quién dice? Yo, 3 millones. O sea, para sacar el costo después de la licencia número, ¿qué?

Speaker B
00:00:14 - 00:00:14
30.

Speaker A
00:00:14 - 00:00:23
¿Seguros? Sí, porque llevo 3 millones, me costó desarrollar y vale 100,000 pesos una licencia.

Speaker B
00:00:26 - 00:00:34
De esos 3 millones tienes que calcular cierto porcentaje para, de acuerdo al tiempo que se mantiene.

Speaker A
00:00:34 - 00:00:41
Pasa diferente cuando lo vendes masivamente. Si tú lo vendes masivamente, obvio, siempre tienes una ganancia.

Speaker B
00:00:42 - 00:00:53
Pero si no, si lo estimando de tiempo para vender esas 30, de tiempo en la pluma, esas 30 licencias te toman cierta cantidad de tiempo, tienes que tomarle el tipo de mantenimiento de tu equipo.

Speaker A
00:00:53 - 00:02:20
Para llegar a recuperar estos, o sea, en teoría deberíamos de ganar desde el principio y no arriesgarnos a que en la licencia número 30 ya corresponde recuperar el costo. ¿Qué tendría yo que hacer entonces para que ya de una vez, este, se tuviera la ganancia? Pues entonces dividir ese desde el costo de licencia, ya estar casi asegurando esa ganancia, ¿no? Pero lo que se dice acá es que te costó 30, este, 3 millones te cuesta 100,000 pesos una licencia, con 30 licencias tú ya recuperaste el costo. La licencia 31 y las que le sigan ya van a ser la ganancia. Sí, es como se maneja realmente. Ahora, si lo vendes a un solo cliente, sí le tienes que agregar ese porcentaje, que casi siempre debe ser como el 100%. O sea, por eso decía yo que si se lo venden a un solo cliente, de 6 millones o mínimo 5 millones. Para que ella tenga la ganancia en esa venta. Porque acuérdate que cuando se lo vendes a un solo cliente, seguramente quiere que sea el único, sea el exclusivo. Entonces ya no lo vas a poder vender a más clientes, aunque se dediquen a lo mismo. Incluso muchos pues ya cedes los derechos del código y demás, y tú te quedas siendo solo el autor moral, pero ellos ya son los dueños del código, y podrían ellos a su vez revenderlo a otras de su compañía, porque son estrategias de mercado. Que muchos llegan a utilizar en este sentido.

Speaker B
00:02:20 - 00:02:26
Eso lo vendes un poquito más barato, pero le pides que tengas un contrato exclusivo de mantenimiento.

Speaker A
00:02:26 - 00:04:00
Sí, sí, sí. Y también eso puedes dejar en contrato. Tanto para darle esa póliza de garantía, tú debes de obligarlos a que la capacitación la tomen contigo, ¿no? Para que funcione y funcione bien, y si no, tú no respondes, ¿no? Porque si no tomaron la capacitación y demás, puede ser que lo primero que hagan sea estar criticando que no funciona, que no sirve, etcétera. Entonces nunca, nunca den el costo por separado de la capacitación, a menos de que pues se los pidan así en el desglose. Pero eso sí, en el contrato condicionen a que deben de hacer la capacitación obligatoria, si quieren, no para todos los elementos de su organización, sino al menos algunos, y que se comprometan a que esos van a capacitar al resto de los usuarios. No, pero la capacitación es algo importantísimo. Y también es importantísimo, señores, que cuando documenten su software, si queremos tener calidad, tengamos manual técnico, verdad, que es donde dice todo cómo se creó, y manual de usuario, que es donde dice cómo lo vas a instalar, cómo funciona, problemas principales, etcétera, etcétera. Bueno, pues vamos a dejar que entonces nuestros compañeros del equipo nos digan qué onda con la gestión. Yo solo fue un preámbulo y pongan atención, por favor, qué involucra la gestión. Y los que hayan investigado algo diferente también nos ayudan a enriquecer esta parte. Entonces, equipo 6, por favor, ¿verdad? O 7, son 7. Ok, Héctor y compañía.

Speaker B
00:04:01 - 00:04:48
Bueno, la gestión de proyectos de software consiste en aplicar conocimientos, capacidades, herramientas y técnicas para planificar Generar, ejecutar y controlar un proyecto de software, asegurando que cumpla con los requisitos del cliente y los estándares de calidad. El objetivo principal es maximizar la eficiencia, minimizar riesgos y mejorar la comunicación y aumentar la satisfacción del cliente. En este caso, la gestión suele estar dividida en 5 fases principales, que sería la de iniciación, que sería definir los objetivos y el alcance y la viabilidad del proyecto. Para documentarlo todo en una acta y que se pueda declarar el trabajo sobre lo que se va a realizar. Después está la planificación, que ya es establecer metas, cronogramas, recursos, presupuestos, entregables, identificando riesgos y los roles dentro del equipo.

Speaker A
00:04:48 - 00:04:48
Perfectísimo.

Speaker B
00:04:48 - 00:05:31
Después sería la ejecución, que ya sería el implementar el plan en el desarrollo del software con los requisitos, y sería ya el trabajo en equipo para desarrollar el software. Después seguiría el monitoreo y control, supervisar el progreso, gestionar cambios, hacer reuniones, controlar la calidad, costos, los riesgos, y checar que se vayan cumpliendo con los objetivos. Finalmente sería el cierre, que sería entregar el producto, obtener la aprobación de los clientes y documentar lo que se ha aprendido para proyectos futuros. Muy bien, son las buenas prácticas, que es definir claramente el alcance. Puedes evitar la expansión no controlada del proyecto y asegurar que todos los involucrados comprendan el objetivo.

Speaker A
00:05:32 - 00:05:35
Formular un equipo competente y motivado.

Speaker B
00:05:36 - 00:05:46
La comunicación constante. Gestión de riesgos, que pues dice identificar problemas potenciales y desarrollar planes de mitigación antes de que se conviertan en crisis.

Speaker A
00:05:48 - 00:08:23
Muy bien, y eso es súper importante porque, a ver, equipo 1 Te toca contratar a la gente, ¿en qué te basas para contratarlos? Equipo 2, te toca motivar a la gente, ¿cómo lo haces para hacer esto? Equipo 3, los sueldos que le vas a asignar y demás, ¿cómo lo harías? Y equipo 4, 5 y 6, la misma pero paralelo, no, en espejo con los que ya asigné. Y equipo 6, 7 y 8, no, sino no, 7, 8 y 9, la misma situación. Y Y el último, todo. Yo confío en ustedes así tan fuerte que les toca ver las 3 cosas que van a ver cada uno de los 3 sectores de cada pila. Dijimos primero, a ustedes el 1 le tocó qué, y los segundos cómo motivar, y los terceros ¿Cuánto debería pagarle los salarios a cada equipo? Bueno, entonces 2 minutos, hagan su equipo con su equipo y me van a decir qué. Ahorita los dejo continuar. ¿Algo más faltaba de ustedes de la gestión? No, digo, para cerrar esta parte de la gestión. ¿Y por qué? ¿Por qué debe hacer el personal? ¿Por qué creen? O sea, todo es importante, ¿no? Pero el personal juega un papel súper fuerte en una organización. Porque, Eric, cuando alguien contrata a una persona le hacen psicométricos. Sí, porque Santiago y equipo, cuando alguien contrata a una persona, es muy capaz técnicamente hablando, pero a lo mejor lo rechazan. ¿Por qué crees? ¿Qué crees que pasa ahí? En paralelo están pensando con la actividad que les tocó, pero a ver, díganme. No le busquen tanto, piensen ustedes. O sea, olvídense que ChatGPT existe, que Google, que todo, y díganme su propio pensar al respecto de esto. Alce la mano quien ya llevó ingeniería de software, que ya la llevó.

Speaker B
00:08:23 - 00:08:24
Ingeniería, ya.

Speaker A
00:08:25 - 00:09:31
Ok, seguramente se toparon con tener que hacer un plan de proyecto, gestionaron ese proyecto que hicieron en el curso, ¿no? Que llevaba ese plan de proyecto, ¿no? Prácticamente ya se lo había comentado en la introducción, ¿no? Pero quien no lo haya llevado, definitivamente es interesante que lo revise y lo estaremos platicando aquí como un recordatorio. Sin embargo, sí sería interesante que si ya lo llevaron, lo revisen en sus notas nuevamente. Si no, pues acá lo vamos a tener que retomar. Porque es algo que tienen que aplicar cada vez que te han citado al frente de un proyecto. Eso porque según yo va a ser todo el tiempo, ¿no? Entonces, a ver, díganme, ¿ya tienen sus 2 minutos o no los dejé pensar en los 2 minutos? Seguí yo hablando. Me callo y 2 minutos a partir de este momento. Eric, tómame el tiempo de 2 minutos para que les avises a los compañeros. Según yo, 12:36 son. 12:40.

Speaker B
00:11:44 - 00:12:09
Ja, dat is het.

Speaker A
00:12:47 - 00:12:55
Para luego, y para interrumpirles, vayan pensando en dónde van a querer trabajar.

Speaker B
00:13:01 - 00:13:03
Ya tienen, ya pasó el tiempo.

Speaker A
00:13:04 - 00:13:11
Sí, pero dijimos que 12:40, ¿no? Que les damos minutos más y un minuto son 12:81.

Speaker B
00:13:11 - 00:15:28
Hasta que pase por allá, si me cae, que yo no sé. परसों ये ना बात कुछ चलेगा। Con esto puedes poner como que un marco de referencia, tal vez como por ejemplo el promedio que se le paga por este A ver, entonces, ¿qué dijo el 1 con respecto a eso?

Speaker A
00:15:31 - 00:15:35
Sí, su equipo, que díganme qué acordaron entre ustedes.

Speaker B
00:15:35 - 00:16:03
A ver, guárdense silencio. La experiencia que lleva la persona, los proyectos que haya realizado. También habilidades como trabajo en equipo, comunicación, el adaptarse a los problemas que vayan surgiendo también mediante entrevistas, cómo resolver los problemas. Bueno, por prácticas, trabajo.

Speaker A
00:16:04 - 00:16:05
Ok, eso iba a preguntar.

Speaker B
00:16:08 - 00:16:32
Entrevistador, bueno, entrevistado tiene que reflejar su conocimiento para esa práctica, es solución de problemas, y cómo desarrolla o tiene los logros. O sea, tiene que ver si el porqué esta persona tiene que seguir en su trabajo, el motivo de por qué deben elegirlo a él.

Speaker A
00:16:33 - 00:16:43
O sea, le preguntarías a él directamente, ¿por qué te tengo que contratar a ti en vez de a los otros? Bueno, ¿qué más?

Speaker B
00:16:44 - 00:16:57
Igual, este, asegurar que todas las personas candidatas sean evaluadas bajo los mismos criterios, o sea, no, no haya sesgos con alguien nada más porque lo conozco, o sea, que sean evaluados bajo el mismo criterio.

Speaker A
00:16:57 - 00:16:59
Sí, ok.

Speaker C
00:16:59 - 00:17:05
Y también revisar pues sus valores personales y su forma Después de trabajar coincidan con el equipo.

Speaker A
00:17:06 - 00:20:17
Sí, también, claro. Yo me acuerdo alguna vez iba a dar clases en Azahar y, este, y una de las cosas que me dijeron es que en la mañana me tocaba la clase a las 7 y entonces tenía que hacer la oración de ahí en la escuela, ¿no? Entonces, este, yo afortunadamente pues sí era católica y todo. De todos modos, no me quedé a trabajar ahí. Pero este, porque me quedaba muy lejos y demás, no. Pero sí dije, pues está medio, acuérdense que la educación de ser laica y otras cosas, no. Entonces a lo mejor, aunque yo sea muy creyente, no iba acorde. Pero imagínate si alguien además, este, de otra creencia iba, pues definitivamente ellos mismos iban a descartar, no, ni siquiera le iban a decir. O sea, a mí me propusieron que tenía que hacer la oración de las 7 de la mañana porque sabían que yo de por sí venía de una escuela religiosa, o qué sé yo, no. Pero no sé si a todos sus candidatos, y precisamente pues no iba a coincidir a lo mejor con sus valores y demás si no eran igual de la misma creencia, no, en ese trabajo. Digo, por dar un ejemplo así súper burdo, pero bueno, eso es algo que también sí es importante. Acuérdense que el recurso humano es el más importante en todo. Es el más complejo porque es autónomo, es independiente. Yo no puedo obligar a alguien, aunque sea muy genial en esto, obligarlo a pensar como pienso yo para que resuelva de la forma en que resuelvo yo. O sea, él tiene su propia forma de resolver, de pensar y demás. Por ejemplo, hablando de nosotros los profesores, no, la libre cátedra. Creo que es muy interesante esto de la libre cátedra, pero también es muy interesante esa parte de respetar lo que sigue del otro lado, con quién, con quién vas a colaborar, ¿no? Este, alguna vez me tocó ver de algún profesor que decía, pues como no te supiste la ecuación, entonces vas a hacer 100 lagartijas aquí delante de tus compañeros. Ay, Dios, está bien duro eso, ¿no? Los derechos humanos y la locura del profe y todo mal, ¿no? Digo yo. Entonces sí es importante el recurso humano. Creo que a los compañeros, a lo mejor otro equipo lo menciona. Los dejo que otro equipo lo mencione, si no, pues ya les diré otra de las cosas también importantes que se deben considerar cuando tú contratas a un recurso humano. A ver, equipo 4, algo más. Y el 1, el 1 nada más. El 4 le tocó esta misma pregunta, ¿no? ¿Quiénes son 4? A ver, díganme, Óscar. Sí, no, porque dijimos el 1, el 1, el 2 y el 3, se repartieron 3 puntos. A ver, entonces, ¿quién más hizo esa misma pregunta que los compañeros? Bueno, a ellos les tocó en qué me baso para contratarlos, ¿no? Y el segundo le tocó cómo los motivo, y al tercero cómo sé pagar este asunto, ¿no?

Speaker B
00:20:17 - 00:20:18
Ese es el que nos queda.

Speaker A
00:20:19 - 00:20:27
Ah, bueno, entonces ustedes son, sí. ¿A quién más le tocó el cómo los contrato? Porque dijimos que se repetían, ¿no?

Speaker D
00:20:28 - 00:20:28
Sí.

Speaker B
00:20:28 - 00:20:29
¿A quién?

Speaker A
00:20:30 - 00:20:54
Al cuatro, según yo. ¿Quién es el cuatro? Entonces vieron otra cosa, o bien si vieron otra cosa pues vemos esta otra cosa. Pero entonces el otro equipo, el 4, el 7, ¿no es el otro? Si no la tienen preparada, ahorita participan en la que sí prepararon, aunque ahí sean más personas.

Speaker D
00:20:54 - 00:22:45
Pero bueno, a ver, entonces pues este no la tenemos preparada como tal, pero este pues podremos este mencionar un poquito de las ideas que tenemos referente al cómo seleccionar el recurso humano. No hay ningún problema. A ver, escucha Que en este caso yo considero que muy importante, pues solamente lo básico siempre es que se cumplan los requerimientos básicos que se piden en el puesto. Pero también hay, sí, aparte de las competencias, también mencionar a mis compañeros la parte de las entrevistas. Más en este área de software es muy importante lo que es la parte de la creatividad, la abstracción y la resolución de problemas, que es lo que se suele hacer en un test técnico para verificar que verdaderamente, aparte de lo que pide el puesto, que esta persona sea capaz de resolver problemas, aplicar los conocimientos que ya tiene, y pues justamente plasmarlos en este caso pues en código, ¿no? Si es para un puesto de gestión, pues en un caso práctico. Pero también es muy importante evaluar la parte, no sé si es la psicológica, referente a la parte que tú tienes que observar y tienes que hacer preguntas para saber si Es serio, porque obviamente es una pérdida el hecho de que tú contrates a alguien que, ok, muy bueno, pero no sabes si en un futuro esta persona sí se va a quedar a largo plazo. Entonces, una parte muy importante para seleccionar el recurso es, este, sondear, es verificar que verdaderamente esta persona te va a ser útil, que va a cumplir, se va a alinear con los objetivos que tienes tú a corto o a largo plazo. Si buscas a alguien para solo un proyecto, o que vas a buscar que esta persona pues sea responsable, que ya tenga proyectos terminados, Pero si tú la quieres a largo plazo como un desarrollador, como un gerente, como un manager de pues un tiempo bastante definido, lo que necesitas considerar es si verdaderamente esta persona con su background, con sus experiencias laborales y con lo que tú llegaste a notar en ese encuentro frente a frente, si verdaderamente se va a quedar, por así decirlo.

Speaker A
00:22:46 - 00:25:40
Yo consideraría que son como, sí, ustedes habrán visto que en algún caso algunas empresas contratan Y no te pagan mucho, pero la motivación, por ejemplo, es que te vamos a certificar, a pagar esas certificaciones, la capacitación y demás. Entonces, bueno, pues ante eso, a lo mejor ahí ya le están dando también un elemento para la parte de cómo los motivo o cómo les pago, ¿no? También del 2 y del 3 de las propuestas que tenían que ver. Pero sí es muy importante ese aspecto psicológico. ¿Hay alguien más de esta misma pregunta? No, ¿verdad? Son solo ustedes. Porque el otro se confundió. Y bueno, no importa. Efectivamente, yo creo que las empresas sí les preocupa mucho esa parte psicológica. Si una persona en el equipo es muy buena técnicamente pero es una persona conflictiva, pues no les conviene en la organización porque les va a mover a toda la gente, les va a dañar el ambiente, el ecosistema de ese equipo de trabajo, ¿no? Siento yo. Y bueno, no solo yo, todos los empleadores como que primero se basan, ok, ya hiciste lo que dicen allá, tu examen, pasaste todos los retos que te puse. Casualmente ocupan mucho esa onda de, hay este proyecto, a ver cómo lo resuelves, hazme este programa, y si veo que lo hiciste bien, ya te contrato, ¿no? Entonces, este, también eso a veces yo siento injusto y mañoso, pero ese es otro tema, ¿no? Entonces, pero ya que vi que técnicamente resuelves, la parte muy importante para contratar es esa. El aspecto psicológico, psicológico y demás, no. Porque también si tengo aquí un loco que va a hacer algún tiroteo, híjole, ya vamos a volar, no. Entonces, aunque sea muy bueno, aunque sea muy genio, no, lo vemos tiro por viajero. Luego, por otro lado, vemos que hay prejuicios, no. Si una persona viene con traje, entonces, este, pues no. O si viene mal arreglado, entonces no. O sea, no, yo creo que a las personas debemos de verlas libres de contexto. Por lo que son, por lo que valen, sin que nos importe nada de eso demás, no, de ellos, no. Sobre todo en nuestra área somos como más flexibles en ese sentido. Lo vemos que Google se acotó a esa parte, no, andan hasta en pijama ya en Estados Unidos y jugando ping pong. Y bueno, pues ahora ya vete a hacer tu programa, y si te quedas en la tarde, en la noche, o aquí vives, o sea, no hay problema. Entonces te estamos dando todas las facilidades para que te desenvuelvas y des lo mejor de ti, ¿no? Como políticas de contratación, ¿no? O de laborales, ¿no? Y a lo mejor por eso te sientes feliz ahí, ¿no? O a lo mejor si somos de otra personalidad, a lo mejor eso no nos gusta. Entonces también hay muchas cosas que se tienen que aprender ahí. ¿Y qué ibas a decir, Óscar?

Speaker B
00:25:40 - 00:26:09
Bueno, también de otro aspecto que incluye es cómo es la empresa hacia este, trabajadores, porque luego hay empresas que sí son un poquito pesadas, principalmente los que pagan con pizza los tiempos extras. Ahí sí, ahí sí es como, o sea, prácticamente quiere la empresa que te pongas la camiseta por ellos, y luego hay ocasiones en las que los jefes ni siquiera hacen nada.

Speaker A
00:26:10 - 00:30:20
Sí, claro, y eso está injusto, ¿no? También Y afortunadamente muchos sí nos podemos percatar de que dices, oye, sí, sí está bien, pero por lo menos me vas a agarrar, ¿no? O sea, sí, sí vengo a trabajar y créeme que yo con mis capacidades me puedo ocupar las pistas que yo quiera. No, no, así, de hecho, si vieron, ahí hasta una categoría de software que se llaman Beerware, que según les dan una cerveza a cambio del software, ¿no? Hasta viene ahí categorizada. Y eso a mí, híjole, me duele pues porque Y yo supe por ahí de alguna empresa que sí les pagaban de repente así también. O sea, y es feo porque nosotros somos personas muy valiosas como para que nos quieran conseguir por ese lado. Pero curiosamente algunos sí los convencen de esa manera, ¿no? Y no, no es correcto, no es justo, digo yo. Y bueno, verlo ahí, no, no hagamos lo que no quieran queramos que nos hagan. El día que ustedes estén enfrente, pues háganlo de la mejor forma, la forma más justa, la forma más digna. Y lo que se les da es trabajo, pues se paga el trabajo, ¿no? Y ya, más pizza. Pues sí, al rato estamos bien gordos, ¿no? Y eso que a mí no me pagaron, que eso me las compraba yo. Tengo que yo es que estoy gorda, ¿no? Su trabajo también es súper sedentario. Esta área del conocimiento es bien sedentaria. Rapidito pueden embarnecer ahora que estén solo programando y sin parar, o estar en ese ámbito estático sí nos llega a causar problemas, ¿no? Entonces, este, yo llevo muchos años con el problema y no me cierro a que hoy ni me siento cuando diga esto está bien gorda esta vez, o si mientras estaba comiendo estaba muy feliz, entonces ni se sientan ni se traumen. No llorabas mientras comías. Entonces yo digo que hay que apechugar y tomar cartas en el asunto ya, no, porque si no, la salud te cobra factura, no, y con los años peor. Entonces lleven una vida bonita, saludable, desde ahorita que pueden, y vayan controlando en la medida para que no les pase lo que a mí, ¿verdad? Y bueno, pues este, todo tiene un nunca es tarde, y yo creo que es momento también de que puede uno seguir mejorando, ¿no? Y a mí, a principio del año, me detectaron, este, que me estaba alterando la presión un poco y el azúcar se estaba subiendo. Traigo un sensor, digo, por si un día me azoto aquí, en mi celular traigo para medirlo, es por vía Bluetooth, y poder saber cuánto traigo de azúcar, ¿no? Porque lo que es peor, me dio el medicamento porque dijo, no, esta gorda no va a hacer caso, va a seguir igual. Y pues solo se me baja el azúcar, ¿no? Y eso es más feo. Y ya me movieron el medicamento y gracias a Dios voy a estar bien. Pero bueno, salga a colación, no, con el tema. ¿Alguien más tiene aquí algún padecimiento preocupante que todos podamos y le vamos a ver por auxiliar en su momento? Digo, hay gente que puede tener también lo mismo, de lo que se te baja el azúcar, sobre la presión, o que te pueden dar convulsiones o alguna cosa, para que sepamos qué hacer en caso o a quién llamar, no. Y si no, pues es interesante. Yo no me mando a hacer la flaquita, pero pues aquí, si me pasa aquí en la comunidad, creo que todos conocen, o la mayoría tendría el sentido humano de ir a avisar a alguna autoridad o a quien pudiera auxiliarlo, o el médico, no sé. Entonces igual, si alguien tiene alguna, que nos la diga a colación de lo que estamos platicando. Y del, y todo salió porque la contratación del personal y las maneras de motivar y otras cosas, o de pagar, de pagar es peor, no, porque sabes qué, sí, invítame la pizza, pero págame mis horas extras. Pues es otra cosa, no. O mejor no me explotes así, no. Organicemos todo, y si tiene un mayor tiempo de desarrollo, pues tiene su mayor tiempo de desarrollo, no. En fin, segunda pregunta era la motivación, ¿verdad? Entonces, ¿quiénes querían participar con la motivación? Era el 2, el 5 y el 8, ¿no? Si no, a ver, entonces el 2, ¿qué dijo?

Speaker C
00:30:21 - 00:31:08
Este, bueno, por nuestra parte reclamamos que la motivación, actualmente las empresas buscan mucho lo que es motivar a sus empleados, ya que se han dado cuenta de que una buena motivación, un buen entorno fomenta una mayor trabajo, una mayor productividad. Sí, y es por ello que actualmente las empresas, aparte de que gusta mucho el tema, fomenta la concentración, también buscan cómo mantener y cómo elevarlo. Parte de eso son las motivaciones, y muchas veces son, este, tipo de facilidades, recompensas, algún tipo que hagan que el empleado, ya sea tanto de oficina como de planta, quiera seguir trabajando.

Speaker A
00:31:09 - 00:32:01
Claro. Sí, yo tengo alumnitos que están, por ejemplo, en Profuturo, exalumnos míos, y que los quiero mucho, nos seguimos frecuentando. Me cuentan, ¿no?, que hacen equipos y que, por ejemplo, si alguien es gordito pues este, si pierdes kilos en tu equipo, pues vamos a ayudarte con un bono de tal. O si ganas kilos, porque también hay unos muy delgaditos, entonces ganas kilos, este, ganas de esos kilos que ganes, te vamos a pagar o le vas a dar un bono a tu equipo. Porque además el equipo te tiene que ayudar a lograr metas o acompañar, no, en ese sentido. Y bueno, pues suena, este, pues motivante también, formas de motivar y de preocuparse por su personal porque quieren esos resultados mejores y una mayor productividad, ¿no? ¿Qué más? 2, 2. La segunda pregunta, ¿quién más decía algo respecto?

Speaker B
00:32:02 - 00:32:21
Bueno, nosotros nos inspiramos un poco con la idea de, este, que es darle la oportunidad de participación sin importar el puesto o la jerarquía, apoyando con estímulos, ya sea como ascensos con este sueldo o ponerlo al frente de su propia propuesta.

Speaker A
00:32:21 - 00:32:47
Sí, eso de ponerlo al frente de su propia propuesta lo hace Microsoft, lo hace Google también. Y por ejemplo, a lo mejor te dan presupuesto limitado, pero eso sí te van cuantificando. O sea, hiciste esta versión, costó tanto, no funcionó, se la vamos agregando al costo, ¿no? Y van viendo todo de cómo va a costar este producto. Pero sí, empresas como este Toyota manejan eso. Y bueno, pues es una motivación también, ¿no?

Speaker B
00:32:47 - 00:33:00
Sí, más que nada para que se sigan, se sientan escuchados, sientan que no hay como tal, que la jerarquía solamente es estructural, no, no, este, no, pues aquí todos somos iguales, ¿no?

Speaker A
00:33:00 - 00:34:06
Todos tenemos acciones o nos dan una participación, y en ese sentido pues se sienten la motivación, ¿no? Telmex también tenían hace años, les daban, este, acciones Y fuera del puesto que fuera, ellos tenían sus acciones. Si después de un tiempo ellos querían vender sus paquetes de acciones, pues ya las vendían, ya costaban más, etcétera. Este, hacer accionista en tu empresa de software podría ser una buena estrategia de tu equipo cuando no cuentas con capital, no estás iniciando, te reúnes con ciertos compañeros o con ciertas personas a hacer tu empresa. Y bueno, pues aquí todos podemos ganar. Ese es nuestro, tu capital es intelectual, ¿no? Y también podría ser contable, una, pues, una forma de, ¿cómo se llama?, de poder motivar a tus equipos, ¿no? Lo usan como estrategia, por eso que les digo también, ¿no? ¿Qué más, Tonatiuh? ¿Qué te llamó la atención?

Speaker B
00:34:06 - 00:34:23
Justo lo que, bueno, comentábamos. Parte de la participación igual hasta varias, no es de, ya bueno, yo tengo este rango, entonces tú.

Speaker A
00:34:27 - 00:37:16
Y también otra forma de motivación podría ser la siguiente: de nuestra área del conocimiento como que nuestro perfil es de repente medio muy ermitaño, no somos muy sociables. A veces nosotros nos gusta estar con tanta gente o amamos no tener que trasladarnos. Entonces trabajar home office puede ser una súper motivación, ¿no? Porque a lo mejor este es más productivo porque para empezar no tienes que hacer todo el gasto y desgaste de traslado, ¿no? Yo, por ejemplo, su casa está a 2 horas de aquí y este, bueno, pues seguramente muchos de ustedes igual, ¿no? 2 horas, 1 hora, el que barato cerca no vive, pues 1 hora, media hora. Pero hay un tiempo de traslado que se gasta en hacerlo físicamente y monetariamente, y la productividad puede de manera proporcional estar siendo baja, baja por esa situación de tenerse que trasladar, ¿no? Yo sé que hay muy bonitas oficinas en Santa Fe y que es una novedad estar yendo, pero les va a gustar la primera semana, la segunda, pero después van a estar mal de tener que trasladarse hasta allá, por ejemplo. Ya mejor se quedan a vivir por allá, buscan que, ojalá, verdad, porque está padre también. Pero si no, te desgasta mucho, ¿no? Entonces esa motivación también de trabajar home office en nuestra área del conocimiento podría ser una solución, ¿no? ¿Para qué lo quieres teniendo aquí en tu oficina? A lo mejor esto puedes tener una oficina virtual y eso ya le va reduciendo costos a la inversión de tu empresa de software, ¿no? ¿Qué otra motivación? O alguien que quiera comentar su experiencia personal, o el que le tocó el equipo. ¿Quién es? ¿Alguien más de ustedes? De la motivación, de cómo motivarían. Está bien, bueno, obviamente todos ellos van a trabajar por dinero, ¿no? Entonces, por ejemplo, algunos bonos de puntualidad, ¿no? Por ejemplo, a lo mejor como ¿Cómo se dice eso? Como que se sientan parte, pero reconocerlos, sí, reconocimiento. Sí, yo tengo un compañero, bueno, es amigo desde que compañeros de la maestría, de la primera maestría que hice en el CineStat, que en su momento hizo un software para la bolsa de valores y le daban regalías. Entonces, pero eso pues te motiva, ¿no? Porque sobre uso, porque si te dan regalías, vale la pena, ¿no? Sí, ¿qué más? ¿Quién más? Compañeros, ¿a ustedes cuál les tocó?

Speaker B
00:37:16 - 00:37:18
Ya participaron.

Speaker A
00:37:18 - 00:37:36
Entonces, los otros, ¿a ustedes qué les tocó? Contratación, va. Ustedes las 3, bueno, nadie más hay del equipo semejante a los puntos que mencionan acá de motivación. ¿Quién más fue de motivación?

Speaker C
00:37:49 - 00:37:56
Tienen espacios para descanso y es algo que le ayuda a la productividad.

Speaker A
00:37:58 - 00:38:56
Sí, claro, lo que decíamos hace ratito, ¿no? Oigan, ¿y cómo hacer que no se desmotiven por motivar a otros? Porque esa es otra, ¿no? Te premio a ti que no eres tan puntual, pero porque eres muy bueno desarrollando Pero a ti no te, a ti que siempre ha sido puntual, estás ahí a la espera del premio. Eso es injusto, ¿no? Pudiera ser y podría, en vez de motivar, desmotivar. Entonces llevar ese balance también lo tiene que hacer un buen líder de proyecto, un buen gestor, una buena gestión de esas historias para no tener problemas en esa organización cuando esté dirigiendo. Sí o no. A ver, motivación. Los que les tocó motivación, a los que no les tocó, ¿cómo hacer para no desmotivar con una motivación de otros a los que no?

Speaker B
00:38:56 - 00:39:11
Entonces, premio para todos, promoviendo a lo mejor cursos de capacitación para también, a lo mejor un bono para también alcancen el nivel de los que sí obtuvieron los mejores bonos.

Speaker A
00:39:12 - 00:39:17
Por ejemplo, sí, evitar el señalamiento.

Speaker B
00:39:17 - 00:39:21
Como si hay un problema, más hablarlo más de forma general antes que señalar a alguien.

Speaker A
00:39:23 - 00:45:05
Eso es bueno. Sí, como hay una frase que dice, no, se felicita en público y se reprende en privado. No sé, no, por ejemplo, eso es algo importante también. El ser humano somos muy complejos, ¿no? Los seres humanos son muy complejos. Y yo les voy a contar una, no voy a decir nombres, pero en algún momento yo estuve a cargo de una jefatura aquí en la escuela, tenía 94 personas a mi cargo, no, primero en 54, y ya tengo muchos años, ustedes no andaban por aquí afortunadamente, pero había otra jefe de departamento que iba a correr a una compañera. Y se estaba agarrando del aspecto de que ya estaba embarazada. Y entonces pues este, ya no le damos otro interinato en la siguiente. Todavía no tenía base, pero ya venían a venir las bases, ¿no? Y luego resulta de que dije, bueno, pues yo la tomo a la profesora para que no se vaya. Yo sí tengo horas que le puedo dar, que dé clases de una materia, obviamente de programación, ¿no? Porque era el área en donde estaba yo. Bueno, pues la profesora, este, de momento no supo quién fue el héroe anónimo que la dejó, o a lo mejor ni siquiera se enteró de que se la iban a ir, ¿no? Y luego, este, yo al director en su momento, cuando estaba ahí, le dije, yo no voy a hacer un despido porque tenía otra profesora en las mismas circunstancias. Eso es ante derechos humanos, no se puede discriminar. Etcétera. Y eso no estaba tan como hoy, ¿verdad? Era hace, te voy a decir, eso hace como 20 años. Entonces es mucho, ¿no? Pero ya después, con el tiempo, al poquito, la maestra estaba enojada conmigo porque yo la contraté y no se quedó en su departamento. O sea, no supo que yo la rescaté, que la corrieron. Y ya después se lo tuve que aclarar. Le miré así, sí, la materia a lo mejor no te gustaba mucho, pero era eso, o que te quedaras sin horas y que te fueras y no sé qué. Pero es complicado el ser humano. No, a veces te puede decir hasta quién te pidió ayuda. Mi hija, médico, le llegan tiro por viaje, gente que ya se iba a mandar al ovino, y luego al final de la historia lo salvan y se enojan, no. Pero dice, bueno, si lo vas a hacer, hazlo bien, infórmate bien, estudia bien, porque ya después de tanto estás a las 3 de la mañana y llegas con una babosada de que te quisiste suicidar con puras vitaminas, pues nada más no. Y ya, y habiendo otras urgencias. Entonces eso es bien, bien duro, pero al final de cuentas, dentro de nuestro contexto, nos van a, les van a pasar cosas, ¿no? De que dices, yo quería ayudar y resulta que sale peor, ¿no? Entonces, este, pero yo creo que nunca se cansen de ayudar. Ayudar es una labor bien bonita, y qué padre que tú estés en la posición de poder ayudar y no de tener que ser el que te ayude. Verdad, si tú puedes ayudar, ayuda. Y alguna gente dice, si no te lo piden, no ayudes. Pues yo no, si me, aunque no me lo pidan y yo veo que alguien lo puedo ayudar, lo ayudo. Y si se enoja, pues ya tendrá dos trabajos, en contentarse y enojarse, o entender el porqué, ¿no? Y bueno, pues ya nada más, como comenté, alcancé. Entonces, hablando del personal, pues es súper complejo. Yo me acuerdo que aquel entonces yo tenía 28 años o 29 cuando era la jefa de esa área. Y tenía compañeros, la mayoría más grande que yo, y yo era su jefa. Y entonces era fuerte, no les gustaba mucho algunos, y otros sí me valoraban muy bien y todo. Pero sí, sí era 54 mundos, porque cada cabeza es un mundo, y todos súper pensantes igual que yo, con sus doctorados, con sus maestrías, con sus investigaciones, con todo. Pero al final de cuentas, el poder llevar ese equilibrio es un gran reto y es una bonita satisfacción. El poder haber hecho y sido partícipe en el crecimiento de algo y manejarlo correctamente. Entonces, a ustedes seguramente también van a verse enfrente a cargo de cosas, no tan lejanamente. Seguramente en 2 años ustedes van a estar muy bien posicionados, primero Dios, y tendrán que tomar decisiones desde qué equipos compro, desde qué gente contrato, que eso yo les vuelvo a insistir, No es la materia del área de humanidades, pero sin embargo, en el ámbito técnico es súper importante que no nos despeguemos y no digamos eso no es mi labor, no, porque te va a tocar trabajar con un equipo hostil. Aguas, no, no podemos, no vas a poder desempeñar igual. Entonces tendrás que, si es hostil, buscar la estrategia para que se deshostilice ese asunto, no. Y a eso los invito. Idealmente debería de poner quién te cae gordo, compañero. Ah, pues con ese vas a trabajar en tu equipo de este semestre. Para que vayan haciendo el ensayo. Pero no, afortunadamente les doy la libertad de que armen sus equipos a su gusto. Pero piensen en ese ejercicio: si te toca trabajar con el que más gordo te caía, ¿cómo vas a sobrellevar esa historia? No, ¿cómo lo vas a llevar? Y bueno, ya nos queda poquito tiempo, pero la última pregunta de la 3, de cómo los contrato, Eric, y equipos de la 3. 3, ¿quiénes son el 3? Sí. A ver, díganme. Y miren, casualmente el destino nos llevó a que la compañera que ella va por dinero le toca hablar de los dineros. Cuéntenme.

Speaker B
00:45:06 - 00:45:41
Bueno, este, algo importante pues es destinar la parte del presupuesto que tenemos entre licencias y todo el equipo que requerimos, computadoras, si es que vamos a rentar oficinas también, para pues no juntarlo todo con la parte de los salarios de nuestros empleados. Eso es algo importante que tenemos que tomar en cuenta cuando hacemos un contrato de algún, cuando vamos a hacer software, luego tenerlo en cuenta ya en base a ese presupuesto de salario.

Speaker C
00:45:42 - 00:46:12
Sí, porque también importa mucho ahora sí que las partes de ganancias, porque no podemos vivirlo todo en que porque sí hay que pagar sueldo y todo lo demás, pero pues dependiendo también de cuánto tiempo vaya a durar el proyecto y cuál es la complejidad del proyecto, hay que verificar los perfiles que más se adecúen para sacar justamente en tiempo y forma. Entonces, dependiendo de eso, hay que enchilar ahora sí que los salarios y personal administrativo para que todo esté bien.

Speaker A
00:46:15 - 00:46:43
Muy bien. Este, sí es interesante lo que comentan los compañeros, pero a ver, equipo 2, bueno, segunda opinión. ¿Algo más que quisieran decir? Sí, compañeros, perdóname, son, digan su nombre para que todos, ¿quién? Armando y Sara, nada más ustedes dos. No llegaron sus compañeros, entonces a ver, compañeros.

Speaker C
00:46:43 - 00:46:50
Que con varios becarios, con una Coca y un ganchito, salen a un desfile.

Speaker A
00:46:50 - 00:46:53
Bueno, qué mal. A ver, dígame.

Speaker B
00:46:55 - 00:47:12
También el tipo de equipo, ¿no? Porque puede haber equipo con jerarquías de jefe, programadores juniors, o puede haber equipos en el que pues todos son al mismo nivel y el modo de pago es diferente.

Speaker A
00:47:19 - 00:47:39
Sí, pero a ver, te dan presupuesto abierto para eso, es para el equipo 3 o el último que le tocó esa, que quiénes son ustedes, te dan presupuesto abierto, pero ¿cómo pudiste estimar que a veces para 30,000, 50,000, 50,000, o sea, el mismo gran? Ah, pues sí, ¿y qué más?

Speaker B
00:47:40 - 00:47:46
Trabajo, el trabajo que hicieron, que puede que hay formas, ¿no?

Speaker A
00:47:46 - 00:47:59
Ya puede haber también una tabla de cuánto se le paga a tal persona, ya definidos, una tabular en la organización, o buscarlo en general las empresas cuánto están pagando a X o Y persona.

Speaker B
00:47:59 - 00:48:14
La competencia entre empresas también es salario, porque por ejemplo, si yo llego, una persona pidiendo trabajo a varias empresas y varias la quieren contratar, obviamente esa persona se va a ir con el que mejor le pague o el menos matado.

Speaker A
00:48:16 - 00:49:31
Oigan, y de eso también nos hablaron los primeros, los de la primera pregunta. Este, tienen que ver ese antecedente, dónde ha trabajado, cuánto tiempo ha trabajado. Cuando ustedes hacen un currículum, este, no es bonito, no es bueno, los empleadores no los cachan si dice 3 meses en Google, 3 meses en Microsoft y un mes en Oracle, ¿no? Oye, pues, ¿por qué tan poquito tiempo estuvo en tal lugar? O sea, las razones. Entonces cuiden mucho cuando hagan su currículum, y si en algún punto algo no fue tan breve, pues, este, sí, sí coméntenlo, pero cuiden ese aspecto porque seguramente fue porque ustedes o son inestables. La gente empleadora luego lo dice, o es inestable o no cumple con los objetivos. Etcétera, cosas lo pueden ver como negativo, ¿no? Entonces ahora también una persona que ha estado mil años en un lugar pues también sabe por qué ya no está en ese lugar si era tan estable, o también, o sea, todo, todo cuenta y todo hay que analizarlo y observarlo y tenerlo en consideración, ¿no? Bueno, entonces, ¿algo más de respecto a los costos iban a decir ahora sí ustedes, Erick y equipo?

Speaker B
00:49:32 - 00:50:00
Pues también puede influir la modalidad en la que es contratado. Remota o presencial. También la ubicación de dónde puedes hacerlo, te cobran también Guadalajara. Los beneficios no monetarios también puede ser como las horas, o sea, ser más flexible con los horarios, este, capacitaciones y presupuesto, los días de descanso, las vacaciones pagadas, las prestaciones que dan.

Speaker A
00:50:00 - 00:53:18
Esto me recuerda algo cuando alguna estaban empezando los de Price Travel. Vinieron a buscar gente acá, ¿no? Y una de las cosas que les ofrecían es que pues vas a vivir allá en Cancún, te vamos a dar un departamento. Se iban con la de híjole, pues qué padre, en el paraíso, el mar y todo lo demás, vale la pena ese trabajo. Pero ya cuando tú maduras y dices yo quiero estar estable en un lugar, no te hace suficiente, ¿no? Este, yo tuve una alumna que igual decía estaba enferma y Y me dijo, oiga, maestra, ¿me podría contratar? Porque después estuve de subdirectora en un área, encargada la dirección aquí en Tecnópolis hace muchos años también. Y me decía, es que estoy en Deloitte en Guadalajara, pero ya tenía el lupus. Ya la contraté, inclusive pues fue jefa, ¿no? Y pues ya después así dio el cambiazo, ¿no? O sea, así que Se le olvidó de dónde venía y quién le apoyó y no sé qué. Se portaba grosera y demás, pero bueno, ese es un tema aparte, ya no tiene caso hablar de eso. Ya después yo renuncié a esa área, me vine de nuevo de regreso a SCOPE, y resulta que ya con el tiempo, porque era un área muy demandante con el área de las empresas, y este, pues paramos a la cansada. Pues sí, en el principio por eso la contraté, porque sé que las negreaban mucho, y como sabían que era foránea Pues entonces ahí en Guadalajara, pues no te vayas a tu casa, quédate haciendo donde los dejabas para que te vayas. Y lo hacíamos, ¿no? Y luego ya después, entonces, cuando ya la contraté y pasaron los años, fui a llamar. Desgraciadamente falleció en la pandemia, ¿no? Porque como era cosa del área de empresas, le hacían ir y seguía accediendo a que fueran, ¿no? Yo ya no estaba ahí al mando ni nada, pero este accedía. Entonces yo creo que hay que saber decir no. Cuando se tenga que decir que no en un trabajo, ni por quererlo conservar soportar cosas que no debas de soportar. Después, por ejemplo, a Deloitte le decían negroide, ¿no? Mi hija, la maestra, antes que la clase está aquí también, también trabajó en Deloitte un tiempo, y cuando entró yo le dije, mira, yo te digo que hay antecedentes, conozco alumnos que le dicen negroide, ¿no? Pero tú sabes si quieres. Y sí, sí era muy demandante. Entonces, y pagaba un poco. Hace un rato por ahí dijeron que becarios y con una Coca-Cola. Sí, pues no, eso no, no lo acepten, no. Dense su valor, no, porque si no también devalúan el costo de un egresado. Y con eso terminamos. Por favor investiguen cuánto gana un egresado de la carrera de la cual van a salir y cuánto gana un egresado de la que querían estudiar. Para que me digan cómo está la cosa. Y este, les acabo de mandar, bueno, hace un rato mientras estaba escribiendo, si era con ustedes el tema, no crean que escribí a alguien más, les mandé un cuadrito, un círculo que tiene que ver con los aspectos de calidad del software. Y vienen varias habilidades, esa es la unidad 1, yo ya les había compartido el material, pero el equipo vamos a repartir para que cada uno de ustedes tome la que quiera de esas y nos diga cuál es

"""

completion = client.beta.chat.completions.parse(
    model="qwen-plus",
    messages=[
        {
            "role": "system",
            "content": """You are Noto's senior note-taker - the one students fight over because your notes are the reason they pass without re-watching the recording. Turn this raw, messy class transcript into notes so complete and well-organized that someone who missed the class could study from them alone.

            IMPORTANT: Create FULL, DETAILED notes. Do not create lazy or abbreviated output. A rushed summary is a failure - thoroughness is the whole point. Include all key concepts, examples, discussions, and insights from the transcript.

            ===== OUTPUT STRUCTURE =====
            Your output contains 7 sections:
            1. **language**: Detected language and note taking used language
            2. **title**: Main topic/subject of the class
            3. **notes_column**: Detailed content organized with block types (below)
            4. **action_items**: Specific tasks/decisions from class discussion
            5. **summary**: Brief overview of main points and takeaways
            6. **support_material**: Books, links, resources MENTIONED/RECOMMENDED by the instructor (extract ONLY what was discussed, do NOT invent)
            7. **homework**: Assignments/exercises ASSIGNED by the instructor (extract ONLY what was assigned, do NOT invent)

            ===== CONTENT BLOCK TYPES =====
            Use these to structure detailed notes:

            **title**: The main topic/subject of the entire note. Use one title per note.

            **HEADING1** (H1): Major sections or main topics discussed. Use for top-level organization.
            - Example: "Software Project Management", "Personnel Management", "Salary Considerations"

            **HEADING2** (H2): Subsections within major topics. Use for secondary organization.
            - Example: Under "Software Project Management": "Project Phases", "Quality Practices"

            **HEADING3, HEADING4**: Further subdivisions for detailed organization when needed.

            **PARAGRAPH**: Regular body text. Use this for explanations, discussions, conclusions, and descriptions.
            - A paragraph is a developed idea, not a fragment - it should read as a real sentence or two of prose, not a clipped phrase.
            - If it's short enough to be a bullet, it IS a bullet - use BULLET_LIST_ITEM instead. Never use PARAGRAPH as a dumping ground for one-liners.
            - Do not artificially pad a thin idea with filler just to hit length - if there isn't a full idea to develop, that content belongs in a bullet, not a paragraph.

            **BULLET_LIST_ITEM**: For lists of related items, steps, or options.
            - Each item is a separate block
            - Use when listing multiple related points

            **NUMBERED_LIST_ITEM**: For sequential steps or prioritized lists.
            - Each number is a separate block
            - Use for procedures or ordered content

            **QUOTE**: For direct, verbatim quotes worth preserving exactly as the speaker said them.
            - Use actual transcript wording
            - Include speaker context when relevant
            - This is NOT the tool for emphasizing a point that isn't a real quote - use inline formatting instead (see below)

            **CALLOUT**: For important warnings, tips, or emphasize critical concepts.
            - Use for key takeaways
            - Highlight decisions or important reminders

            **CODE**: For technical content, formulas, or code examples if mentioned.

            **TABLE**: For structured data, comparisons, or complex information (if applicable).

            **TODO_LIST_ITEM**: For action items or tasks mentioned.

            ===== INLINE TEXT FORMATTING =====
            Not every important statement deserves its own QUOTE or CALLOUT block. To emphasize something INSIDE a normal block's "text" (a paragraph, a bullet item, a heading - any of them), use these inline markers, the same ones Notion uses:

            - `**bold**` - wrap key terms, names, and important phrases in double asterisks.
            - `` `highlighted term` `` - wrap standout keywords, technical terms, or numbers in backticks, like Notion's inline-code highlight, when they deserve attention but not a whole callout.
            - `__underlined__` - wrap the single most important phrase in a block in double underscores. Use sparingly - if everything is underlined, nothing is.

            Example: {"type": "paragraph", "emoji": "", "text": "Break-even hits at `license #30` - everything from **license #31** onward is __pure profit__, and that's the number the whole pricing strategy hinges on."}

            These markers only ever live inside "text" as inline styling. They never replace the correct block "type", and never combine with the forbidden leading bullet/icon characters below.

            GUIDELINES:
            1. All generated content goes in the same language as the transcript
            2. Capture ALL significant discussion points - don't omit details
            3. Organize logically with appropriate heading hierarchy
            4. Use bullet points for lists and multiple related items
            5. Use callout and quote for important definitions, details, etc.
            6. For statistic data or calculations use tables
            7. Extract and organize all examples given
            8. Create a complete, thorough note - assume this is the only record of this class
            9. The "text" field is rich text limited to the three inline markers above (**bold**, `backtick`, __underline__) - nothing else. Never prepend bullet symbols (•, -, *), numbering ("1.", "2)"), or icons/emoji (⚠️, ✅, 📌) to "text" - the "type" field already conveys that a block is a bullet, number, or callout, so repeating it as a character inside "text" is a duplicate and is forbidden.
                Example - WRONG: {"type": "bullet_list_item", "text": "• Scope clarity prevents scope creep"}
                Example - WRONG: {"type": "callout", "text": "⚠️ Warning: skipping training voids the guarantee"}
                Example - CORRECT: {"type": "bullet_list_item", "text": "Scope clarity prevents scope creep"}
                Example - CORRECT: {"type": "callout", "text": "Skipping training voids the guarantee"}
            10. Each block has an "emoji" field. ONLY set it for HEADING1-4, TABLE, or CALLOUT blocks, to mark section headings, table topics, or important/critical statements. Leave it as "" for every other block type (PARAGRAPH, QUOTE, BULLET_LIST_ITEM, NUMBERED_LIST_ITEM, TODO_LIST_ITEM, CODE). The emoji goes ONLY in "emoji", never inside "text".
                Example - CORRECT: {"type": "heading1", "emoji": "💰", "text": "Compensation & Salary Design"}
                Example - CORRECT: {"type": "callout", "emoji": "⚠️", "text": "Skipping training voids the guarantee"}
                Example - CORRECT: {"type": "paragraph", "emoji": "", "text": "Break-even analysis for software licensing..."}
            ===== CRITICAL: EXTRACT, DO NOT INVENT =====
            - **support_material**: Only include resources (books, links, materials, tools) that the instructor mentioned or recommended during the class. If none were mentioned, leave as empty list.
            - **homework**: Only include assignments that the instructor explicitly assigned. Do NOT create homework based on the topic. If no homework was assigned, leave as empty list.
            - **action_items**: Extract tasks and decisions discussed, but do NOT invent tasks that weren't mentioned.

            Now go make notes worth studying from."""
        },
        {
            "role": "user",
            "content": f"Create structured notes from this class transcript:\n\n{transcript}"
        }
    ],
    response_format=NotesModel,
)

# Get the model's parsed response
if completion.choices[0].message.parsed:
    result = completion.choices[0].message.parsed
    with open("note2.json", "w", encoding="utf-8") as file:
        file.write(result.model_dump_json(indent=2))
else:
    print("Failed to parse response")
    print(completion.choices[0].message.content)
