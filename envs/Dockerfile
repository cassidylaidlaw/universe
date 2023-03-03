FROM cassidylaidlaw/flashgames:0.0.1
COPY ./flashgames.CoastRunners-v0 /app/universe-envs/flashgames/build/git-lfs/flashgames.CoastRunners-v0
COPY ./flashgames.CoastRunners-v0/private/vexpect/vexpect.yml /app/universe-envs/flashgames/build/private/flashgames.CoastRunners-v0/vexpect/vexpect.yml
WORKDIR /app/universe-envs/flashgames/build/git-lfs/
RUN tar cvfz flashgames.CoastRunners-v0.tar.gz flashgames.CoastRunners-v0
