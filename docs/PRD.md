# PRD — Step By Step: Data Engineering & AI Learning System

## 1. Visão Geral

O **Step By Step** será uma plataforma de aprendizado interativa, gamificada e expansível. A primeira trilha será focada em **Data Engineering & AI Concepts**, transformando os 100 conceitos da imagem de referência em uma jornada de estudo com botões, lições, desafios, perguntas, jogos rápidos e certificado final.

A ideia central não é criar um curso parado, daqueles que parecem treinamento obrigatório de compliance às 18h de sexta-feira. O objetivo é construir uma experiência onde o aluno avance por fases, desbloqueie conteúdos, resolva pequenas missões e aprenda conceitos técnicos de forma clara, visual e divertida.

No futuro, o mesmo motor do sistema poderá ser reutilizado para outras áreas, como Inteligência Artificial, Engenharia de Software, Cloud, Segurança, Telecom, Power BI, Automação, Processos Corporativos e qualquer outro tema estruturado em etapas.

---

## 2. Nome do Produto

**Step By Step**

### Slogan sugerido

**Learn one step. Unlock the next.**

### Conceito

Uma metodologia de ensino baseada em progressão por etapas, onde cada conceito vira um **Step**. Cada Step contém explicação, exemplo prático, analogia divertida, interação, mini desafio e validação de aprendizado.

---

## 3. Problema a Resolver

Muitos conteúdos técnicos de Data Engineering são ensinados de forma muito pesada, cheia de termos soltos, ferramentas específicas e pouca conexão prática. O aluno vê nomes como Lakehouse, CDC, Delta Lake, Spark, RAG, DAG, Vector DB e pensa: “beleza, agora vou abrir uma padaria”.

O problema é que normalmente o aprendizado é:

- Linear demais.
- Monótono.
- Pouco visual.
- Pouco prático.
- Focado em ferramentas antes dos conceitos.
- Sem sensação de avanço.
- Sem feedback imediato.
- Sem gamificação real.

O **Step By Step** resolve isso criando uma experiência de aprendizado baseada em fases, pontuação, desafios e trilhas desbloqueáveis.

---

## 4. Objetivos do Produto

### Objetivo principal

Criar uma plataforma local, estruturada com banco de dados e login, capaz de ensinar os 100 conceitos de Data Engineering & AI da imagem de referência por meio de uma jornada interativa e gamificada.

### Objetivos secundários

- Permitir que cada conceito seja acessado como um botão de lição.
- Criar explicações claras e progressivas.
- Usar analogias simples e divertidas.
- Adicionar perguntas ao final de cada Step.
- Criar pontuação por conclusão, acertos e atividades.
- Permitir avanço por fases.
- Gerar certificado ao final da trilha.
- Criar base técnica preparada para futura publicação em Cloud.
- Permitir que no futuro novas trilhas sejam cadastradas sem reconstruir o sistema.

---

## 5. Público-Alvo

### Público inicial

- Profissionais de tecnologia que querem aprender Data Engineering.
- Analistas de dados querendo evoluir para engenharia de dados.
- Gerentes de transformação digital que precisam entender arquitetura de dados.
- Desenvolvedores que querem entrar em pipelines, lakehouse, AI systems e governança.
- Profissionais de telecom, operações e BI que precisam falar de igual para igual com times técnicos.

### Perfil do usuário

O usuário pode não querer virar programador hardcore, mas precisa entender o que acontece por trás dos sistemas. Ele quer saber o que é cada conceito, onde se encaixa, por que existe e como explicar isso sem parecer que engoliu um manual da AWS com gosto de isopor.

---

## 6. Escopo da Primeira Versão

A primeira versão terá uma trilha chamada:

## Data Engineering & AI Concepts

Baseada em 100 conceitos organizados em 7 seções principais:

1. Data Fundamentals
2. Pipelines & Processing
3. Spark & Distributed Systems
4. Orchestration & Reliability
5. Lakehouse & Storage
6. AI / ML Systems
7. Governance & Scale

Cada conceito será representado como um botão/card clicável. Ao clicar, o usuário acessa uma lição com conteúdo, exemplos, atividade e perguntas.

---

## 7. Estrutura da Jornada de Aprendizado

### 7.1 Organização por Seções

A trilha será dividida em grandes blocos. Cada bloco funciona como uma fase do jogo.

### Fase 1 — Data Fundamentals

Conceitos iniciais para entender como dados são modelados, armazenados e organizados.

Steps:

1. Data Modeling
2. OLTP vs OLAP
3. Star Schema
4. Snowflake Schema
5. Normalization
6. Denormalization
7. Data Warehouse
8. Data Lake
9. Lakehouse
10. Medallion

### Fase 2 — Pipelines & Processing

Conceitos sobre movimentação, transformação e processamento de dados.

Steps:

11. Batch Processing
12. Stream Processing
13. Micro-batch
14. Event-Driven
15. CDC
16. Data Pipeline
17. ETL vs ELT
18. Ingestion
19. Transformation
20. Serving
21. Partitioning
22. Bucketing
23. Indexing
24. File Formats
25. Compression
26. Schema Evolution
27. Schema Enforcement
28. Data Skipping
29. Z-Ordering
30. Small Files

### Fase 3 — Spark & Distributed Systems

Conceitos sobre processamento distribuído, Spark e performance.

Steps:

31. Distributed Systems
32. Parallelism
33. Fault Tolerance
34. Data Locality
35. Shuffle
36. Narrow vs Wide
37. Lazy Evaluation
38. DAG
39. Catalyst
40. Tungsten
41. Joins
42. Skew Handling
43. Repartition vs Coalesce
44. Caching
45. Memory Management
46. Spill to Disk
47. Driver vs Executor
48. Cluster Sizing
49. Resource Allocation
50. Optimization

### Fase 4 — Orchestration & Reliability

Conceitos para agendar, monitorar, controlar e garantir confiabilidade nos pipelines.

Steps:

51. Airflow
52. DAG Scheduling
53. Task Dependencies
54. Retry Logic
55. Backfill
56. SLA
57. Observability
58. Data Quality
59. Data Contracts
60. Lineage

### Fase 5 — Lakehouse & Storage

Conceitos sobre formatos modernos de armazenamento, tabelas, versionamento e manutenção.

Steps:

61. Delta Lake
62. Iceberg
63. Hudi
64. ACID Lakes
65. Time Travel
66. Merge / Upserts
67. Incremental Loads
68. Streaming Reads
69. Compaction
70. Vacuum

### Fase 6 — AI / ML Systems

Conceitos para conectar engenharia de dados com inteligência artificial, ML e LLMs.

Steps:

71. Feature Engineering
72. Feature Store
73. Training vs Inference
74. Batch ML
75. Real-time ML
76. Model Drift
77. Data Drift
78. Model Monitoring
79. Model Serving
80. Vector ID
81. Vector DB
82. Embeddings
83. RAG
84. LLM Pipelines
85. Prompt Engineering
86. Tokenization
87. Context Window
88. Agents
89. Tool Calling
90. Memory

### Fase 7 — Governance & Scale

Conceitos de governança, segurança, escala, custos e arquitetura.

Steps:

91. Data Governance
92. Data Privacy
93. PII
94. Access Control
95. RBAC
96. Encryption
97. Cost Optimization
98. FinOps
99. Cloud Storage
100. Architecture

---

## 8. Estrutura de Cada Step

Cada Step deverá seguir uma estrutura padronizada, para que o aluno saiba o que esperar e o sistema seja escalável.

### 8.1 Componentes de uma lição

Cada lição terá:

1. Título do conceito.
2. Resumo rápido em uma frase.
3. Explicação simples.
4. Explicação técnica.
5. Exemplo prático.
6. Analogia divertida.
7. Onde isso aparece no mundo real.
8. Erros comuns.
9. Mini interação.
10. Quiz final.
11. Pontuação.
12. Status de conclusão.

### 8.2 Exemplo de Step

#### Step: OLTP vs OLAP

**Resumo rápido:**  
OLTP é para operação do dia a dia. OLAP é para análise e tomada de decisão.

**Explicação simples:**  
OLTP é usado em sistemas que registram ações, como vendas, pagamentos, cadastro de clientes e pedidos. OLAP é usado para analisar grandes volumes de dados e responder perguntas como “quanto vendemos por região nos últimos 12 meses?”.

**Analogia divertida:**  
OLTP é o caixa do mercado registrando cada compra. OLAP é o gerente olhando o relatório no fim do mês e descobrindo que o estoque de paçoca sumiu porque alguém claramente perdeu o controle emocional.

**Mini interação:**  
Arraste cada exemplo para OLTP ou OLAP:

- Registrar compra no app.
- Gerar dashboard mensal.
- Atualizar senha do usuário.
- Analisar vendas por região.

**Quiz:**  
Qual cenário combina mais com OLAP?

A. Salvar login do usuário.  
B. Registrar pagamento instantâneo.  
C. Analisar comportamento de compra dos últimos 2 anos.  
D. Atualizar endereço de entrega.

Resposta correta: C.

---

## 9. Metodologia de Ensino

O Step By Step será baseado em uma metodologia própria com 5 camadas.

### 9.1 Camada 1 — Entender

O usuário recebe uma explicação simples, sem jargão desnecessário.

### 9.2 Camada 2 — Visualizar

O conceito é apresentado com cards, diagramas, fluxos ou comparações.

### 9.3 Camada 3 — Interagir

O usuário faz uma ação simples, como:

- Arrastar cards.
- Ligar conceitos.
- Ordenar etapas.
- Escolher arquitetura correta.
- Montar um mini pipeline.
- Marcar verdadeiro ou falso.

### 9.4 Camada 4 — Aplicar

O usuário resolve um mini cenário prático.

Exemplo:

“Você recebeu dados de vendas em CSV todo dia às 23h. Qual abordagem faz mais sentido: Batch, Stream ou CDC?”

### 9.5 Camada 5 — Desbloquear

Ao acertar ou concluir, o usuário ganha pontos, experiência e desbloqueia o próximo Step.

---

## 10. Gamificação

### 10.1 Elementos de jogo

O sistema terá:

- Pontos por Step concluído.
- Pontos extras por acerto no quiz.
- Combo por acertos consecutivos.
- Medalhas por seção concluída.
- Ranking local opcional.
- Barra de progresso.
- Fases bloqueadas e desbloqueadas.
- Certificado final.
- Badges especiais.

### 10.2 Pontuação sugerida

| Ação                          |    Pontos |
| ----------------------------- | --------: |
| Abrir lição pela primeira vez |         5 |
| Concluir leitura              |        10 |
| Completar interação           |        20 |
| Acertar quiz                  |        30 |
| Acertar quiz sem erro         | +20 bônus |
| Concluir uma fase             |       100 |
| Concluir todos os 100 Steps   |      1000 |

### 10.3 Níveis do usuário

| Nível | Pontuação | Nome              |
| ----- | --------: | ----------------- |
| 1     |     0–499 | Data Rookie       |
| 2     |  500–1499 | Pipeline Explorer |
| 3     | 1500–2999 | Lakehouse Builder |
| 4     | 3000–4999 | Spark Survivor    |
| 5     | 5000–7999 | AI Data Ranger    |
| 6     |     8000+ | Step Master       |

### 10.4 Badges sugeridas

- **Primeiro Step:** concluiu a primeira lição.
- **Sem Travar o Pipeline:** concluiu 10 Steps seguidos.
- **Spark não me assusta:** concluiu a fase Spark.
- **Governança sem sono:** concluiu Governance & Scale.
- **Mestre dos 100 Steps:** finalizou a trilha completa.

---

## 11. Tipos de Atividades Interativas

### 11.1 Quiz de múltipla escolha

Perguntas simples com 4 opções.

### 11.2 Verdadeiro ou falso

O usuário marca se a afirmação está correta.

### 11.3 Drag and Drop

O usuário arrasta conceitos para colunas corretas.

Exemplo:

- Batch vs Stream
- OLTP vs OLAP
- ETL vs ELT
- Training vs Inference

### 11.4 Ordenação de etapas

O usuário organiza uma sequência lógica.

Exemplo:

Ingestion → Transformation → Storage → Serving → Monitoring

### 11.5 Monte o pipeline

O usuário recebe um cenário e escolhe blocos para montar uma arquitetura simples.

Exemplo:

“Uma empresa recebe eventos de compra em tempo real e quer recomendar produtos imediatamente.”

Blocos disponíveis:

- Stream Processing
- Feature Store
- Real-time ML
- Model Serving
- Observability

### 11.6 Ligue os pares

O usuário conecta conceito e definição.

Exemplo:

- Embeddings → Representação vetorial de texto.
- RBAC → Controle de acesso por papel.
- Vacuum → Limpeza de arquivos antigos.

### 11.7 Mini boss por fase

Ao final de cada fase, o usuário enfrenta um desafio maior com 5 a 10 perguntas ou uma montagem de cenário.

Exemplo:

**Boss da Fase 2 — O Pipeline Quebrado**

O usuário precisa identificar onde está o erro em um pipeline fictício.

---

## 12. Fluxo do Usuário

### 12.1 Primeiro acesso

1. Usuário acessa a aplicação.
2. Cria conta ou faz login.
3. Visualiza a tela inicial.
4. Escolhe a trilha “Data Engineering & AI Concepts”.
5. Inicia no Step 1.

### 12.2 Jornada de estudo

1. Usuário clica em um Step disponível.
2. Lê a explicação.
3. Faz interação simples.
4. Responde perguntas.
5. Recebe pontuação.
6. Desbloqueia próximo Step.
7. Avança até concluir a seção.
8. Faz o Boss da seção.
9. Desbloqueia próxima fase.

### 12.3 Finalização

1. Usuário conclui os 100 Steps.
2. Realiza um desafio final.
3. Recebe nota geral.
4. Gera certificado.
5. Pode baixar o certificado em PDF.

---

## 13. Perfis de Usuário

### 13.1 Aluno

Permissões:

- Criar conta.
- Fazer login.
- Acessar trilhas liberadas.
- Concluir Steps.
- Responder quizzes.
- Ver progresso.
- Baixar certificado.

### 13.2 Administrador

Permissões:

- Criar, editar e remover trilhas.
- Criar, editar e remover Steps.
- Gerenciar perguntas.
- Visualizar usuários.
- Ver progresso geral dos alunos.
- Configurar pontuação.
- Publicar ou ocultar conteúdos.

### 13.3 Instrutor/Editor

Permissões:

- Criar e editar conteúdo.
- Criar perguntas.
- Revisar lições.
- Não pode excluir usuários ou alterar configurações críticas.

---

## 14. Requisitos Funcionais

### RF001 — Cadastro de usuário

O sistema deve permitir cadastro com nome, e-mail e senha.

### RF002 — Login

O sistema deve permitir login com e-mail e senha.

### RF003 — Recuperação de senha

O sistema deve permitir recuperação de senha por e-mail em versão futura. Na versão local inicial, pode ser feita por reset administrativo.

### RF004 — Dashboard do aluno

O sistema deve exibir:

- Progresso geral.
- Pontuação total.
- Fase atual.
- Steps concluídos.
- Próximo Step recomendado.
- Badges conquistadas.

### RF005 — Tela da trilha

O sistema deve exibir os 100 Steps como cards ou botões organizados por seção.

### RF006 — Bloqueio e desbloqueio de Steps

O sistema deve permitir que apenas Steps liberados sejam acessados, seguindo regra de progressão configurável.

### RF007 — Página de lição

Cada Step deve conter:

- Título.
- Descrição curta.
- Conteúdo principal.
- Exemplo prático.
- Analogia.
- Interação.
- Quiz.
- Botão de concluir.

### RF008 — Sistema de quiz

O sistema deve permitir perguntas de múltipla escolha, verdadeiro/falso e associação simples.

### RF009 — Atividades drag and drop

O sistema deve permitir atividades simples de arrastar e soltar.

### RF010 — Pontuação

O sistema deve calcular pontos automaticamente por ação concluída.

### RF011 — Badges

O sistema deve liberar badges com base em regras configuradas.

### RF012 — Progresso

O sistema deve salvar progresso por usuário, trilha, seção e Step.

### RF013 — Certificado

O sistema deve gerar certificado ao final da trilha com:

- Nome do usuário.
- Nome da trilha.
- Data de conclusão.
- Pontuação final.
- Código de validação.

### RF014 — Administração de conteúdo

O sistema deve permitir ao admin criar e editar:

- Trilhas.
- Seções.
- Steps.
- Conteúdo das lições.
- Perguntas.
- Atividades.
- Pontuação.

### RF015 — Histórico de tentativas

O sistema deve armazenar tentativas de quiz para análise futura.

### RF016 — Modo local

A aplicação deve rodar localmente em ambiente de desenvolvimento.

### RF017 — Preparação para Cloud

A arquitetura deve permitir deploy futuro em Cloud sem reescrever o sistema.

---

## 15. Requisitos Não Funcionais

### RNF001 — Performance

As páginas principais devem carregar em menos de 2 segundos em ambiente local.

### RNF002 — Segurança

Senhas devem ser armazenadas com hash seguro, nunca em texto puro.

### RNF003 — Escalabilidade

A arquitetura deve suportar novas trilhas no futuro.

### RNF004 — Manutenibilidade

Conteúdo das lições deve ficar no banco de dados ou em estrutura facilmente editável.

### RNF005 — Responsividade

A interface deve funcionar em desktop, tablet e celular.

### RNF006 — Usabilidade

A experiência deve ser simples, visual e com feedback constante.

### RNF007 — Portabilidade

O sistema deve rodar localmente via Docker ou ambiente Python/Node estruturado.

### RNF008 — Backup

O banco de dados deve permitir backup simples.

---

## 16. Arquitetura Recomendada

### 16.1 Versão inicial local

Para a primeira versão, recomenda-se uma arquitetura simples e robusta:

- Frontend: React + Vite
- Backend: FastAPI ou Node.js/NestJS
- Banco de dados local: PostgreSQL via Docker ou SQLite para MVP rápido
- Autenticação: JWT
- ORM: SQLAlchemy, Prisma ou equivalente
- Certificado: geração em PDF
- Deploy local: Docker Compose

### 16.2 Opção mais simples para MVP

Caso o objetivo seja acelerar:

- Backend: FastAPI
- Frontend: React
- Banco: SQLite inicialmente
- Depois migrar para PostgreSQL

### 16.3 Opção preparada para produção

- Frontend: React/Next.js
- Backend: FastAPI ou NestJS
- Banco: PostgreSQL
- Storage: S3 compatible ou Cloud Storage
- Auth: JWT + refresh token
- Deploy: Docker + Cloud VPS
- Proxy: Nginx/Cloudflare

---

## 17. Estrutura Organizacional da Aplicação

### 17.1 Entidades principais

- User
- Role
- Track
- Section
- Step
- LessonContent
- Activity
- Question
- AnswerOption
- UserProgress
- UserScore
- Badge
- UserBadge
- Certificate
- QuizAttempt

### 17.2 Hierarquia

```text
Track
 └── Section
      └── Step
           ├── LessonContent
           ├── Activity
           └── Questions
```

### 17.3 Exemplo

```text
Track: Data Engineering & AI Concepts
Section: Data Fundamentals
Step: OLTP vs OLAP
LessonContent: explicação, analogia, exemplo
Activity: drag and drop
Questions: 5 perguntas
```

---

## 18. Modelo de Banco de Dados

### 18.1 users

| Campo         | Tipo     | Descrição                |
| ------------- | -------- | ------------------------ |
| id            | UUID     | Identificador do usuário |
| name          | string   | Nome completo            |
| email         | string   | E-mail único             |
| password_hash | string   | Senha criptografada      |
| role_id       | UUID     | Perfil do usuário        |
| created_at    | datetime | Data de criação          |
| updated_at    | datetime | Data de atualização      |

### 18.2 roles

| Campo | Tipo   | Descrição              |
| ----- | ------ | ---------------------- |
| id    | UUID   | Identificador          |
| name  | string | admin, editor, student |

### 18.3 tracks

| Campo       | Tipo     | Descrição                  |
| ----------- | -------- | -------------------------- |
| id          | UUID     | Identificador              |
| title       | string   | Nome da trilha             |
| description | text     | Descrição                  |
| status      | string   | draft, published, archived |
| created_at  | datetime | Data de criação            |

### 18.4 sections

| Campo       | Tipo    | Descrição          |
| ----------- | ------- | ------------------ |
| id          | UUID    | Identificador      |
| track_id    | UUID    | Trilha relacionada |
| title       | string  | Nome da seção      |
| order_index | integer | Ordem              |

### 18.5 steps

| Campo             | Tipo    | Descrição          |
| ----------------- | ------- | ------------------ |
| id                | UUID    | Identificador      |
| section_id        | UUID    | Seção relacionada  |
| title             | string  | Nome do Step       |
| short_description | string  | Resumo             |
| order_index       | integer | Ordem              |
| xp_reward         | integer | Pontuação base     |
| is_required       | boolean | Obrigatório ou não |

### 18.6 lesson_contents

| Campo                 | Tipo | Descrição          |
| --------------------- | ---- | ------------------ |
| id                    | UUID | Identificador      |
| step_id               | UUID | Step relacionado   |
| simple_explanation    | text | Explicação simples |
| technical_explanation | text | Explicação técnica |
| analogy               | text | Analogia divertida |
| real_world_example    | text | Exemplo real       |
| common_mistakes       | text | Erros comuns       |

### 18.7 activities

| Campo       | Tipo    | Descrição                                     |
| ----------- | ------- | --------------------------------------------- |
| id          | UUID    | Identificador                                 |
| step_id     | UUID    | Step relacionado                              |
| type        | string  | quiz, drag_drop, ordering, matching, scenario |
| title       | string  | Título                                        |
| config_json | json    | Configuração da atividade                     |
| xp_reward   | integer | Pontuação                                     |

### 18.8 questions

| Campo         | Tipo    | Descrição                   |
| ------------- | ------- | --------------------------- |
| id            | UUID    | Identificador               |
| step_id       | UUID    | Step relacionado            |
| question_text | text    | Pergunta                    |
| type          | string  | multiple_choice, true_false |
| explanation   | text    | Explicação da resposta      |
| points        | integer | Pontos                      |

### 18.9 answer_options

| Campo       | Tipo    | Descrição            |
| ----------- | ------- | -------------------- |
| id          | UUID    | Identificador        |
| question_id | UUID    | Pergunta relacionada |
| option_text | text    | Texto da alternativa |
| is_correct  | boolean | Indica se é correta  |

### 18.10 user_progress

| Campo        | Tipo     | Descrição                                 |
| ------------ | -------- | ----------------------------------------- |
| id           | UUID     | Identificador                             |
| user_id      | UUID     | Usuário                                   |
| track_id     | UUID     | Trilha                                    |
| section_id   | UUID     | Seção                                     |
| step_id      | UUID     | Step                                      |
| status       | string   | locked, available, in_progress, completed |
| completed_at | datetime | Data de conclusão                         |

### 18.11 user_scores

| Campo        | Tipo    | Descrição       |
| ------------ | ------- | --------------- |
| id           | UUID    | Identificador   |
| user_id      | UUID    | Usuário         |
| track_id     | UUID    | Trilha          |
| total_points | integer | Pontuação total |
| level        | integer | Nível           |

### 18.12 certificates

| Campo            | Tipo     | Descrição       |
| ---------------- | -------- | --------------- |
| id               | UUID     | Identificador   |
| user_id          | UUID     | Usuário         |
| track_id         | UUID     | Trilha          |
| certificate_code | string   | Código único    |
| issued_at        | datetime | Data de emissão |
| final_score      | integer  | Pontuação final |
| pdf_url          | string   | Caminho do PDF  |

---

## 19. Telas do Sistema

### 19.1 Tela de Login

Elementos:

- Logo Step By Step.
- Campo de e-mail.
- Campo de senha.
- Botão Entrar.
- Link Criar Conta.
- Link Esqueci minha senha, opcional no MVP.

### 19.2 Tela de Cadastro

Elementos:

- Nome.
- E-mail.
- Senha.
- Confirmação de senha.
- Botão Criar Conta.

### 19.3 Home/Dashboard

Elementos:

- Saudação personalizada.
- Card da trilha atual.
- Progresso geral.
- Pontuação.
- Nível.
- Badges recentes.
- Botão Continuar.

### 19.4 Tela da Trilha

Elementos:

- Nome da trilha.
- Descrição.
- Seções em formato de mapa.
- Cards dos 100 Steps.
- Status visual:
  - Bloqueado.
  - Disponível.
  - Em andamento.
  - Concluído.

### 19.5 Tela da Lição

Elementos:

- Título do Step.
- Progresso da lição.
- Explicação em blocos.
- Exemplo visual.
- Atividade interativa.
- Quiz.
- Botão concluir.

### 19.6 Tela de Desafio da Fase

Elementos:

- Nome do Boss.
- Cenário do desafio.
- Perguntas.
- Resultado.
- Pontuação obtida.
- Feedback.

### 19.7 Tela de Certificado

Elementos:

- Nome do aluno.
- Trilha concluída.
- Data.
- Pontuação.
- Código de validação.
- Botão baixar PDF.

### 19.8 Painel Administrativo

Elementos:

- Gestão de trilhas.
- Gestão de seções.
- Gestão de Steps.
- Editor de conteúdo.
- Gestão de perguntas.
- Gestão de usuários.
- Relatórios de progresso.

---

## 20. Experiência Visual

### 20.1 Estilo recomendado

O visual deve parecer uma mistura de plataforma de estudos com game leve.

Características:

- Cards modernos.
- Cores por seção.
- Ícones para cada conceito.
- Barra de progresso clara.
- Animações sutis.
- Feedback visual ao acertar/errar.
- Mapa de fases.
- Badges colecionáveis.

### 20.2 Referência de experiência

A experiência deve lembrar:

- Duolingo pela progressão.
- Codecademy pela prática.
- Notion pelo conteúdo organizado.
- Game casual pela leveza.

Sem transformar tudo num carnaval visual onde o usuário aprende Data Lake e sai com enxaqueca.

---

## 21. Conteúdo das Lições

### 21.1 Tom do conteúdo

As lições devem ser:

- Claras.
- Didáticas.
- Leves.
- Divertidas.
- Técnicas na medida certa.
- Com exemplos reais.
- Sem excesso de jargão.

### 21.2 Estrutura textual padrão

Para cada Step:

```text
1. O que é?
2. Por que existe?
3. Como funciona?
4. Exemplo no mundo real.
5. Analogia rápida.
6. Quando usar?
7. Erros comuns.
8. Mini desafio.
9. Quiz.
```

### 21.3 Promessa de aprendizado

Ao final da trilha, o usuário deverá conseguir:

- Entender os principais conceitos de Data Engineering.
- Explicar diferenças entre arquiteturas de dados.
- Entender pipelines batch, streaming e event-driven.
- Entender a lógica de Spark e sistemas distribuídos.
- Entender orquestração, SLA e observabilidade.
- Entender Lakehouse, Delta, Iceberg e Hudi.
- Entender a base de sistemas de AI/ML modernos.
- Entender governança, privacidade, custo e arquitetura.

---

## 22. Regras de Progressão

### 22.1 Progressão linear padrão

O usuário começa no Step 1 e desbloqueia o próximo após concluir o anterior.

### 22.2 Progressão por seção

Cada seção só desbloqueia depois que a anterior for concluída.

### 22.3 Desafio de fase

Ao final de cada seção, o usuário precisa concluir um desafio para liberar a próxima fase.

### 22.4 Nota mínima

Sugestão:

- Para concluir um Step: mínimo de 60% no quiz.
- Para concluir uma fase: mínimo de 70% no Boss.
- Para certificado: mínimo geral de 75%.

---

## 23. Certificado

### 23.1 Requisitos para emissão

O certificado será emitido quando:

- Todos os Steps obrigatórios forem concluídos.
- Todos os desafios de fase forem concluídos.
- O desafio final for concluído.
- A pontuação mínima for atingida.

### 23.2 Informações do certificado

- Logo Step By Step.
- Nome do aluno.
- Nome da trilha.
- Carga horária estimada.
- Data de emissão.
- Pontuação final.
- Código de validação.
- Assinatura digital simples da plataforma.

### 23.3 Validação futura

Em versão futura, o certificado poderá ter uma URL pública de validação.

---

## 24. Relatórios e Métricas

### 24.1 Métricas para aluno

- Steps concluídos.
- Pontuação total.
- Percentual da trilha.
- Melhor fase.
- Fase com maior dificuldade.
- Badges.
- Tempo estimado de estudo.

### 24.2 Métricas para administrador

- Usuários cadastrados.
- Usuários ativos.
- Média de conclusão.
- Steps com maior erro.
- Perguntas mais difíceis.
- Tempo médio por lição.
- Taxa de conclusão da trilha.

---

## 25. MVP — Primeira Entrega

### 25.1 O que deve entrar no MVP

- Login e cadastro.
- Dashboard do aluno.
- Trilha Data Engineering & AI Concepts.
- 7 seções.
- 100 cards de Steps cadastrados.
- Conteúdo inicial para pelo menos 10 Steps completos.
- Quiz de múltipla escolha.
- Pontuação.
- Progresso salvo no banco.
- Certificado simples em PDF.
- Painel admin básico para editar conteúdo.

### 25.2 O que pode ficar para depois

- Drag and drop avançado.
- Ranking global.
- Certificado com validação pública.
- Multiplayer.
- IA gerando perguntas automaticamente.
- App mobile nativo.
- Marketplace de trilhas.

---

## 26. Roadmap de Desenvolvimento

### Fase 1 — Base técnica

- Criar estrutura do projeto.
- Configurar frontend.
- Configurar backend.
- Configurar banco de dados.
- Criar autenticação.
- Criar modelos principais.

### Fase 2 — Conteúdo e trilha

- Criar trilha Data Engineering.
- Criar 7 seções.
- Criar 100 Steps.
- Criar estrutura de lição.
- Criar primeiros conteúdos completos.

### Fase 3 — Gamificação

- Criar sistema de pontos.
- Criar progresso.
- Criar badges.
- Criar desbloqueio de Steps.

### Fase 4 — Interatividade

- Criar quizzes.
- Criar verdadeiro/falso.
- Criar drag and drop.
- Criar ordenação.
- Criar matching.

### Fase 5 — Certificado

- Criar regra de conclusão.
- Criar geração de PDF.
- Criar código de validação.

### Fase 6 — Admin

- Criar painel para conteúdo.
- Criar editor de perguntas.
- Criar gestão de usuários.

### Fase 7 — Preparação para Cloud

- Dockerizar aplicação.
- Migrar para PostgreSQL se necessário.
- Configurar variáveis de ambiente.
- Preparar Nginx/Cloudflare.
- Criar documentação de deploy.

---

## 27. Stack Técnica Recomendada

### Frontend

- React
- Vite
- Tailwind CSS
- Framer Motion para animações
- React Router
- Zustand ou Redux Toolkit para estado
- DnD Kit para drag and drop

### Backend

Opção recomendada:

- Python FastAPI
- SQLAlchemy
- Pydantic
- JWT Auth
- Alembic para migrations

### Banco

MVP:

- SQLite

Produção:

- PostgreSQL

### PDF

- WeasyPrint, ReportLab ou Playwright PDF

### Deploy futuro

- Docker
- Docker Compose
- VPS ou Oracle Cloud
- Cloudflare
- Nginx

---

## 28. Estrutura de Pastas Sugerida

```text
step-by-step/
 ├── backend/
 │   ├── app/
 │   │   ├── main.py
 │   │   ├── models/
 │   │   ├── schemas/
 │   │   ├── routes/
 │   │   ├── services/
 │   │   ├── auth/
 │   │   └── database/
 │   ├── migrations/
 │   ├── requirements.txt
 │   └── Dockerfile
 │
 ├── frontend/
 │   ├── src/
 │   │   ├── components/
 │   │   ├── pages/
 │   │   ├── layouts/
 │   │   ├── services/
 │   │   ├── store/
 │   │   └── assets/
 │   ├── package.json
 │   └── Dockerfile
 │
 ├── database/
 │   ├── seed_data/
 │   └── init.sql
 │
 ├── docs/
 │   ├── PRD.md
 │   └── architecture.md
 │
 ├── docker-compose.yml
 └── README.md
```

---

## 29. Seed Inicial dos 100 Steps

O sistema deve ter um arquivo de seed para cadastrar automaticamente a primeira trilha.

Formato sugerido em JSON:

```json
{
  "track": "Data Engineering & AI Concepts",
  "sections": [
    {
      "title": "Data Fundamentals",
      "steps": [
        "Data Modeling",
        "OLTP vs OLAP",
        "Star Schema",
        "Snowflake Schema",
        "Normalization",
        "Denormalization",
        "Data Warehouse",
        "Data Lake",
        "Lakehouse",
        "Medallion"
      ]
    }
  ]
}
```

---

## 30. Critérios de Aceite

### CA001 — Login

Dado que o usuário possui cadastro, quando informar e-mail e senha válidos, então deve acessar o dashboard.

### CA002 — Visualização da trilha

Dado que o usuário está logado, quando acessar a trilha, então deve visualizar as 7 seções e os 100 Steps.

### CA003 — Conclusão de Step

Dado que o usuário iniciou um Step, quando concluir a lição e responder o quiz com nota mínima, então o Step deve ser marcado como concluído.

### CA004 — Pontuação

Dado que o usuário concluiu uma atividade, quando a atividade for validada, então os pontos devem ser adicionados ao perfil.

### CA005 — Desbloqueio

Dado que o usuário concluiu um Step, quando a regra de progressão for atendida, então o próximo Step deve ser desbloqueado.

### CA006 — Certificado

Dado que o usuário concluiu todos os requisitos da trilha, quando acessar a tela de certificado, então deve conseguir gerar e baixar o PDF.

---

## 31. Riscos e Cuidados

### 31.1 Conteúdo ficar superficial

Mitigação: cada Step deve ter explicação simples e técnica, com exemplo real.

### 31.2 Gamificação virar distração

Mitigação: jogos devem reforçar o aprendizado, não virar firula digital com confete gratuito.

### 31.3 Dificuldade de manter 100 lições

Mitigação: criar editor administrativo e seed estruturado.

### 31.4 Escalabilidade futura

Mitigação: desde o início criar Track, Section e Step como entidades genéricas.

### 31.5 Segurança fraca

Mitigação: hash de senha, JWT, validação de input e controle de permissões.

---

## 32. Futuras Evoluções

### 32.1 IA assistente de aprendizado

Criar um tutor com IA dentro do sistema para explicar conceitos de formas diferentes.

Exemplo:

“Explique Data Lake como se eu tivesse 12 anos.”

### 32.2 Geração automática de quizzes

A IA poderá sugerir perguntas com base no conteúdo da lição.

### 32.3 Trilhas personalizadas

Admins poderão criar novas trilhas usando a metodologia Step By Step.

Exemplos:

- Step By Step AI
- Step By Step Cloud
- Step By Step Cybersecurity
- Step By Step Power BI
- Step By Step Software Engineering
- Step By Step Telecom Operations

### 32.4 Ranking e turmas

Criar grupos de usuários, turmas e ranking por turma.

### 32.5 Modo empresa

Empresas poderão usar a plataforma para treinamento interno.

### 32.6 Marketplace de trilhas

Criadores poderão publicar trilhas próprias.

---

## 33. Exemplo de Conteúdo para os Primeiros 5 Steps

### Step 1 — Data Modeling

**O que é:**  
Data Modeling é a forma de organizar os dados para que eles façam sentido, sejam fáceis de consultar e representem corretamente o negócio.

**Analogia:**  
É como organizar uma gaveta. Você pode jogar tudo lá dentro e chamar de “Big Data”, mas depois vai sofrer para achar uma meia. Modelagem é separar meia, cueca, camiseta e aquele cabo USB misterioso que ninguém sabe de onde veio.

**Mini desafio:**  
Escolha qual modelo representa melhor uma loja online: Cliente, Pedido, Produto e Pagamento.

### Step 2 — OLTP vs OLAP

**O que é:**  
OLTP registra operações. OLAP analisa dados.

**Analogia:**  
OLTP é a pessoa passando compra no caixa. OLAP é o gerente olhando o relatório e descobrindo que terça-feira vende mais pão de queijo do que deveria ser legalmente permitido.

### Step 3 — Star Schema

**O que é:**  
Modelo em estrela usado em Data Warehouses, com uma tabela fato no centro e dimensões ao redor.

**Analogia:**  
É uma estrela mesmo: no meio fica o evento principal, tipo venda. Ao redor ficam os detalhes: cliente, produto, loja, data. É fofinho até você ter que explicar isso em reunião com 37 abas do Excel abertas.

### Step 4 — Snowflake Schema

**O que é:**  
Variação do Star Schema onde as dimensões são mais normalizadas e quebradas em tabelas menores.

**Analogia:**  
É a estrela que resolveu fazer pós-graduação e ficou cheia de ramificações.

### Step 5 — Normalization

**O que é:**  
Processo de organizar dados para evitar repetição e inconsistência.

**Analogia:**  
É evitar escrever o mesmo endereço do cliente em 15 lugares diferentes, porque uma hora alguém vai escrever “Rua das Flores” e outro vai escrever “R. das Florez”, e aí nasce o caos.

---

## 34. Definition of Done

A primeira versão será considerada pronta quando:

- Usuário conseguir criar conta e logar.
- Trilha Data Engineering aparecer com 7 seções.
- Os 100 Steps estiverem cadastrados.
- Pelo menos 10 Steps tiverem conteúdo completo.
- Quiz funcionar.
- Progresso for salvo.
- Pontuação for calculada.
- Certificado for gerado ao concluir a trilha.
- Sistema rodar localmente com instruções claras.
- Estrutura permitir deploy futuro em Cloud.

---

## 35. Resumo Executivo

O **Step By Step** será uma plataforma de aprendizado gamificada e expansível, começando pela trilha **Data Engineering & AI Concepts** com 100 conceitos transformados em Steps interativos.

Cada Step terá explicação clara, exemplo real, analogia divertida, atividade prática, quiz e pontuação. O usuário avança por fases, desbloqueia conteúdos, acumula pontos, ganha badges e recebe certificado ao final.

A primeira versão deve rodar localmente com login, banco de dados e estrutura preparada para Cloud. A arquitetura deve ser genérica o suficiente para que, no futuro, o Step By Step vire uma metodologia reutilizável para qualquer área de conhecimento.

O objetivo é simples: transformar aprendizado técnico em uma jornada menos chata, mais prática e com sensação real de progresso. Porque aprender Data Engineering já é difícil o suficiente; não precisa parecer uma planilha sem café.
