
                            echo "🤖 Running AI Fix Agent..."

			    pwd
			    ls -l agents/

                            python3 agents/fix_agent.py

                            git config user.email "jenkins@ai.com"
                            git config user.name "AI Bot"

                            git add -A

                            git commit -m "[AI] auto fix applied" || true

                            git remote set-url origin https://$GIT_USER:$GIT_PASS@github.com/Rohitcs09/MLOPS.git

                            git push origin main --force || true
                            