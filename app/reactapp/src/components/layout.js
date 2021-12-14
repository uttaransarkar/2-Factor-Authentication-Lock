import { Layout, Menu, Breadcrumb } from 'antd';
import { UserOutlined, LaptopOutlined } from '@ant-design/icons';
import MyStats from './MyStats'

const { SubMenu } = Menu;
const { Header, Content, Sider } = Layout;

function MyLayout(){
    return (
        <div>
            <Layout>
                <Header className="header">
                <div className="logo" />
                    <h1 style={{ color: 'white' }}>2 Factor Authentication Lock</h1>
                </Header>
                <Layout>
                <Sider width={200} className="site-layout-background">
                    <Menu
                    mode="inline"
                    defaultSelectedKeys={['1']}
                    defaultOpenKeys={['sub1']}
                    style={{ height: '100%', borderRight: 0 }}
                    >
                    <SubMenu key="sub1" icon={<UserOutlined />} title="Face Auth">
                        <Menu.Item key="1">Add User</Menu.Item>
                        <Menu.Item key="2">Update User</Menu.Item>
                        <Menu.Item key="3">Delete User</Menu.Item>
                    </SubMenu>
                    <SubMenu key="sub2" icon={<LaptopOutlined />} title="Password">
                        <Menu.Item key="5">Set Password</Menu.Item>
                        <Menu.Item key="6">Change Password</Menu.Item>
                        <Menu.Item key="7">Forgot Password</Menu.Item>
                    </SubMenu>
                    </Menu>
                </Sider>
                <Layout style={{ padding: '0 24px 24px' }}>
                    <Breadcrumb style={{ margin: '16px 0' }}>
                    <Breadcrumb.Item>Home</Breadcrumb.Item>
                    <Breadcrumb.Item>List</Breadcrumb.Item>
                    <Breadcrumb.Item>App</Breadcrumb.Item>
                    </Breadcrumb>
                    <Content
                    className="site-layout-background"
                    style={{
                        padding: 24,
                        margin: 0,
                        minHeight: 280,
                    }}
                    >
                        <MyStats/>
                    </Content>
                </Layout>
                </Layout>
            </Layout>
        </div>
    )
}
export default MyLayout;