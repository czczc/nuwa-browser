# fabric tasks
from fabric.api import *

env.hosts = ['pdsf.nersc.gov']
env.user = 'chaoz'

# =============================
# def update(site='local', target='odmrun', dryrun='dryrun'):
#     '''update remote json files'''
    
#     cmd = './manage.py runscript scrape --script-args "%s %s"' % (target, dryrun)
    
#     if site == 'local':
#         if dryrun != 'dryrun':
#             local('cp -f db/odm.db ~/bin/backup/')
#         local(cmd)
#     elif site == 'portal':
#         run('source dayabay/load_odm_env.sh')
#         with cd('dayabay/odm'):
#             # back up database
#             if dryrun != 'dryrun':
#                 run('cp -f db/odm.db ~/backup/')
#             with prefix('source ~/dayabay/load_odm_env.sh'):
#                 # run('echo $PYTHONPATH')
#                 run(cmd)
#     else:
#         print 'site not found %s' % site
#         return

# =============================
@hosts('chaoz@pdsf3.nersc.gov')
def deploy_pdsf(dryrun=False):
    '''deploy to pdsf'''
    from fabric.contrib.project import rsync_project
    
    if dryrun: 
        dry_run = ' --dry-run'
    else: 
        dry_run = ''
    
    # media server
    rsync_project(
        remote_dir='/project/projectdirs/dayabay/www/nuwa-browser/',
        local_dir='./',
        exclude=('.git/', '.gitignore', '.DS_Store', '*.pyc'),
        extra_opts='--update' + dry_run,
    )
                
# =============================
def test_remote():
    run('cd dayabay')
    run('pwd')
    run('ls')

